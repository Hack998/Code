import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw

# Funcions

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
            label_error.config(text="❌ Error: El número hexadecimal debe tener exactamente 3 dígitos.", foreground='#f00')
        else:
            conversor()
    except:
        if len(str(hexadecimal_box.get())) != 3:
            label_error.config(text="❌ Error: Introduzca un número hexadecimal válido y de exactamente 3 dígitos.", foreground='#f00')
            center_window(460, 100, window_main)
        else:
            label_error.config(text="❌ Error: Introduzca un número hexadecimal válido.", foreground='#f00')
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

# Hamming Window Config
def w_hamming(window_to_destroy, binary, parity):
    window_hamming = tk.Tk()
    window_hamming.title("Hamming")
    
    ttk.Button(window_hamming, text="Nuevo numero", command=lambda: refresh(window_hamming)).place(x=935, y=230)
    ttk.Label(window_hamming, text="Binario: " + str(binary)).place(x=450, y=10)
    ttk.Label(window_hamming, text="Paridad: " + str.capitalize(parity)).place(x=460, y=40)

    table_hamming = ttk.Treeview(window_hamming, column=("c1", "c2" , "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16", "c17"), show='headings', height=6)
    table_hamming.column("# 1", anchor=tk.CENTER)
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
    table_hamming.heading("# 17", text="d12")

    table_hamming.insert('', 'end', text="1", values=('Numero sin paridad: ','','','','','','','','','','','','','','','',''))
    table_hamming.insert('', 'end', text="2", values=('P1','','','','','','','','','','','','','','','',''))
    table_hamming.insert('', 'end', text="3", values=('P2','','','','','','','','','','','','','','','',''))
    table_hamming.insert('', 'end', text="4", values=('P3','','','','','','','','','','','','','','','',''))
    table_hamming.insert('', 'end', text="5", values=('P4','','','','','','','','','','','','','','','',''))
    table_hamming.insert('', 'end', text="6", values=('Numero con paridad: ','','','','','','','','','','','','','','','',''))
    table_hamming.place(x=25,y=70)

    separator_error = ttk.Separator(master=window_hamming, orient=tk.HORIZONTAL)
    separator_error.place(relx=0, rely=0.70, relheight=1, relwidth=1)
    
    ttk.Label(window_hamming, text="Modificador para simular error").place(x=450, rely=0.68)
    ttk.Label(window_hamming, text="Bit con Paridad: "+ str(binary)).place(x=65, y=280)
    ttk.Label(window_hamming, text="Ingrese Bit con Error : ").place(x=65, y=310)
    error_box = ttk.Entry(window_hamming)
    error_box.insert(0,str(binary))
    error_box.place(x=184, y=310, width=100)
    ttk.Button(window_hamming, text="Buscar Error de Bit",command=lambda: hamming_error(window_hamming,binary,parity,binary)).place(x=300, y=310)

    center_window(1050, 380, window_hamming)
    window_to_destroy.destroy()

def hamming_error(window_to_destroy, bit_w_parity, parity, bit_error):
    hamming_error= tk.Tk()
    hamming_error.title("Hamming Error")
    table_hamming_error = ttk.Treeview(hamming_error, column=("c1", "c2" , "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16", "c17", "c18", "c19"), show='headings', height=5)
    table_hamming_error.column("# 1", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 1", text="")
    table_hamming_error.column("# 2", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 2", text="p1")
    table_hamming_error.column("# 3", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 3", text="p2")
    table_hamming_error.column("# 4", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 4", text="d1")
    table_hamming_error.column("# 5", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 5", text="p3")
    table_hamming_error.column("# 6", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 6", text="d2")
    table_hamming_error.column("# 7", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 7", text="d3")
    table_hamming_error.column("# 8", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 8", text="d4")
    table_hamming_error.column("# 9", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 9", text="p4")
    table_hamming_error.column("# 10", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 10", text="d5")
    table_hamming_error.column("# 11", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 11", text="d6")
    table_hamming_error.column("# 12", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 12", text="d7")
    table_hamming_error.column("# 13", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 13", text="d8")
    table_hamming_error.column("# 14", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 14", text="d9")
    table_hamming_error.column("# 15", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 15", text="d10")
    table_hamming_error.column("# 16", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 16", text="d11")
    table_hamming_error.column("# 17", anchor=tk.CENTER, minwidth=0, width=50)
    table_hamming_error.heading("# 17", text="d12")
    table_hamming_error.column("# 18", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 18", text="Prueba de Paridad")
    table_hamming_error.column("# 19", anchor=tk.CENTER, width=120)
    table_hamming_error.heading("# 19", text="Bit de Comprobacion")

    table_hamming_error.insert('', 'end', text="1", values=('Numero sin paridad: ','','','','','','','','','','','','','','','',''))
    table_hamming_error.insert('', 'end', text="2", values=('P1','','','','','','','','','','','','','','','','','',''))
    table_hamming_error.insert('', 'end', text="3", values=('P2','','','','','','','','','','','','','','','','','',''))
    table_hamming_error.insert('', 'end', text="4", values=('P3','','','','','','','','','','','','','','','','','',''))
    table_hamming_error.insert('', 'end', text="5", values=('P4','','','','','','','','','','','','','','','','','',''))
    table_hamming_error.pack()

    ttk.Label(hamming_error, text="El Bit Erroneo se Encuentra en : ").place(x=30, y=130)
    ttk.Label(hamming_error, text="El Numero Correcto Deberia Ser : ").place(x=30, y=160)
    ttk.Button(hamming_error, text="Nuevo numero", command=lambda: refresh(hamming_error)).place(x=1090, y=130)
    center_window(1200, 200, hamming_error)
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
    
    ttk.Button(window_conversor, text="Nuevo numero", command=lambda: refresh(window_conversor)).place(x=322, y=135)
    
    separator_grafic = ttk.Separator(master=window_conversor, orient=tk.HORIZONTAL)
    separator_grafic.place(relx=0, rely=0.51, relheight=1, relwidth=1)
    
    ttk.Label(window_conversor, text="Grafica NRZI").place(x=180, y=159)
    
    ttk.Button(window_conversor, text="Grafica NRZI con estado bajo antes de t=0", command=lambda: create_nrzi(binary_number, 0)).place(relx=0.25, y=185)
    ttk.Button(window_conversor, text="Grafica NRZI con estado alto antes de t=0", command=lambda: create_nrzi(binary_number, 1)).place(x=107, y=220)
    
    separator = ttk.Separator(master=window_conversor, orient=tk.HORIZONTAL)
    separator.place(relx=0, rely=0.80, relheight=1, relwidth=1)
    
    ttk.Label(window_conversor, text="Hamming").place(x=185, y=253)
    
    ttk.Button(window_conversor, text="Paridad: Par", command=lambda: w_hamming(window_conversor, binary_number, 'par')).place(x=100, y=285)
    ttk.Button(window_conversor, text="Paridad: Impar", command=lambda: w_hamming(window_conversor, binary_number, 'impar')).place(x=240, y=285)
    
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