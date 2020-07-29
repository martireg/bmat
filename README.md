### BMAT Works Singe View

This project aggregates, cleans and exposes metadata for musical works, to ensure high reliable and consistent information.

It exposes to the user an an API and interactive swagger interface for API discover and uploading/downloading work spreadsheets.   

### Requirements

- docker
- docker-compose
- [pipenv](https://github.com/pypa/pipenv "pipenv") (for developing)

### Installation and launch

Clone/Download this repository and go to the root directory. Be aware, this project might be private until an agreement with the company making the test.  
```bash
git clone https://github.com/martireg/bmat.git ~/MyFolder/bmat
cd ~/MyFolder/bmat
```

with make
    
```bash
make init
make start-server
```

manual

```bash
docker volume create --name=mongodb_data
docker-compose build
docker-compose up web_app
```
    
### Usage

When the project is started the server is exposed on the port 5000,
you check the swagger on the root for full list of endpoints. 

eg. on local [localhost:5000/](http://localhost:5000/)

otherwise <your_domain>:5000/

You can upload, download files and make requests from the swagger o via API requests

**Example** Get all musical works from the API:
```bash
curl -X GET "http://localhost:5000/works" -H  "accept: application/json" 
``` 

### Configuration

Use an .env file to change default values on the [config](/app/config.py) file.

For development you should use it to change the mongodb host.

example: `MONGO_HOST=localhost`

You can change the default threshold used to match similarity on names `SIMILARITY_THRESHOLD`, defaults to 80.

### FastApi
    
[FastApi](https://fastapi.tiangolo.com/) is a modern python open source web Framework.

The project uses this framework among other popular frameworks for it's integration with async, type hints and built-in Swagger documentation. 

### Clean architecture
    
Clean architecture is a Layer-based architecture aimed to make a decoupled, maintainable yet extensible application.

Main domain logic is placed in [use_cases](app/business_layers/use_cases.py), and the API is built on the [presentation layer](app/business_layers/presentation.py) 

This project uses clean architecture because it gives extra flexibility on the selection of frameworks used.
  
[Online resource for quick overview](https://www.freecodecamp.org/news/a-quick-introduction-to-clean-architecture-990c014448d2/)


### where is the requirements.txt?

This project uses [pipenv](https://github.com/pypa/pipenv) for modern requirements management.

All the requirements are managed with this tool and recorded automatically to the Pipenv and Pipenv.lock files.


   
### Developing

See [contributing file](CONTRIBUTING.md)

default developing port is 8000
```bash
make start-local
```

Mock project made by Martí Regola.