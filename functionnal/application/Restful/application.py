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
from sqlalchemy import *

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
    
    pd1_airport = pd1[discard1 & ~discard2];
    pd1_month = pd1[discard2 & ~discard1];
    pd1=pd1[~discard1 & ~discard2];
    pd1[["Month_num"]] = pd1[["Month_num"]].apply(pd.to_numeric);
    pd1_airport[["Month_num"]] = pd1_airport[["Month_num"]].apply(pd.to_numeric);

    pd1_list_month=pd1["Month"].drop_duplicates(keep='first', inplace=False)
    pd1_list_year=pd1["Year"].drop_duplicates(keep='first', inplace=False)	
    notice = "Passenger numbers refer to commercial passengers only. Transit passengers are included and are counted twice (i.e. both as arriving and departing passengers) Knock airport was closed from April to June 2020 and from February to May 2021 and Cork airport was closed in October 2021 Minor revisions to data for Cork and Dublin airports for 2021 on 24 May 2022.";
    
    #reducing to 2020
    pd1_2020 = pd1[pd1["Year"] == 2020];
    pd1_2020 = pd1_2020.drop(labels=["Year"], axis=1,errors='ignore');
    # print(pd1_2020)
    airport_2020 = pd1_2020["Airport"];
    month_2020 = pd1_2020["Month"];
    month_num_2020 = pd1_2020["Month_num"];
    value_2020 = pd1_2020["Value"];
    DATABASE_URL = "mysql+pymysql://"+db['mysql_user']+":"+db['mysql_password']+"@"+db['mysql_host']+":"+str(db["mysql_port"])+"/"+db['mysql_db']
    engine = create_engine(DATABASE_URL)
    engine.execute("CREATE TABLE IF NOT EXISTS airports (airport VARCHAR(255), month VARCHAR(255), month_num INT(255), value INT(255))")

    
    return render_template('index.html', tables_cleaned=[pd1.to_html(classes='data', header="true")], titles_cleaned=pd1.columns.values, notice=notice, types_cleaned=pd1.dtypes, tables_month=[pd1_month.to_html(classes='data', header="true")], titles_month=pd1_month.columns.values, types_month=pd1_month.dtypes, tables_airport=[pd1_airport.to_html(classes='data', header="true")], titles_airport=pd1_airport.columns.values, types_airport=pd1_airport.dtypes, years=pd1_list_year)

if __name__ == '__main__':
    application.run() #debug=True can be added for debugging