from html.parser import HTMLParser
import os


# 定义一个HTML解析器
class ShareSpanParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.shares = []

    def handle_starttag(self, tag, attrs):
        # 检查是否是我们要查找的span标签
        if tag == "span":
            # 检查属性中是否有data-res-action="share"
            attrs_dict = dict(attrs)
            if attrs_dict.get("data-res-action") == "share":
                # 如果是，则提取data-res-name和data-res-author
                share_info = {
                    "song_id": 0,
                    "song_name": attrs_dict.get("data-res-name"),
                    "singer": attrs_dict.get("data-res-author"),
                    "genre": "",
                    "language": "",
                    "sc": 0,
                    "url_or_other": ""
                }
                self.shares.append(share_info)


# 实例化解析器
parser = ShareSpanParser()
# 读取HTML文件并解析
file_path = os.path.expanduser('D:/Desktop/temp2.html')
with open(file_path, 'r', encoding='utf-8') as file:
    parser.feed(file.read())
# 输出提取的信息
for share in parser.shares:
    print(share, ",")

print("歌单中歌曲的数量：", len(parser.shares))
