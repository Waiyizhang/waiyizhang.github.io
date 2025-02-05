from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

host = "localhost"
port = 8081

# 获取当前文件的所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
project_root = os.path.dirname(current_dir)
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
from reports import  fetch_gender_purchase_count,fetch_age_group_purchase_count,get_city_category_purchases,get_occupation_preference,get_stay_duration_purchases,get_marital_status_preference,get_product_category_purchases,get_top_selling_products

# insert_one
from insert_one import insert_users

app = FastAPI()
# 跨域配置

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载 static 目录来服务静态文件
app.mount("/static", StaticFiles(directory="server/static"), name="static")
templates = Jinja2Templates(directory="server/templates")

images_directory_path = os.path.join(project_root, "./images")
app.mount("/images", StaticFiles(directory=images_directory_path), name="images")

# 定义路由
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class TypeModel(BaseModel):
    type: str
    params: str

@app.post("/searchType")
async def create_item(item: TypeModel):
    print(item)
    type = item.type
    params = item.params
    image = ''
    summary = ''
    if type == 'fetch_gender_purchase_count':
        data = fetch_gender_purchase_count()
        gender_map = {'F': 'female', 'M': 'male'}
        for item in data:
            if item[0] == params:
                summary = f"As for {gender_map[item[0]]} consumer, they made {item[1]} purchases"
                image = f"http://{host}:{port}/images/gender_distribution.png"
    elif type == 'fetch_age_group_purchase_count':
        data = fetch_age_group_purchase_count()
        image = f"http://{host}:{port}/images/age_distribution.png"
        for item in data:
            if item[0] == params:
                summary = f"For customers age between {item[0]} made {item[1]} purchases，occupied {item[2]:.1f}% of the total age group"
    elif type == 'get_city_category_purchases':
        data = get_city_category_purchases()
        image = f"http://{host}:{port}/images/city_distribution.png"
        for item in data:
            if item[0] == params:
                summary = f"For customers who live in {item[0]} made {item[1]} purchases"
    elif type == 'get_occupation_preference':
        data = get_occupation_preference()
        print(data, params)
        image = f"http://{host}:{port}/images/occupation_distribution.png"
        for item in data:
            print(item[0] ,params, item[0] == params)
            if int(item[0]) == int(params):
                summary = f"For consumers is {item[0]}, people are bought {item[1]} most ."
    elif type == 'get_stay_duration_purchases':
        pass
    elif type == 'get_marital_status_preference':
        pass
    elif type == 'get_product_category_purchases':
        pass
    elif type == 'get_top_selling_products':
        data = get_top_selling_products()
        image = f"http://{host}:{port}/images/top_ten.png"
        label = ''
        for item in data:
                label = f"{item[0]} was purchased in {item[1]},which is NO.{item[2]} in the best selling products."
                summary += label + '\n'

    return {
            "code": 200,
            "data": {
                "summary": summary,
                "image": image
            }
        }


# User_ID, Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status
class DataTypeModel(BaseModel):
    User_ID: str
    Gender: str
    Age: str
    Occupation: str
    City_Category: str
    Stay_In_Current_City_Years: str
    Marital_Status: str
class FormDataModel(BaseModel):
    data: DataTypeModel

@app.post("/insertData")
async def create_item(item: DataTypeModel):
    # def insert_users(user_id, gender, age, occupation, city_category, stay_in_current_city_years, marital_status)
    lastrowid = insert_users(item.User_ID, item.Gender, item.Age, item.Occupation, item.City_Category, item.Stay_In_Current_City_Years, item.Marital_Status)
    return {
        "code": 200,
        "data": {
            "lastrowid": lastrowid
        },
        "message": f"insert success with lastrowid: {lastrowid}, data: {item}"
    }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8081)