import ast
import yaml
from pathlib import Path
with open(Path()/'/var'/'app'/'current'/'db.yaml') as stream:
    db = yaml.safe_load(stream);
import numpy as np
import pandas as pd
import requests
from flask import Flask, redirect, render_template, request, session
from pymysql import connect
from sqlalchemy import create_engine, text



application = Flask(__name__, template_folder='templates')


pd1=pd.DataFrame({});


@application.route('/',methods=['GET','POST'])
def index():
        global pd1
        pd1 = pd.read_csv(r"TAM06.20221111183248.csv", sep=',', header=0);
        pd1["VALUE"]=pd1["VALUE"].fillna(0);
        pd1.rename(columns={'VALUE': 'Value'}, inplace=True);
        pd1.rename(columns={'C01885V02316': 'Month_num'}, inplace=True);
        pd1.drop(labels=["Statistic Label", "STATISTIC","UNIT","TLIST(A1)","C02935V03550"], axis=1, inplace=True,errors='ignore');
        discard1 = pd1["Airport"] == "All main airports"
        discard2 = pd1["Month"] == "All months"
           
        #Keeping the rows for all airports on their own without the rows "all months"
        pd1_all_airports_label = pd1[discard1 & ~discard2]; #meaning rows with "all airports" and not "all months"
        #Keeping the rows for all months on their own without the rows "all airports"
        pd1_all_months = pd1[discard2 & ~discard1]; #meaning rows with all months but not rows with all airports
        #Keeping the rows for all months and all airports
        pd1_all_airports_months = pd1[discard1 & discard2]; #meaning rows with all airports and all months
        #taking out the rows with all airports and all months
        pd1=pd1[~discard1 & ~discard2];

        
        #PLEASE NOTE THAT I DIDN'T TAKE OUT THE ROW Numerical Month for now as I am still testing elements

        ###Cleaning the tables
        pd1[["Month_num"]] = pd1[["Month_num"]].apply(pd.to_numeric);
        pd1_all_airports_label[["Month_num"]] = pd1_all_airports_label[["Month_num"]].apply(pd.to_numeric);
        pd1[["VALUE"]] = pd1[["VALUE"]].apply(pd.to_numeric);
        pd1_all_airports_label[["VALUE"]] = pd1_all_airports_label[["VALUE"]].apply(pd.to_numeric);
        pd1_all_months[["VALUE"]] = pd1_all_months[["VALUE"]].apply(pd.to_numeric);
        pd1_all_airports_months[["VALUE"]] = pd1_all_airports_months[["VALUE"]].apply(pd.to_numeric);

        
        #creating a column with all the months for a possible graph to be used as labels
        pd1_list_month=pd1["Month"].drop_duplicates(keep='first', inplace=False);
        #creating a column with all the years for a possible graph to be used as labels
        pd1_list_year=pd1["Year"].drop_duplicates(keep='first', inplace=False);
        
        notice = "Passenger numbers refer to commercial passengers only. Transit passengers are included and are counted twice (i.e. both as arriving and departing passengers) Knock airport was closed from April to June 2020 and from February to May 2021 and Cork airport was closed in October 2021 Minor revisions to data for Cork and Dublin airports for 2021 on 24 May 2022.";
        
        #reducing to 2019 for global pd1
        pd1_2019 = pd1[pd1["Year"] == 2019];
        pd1_2019 = pd1_2019.drop(labels=["Year"], axis=1,errors='ignore');
        
        #reducing to 2020 for global pd1
        pd1_2020 = pd1[pd1["Year"] == 2020];
        pd1_2020 = pd1_2020.drop(labels=["Year"], axis=1,errors='ignore');
        
        #reducing to 2021 for global pd1
        pd1_2021 = pd1[pd1["Year"] == 2021];
        pd1_2021 = pd1_2021.drop(labels=["Year"], axis=1,errors='ignore'); 
        
        #reducing to 2022 for global pd1
        pd1_2022 = pd1[pd1["Year"] == 2022];
        pd1_2022 = pd1_2022.drop(labels=["Year"], axis=1,errors='ignore');
        

        ##### MONTH TABLE
        #reducing to 2019 for pd1_all_months
        pd1_all_months_2019 = pd1_all_months[pd1_all_months["Year"] == 2019];
        pd1_all_months_2019 = pd1_all_months_2019.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_months_2019 = pd1_all_months_2019.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_months_2019 = pd1_all_months_2019.drop(labels=["Month"], axis=1,errors='ignore');
        

        #reducing to 2020 for pd1_all_months
        pd1_all_months_2020 = pd1_all_months[pd1_all_months["Year"] == 2020];
        pd1_all_months_2020 = pd1_all_months_2020.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_months_2020 = pd1_all_months_2020.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_months_2020 = pd1_all_months_2020.drop(labels=["Month"], axis=1,errors='ignore');

        #reducing to 2021 for pd1_all_months
        pd1_all_months_2021 = pd1_all_months[pd1_all_months["Year"] == 2021];
        pd1_all_months_2021 = pd1_all_months_2021.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_months_2021 = pd1_all_months_2021.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_months_2021 = pd1_all_months_2021.drop(labels=["Month"], axis=1,errors='ignore');
        
        
        #reducing to 2022 for pd1_all_months
        pd1_all_months_2022 = pd1_all_months[pd1_all_months["Year"] == 2022];
        pd1_all_months_2022 = pd1_all_months_2022.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_months_2022 = pd1_all_months_2022.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_months_2022 = pd1_all_months_2022.drop(labels=["Month"], axis=1,errors='ignore');
        print(pd1_all_months_2022);

        ##### AIRPORT TABLE
        #reducing to 2019 for pd1_all_airports_label
        pd1_all_airports_label_2019 = pd1_all_airports_label[pd1_all_airports_label["Year"] == 2019];
        pd1_all_airports_label_2019 = pd1_all_airports_label_2019.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_label_2019 = pd1_all_airports_label_2019.drop(labels=["Airport"], axis=1,errors='ignore');

        #reducing to 2020 for pd1_all_airports_label
        pd1_all_airports_label_2020 = pd1_all_airports_label[pd1_all_airports_label["Year"] == 2020];
        pd1_all_airports_label_2020 = pd1_all_airports_label_2020.drop(labels=["Year"], axis=1,errors='ignore')
        pd1_all_airports_label_2020 = pd1_all_airports_label_2020.drop(labels=["Airport"], axis=1,errors='ignore')

        #reducing to 2021 for pd1_all_airports_label
        pd1_all_airports_label_2021 = pd1_all_airports_label[pd1_all_airports_label["Year"] == 2021];
        pd1_all_airports_label_2021 = pd1_all_airports_label_2021.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_label_2021 = pd1_all_airports_label_2021.drop(labels=["Airport"], axis=1,errors='ignore');

        #reducing to 2022 for pd1_all_airports_label
        pd1_all_airports_label_2022 = pd1_all_airports_label[pd1_all_airports_label["Year"] == 2022];
        pd1_all_airports_label_2022 = pd1_all_airports_label_2022.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_label_2022 = pd1_all_airports_label_2022.drop(labels=["Airport"], axis=1,errors='ignore');


        ##### ALL AIRPORT ALL MONTHS TABLE
        #reducing to 2019 for pd1_all_airports_all_months
        pd1_all_airports_months_2019 = pd1_all_airports_months[pd1_all_airports_months["Year"] == 2019];
        pd1_all_airports_months_2019 = pd1_all_airports_months_2019.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_months_2019 = pd1_all_airports_months_2019.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_airports_months_2019 = pd1_all_airports_months_2019.drop(labels=["Month"], axis=1,errors='ignore');
        pd1_all_airports_months_2019 = pd1_all_airports_months_2019.drop(labels=["Airport"], axis=1,errors='ignore');

        #reducing to 2020 for pd1_all_airports_all_months
        pd1_all_airports_months_2020 = pd1_all_airports_months[pd1_all_airports_months["Year"] == 2020];
        pd1_all_airports_months_2020 = pd1_all_airports_months_2020.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_months_2020 = pd1_all_airports_months_2020.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_airports_months_2020 = pd1_all_airports_months_2020.drop(labels=["Month"], axis=1,errors='ignore');
        pd1_all_airports_months_2020 = pd1_all_airports_months_2020.drop(labels=["Airport"], axis=1,errors='ignore');

        #reducing to 2021 for pd1_all_airports_all_months
        pd1_all_airports_months_2021 = pd1_all_airports_months[pd1_all_airports_months["Year"] == 2021];
        pd1_all_airports_months_2021 = pd1_all_airports_months_2021.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_months_2021 = pd1_all_airports_months_2021.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_airports_months_2021 = pd1_all_airports_months_2021.drop(labels=["Month"], axis=1,errors='ignore');

        #reducing to 2022 for pd1_all_airports_all_months
        pd1_all_airports_months_2022 = pd1_all_airports_months[pd1_all_airports_months["Year"] == 2022];
        pd1_all_airports_months_2022 = pd1_all_airports_months_2022.drop(labels=["Year"], axis=1,errors='ignore');
        pd1_all_airports_months_2022 = pd1_all_airports_months_2022.drop(labels=["Month_num"], axis=1,errors='ignore');
        pd1_all_airports_months_2022 = pd1_all_airports_months_2022.drop(labels=["Month"], axis=1,errors='ignore');

        # Source given by a tutor during lab session 
        DATABASE_URL = "mysql+pymysql://"+db['mysql_user']+":"+db['mysql_password']+"@"+db['mysql_host']+":"+str(db["mysql_port"])+"/"+db['mysql_db'];
        engine = create_engine(DATABASE_URL)
        
        #creating tables in database
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports2019 (month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports2020 (month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports2021 (month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports2022 (month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("INSERT INTO all_airports2019(month, month_num, value) VALUES(%s, %i, %f)", (pd1_all_airports_label_2019["Month"], pd1_all_airports_label_2019["Month_num"],pd1_all_airports_label_2019["Value"]));
        engine.execute("INSERT INTO all_airports2020(month, month_num, value) VALUES(%s, %i, %f)", (pd1_all_airports_label_2020["Month"], pd1_all_airports_label_2020["Month_num"],pd1_all_airports_label_2020["Value"]));
        engine.execute("INSERT INTO all_airports2021(month, month_num, value) VALUES(%s, %i, %f)", (pd1_all_airports_label_2021["Month"], pd1_all_airports_label_2021["Month_num"],pd1_all_airports_label_2021["Value"]));
        engine.execute("INSERT INTO all_airports2022(month, month_num, value) VALUES(%s, %i, %f)", (pd1_all_airports_label_2022["Month"], pd1_all_airports_label_2022["Month_num"],pd1_all_airports_label_2022["Value"]));
        
        engine.execute("CREATE TABLE IF NOT EXISTS all_months2019 (airport VARCHAR(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_months2020 (airport VARCHAR(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_months2021 (airport VARCHAR(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_months2022 (airport VARCHAR(255), value FLOAT(255));");
        engine.execute("INSERT INTO all_months2019(airport, value) VALUES(%s, %f)", (pd1_all_months_2019["Airport"], pd1_all_months_2019["Value"]));
        engine.execute("INSERT INTO all_months2020(airport, value) VALUES(%s, %f)", (pd1_all_months_2020["Airport"], pd1_all_months_2020["Value"]));
        engine.execute("INSERT INTO all_months2021(airport, value) VALUES(%s, %f)", (pd1_all_months_2021["Airport"], pd1_all_months_2021["Value"]));
        engine.execute("INSERT INTO all_months2022(airport, value) VALUES(%s, %f)", (pd1_all_months_2022["Airport"], pd1_all_months_2022["Value"]));


        engine.execute("CREATE TABLE IF NOT EXISTS years2019 (airport VARCHAR(255), month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS years2020 (airport VARCHAR(255), month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS years2021 (airport VARCHAR(255), month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS years2022 (airport VARCHAR(255), month VARCHAR(255), month_num INT(255), value FLOAT(255));");
        engine.execute("INSERT INTO year2019(airport, month, month_num, value) VALUES(%s, %s, %i, %f)", (pd1_2019["Airport"], pd1_2019["Month"], pd1_2019["Month_num"],pd1_2019["Value"]));
        engine.execute("INSERT INTO year2020(airport, month, month_num, value) VALUES(%s, %s, %i, %f)", (pd1_2020["Airport"], pd1_2020["Month"], pd1_2020["Month_num"],pd1_2020["Value"]));
        engine.execute("INSERT INTO year2021(airport, month, month_num, value) VALUES(%s, %s, %i, %f)", (pd1_2021["Airport"], pd1_2021["Month"], pd1_2021["Month_num"],pd1_2021["Value"]));
        engine.execute("INSERT INTO year2022(airport, month, month_num, value) VALUES(%s, %s, %i, %f)", (pd1_2022["Airport"], pd1_2022["Month"], pd1_2022["Month_num"],pd1_2022["Value"]));

        engine.execute("CREATE TABLE IF NOT EXISTS all_airports_months2019 (value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports_months2020 (value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports_months2021 (value FLOAT(255));");
        engine.execute("CREATE TABLE IF NOT EXISTS all_airports_months2022 (value FLOAT(255));");
        engine.execute("INSERT INTO all_airports_months2019(value) VALUES(%f)", (pd1_all_airports_months_2019["Value"]));
        engine.execute("INSERT INTO all_airports_months2020(value) VALUES(%f)", (pd1_all_airports_months_2020["Value"]));
        engine.execute("INSERT INTO all_airports_months2021(value) VALUES(%f)", (pd1_all_airports_months_2021["Value"]));
        engine.execute("INSERT INTO all_airports_months2022(value) VALUES(%f)", (pd1_all_airports_months_2022["Value"]));


        
        return render_template('index.html', years=pd1_list_year, notice=notice)

if __name__ == '__main__':
    application.run(debug=True)