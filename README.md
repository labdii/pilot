# Pilot Project

### Hours Management for XBOX

<br>

To get the project just type

```bash
git clone https://github.com/labdii/pilot
```

To setup the python environment we'll use virtualenv

For apt-get based systems
 ```bash
 sudo apt-get install python3-pip
 ```

Then install virtualenv

```bash
pip3 install virtualenv
```
**NOTE:** We are using **Python 3.x**

Now let's create the environment and activate it

```bash
virtualenv -p python3 <name_of_enviroment>
source <name_of_enviroment>/bin/activate
```

Now go inside the project folder and install dependencies

```bash
cd pilot
pip3 install -r requirements.txt
```

### Using script to start local development server

Ensure .env file with environmental variables exists and is placed in the root folder.

#### Example

```
MONGODB_URI=<mongodb uri>
MONGODB_DBNAME=<database name>
```

Grant permissions and run the script

```bash
sudo chmod +x start_dev.sh
./start_dev.sh
```

### Using gunicorn

If you want to use gunicorn

```bash
# Using just 1 worker. You can replace the 1 for any number of workers
gunicorn -w1 app:app
```

<br>

### To Do

* Write a build env script
