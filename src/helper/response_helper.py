def Response(data,message="success",code=200):
    return {
        "data":[data],
        "message":message,
        "code":code
    }