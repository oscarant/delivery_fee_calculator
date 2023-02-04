
## Development

I decided to use pipenv because I find the installation of dependencies and its 
app setup very easy and convenient.

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

#### Running directly the app

or as an alternative, you can try this:

```shell
pipenv run python runserver.py
```

## Author

* Oscar Pacheco - Backend Developer