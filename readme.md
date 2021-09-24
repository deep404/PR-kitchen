> Network Programming Laboratory Work No1 [Kitchen]
>
> FAF 192 Y3-S1
>
> Pasecinic Nichita

​	Kitchen configuration `config.py` has following configuration variables: food, orders, cooks list and a queue of stoves, ovens, and food_items (individual food items from orders). Once a order is received on `/order` endpoint, food items of that order are added to the mapping food_item queue (1queue item = 1 food item) and the order is appended to kitchen orders list (same as request payload but with 3 more fields: `received_time, cooking_details, is_done_counter` ). Each cook is a separate thread, but a cook can work simultaneously on several food items, so a cook will handle a number of threads = `proficiency`, lets call them hands. Each cook hand is getting a food item to prepare from the queue and checks if the cook can prepare it following the logic from the task. If the cook hand can prepare the order then he will get the cooking apparatus from corresponding queue. After the cook hand is done preparing the order, it put new apparatus to queue, updated the cooking details and the food item counter, once the counter is equal to number of food items from the order then is notified the dinning hall to serve the order to table. In case the cook hand is not able to cook that food item then item is pushed back to the queue.

#### Run

```bash
$ # clone repository
$ py -m venv env # create env
$ env\Scripts\activate # activate env
$ pip install -r requirements.txt # install dependecies
$ py main.py # start the server
```

#### with docker

```bash
$ docker build --tag kitchen . # create kitchen image
$ docker network create nt # create docker network 
$ docker run -d --net nt --name kitchen kitchen # run docker container on created network
```

