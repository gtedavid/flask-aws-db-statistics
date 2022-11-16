# flask-db-statistics - Lab 2

## Task - Create an AWS instance and RDS on which to store :
 - files for the code
 - the application
 - the database storing data

## Notice

   1. This python code was developped with the help of a few websites for a Lab.
Those sites are mentioned in the code.
- _Sites to come, the sources weren't taken while researching contrarily to lab 1 due to a large amount of testing of several sources_
- Line 41 for splitting dataframes [1](https://www.geeksforgeeks.org/how-to-drop-rows-that-contain-a-specific-string-in-pandas/) [2](https://www.geeksforgeeks.org/split-dataframe-in-pandas-based-on-values-in-multiple-columns/)
- Lines 161 Sources for the .execute() method: [1](https://www.w3schools.com/python/python_mysql_insert.asp) [2](https:// www.w3schools.com/python/python_mysql_getstarted.asp) <br />
  [Sources for the insert](https://akashtikkiwal.medium.com/deploying-flask-web-application-integrated-with-mysql-database-server-running-on-aws-d9ce560add89)
- For the connection to the database [1](https://dev.to/chrisgreening/connecting-to-a-relational-database-using-sqlalchemy-and-python-1619)
- For AWS db connection : this [source was used](https://akashtikkiwal.medium.com/deploying-flask-web-application-integrated-with-mysql-database-server-running-on-aws-d9ce560add89)
https://stackoverflow.com/questions/49628274/unable-to-get-value-selected-in-python-from-a-dropdown-using-flask

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

TAM06 was used for the data from https://data.cso.ie/.
## About the code

### Installation and use

We are using here AWS Free Tier. We already created an Elastic Beanstalk environnement running under Python 3.8 running on 64bit Amazon Linux 2/3.4.1.<br />
You will need to ahve Python 3.X installed, note that here we used 3.11. <br />
I may add a category to the README about the AWS setup of the dataabase and Elastic Beanstalk, this may be in progress post deadline of the hand in of this lab.<br />

_Please note that there has been a vulnerabilty found on all Python 3.X versions allowing to cause a deny of service remotly [fr](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-1017/](en)[https://www.cve.org/CVERecord?id=CVE-2022-45061) [en](https://www.cve.org/CVERecord?id=CVE-2022-45061)._<br />

1. How to set up the working environement on your computer

 GENERAL NOTICE : for the import to work properly, all packages had to be installed before on the main pc.
  1. Windows <br />
  Open a command prompt from the folder you want your project to be. Type ¹`pip install virtualenv`, then type ¹`virtualenv env`. Note that you can call it whatever you want. <br />
    For the first activation, `env\Scripts\activate.bat` is needed, the next times you'll be able to do ativate the virtual environment with `source env\bin\activate`, if you typed in something different from `env`be sure to replace that with how you called it.<br />
Your command prompt/terminal is now in the python environement `env`. Type now `pip install flask`. <br />
  For this exercise, please install the above libraries as they are required and if not installed, the code may not work. If you have [issues with installing the yaml package on Windows](https://www.geeksforgeeks.org/how-to-install-pyyaml-on-windows/).<br />
  
  ¹Please note that : `C:\Users\user\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_xxxxxxxxxxxxx\python.exe -m ` may need to be used previously if you are using a Python version installed from the Windows Store. <br />
  Please not that I haven't had time to figure out fully how the start actually works, due to my laptop's configuration. <br />
  It may vary depending on the source and which python.exe you are using, whether it be global or the one installed locally in the folder after installation of the virtual environment.
  
  2. Mac Apple ² <br />
  Open a command prompt from the folder you want your project to be. Type `pip install virtualenv`, then type `virtualenv env`. <br />
  Note that you can call it whatever you want.<br />
  Then to activate the virtual environment `source env/bin/activate`, if you typed in something different from `env`be sure to replace that with how you called it.<br />
  Your command prompt/terminal is now in the python environement `env`. Type now `pip install flask`.  <br />
  For this exercise, please install the above libraries as they are required and if not installed, the code may not work.  <br />
  If you have [issues with installing the yaml package on Mac](https://stackoverflow.com/questions/14261614/how-do-i-install-the-yaml-package-for-python/21317961#21317961).
  
  ² N.B. This was taken by a helping paper, commands may vary slightly or extra steps may be needed.
  
2. AWS Setup
  This [tutorial](https://dev.to/chrisgreening/connecting-to-a-relational-database-using-sqlalchemy-and-python-1619) can be followed for some help putting in place the environment.
  
  You will just to have to upload as a zip file one of the folders `application`.


