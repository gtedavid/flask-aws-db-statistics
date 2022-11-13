# flask-db-statistics - Lab 2

## Task - Create an AWS instance and RDS on which to store :
 - files for the code
 - the application
 - the database storing data

## Notice

   1. This python code was developped with the help of a few websites for a Lab.
Those sites are mentioned in the code.
- _Sites to come, the sources weren't taken while researching contrarily to lab 1 due to a large amount of testing of several sources_

_Please note that I'm not in anyway responsible for malfunctioning of the use of Python, abusive number entry in the program or any of the librairies used._

If the authors of the above posts would like to see their content be deleted from this program, feel free to provide any proof of it being yours.

## Use / licencing not set

Please feel free to use this program if you need it.
If you use it in any project, hand-in lab, etc, please credit the work done by others and what I did, as I do my best to give credit to the work of others that help me.
####

1. Librairies used in this program :

- flask_mysqldb
- numpy
- pandas
- matplotlib *to be confirmed*

## About the code

### Installation and use

We are using here AWS Free Tier. We already created an Elastic Beanstalk environnement running under Python 3.8 running on 64bit Amazon Linux 2/3.4.1.
You will need to ahve Python 3.X installed, note that here we used 3.11.
I may add a category to the README about the AWS setup of the dataabase and Elastic Beanstalk, this may be in progress post deadline of the hand in of this lab.

_Please note that there has been a vulnerabilty found on all Python 3.X versions allowing to cause a deny of service remotly [fr](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-1017/](en)[https://www.cve.org/CVERecord?id=CVE-2022-45061) [en](https://www.cve.org/CVERecord?id=CVE-2022-45061)._

1. How to set up the working environement on your computer

 GENERAL NOTICE : for the import to work properly, all packages had to be installed before on the main pc.
  1. Windows
  Open a command prompt from the folder you want your project to be. Type `pip install virtualenv`, then type `virtualenv env`. Note that you can call it whatever you want.
  Then to activate the virtual environment `source env\bin\activate`, if you typed in something different from `env`be sure to replace that with how you called it.
Your command prompt/terminal is now in the python environement `env`. Type now `pip install flask`.
  For this exercise, please install the above libraries as they are required and if not installed, the code may not work. If you have [issues with installing the yaml package on Windows](https://www.geeksforgeeks.org/how-to-install-pyyaml-on-windows/).
  
  
  
  2. Mac Apple *
  Open a command prompt from the folder you want your project to be. Type `pip install virtualenv`, then type `virtualenv env`. 
Note that you can call it whatever you want.
  
Then to activate the virtual environment `source env/bin/activate`, if you typed in something different from `env`be sure to replace that with how you called it.
  
Your command prompt/terminal is now in the python environement `env`. Type now `pip install flask`.

  For this exercise, please install the above libraries as they are required and if not installed, the code may not work.
  If you have [issues with installing the yaml package on Mac](https://stackoverflow.com/questions/14261614/how-do-i-install-the-yaml-package-for-python/21317961#21317961).
  
  
2. AWS Setup

  
  
* N.B. This was taken by a helping paper, commands may vary slightly or extra steps may be needed.
