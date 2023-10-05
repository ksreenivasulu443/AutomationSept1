class Movie:
    def __init__(self,title, hero):
        self.title=title
        self.hero=hero
    def info(self):
        print("Movie name is ", self.title)
        print("Hero name is", self.hero)

ls=[]
while True:
    title= input("Enter title")
    hero= input("Enter hero name")
    m=Movie(title,hero)
    ls.append(m)
    option= input("Enter option Yes|no")
    if option.lower()=='no':
        break

print(ls)
for i in ls:
    print(i)
    i.info()