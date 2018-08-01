class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        json_dict = {"title":self.title, "content":self.content}
        return(json_dict)
