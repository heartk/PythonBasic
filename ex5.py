
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_centimeters = height / 0.39370


weight = 180 # lbs LBS是英文pounds（磅） 一种不恰当的缩写，lb来自拉丁语 libra :scales / balance
weight_kilograms = weight / 2.2046


eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s" % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eys and %s hair." % (eyes, hair))
print("His teeth ara usually %s depending on the coffee." % teeth)

print("He's %d centimeters tall. " % height_centimeters)
print("He's %d kilograms weight" % weight_kilograms)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

print("this is %r" % eyes)

test_array = []
print("this is array %r" % test_array)

# print this no matter what
test_ch = "中文"
print("this is 中文 %r" % test_ch)


print(round(1.73333))

print("test error s" % eyes)