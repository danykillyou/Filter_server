import os
from datetime import datetime
import nest_asyncio
import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from starlette.requests import Request
os.makedirs("Filter_app_pics",exist_ok=True)
app = FastAPI(debug=False)
@app.get('/')
async def Get_Filters():
    return {"":[0,0,0,0],"https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-1100x628.jpg":[125.0,60.0,100.0,60.0],"https://firebasestorage.googleapis.com/v0/b/bold-cable-286310.appspot.com/o/DSC06508-removebg-preview.png?alt=media&token=62262612-2b67-4fe9-8589-eb5fc7d56814":[125.0,60.0,100.0,60.0],"https://firebasestorage.googleapis.com/v0/b/bold-cable-286310.appspot.com/o/Lipharoj_kaj_monoklo.svg-removebg-preview.png?alt=media&token=d71f25e2-bdd3-493c-8c1c-305293a7b4f4":[155.0,35.0,155.0,35.0],"https://firebasestorage.googleapis.com/v0/b/bold-cable-286310.appspot.com/o/sunglasses-glasses-png-image-removebg-preview.png?alt=media&token=2e4b595f-9ba0-4002-b662-7b76017ce328":[145,80.0,140.0,80.0],"https://firebasestorage.googleapis.com/v0/b/bold-cable-286310.appspot.com/o/mustache_c-removebg-preview.png?alt=media&token=1dd08b86-5e38-4869-aecd-0fa3296b30ea":[94.7,-100,110,-100]} #,"url":"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*","url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzWXrymxSqiZCf8mTMWSqymDlPvnIYCyPeoA&usqp=CAU","url":"https://1.bp.blogspot.com/-KFur-JKmlEg/X_YMCguVqNI/AAAAAAAAkQI/QmPfDA810dkasSXoO2aZBzQKFdScYz1YQCPcBGAYYCw/s1212/DSC06508.jpg","url":"https://gumlet.assettype.com/freepressjournal%2F2020-05%2Ff7aff896-c6b5-468a-99d0-13274e459321%2F93795360_1653085578180407_5647917878148239252_n.jpg?rect=0%2C0%2C760%2C428&w=1200","url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Lipharoj_kaj_monoklo.svg/1200px-Lipharoj_kaj_monoklo.svg.png"}
@app.post('/add_pic')
async def add_pic(req: Request):
    form = await req.form()
    for i in form.keys():
#fffffffffff
#zzzzzzzzz
        print(form[i])
        filend = form[i].filename.split(".")[-1]
        name = fr'{ form[i].filename.split(".")[0]+ str(datetime.now().strftime("_%Y-%m-%d__%H-%M-%S.")) }'
        contents = await form[i].read()
        f =open(fr"Filter_app_pics\{str(name+filend)}",'wb')
        f.write(contents)
        f.close
        print(filend)
@app.get('/a')
async def Get_pics(url:str):
    print(url+"00000000000")
    print("aaaaaa")
    return FileResponse(url)
@app.get('/all_pics')
async def Get_all_pics():
    x=os.listdir("Filter_app_pics")
    print(x)
    return x
nest_asyncio.apply()
uvicorn.run(app, host="0.0.0.0", port=8010)

