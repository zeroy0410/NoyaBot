from flask import  Flask,request
from lib import replyGroup
app=Flask(__name__)         #实例化并命名为app实例


@app.route('/',methods=["POST"])
def analyse():
    jsonData=request.get_json()
    if 'message_type' not in jsonData:
        return "OK"
    if jsonData['message_type']=='group':
        gid = jsonData['group_id']  # 获取群号
        uid = jsonData['sender']['user_id']  # 获取信息发送者的 QQ号码
        nickname=jsonData['sender']['nickname']
        message = jsonData['raw_message']  #获取原始信息
        replyGroup.groupSolve(gid,uid,nickname,message)
    elif jsonData['message_type']=='private':
        uid = jsonData['sender']['user_id']
        nickname=jsonData['sender']['nickname']
        message = jsonData['raw_message']  #获取原始信息
        replyGroup.singleSolve(uid,nickname,message)
    return "OK"
    

if __name__=="__main__":
    replyGroup.reLoad()
    app.run(port=5701,host="127.0.0.1",debug=True)   #调用run方法，设定端口号，启动服务

