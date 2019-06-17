# DashSkeleton

### WHAT THIS IS
This is a skeleton dash app with an HTML landing page for Google Signin. 
I tried the existing GoogleOAuth implementation but it signs you in without even asking you or telling you where you were

### HOW THIS WORKS
This uses a top level flask server route to redirect non authenticated users to an HTML landing page with a Google Signin button.
Upon authentication the HTML page posts the googleToken to the a dedicated flask server route for server side authentication.
If the authentication is successful the app opens a session and the user is redirected to the main dash app, otherwise to the Signin page.
If the user clicks on logout in your app, redirect to /revoke. This will revoke the session and redirect to the signin page.

### SETUP
- pip install --upgrade google-auth
- pip install visdcc
- [Setup google authentication in the google developer console](https://console.developers.google.com/apis/)


### USEFUL LINKS
- http://flask.pocoo.org/docs/0.12/quickstart/
- https://dash.plot.ly/urls
- https://dash.plot.ly/authentication
- https://google-auth.readthedocs.io/en/latest/
- http://flask.pocoo.org/docs/0.12/api/#flask.request
- https://developers.google.com/identity/protocols/OAuth2WebServer#tokenrevoke
- ###### TODO: [Setup Google cross account protection https](//developers.google.com/identity/risc) 