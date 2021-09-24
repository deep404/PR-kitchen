import queue

global TIME_UNIT
TIME_UNIT = 1

"""
Foods list Configuration
{
    "food_id": 1,
    "order_id": 2
}
"""
global FOOD_ITEMS_Q
FOOD_ITEMS_Q = queue.Queue()
"""
Orders Config
{
    "id": 1,
    "items": [5, 4, 6, 9, 1],
    "priority": 4,
    "max_wait": 46,
    "status": "waiting",
    "is_done_counter": 0,
    "time_start": time.time(),
    "time_diff": None,
    "table_id": 1,
    "waiter_id": 2,
    "cooking_details": queue.Queue()
}
"""
global ORDER_LIST
ORDER_LIST = []

"""
Cooks Config
"""
global COOKS_LIST
COOKS_LIST = [{
    "id": 1,
    "rank": 3,
    "proficiency": 3,
    "name": "Jamie Oliver",
    "catch-phrase": "🤡",
    "parallel_items": 0
}, {
    "id": 2,
    "rank": 2,
    "proficiency": 3,
    "name": "Heston Blumenthal",
    "catch-phrase": "👾",
    "parallel_items": 0
}, {
    "id": 3,
    "rank": 1,
    "proficiency": 3,
    "name": "Ferran Adria",
    "catch-phrase": "🤔",
    "parallel_items": 0
}]

"""
Apparatuses
"""

global STOVES_Q
STOVES_Q = queue.Queue()
STOVES_Q.put(0)
STOVES_Q.put(1)
STOVES_Q.put(2)
STOVES_Q.put(3)

global OVENS_Q
OVENS_Q = queue.Queue()
OVENS_Q.put_nowait(0)
OVENS_Q.put_nowait(1)
OVENS_Q.put_nowait(2)
OVENS_Q.put_nowait(3)

"""
Food Config
"""
global FOOD_LIST
FOOD_LIST = [{
    "id": 1,
    "name": "pizza",
    "preparation-time": 20,
    "complexity": 2,
    "cooking-apparatus": "oven"
}, {
    "id": 2,
    "name": "salad",
    "preparation-time": 10,
    "complexity": 1,
    "cooking-apparatus": None
}, {
    "id": 4,
    "name": "Scallop Sashimi with Meyer Lemon Confit",
    "preparation-time": 32,
    "complexity": 3,
    "cooking-apparatus": None
}, {
    "id": 5,
    "name": "Island Duck with Mulberry Mustard",
    "preparation-time": 35,
    "complexity": 3,
    "cooking-apparatus": "oven"
}, {
    "id": 6,
    "name": "Waffles",
    "preparation-time": 10,
    "complexity": 1,
    "cooking-apparatus": "stove"
}, {
    "id": 7,
    "name": "Aubergine",
    "preparation-time": 20,
    "complexity": 2,
    "cooking-apparatus": None
}, {
    "id": 8,
    "name": "Lasagna",
    "preparation-time": 30,
    "complexity": 2,
    "cooking-apparatus": "oven"
}, {
    "id": 9,
    "name": "Burger",
    "preparation-time": 15,
    "complexity": 1,
    "cooking-apparatus": "oven"
}, {
    "id": 10,
    "name": "Gyros",
    "preparation-time": 15,
    "complexity": 1,
    "cooking-apparatus": None
}]
