import json
import base64
import cv2
from io import BytesIO
import requests
import time
import json
main_dict={}
main_list=[]
img=cv2.imread("images2\\0.jpg")
_, im_arr = cv2.imencode('.jpg', img)
im_b64 = base64.b64encode(im_arr).decode()

img2=cv2.imread("images2\\179.jpg")
_, im_arr2 = cv2.imencode('.jpg', img2)
im_b642 = base64.b64encode(im_arr2).decode()

img3=cv2.imread("images2\\1.jpg")
_, im_arr3 = cv2.imencode('.jpg', img3)	
im_b643 = base64.b64encode(im_arr3).decode()

img4=cv2.imread("images2\\13.jpg")
_, im_arr4 = cv2.imencode('.jpg', img4)	
im_b644 = base64.b64encode(im_arr4).decode()

img5=cv2.imread("images2\\9.jpg")
_, im_arr5 = cv2.imencode('.jpg', img5)	
im_b645 = base64.b64encode(im_arr5).decode()

img6=cv2.imread("images2\\20.jpg")
_, im_arr6 = cv2.imencode('.jpg', img6)	
im_b646 = base64.b64encode(im_arr6).decode()

img7=cv2.imread("images2\\4.jpg")
_, im_arr7 = cv2.imencode('.jpg', img7)	
im_b647 = base64.b64encode(im_arr7).decode()

img8=cv2.imread("images2\\180.jpg")
_, im_arr8 = cv2.imencode('.jpg', img8)	
im_b648 = base64.b64encode(im_arr8).decode()

img9=cv2.imread("images2\\183.jpg")
_, im_arr9 = cv2.imencode('.jpg', img9)	
im_b649 = base64.b64encode(im_arr9).decode()

img10=cv2.imread("images2\\171.jpg")
_, im_arr10 = cv2.imencode('.jpg', img10)	
im_b6410 = base64.b64encode(im_arr10).decode()
#________________________________________________________________________#
img11=cv2.imread("images2\\0.jpg")
_, im_arr11 = cv2.imencode('.jpg', img11)
im_b6411 = base64.b64encode(im_arr11).decode()

img12=cv2.imread("images2\\179.jpg")
_, im_arr12 = cv2.imencode('.jpg', img12)
im_b6412 = base64.b64encode(im_arr12).decode()

img13=cv2.imread("images2\\1.jpg")
_, im_arr13 = cv2.imencode('.jpg', img13)	
im_b6413 = base64.b64encode(im_arr13).decode()

img14=cv2.imread("images2\\13.jpg")
_, im_arr14 = cv2.imencode('.jpg', img14)	
im_b6414 = base64.b64encode(im_arr14).decode()

img15=cv2.imread("images2\\9.jpg")
_, im_arr15 = cv2.imencode('.jpg', img15)	
im_b6415 = base64.b64encode(im_arr15).decode()

img16=cv2.imread("images2\\20.jpg")
_, im_arr16 = cv2.imencode('.jpg', img16)	
im_b6416 = base64.b64encode(im_arr16).decode()

img17=cv2.imread("images2\\4.jpg")
_, im_arr17 = cv2.imencode('.jpg', img17)	
im_b6417 = base64.b64encode(im_arr17).decode()

img18=cv2.imread("images2\\180.jpg")
_, im_arr18 = cv2.imencode('.jpg', img18)	
im_b6418 = base64.b64encode(im_arr18).decode()

img19=cv2.imread("images2\\183.jpg")
_, im_arr19 = cv2.imencode('.jpg', img19)	
im_b6419 = base64.b64encode(im_arr19).decode()

img20=cv2.imread("images2\\171.jpg")
_, im_arr20 = cv2.imencode('.jpg', img20)	
im_b6420 = base64.b64encode(im_arr20).decode()



main_list.append(['7510','gun21.jpg',im_b64,])
main_list.append(['9781','gun22.jpg',im_b642, ])
main_list.append(['9782','gun23.jpg',im_b643,])
main_list.append(['9783','gun24.jpg',im_b644,])

# print(main_list)
# main_list.append({'idx': '9787','image':'','image_name': 'gun28.jpg'})
# main_list.append({'idx': '9788','image':'','image_name': 'gun29.jpg'})
# main_list.append({'idx': '9789','image':'','image_name': 'gun30.jpg'})

# main_list.append({'idx': '7588','image':'','image_name': 'gun31.jpg'})
# main_list.append({'idx': '9790','image':'','image_name': 'gun32.jpg'})
# main_list.append({'idx': '9791','image':'','image_name': 'gun33.jpg'})
# main_list.append({'idx': '9792','image':'','image_name': 'gun34.jpg'})
# main_list.append({'idx': '9793','image':'','image_name': 'gun35.jpg'})
# main_list.append({'idx': '9794','image':'','image_name': 'gun36.jpg'})
# main_list.append({'idx': '9795','image':'','image_name': 'gun37.jpg'})
# main_list.append({'idx': '9796','image':'','image_name': 'gun38.jpg'})
# main_list.append({'idx': '9797','image':'','image_name': 'gun39.jpg'})
# main_list.append({'idx': '9798','image':'','image_name': 'gun40.jpg'})







main_dict["registration"]=main_list
with open('out.json','w+') as f:
    json.dump(main_dict,f)
start=time.time()
response = requests.post("https://us-central1-fit-overview-356508.cloudfunctions.net/function-heydome_demo",json=main_dict)
end=time.time()
print("time taken =",end-start)
print(len(main_list))
print(len(main_dict["registration"]))
print(response.status_code)
#dict.update({"image":dict["image"].replace("base64string",str(imb64))})
#data['registration'].append(dict)
#print(data)


