## 0x1A. Application server

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/311/QbqjElZ.jpg)

**0. Welcome Gunicorn**

     Let’s serve what you built for AirBnB clone v2 - Web
     framework on web01.

Requirements:

* Git clone your AirBnB_clone_v2
* Install Gunicorn and other libraries required by your application
* Create an Upstart script that starts a Gunicorn instance to
  serve web_flask/0-hello_route.py from your AirBnB_clone_v2
* Setup Nginx so that the route /airbnb-onepage/ points to your
  Gunicorn instance
* Nginx must serve this page both locally and on its public IP on
  port 80
* Upload your Upstart config file as
  0-welcome_gunicorn-upstart_config
* Upload your Nginx config file as 0-welcome_gunicorn-nginx_config

Do not forget that logs are your friends! (E.g. Nginx‘s logs are
located in /var/log/nginx) Also init-checkconf is great for
checking your Upstart config files.