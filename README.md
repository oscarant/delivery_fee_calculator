# Delivery Fee Calculator
This is a simple delivery fee calculator that calculates the delivery fee based on many
variables

## Development

I decided to use pipenv because I find the installation of dependencies and its 
app setup very easy and convenient. I used python 3.10.4 for this project, 
but theoretically it should work with any python 3.7+ version.

### Setup

1. Install pipenv
    ```shell
    pip install pipenv
    ```
2. Install the dependencies:
    ```shell
    cd <project_dir>
    pipenv install --three
    ```

### Run it

If you are not already in the `delivery_fee_calculator` directory:

```shell
cd <project_dir>
```

At this moment you have two options to run the app:

#### Activating the virtual environment

Activate the pipenv shell and run the python file.

```shell
pipenv shell
python runserver.py
```
After this moment you can send requests to the app.

### Using the app
Usable endpoints:
* ```/v1/calculator/delivery_fee``` - POST
* ```/-/ping``` - GET

For default when you run the app it will be listening on port ```8080``` and the 
host will be ```127.0.0.1```.

So the full URL will be ```http://127.0.0.1:8080/v1/calculator/delivery_fee```.

### Testing
If you are not in the virtual environment, activate it:

```shell
pipenv shell
```

Run the tests:

```shell
python -m unittest discover
```

## Author

* Oscar Pacheco - Backend Developer