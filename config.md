# Twitter Assist

### How to run Twitter Assist django web app on your local machine

Make sure you have python3 installed on you computer if you don't know run the command below to check python version

```bash
python3 --version
```
Use virtual environment to install all the dependencies without effecting other packages in you system

These command will now create new virtual environment in your current folder and activate them

```bash
sudo apt install virtualenv
virtualenv env
source env/bin/activate

```

Once you have activated your virtual environment clone the respository

```bash
git clone https://github.com/python-project-tinkerhub/project-python.git
cd project-python/twitter_assist
git checkout main
```
Then you need to install all the required dependencies

```bash
pip install -r ../requirements.txt
```

You will need a twitter developers account to use the twitter API used in this project the [mainapp/secret_keys.py] should be included in the twitter_scripts folder 

```python
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
```

Then you will need to create a database for the project by running

```bash
python manage.py makemigrations
python manage.py migrate
```

Once you have migrated the database you can start the development server just by running

```bash
python manage.py runserver
```

Open the link provided in the terminal in browser.
