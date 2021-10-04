import requests
datalist=requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
data=datalist.json()["data"]
full_date=str(data["update_date_time"])
new_pos=str(data["local_new_cases"])
total_pos=str(data["local_total_cases"])
new_death=str(data["local_new_deaths"])
total_death=str(data["local_deaths"])
new_good=str(data["local_recovered"])

date=full_date[:10]
if date[6]=="8":
    month="wf.daia;= "
if date[6]=="9":
    month="iema;eïn¾ "

today="2021 "+month+date[-2:]
print(month, date[-2:])
file=open("datatoday.csv","w")
file.write("Today,new_pos,new_good,new_death,total_pos,total_death\n")
dataline=today+","+new_pos+","+new_good+","+new_death+","+total_pos+","+total_death
print(dataline)
#Printing the deadline
file.write(dataline)
#Closing File
file.close()


