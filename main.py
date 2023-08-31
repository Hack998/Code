import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw

# Variables

P1 = [0,1,3,4,6,8,10,11]
P2 = [0,2,3,5,6,9,10]
P3 = [1,2,3,7,8,9,10]
P4 = [4,5,6,7,8,9,10]
P5 = [11]

# Funcions

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1

# It is responsible for centering the window
def center_window(width,height, window) :
    window_x = int((window.winfo_screenwidth() / 2) - (width / 2)) 
    window_y = int((window.winfo_screenheight() / 2) - (height / 2)) 

    window_geometry = str(width) + 'x' + str(height) + '+' + str(window_x) + '+' + str(window_y)
    window.geometry(window_geometry)
    return

# It is responsible for checking the hexadecimal number
def check():
    try:
        int(hexadecimal_box.get(), 16)
        if len(str(hexadecimal_box.get())) != 3:
            center_window(420, 100, window_main)
            label_error.config(
                text="❌ Error: El número hexadecimal debe tener exactamente 3 dígitos."
                , foreground='#f00')
        else:
            conversor()
    except:
        if len(str(hexadecimal_box.get())) != 3:
            label_error.config(
                text="❌ Error: Introduzca un número hexadecimal válido y de exactamente 3 dígitos."
                , foreground='#f00')
            center_window(460, 100, window_main)
        else:
            label_error.config(text="❌ Error: Introduzca un número hexadecimal válido."
                               , foreground='#f00')
            center_window(420, 100, window_main) 

# It is responsible for convert binary to NRZI
def binary_to_nrzi(binary):
    nrzi = []
    for bit in binary:
        if bit == '0':
            nrzi.append(False)
        else:
            nrzi.append(True)
    return nrzi

# It is responsible for creating the NRZ chart
def generate_nrzi_image(nrzi_data, image_path, estado):
    image_width = 800
    image_height = 400
    
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)
    
    y_i = image_height // 2
    x_i = 100

    if estado == 1:
        y1 = y_i - 100
        draw.line((0, y_i - 100, 100, y_i - 100), fill='black', width = 2)
    else:
        draw.line((0, y_i + 100, 100, y_i + 100), fill='black', width = 2)
        y1 = y_i + 100

    draw.line((0, y_i, image_width , y_i), fill='black')
    draw.line((x_i, 0, x_i , image_height), fill='black')
    
    for i in range(len(nrzi_data) ):

        x0 = (i * 50) + x_i
        x1 = x0
        g = nrzi_data[i]

        if x0 != 100:
            draw.line((x0, 50, x0, 350), fill='blue', width = 1)

        if g == True:
            draw.text((x0+25,50), "1", "black")
            if y1 == 300:
              y1 = y1 - 200
              draw.line((x0, 300, x1, y1), fill='red', width = 4)
              x1 = x1 + 50
              draw.line((x0, y1, x1 , y1), fill='red', width = 4)
            else:
                y1 = y1 + 200
                draw.line((x0, 100, x1, y1), fill='red', width = 4)
                x1 = x1 + 50
                draw.line((x0, y1, x1 , y1), fill='red', width = 4)
        else:
            draw.text((x0+25,50), "0", "black")
            if y1 == 300:
                x1 = x0 + 50
                draw.line((x0, 300, x1, y1), fill='red', width = 4)
            else:
                x1 = x0 + 50
                draw.line((x0, 100, x1, y1), fill='red', width = 4)
    image.save(image_path)

# It is in charge of saving and presenting the NRZI graph
def create_nrzi(binary,estado):
    nrzi_data = binary_to_nrzi(binary)
    image_path = "nrzi_image.png"
    generate_nrzi_image(nrzi_data, image_path, estado)
    img = Image.open("nrzi_image.png")
    img.show()


"""
xor para calcular los numeros de paridad

"""

def xor(input_list):
    resultado = None
    for o in input_list:
        if o is not None:
            if resultado is None:
                resultado = o
            else:
                resultado ^= o

    return resultado

"""
inversor para pasar de paridad par a impar

"""
def invertir(bit):
    if bit == 0:
        return 1
    elif bit == 1:
        return 0
"""
algoritmo de paridad, recibe la lista de datos y la paridad par/impar
crea una lista para cada linea de paridad y le aplica la operación xor
luego agrega todos los bits de paridad a una lista segun su paridad y la retorna
"""

def calcular_bits_paridad(lista_bits, paridad):
    p1= []
    p2= []
    p3= []
    p4= []
    lista_final= []
    #crear la lista para calcular p1
    for t in range(12):
        
        if t in P1:
            p1.append(lista_bits[t])
            
            
    #crear la lista para calcular p2
    for s in range(12):
        
        if s in P2:
            p2.append(lista_bits[s])
    
    
    #crear la lista para calcular p3
    for f in range(12):
        
        if f in P3:
           p3.append(lista_bits[f])
            
            
    #crear la lista para calcular p4
    
    for y in range(12):
        
        if y in P4:
            p4.append(lista_bits[y])

    if (paridad == 'par'):
        lista_final=[xor(p1),xor(p2),xor(p3),xor(p4),lista_bits[11]]
        return lista_final
    else:
        lista_final=[invertir(xor(p1)),invertir(xor(p2)),invertir(xor(p3)),invertir(xor(p4))
                     ,invertir(lista_bits[11])]
        return lista_final

"""
une la lista de paridad y la de datos en el codigo completo

"""
def crear_hamming_completo(list1, list2):

    combined_list = [None] * 17

    positions_to_fill = [0, 1, 3, 7, 15]

    for pos, value in zip(positions_to_fill, list1):
        combined_list[pos] = value
    
    list2_index = 0
    for i in range(len(combined_list)):
        if combined_list[i] is None:
            combined_list[i] = list2[list2_index]
            list2_index += 1

    return combined_list

"""
invierte los bits de paridad y realiza la operación xor sobre ellos para obtener 
el numero binario que indica el lugar del error, luego pasa el binario a decimal y lo retorna



"""
    
def calcular_error(a, b):
    xor_result = []
    a = list(reversed(a))
    b = list(reversed(b))
    for bit_a, bit_b in zip(a, b):
        xor_result.append(bit_a ^ bit_b)
    
    binary_string = ''.join(map(str, xor_result))
    decimal_result = int(binary_string, 2)
    
    return decimal_result

def check_parity(a,b, word):
    if a == b:
        if word == 1:
            return 0
        return str('Correcto')
    else:
        if word == 1:
            return 1
        return str('Error')

def check_error(pos):
    if pos == 0:
        return 'No presenta error'
    else:
        return "El Bit Erroneo se Encuentra en la Posicion " + str(pos)

def fixed(error_data,pos):
    if pos != 0:
        if error_data[pos-1] == 1:
            error_data[pos-1] = 0
        else:
            error_data[pos-1] = 1
    fixed =[]
    positions_to_fill = [0, 1, 3, 7, 15]
    for x in range(len(error_data)):
        if not x in positions_to_fill:
            fixed.append(error_data[x])
    return str(listToString(fixed))
    
    
# Hamming Window Config
def w_hamming(window_to_destroy, binary, parity):
    window_hamming = tk.Tk()
    window_hamming.title("Hamming")
    
    bits = []
    if len(binary) != 12:
        for x in range(12 - len(binary)):
            bits.append(0)
    for bit in binary:
        if bit == '0':
            bits.append(0)
        else:
            bits.append(1)
    
    bit_parity= calcular_bits_paridad(bits, parity)
    bit_complete= crear_hamming_completo(bit_parity, bits)
    
    ttk.Button(window_hamming, text="Nuevo numero"
               , command=lambda: refresh(window_hamming)).place(x=915, y=250)
    ttk.Label(window_hamming, text="Binario: " + str(binary)).place(x=450, y=10)
    ttk.Label(window_hamming, text="Paridad: " + str.capitalize(parity)).place(x=460, y=40)

    table_hamming = ttk.Treeview(window_hamming, column=("c1", "c2" , "c3", "c4", "c5", "c6", "c7"
                                                         , "c8", "c9", "c10", "c11", "c12", "c13"
                                                         , "c14", "c15", "c16", "c17","c18")
                                 , show='headings', height=7)
    table_hamming.column("# 1", anchor=tk.CENTER, width=130)
    table_hamming.heading("# 1", text="")
    table_hamming.column("# 2", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 2", text="p1")
    table_hamming.column("# 3", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 3", text="p2")
    table_hamming.column("# 4", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 4", text="d1")
    table_hamming.column("# 5", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 5", text="p3")
    table_hamming.column("# 6", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 6", text="d2")
    table_hamming.column("# 7", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 7", text="d3")
    table_hamming.column("# 8", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 8", text="d4")
    table_hamming.column("# 9", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 9", text="p4")
    table_hamming.column("# 10", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 10", text="d5")
    table_hamming.column("# 11", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 11", text="d6")
    table_hamming.column("# 12", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 12", text="d7")
    table_hamming.column("# 13", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 13", text="d8")
    table_hamming.column("# 14", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 14", text="d9")
    table_hamming.column("# 15", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 15", text="d10")
    table_hamming.column("# 16", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 16", text="d11")
    table_hamming.column("# 17", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 17", text="p5")
    table_hamming.column("# 18", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming.heading("# 18", text="d12")

    table_hamming.insert('', 'end', text="1", values=('Numero sin paridad: ','','',str(bits[0]),''
                                                      ,str(bits[1]),str(bits[2]),str(bits[3]),''
                                                      ,str(bits[4]),str(bits[5]),str(bits[6])
                                                      ,str(bits[7]),str(bits[8]),str(bits[9])
                                                      ,str(bits[10]),'',str(bits[11])))
    table_hamming.insert('', 'end', text="2", values=('P1',str(bit_complete[0]),'',str(bits[0]),''
                                                      ,str(bits[1]),'',str(bits[3]),'',str(bits[4]),''
                                                      ,str(bits[6]),'',str(bits[8]),'',str(bits[10])
                                                      ,'',str(bits[11])))
    table_hamming.insert('', 'end', text="3", values=('P2','',str(bit_complete[1]),str(bits[0]),'',''
                                                      ,str(bits[2]),str(bits[3]),'','',str(bits[5])
                                                      ,str(bits[6]),'','',str(bits[9]),str(bits[10])
                                                      ,'',''))
    table_hamming.insert('', 'end', text="4", values=('P3','','','',str(bit_complete[3]),str(bits[1])
                                                      ,str(bits[2]),str(bits[3]),'','','',''
                                                      ,str(bits[7]),str(bits[8]),str(bits[9])
                                                      ,str(bits[10]),'',''))
    table_hamming.insert('', 'end', text="5", values=('P4','','','','','','','',str(bit_complete[7])
                                                      ,str(bits[4]),str(bits[5]),str(bits[6])
                                                      ,str(bits[7]),str(bits[8]),str(bits[9])
                                                      ,str(bits[10]),'',''))
    table_hamming.insert('', 'end', text="6", values=('P5','','','','','','','','','','','','','',''
                                                      ,'',str(bit_complete[15]),str(bits[11])))
    table_hamming.insert('', 'end', text="7", values=('Numero con paridad: ',str(bit_complete[0])
                                                      ,str(bit_complete[1]),str(bit_complete[2])
                                                      ,str(bit_complete[3]),str(bit_complete[4])
                                                      ,str(bit_complete[5]),str(bit_complete[6])
                                                      ,str(bit_complete[7]),str(bit_complete[8])
                                                      ,str(bit_complete[9]),str(bit_complete[10])
                                                      ,str(bit_complete[11]),str(bit_complete[12])
                                                      ,str(bit_complete[13]),str(bit_complete[14])
                                                      ,str(bit_complete[15]),str(bit_complete[16])))
    table_hamming.place(x=25,y=70)

    ttk.Label(window_hamming, text="Bit con Paridad: "
              + str(listToString(bit_complete))).place(x=25, y=250)
    
    separator_error = ttk.Separator(master=window_hamming, orient=tk.HORIZONTAL)
    separator_error.place(relx=0, rely=0.76, relheight=1, relwidth=1)
    
    ttk.Label(window_hamming, text="Modificador para simular error").place(x=450, rely=0.74)
    
    ttk.Label(window_hamming, text="Ingrese Bit con Error : ").place(x=65, y=310)
    error_box = ttk.Entry(window_hamming)
    error_box.insert(0,binary)
    error_box.place(x=184, y=310, width=120)
    
    error_label = ttk.Label(window_hamming)
    error_label.place(x=65, y=340)
    
    ttk.Button(window_hamming, text="Buscar Error de Bit"
               ,command=lambda: check_hamming_error(window_hamming,binary,bit_parity,parity
                                              ,str(error_box.get()),error_label)).place(x=320, y=310)

    center_window(1050, 380, window_hamming)
    window_to_destroy.destroy()

def check_hamming_error(window_to_destroy, binary, bit_w_parity, parity, bit_error,label):
    try:
        int(bit_error, 2)
        if len(str(binary)) != len(str(bit_error)):
            label.config(
                text="❌ Error: El largo del numero no se puede modificar."
                , foreground='#f00')
        else:
            hamming_error(window_to_destroy, binary, bit_w_parity, parity, bit_error)
    except:
        if len(str(binary)) != len(str(bit_error)):
            label.config(
                text="❌ Error: El numero tiene que ser binario y no se puede modificar el largo."
                , foreground='#f00')
        else:
            label.config(
                text="❌ Error: El numero tiene que ser binario."
                , foreground='#f00')

def hamming_error(window_to_destroy, binary, bit_w_parity, parity, bit_error):
    hamming_error= tk.Tk()
    hamming_error.title("Hamming Error")
    
    bits_error = []
    if len(bit_error) != 12:
        for x in range(12 - len(bit_error)):
            bits_error.append(0)
    for bit in bit_error:
        if bit == '0':
            bits_error.append(0)
        else:
            bits_error.append(1)
    
    bit_parity_error = calcular_bits_paridad(bits_error, parity)
    bit_error_complete= crear_hamming_completo(bit_parity_error, bits_error)
    
    table_hamming_error = ttk.Treeview(hamming_error, column=("c1", "c2" , "c3", "c4", "c5", "c6"
                                                              , "c7", "c8", "c9", "c10", "c11", "c12"
                                                              , "c13", "c14", "c15", "c16", "c17"
                                                              , "c18", "c19", "c20"), show='headings'
                                       , height=6)
    table_hamming_error.column("# 1", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 1", text="")
    table_hamming_error.column("# 2", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 2", text="p1")
    table_hamming_error.column("# 3", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 3", text="p2")
    table_hamming_error.column("# 4", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 4", text="d1")
    table_hamming_error.column("# 5", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 5", text="p3")
    table_hamming_error.column("# 6", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 6", text="d2")
    table_hamming_error.column("# 7", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 7", text="d3")
    table_hamming_error.column("# 8", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 8", text="d4")
    table_hamming_error.column("# 9", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 9", text="p4")
    table_hamming_error.column("# 10", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 10", text="d5")
    table_hamming_error.column("# 11", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 11", text="d6")
    table_hamming_error.column("# 12", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 12", text="d7")
    table_hamming_error.column("# 13", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 13", text="d8")
    table_hamming_error.column("# 14", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 14", text="d9")
    table_hamming_error.column("# 15", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 15", text="d10")
    table_hamming_error.column("# 16", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 16", text="d11")
    table_hamming_error.column("# 17", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 17", text="p5")
    table_hamming_error.column("# 18", anchor=tk.CENTER, minwidth=0, width=48)
    table_hamming_error.heading("# 18", text="d12")
    table_hamming_error.column("# 19", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 19", text="Prueba de Paridad")
    table_hamming_error.column("# 20", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 20", text="Bit de Comprobacion")

    table_hamming_error.insert('', 'end', text="1", values=('Numero sin paridad: ','',''
                                                            ,str(bits_error[0]),'',str(bits_error[1])
                                                            ,str(bits_error[2]),str(bits_error[3])
                                                            ,'',str(bits_error[4]),str(bits_error[5])
                                                            ,str(bits_error[6]),str(bits_error[7])
                                                            ,str(bits_error[8]),str(bits_error[9])
                                                            ,str(bits_error[10]),''
                                                            ,str(bits_error[11])
                                                            ,str.capitalize(parity),''))
    table_hamming_error.insert('', 'end', text="2", values=('P1',str(bit_w_parity[0]),''
                                                            ,str(bits_error[0]),'',str(bits_error[1])
                                                            ,'',str(bits_error[3]),''
                                                            ,str(bits_error[4]),'',str(bits_error[6])
                                                            ,'',str(bits_error[8]),''
                                                            ,str(bits_error[10]),''
                                                            ,str(bits_error[11])
                                                            ,check_parity(bit_parity_error[0]
                                                                          ,bit_w_parity[0],0)
                                                            ,str(check_parity(bit_parity_error[0]
                                                                              ,bit_w_parity[0],1))))
    table_hamming_error.insert('', 'end', text="3", values=('P2','',str(bit_w_parity[1])
                                                            ,str(bits_error[0]),'',''
                                                            ,str(bits_error[2]),str(bits_error[3]),''
                                                            ,'',str(bits_error[5]),str(bits_error[6])
                                                            ,'','',str(bits_error[9])
                                                            ,str(bits_error[10]),'',''
                                                            ,check_parity(bit_parity_error[1]
                                                                          ,bit_w_parity[1],0)
                                                            ,str(check_parity(bit_parity_error[1]
                                                                              ,bit_w_parity[1],1))))
    table_hamming_error.insert('', 'end', text="4", values=('P3','','','',str(bit_w_parity[2])
                                                            ,str(bits_error[1]),str(bits_error[2])
                                                            ,str(bits_error[3]),'','','',''
                                                            ,str(bits_error[7]),str(bits_error[8])
                                                            ,str(bits_error[9]),str(bits_error[10])
                                                            ,'','',check_parity(bit_parity_error[2]
                                                                                ,bit_w_parity[2],0)
                                                            ,str(check_parity(bit_parity_error[2]
                                                                              ,bit_w_parity[2],1))))
    table_hamming_error.insert('', 'end', text="5", values=('P4','','','','','','',''
                                                            ,str(bit_w_parity[3]),str(bits_error[4])
                                                            ,str(bits_error[5]),str(bits_error[6])
                                                            ,str(bits_error[7]),str(bits_error[8])
                                                            ,str(bits_error[9]),str(bits_error[10])
                                                            ,'','',check_parity(bit_parity_error[3]
                                                                                ,bit_w_parity[3],0)
                                                            ,str(check_parity(bit_parity_error[3]
                                                                              ,bit_w_parity[3],1))))
    table_hamming_error.insert('', 'end', text="6", values=('P5','','','','','','','','','','','',''
                                                            ,'','','',str(bit_w_parity[4])
                                                            ,str(bits_error[11])
                                                            ,check_parity(bit_parity_error[4]
                                                                          ,bit_w_parity[4],0)
                                                            ,str(check_parity(bit_parity_error[4]
                                                                              ,bit_w_parity[4],1))))
    table_hamming_error.pack()

    pos_error = calcular_error(bit_w_parity, bit_parity_error)
    
    ttk.Label(hamming_error, text=check_error(pos_error)).place(x=30, y=155)
    ttk.Label(hamming_error, text="Bit ingresado sin error: "+str(binary)).place(x=1000, y=182)
    ttk.Label(hamming_error, text="Bit ingresado con error: "+str(bit_error)).place(x=995, y=200)
    ttk.Label(hamming_error, text="El Numero Correcto Deberia Ser : "
              + fixed(bit_error_complete,pos_error)).place(x=30, y=185)
    ttk.Button(hamming_error, text="Nuevo numero"
               , command=lambda: refresh(hamming_error)).place(x=1095, y=155)
    center_window(1200, 230, hamming_error)
    window_to_destroy.destroy()


# Conversor Window Config
def conversor():
    window_conversor = tk.Tk()
    window_conversor.title("Conversor Hexadecimal")
    
    hexadecimal = hexadecimal_box.get()
    binary_number = str(bin(int(hexadecimal, 16))[2:])
    
    table_conversor = ttk.Treeview(window_conversor, column=("c1", "c2"), show='headings', height=5)
    table_conversor.column("# 1", anchor=tk.CENTER)
    table_conversor.heading("# 1", text="Base")
    table_conversor.column("# 2", anchor=tk.CENTER)
    table_conversor.heading("# 2", text="Valor")
    table_conversor.insert('', 'end', text="1", values=('Hexadecimal', str(hexadecimal).upper()))
    table_conversor.insert('', 'end', text="2", values=('Octal', str(oct(int(hexadecimal, 16))[2:])))
    table_conversor.insert('', 'end', text="3", values=('Binario', binary_number))
    table_conversor.insert('', 'end', text="4", values=('Decimal', int(hexadecimal, 16)))

    table_conversor.pack()
    
    ttk.Button(window_conversor, text="Nuevo numero"
               , command=lambda: refresh(window_conversor)).place(x=322, y=135)
    
    separator_grafic = ttk.Separator(master=window_conversor, orient=tk.HORIZONTAL)
    separator_grafic.place(relx=0, rely=0.51, relheight=1, relwidth=1)
    
    ttk.Label(window_conversor, text="Grafica NRZI").place(x=180, y=159)
    
    ttk.Button(window_conversor, text="Grafica NRZI con estado bajo antes de t=0"
               , command=lambda: create_nrzi(binary_number, 0)).place(relx=0.25, y=185)
    ttk.Button(window_conversor, text="Grafica NRZI con estado alto antes de t=0"
               , command=lambda: create_nrzi(binary_number, 1)).place(x=107, y=220)
    
    separator = ttk.Separator(master=window_conversor, orient=tk.HORIZONTAL)
    separator.place(relx=0, rely=0.80, relheight=1, relwidth=1)
    
    ttk.Label(window_conversor, text="Hamming").place(x=185, y=253)
    
    ttk.Button(window_conversor, text="Paridad: Par"
               , command=lambda: w_hamming(window_conversor, binary_number, 'par')).place(x=100
                                                                                          , y=285)
    ttk.Button(window_conversor, text="Paridad: Impar"
               , command=lambda: w_hamming(window_conversor, binary_number, 'impar')).place(x=240
                                                                                            , y=285)
    
    center_window(420, 330, window_conversor)
    window_main.destroy()
    
# Main Window Config
def Start_gui():
    global window_main, label_error, hexadecimal_box
    window_main = tk.Tk()
    window_main.title("Conversor Hexadecimal")
    
    center_window(420, 60, window_main)

    ttk.Label(window_main,text="Ingrese un número hexadecimal de 3 bits: ").place(x=20, y=20)

    hexadecimal_box = ttk.Entry()
    hexadecimal_box.place(x=250, y=20, width=60)

    ttk.Button(text="Convertir", command=check).place(x=320, y=18)

    label_error = ttk.Label()
    label_error.place(x=20, y=60)

    window_main.mainloop()

# It is responsible for refresh the app
def refresh(window_to_destroy):
        window_to_destroy.destroy()
        Start_gui()

Start_gui()