import requests
import os 
import random
dir_path = os.path.dirname(os.path.realpath(__file__))
def numConvert(number):
    return "{:,}".format(int(number)).replace(",","""\"""")



from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


datalist=requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
data=datalist.json()["data"]
full_date=str(data["update_date_time"])

def getData(new_pos,name):
    new_pos_text=new_pos.replace("\"","")
    new_pos1=str(input(f"Reported {name} {new_pos_text}. Enter the number."))
    new_pos1.replace("\n","")
    if new_pos1!="":

        new_pos=numConvert(new_pos1)
    return new_pos



new_pos=numConvert(data["local_new_cases"])
new_pos=getData(new_pos,"නව ආසදිතයින්")

new_death=numConvert(data["local_new_deaths"])
new_death=getData(new_death,"නව මරණ")


active_cases=numConvert(data["local_active_cases"])
active_cases=getData(active_cases,"දැනට ආසාධිත සංඛ්‍යාව")


total_pos=numConvert(data["local_total_cases"])
total_pos=getData(total_pos,"ආසාධිත මුළු")




total_death=numConvert(data["local_deaths"])
total_death=getData(total_death,"මුළු මරණ")


new_good=numConvert(data["local_recovered"])

date=full_date[:10]
print(date)
if date[6]=="8":
    month="wf.daia;= "
if date[6]=="9":
    month="iema;eïn¾ "
if date[5:7]=="10":
    month="Tlaf;dan¾ "
if date[5:7]=="11":
    month="fkdjeïn¾ "
if date[5:7]=="12":
    month="foieïn¾ "

today="2021 "+month+date[-2:]
file=open("datatoday.csv","w")
file.write("Today,new_pos,new_good,new_death,total_pos,total_death\n")
dataline=today+","+new_pos+","+new_good+","+new_death+","+total_pos+","+total_death

file.write(dataline)
file.close()


from PIL import Image, ImageFont, ImageDraw



myImage=Image.open(f"{dir_path}/CovidTemplate.jpg")

titleFont=ImageFont.truetype(f'{dir_path}/FM_GANGA.TTF',160)


casesFont=ImageFont.truetype(f'{dir_path}/FM_GANGA.TTF',140)


dateFont=ImageFont.truetype(f'{dir_path}/FM_GANGA.TTF',70)

updatedOnFont=ImageFont.truetype(f'{dir_path}/FM_GANGA.TTF',30)
createdOnFont=ImageFont.truetype(f'{dir_path}/FM_GANGA.TTF',15)

image_editable=ImageDraw.Draw(myImage)
#නව ආසාදිතයින්

image_editable.text((165,465),new_pos,(255, 255, 255),titleFont)
#නව මරණ
image_editable.text((1021,465),new_death,(255, 255, 255),titleFont)
#active cases
image_editable.text((1268,787),active_cases,(255, 255, 255),casesFont)

#total patients
image_editable.text((163,1212),total_pos,(255, 255, 255),titleFont)
#total deaths
image_editable.text((1018,1212),total_death,(255, 255, 255),titleFont)




#date
image_editable.text((120,65),today,(255, 255, 255),dateFont)

#updated on
image_editable.text((915,1953),full_date.replace(":","("),(255, 255, 255),updatedOnFont)


#created on
image_editable.text((1550,1983),dt_string,(255, 255, 255))


myImage.save("result-manual"+today+".jpg")
print("Image Created")
exit()



