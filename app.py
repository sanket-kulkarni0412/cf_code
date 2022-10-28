
from email.mime import base
from fileinput import filename
from flask import Flask,request, jsonify
import os   
import tempfile
import pandas as pd
from PIL import Image
import io
import base64
import json
from datetime import datetime, timedelta
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='fit-overview-356508-c4019b6367ab.json'
storage_client= storage.Client()
bucket=storage_client.get_bucket('heydome_demo')
_,temp_local_filename=tempfile.mkstemp()
temp_dir = tempfile.TemporaryDirectory()
app = Flask(__name__)
def blob_exists( bucket_name, filename):
   client = storage.Client()
   bucket = client.get_bucket(bucket_name)
   blob = bucket.blob(filename)
   return blob.exists()
def upload_json(bucket, destination_jsonfile_name, result_json):
    bucket.blob(destination_jsonfile_name).upload_from_string(
        data=json.dumps(result_json), content_type='application/json')
    print('Data uploaded to {}.'.format(destination_jsonfile_name))

def save_response_json(bucket, response_json, str_datetime, date):
    destination_jsonfile_name = "jewellery-search-project/logs/{}/{}_response.json".format(date, str_datetime)
    upload_json(bucket, destination_jsonfile_name, response_json)

def save_request_json(bucket, request_json, str_datetime, date):
    destination_jsonfile_name = "jewellery-search-project/logs/{}/{}_request.json".format(
        date, str_datetime)
    upload_json(bucket, destination_jsonfile_name, request_json)

sta=blob_exists('heydome_demo','jewellery-search-project/temp_data.csv')                                                                        
if sta==False:
    fields = ['unique_id', 'image_name', 'idx','file_extension','image_url','image_storage_path','pickle_file_storage_path','is_image_url_valid','download_status','pickle_file_storage','index_filename','error_status','drive_storage_path'] 
    df = pd.DataFrame(columns=fields)
    df.to_csv(temp_local_filename, index = False)
    bucket.blob('jewellery-search-project/temp_data.csv').upload_from_filename(temp_local_filename)
else:
    print(sta)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("Entered function")
    print("request.method =",request.method)
    
    current_blob=bucket.blob('jewellery-search-project/temp_data.csv')
    current_blob.download_to_filename(temp_local_filename)
    print(f"df was downloaded to {temp_local_filename}.")
    df_f=pd.read_csv(temp_local_filename)
    print(df_f) 
    df_temp=pd.DataFrame(columns=['image_name','idx','image_storage_path'])
    if request.method == 'POST':
        current_datetime = datetime.now()
        print(type(current_datetime))
        str_datetime = str(current_datetime).replace(" ", "_").replace(":", "-").replace(".", "_")
        date = str(current_datetime.date())
        data = request.get_json(force=True)
        save_request_json(bucket,data,str_datetime,date)
        print("len(data)=",len(data["registration"]))
        data_list=data["registration"]
        message_logs=[]
        for dictd in data_list:
            id_val=dictd[0]
            img_base=dictd[2]
            # category_cd=dictd['category_code']
            img_name=dictd[1]
            # for content in img_base:
            #     print("content :", content)
            #     # print("base_64_img :", img_base)
            #     if "," in content:
            data_img = img_base.split(",")[-1].encode("utf8")

                # else:
            data_img = img_base.encode("utf8")
            
            try:
                blob_path='jewellery-search-project/similar_product_search/{}/{}'.format(id_val,img_name)
                imag_data=base64.b64decode(data_img)
                bs = io.BytesIO()
                image_=Image.open(io.BytesIO(imag_data))
                image_.save(bs, "jpeg")
                bucket.blob(blob_path).upload_from_string(bs.getvalue(), content_type="image/jpeg")
                try:
                    data_csv_f=[]
                    data_csv=[]
                    data_csv.append(img_name)
                    data_csv.append(id_val)
                    # data_csv.append(category_cd)
                    data_csv.append(blob_path)
                    data_csv_f.append(data_csv)
                    df_temp.loc[len(df_temp)]=data_csv
                except Exception as e:
                    print(e)
                mes="Image saved to:{}".format(str(blob_path))
                message_logs.append(mes)
                json_dict_main = {"status": "success","timestamp": str(current_datetime), "message":message_logs}  
            except Exception as e:
                print(e)
                json_dict_main = {"status": "failure","timestamp": str(current_datetime), "message": str(
                e)}
        save_response_json(bucket,json_dict_main, str_datetime, date)
        df_final=pd.concat([df_f,df_temp],axis=0,ignore_index=True)
        df_final.drop(df_final.columns[df_final.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        df_final.to_csv(temp_local_filename,index=True)
        bucket.blob('jewellery-search-project/temp_data.csv').upload_from_filename(temp_local_filename)
    return jsonify(json_dict_main)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5030)
