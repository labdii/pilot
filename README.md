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
pip3 install virtualenv
```
**NOTE:** We are using **Python 3.x**

Now let's create the environment and activate it

```bash
virtualenv -p python3 <name_of_enviroment>
source <name_of_enviroment>/bin/activate
```

Now go inside the project folder and run

```bash
cd pilot
pip3 install -r requirements.txt
python3 app.py
```

If you want to use gunicorn

```bash
pip3 install gunicorn

# Using just 1 worker. You can replace the 1 for any number of workers
gunicorn -w1 app:app
```
