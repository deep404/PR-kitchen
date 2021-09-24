import time
import queue
import threading
import requests
from flask import Flask, request
import config as config
from PrintUtils import PrintUtils

log = PrintUtils()

app = Flask(__name__)


@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    log.print_red(f'[  kitchen  ] new order {data["order_id"]} with {data["items"]} items')
    convert_order_to_food_items(data)
    return {'isSuccess': True}


def convert_order_to_food_items(data):
    kitchen_order = {
        'order_id': data['order_id'],
        'table_id': data['table_id'],
        'waiter_id': data['waiter_id'],
        'items': data['items'],
        'priority': data['priority'],
        'max_wait': data['max_wait'],
        'received_time': time.time(),
        'cooking_details': queue.Queue(),
        'is_done_counter': 0,
        'time_start': data['time_start'],
    }
    config.ORDER_LIST.append(kitchen_order)
    for item_id in data['items']:
        food = next((f for i, f in enumerate(config.FOOD_LIST) if f['id'] == item_id), None)
        if food is not None:
            config.FOOD_ITEMS_Q.put_nowait({
                'food_id': food['id'],
                'order_id': data['order_id']
            })


def can_prepare(cook, ovens: queue.Queue, stoves: queue.Queue, food, order):
    if food['complexity'] == cook['rank'] or food['complexity'] - 1 == cook['rank']:
        apparatus = food['cooking-apparatus']
        if apparatus == 'oven':
            try:
                o = ovens.get_nowait()
                log.print_yellow(f'{threading.current_thread().name} cooking food: {food} for order {order["order_id"]} oven-{o}')
                return True
            except Exception as e:
                return False
        elif apparatus == 'stove':
            try:
                s = stoves.get_nowait()
                log.print_yellow(f'{threading.current_thread().name} cooking food: {food} for order {order["order_id"]} stove-{s}')
                return True
            except Exception as e:
                return False
        elif apparatus is None:
            log.print_yellow(f'{threading.current_thread().name} cooking food: {food} for order {order["order_id"]} with hands only')
            return True
        return False
    return False


def cook_hand_work(cook, ovens: queue.Queue, stoves: queue.Queue, food_items: queue.Queue):
    while True:
        try:
            food_item = food_items.get_nowait()
            food_details = next((f for f in config.FOOD_LIST if f['id'] == food_item['food_id']), None)
            (order_idx, order_details) = next(((idx, order) for idx, order in enumerate(config.ORDER_LIST) if order['order_id'] == food_item['order_id']), (None, None))

            if can_prepare(cook, ovens, stoves, food_details, order_details):
                time.sleep(food_details['preparation-time'] * config.TIME_UNIT)
                # check if all food items from order are done
                config.ORDER_LIST[order_idx]['is_done_counter'] += 1
                if config.ORDER_LIST[order_idx]['is_done_counter'] == len(config.ORDER_LIST[order_idx]['items']):
                    # notify dinning hall
                    log.print_green(f'{threading.current_thread().name} prepared order {order_details["order_id"]}')
                    config.ORDER_LIST[order_idx]['cooking_details'].put({'food_id': food_details['id'], 'cook_id': cook['id']})
                    payload = {
                        **config.ORDER_LIST[order_idx],
                        'cooking_time': int(time.time() - config.ORDER_LIST[order_idx]['received_time']),
                        'cooking_details': list(config.ORDER_LIST[order_idx]['cooking_details'].queue)
                    }
                    requests.post('http://dinning:5000/distribution', json=payload, timeout=0.0000000001)
                # add new free cooking apparatus to queue
                apparatus = food_details['cooking-apparatus']
                if apparatus == 'oven':
                    n = ovens.qsize()
                    ovens.put_nowait(n)
                elif apparatus == 'stove':
                    n = stoves.qsize()
                    stoves.put_nowait(n)
            else:
                food_items.put_nowait(food_item)

        except Exception as e:
            pass


def cook_work(info, ovens, stoves, food_items):
    # each cook can work on multiple food items at once
    for i in range(info['proficiency']):
        hand_thread = threading.Thread(target=cook_hand_work, args=(info, ovens, stoves, food_items,), daemon=True, name=f'{info["name"]}-#{i}')
        hand_thread.start()


def start_kitchen():
    flask_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8000, debug=False, use_reloader=False), daemon=True)
    flask_thread.start()

    for _, cook_data in enumerate(config.COOKS_LIST):
        cook_thread = threading.Thread(target=cook_work, args=(cook_data, config.OVENS_Q, config.STOVES_Q, config.FOOD_ITEMS_Q,), daemon=True)
        cook_thread.start()

    # main thread loop
    while True:
        pass


if __name__ == '__main__':
    start_kitchen()
