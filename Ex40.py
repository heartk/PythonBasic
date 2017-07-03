
import  mystuff

mystuff1 = {'apple': 'I AM APPLES!'}

print(mystuff1['apple']) # get apple from dict
# mystuff.apple()           #  get apple from the module
# print(mystuff.tangerine)  # same thing, it's just a variable

thing = mystuff.MyStuff()

thing.apple()
print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()