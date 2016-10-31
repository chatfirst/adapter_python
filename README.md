# Demo Adapter for Chatfirst Platform
This project contains simple Flask application that can be used as adapter for [Chatfirst Platform](https://dashdoard.chatfirst.co)

## Step 1: Setup and deploy
- Use `gunicorn` to start the app locally
```
pip install -r requirements.txt
gunicorn -w 3 demoapp
```
- The application is ready to be deployed to [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
```
heroku git:remote -a <your_heroku_app_name>
git push heroku master
```

## Step 2: Use adapter calls in scenario
- Use `action` parameter in `transition` tags
```
<transition input="*" next="Start" action="https://<your_heroku_app_name>.herokuapp.com/">Some text</transition>
```
- Be sure that endpoint returns `ActionResponse` as json otherwise the platform rolls back to previous state showing error message