import os
import socket


def lambda_handler(event, context):
    try:
        addr1 = socket.gethostbyname('www.baidu.com')
    except PermissionError:
        addr1 = "Cannot get Google"

    try:
        addr2 = socket.gethostbyname('www.sina.cn')
    except PermissionError:
        addr2 = "Cannot get Yahoo"

    addr = "www.baidu.com : " + addr1 + "<br>" + "www.sina.cn : " + addr2

    response = "<html><body><h1>" + addr + "</h1></body></html>"
    return {
        'statusCode': 200,
        'body': response,
        'headers': {
            'Content-Type': 'text/html',
        }
    }
