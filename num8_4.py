# 8.9
def show_message(liebiao):
    for v in liebiao:
        print(f'{v}')
data = ['optimus','megatron','lili']
show_message(data)
# 8.10/8.11 复制列表在函数里面
def send_message(send_messages,show_messages):
    while show_messages:
        message = show_messages.pop()
        print(f"{message}")
        send_messages.append(message)
    print(f"show_message is {show_messages}")
    print(f"send_messages is {send_messages}")
send_messages = []

send_message(send_messages,data[:])
print(f"{data}")
print(f"{send_messages}")
#8.11
 