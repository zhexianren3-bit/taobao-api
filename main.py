from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "淘宝商品API"}
@app.get("/item")
def item(id: str = ""):
    return {"success": True, "item": {"title": "商品", "price": 99}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
