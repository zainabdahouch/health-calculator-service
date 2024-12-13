import requests

bmi_url = "http://localhost:5000/bmi"
bmr_url = "http://localhost:5000/bmr"


heigh=1.75
weight=70
HEIGH=175
age=30
gender="male"
data_bmi={"height":heigh , "weight":weight}
reponse_bmi=requests.post(bmi_url, json=data_bmi)

print(f"the bmi is {reponse_bmi.json()['result']}")

data_bmr={"height":HEIGH , "weight":weight , "age":age , "gender":gender}
reponse_bmr=requests.post(bmr_url, json=data_bmr)
print(f"the bmr is {reponse_bmr.json()['result']}")