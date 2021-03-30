
#分别传入网络连接和本地路径
def request_download(imgUrl, Path):
    import requests
    r = requests.get(imgUrl)
    with open(Path, 'wb') as f:
        f.write(r.content) 


if __name__ == "__main__":
    request_download('https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2018604370,3101817315&fm=26&gp=0.jpg', 'images/1.jpg')