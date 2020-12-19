from provinces import nei

main_list = []  # shahr haye rang nashode
color_prov = [] #shahr haye rang shode

class province():
    def __init__(self, name):
        self.name = name
        self.neighbors = nei[name]['names']
        self.neighbors_number = nei[name]['number']
        self.color_can = ['sabz',   'ghermez',  'zard',  'abi']
        self.color_yes_no = False  #rang shode ya nashode
        self.color = ''

    def __str__(self):
        return (self.name+'\n'+str(self.color))



def end():
    if not main_list:
        return True
    return False

def choose_province(count):
    if count == 0 :
        a = 0
        for i in range (1,len(main_list)):
            if (main_list[i].neighbors_number > main_list[a].neighbors_number):
                a = i
        main_list[a].color = 'sabz'
        main_list[a].color_yes_no = True
        prov = main_list[a]

    else:
        a = 0
        for i in range (1,len(main_list)):
            if (len(main_list[i].color_can) < len(main_list[a].color_can)):
                a = i       
        main_list[a].color = main_list[a].color_can[0]
        main_list[a].color_yes_no = True
        prov = main_list[a]
    
    main_list.remove(prov)
    color_prov.append(prov)
    for i in range (0,len(main_list)):
        if prov.name in main_list[i].neighbors:
            try:
                main_list[i].color_can.remove(prov.color)
                
            except Exception:
                continue
        


def main_colorize ():
    count=-1
    while True:
        count=count+1
        if (end()):
            break
        choose_province(count)
        if not main_list:
            return


for i in nei:
    prov = province(i)
    main_list.append(prov)
    
main_colorize()

for i in range (0,len(color_prov)):   #namayesh natije
    print (color_prov[i],'\n')




