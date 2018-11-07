def gen_list():
    liste = []
    for i in range(0, 10):
        print("Liste element # " + str(i) +" first generated.")
        liste.append(i)
    return liste

# without Generators:
for element in gen_list():
    print("and Then For element # " + str(element) + " generated.")

def gen_generator():
    for i in range(0, 10):
        print("With Generator, generate element at first  # " + str(i) +" and send to called method and wait.")
        yield i # <-- This work like : generate i and send it to called method and wait until next call.

# wit Generators:
for element in gen_generator():
    print("and then i here landed : For # " + str(element) + " worked.")