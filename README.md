### 诺雅Noya

#### qq机器人的后端实现，与go-cqhttp结合使用

已经实现的功能：

* 闲聊
* * 回答指定的问题
  * 设定回答问题的概率
* 数学计算
* * 计算能用一行字符串表示的Sympy库格式的数据

```python
/teach A|B #当输入为A时以B来回答
/let talk_enable (True or False) #是否在群内开启闲聊
/let talk_probability 一个浮点数 #闲聊时接话的概率
/ask A #问话就会回答（无视上面两条指令的限制）
/calc sympy库格式的一条算式 #不要尝试计算复杂度过高的式子，计算时间过长会阻塞进程
```

于5701端口监听。