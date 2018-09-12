## 0x18. Webstack monitoring

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

“You cannot fix or improve what you cannot measure” is a famous saying in the
Tech industry. In the age of the data-ism, monitoring how our Software systems
are doing is an important thing. In this project, we will implement one of many
tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

* Application monitoring: getting data about your running software and making
  sure it is behaving as expected
* Server monitoring: getting data about your virtual or physical server and
  making sure they are not overloaded (could be CPU, memory, disk or network
  overload)

**0. Monitor your Nginx traffic**

     Let’s monitor our Nginx server traffic (access log and error log), by
     installing Sumo Logic on web-01 (feel free to do it on other servers a
     well). Create an account and follow the setup wizard flow.

Requirements:

* The account must be a SUMO LOGIC FREE
* The account must be configured for NORTH AMERICA
* You must use your ID@holbertonschool.com email address
* You must select Nginx as Data Type to import
* Create a Sumo Logic access key, share it in your answer file:
* First line: Access ID
* Second line: Access Key