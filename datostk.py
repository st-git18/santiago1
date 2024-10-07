import tkinter as tk
from tkinter import messagebox
import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname = 'santiago',
            user ='postgres',
            password ='santiago',
            host = 'localhost',
            port ='5432',
        )
        print("conectado exitosamente ")
        return Conn
    except psycopg2.error as e:
        messagebox.showerror("error de conecion", f"no se puede conectar a la base de datos {e} ")
        exit()

def agregar_venta():
    id = entry_id.get()
    nombre = entry_nombre.get()
    venta = entry_venta.get()
    sucursal = entry_sucursal.get()
    
    if nombre and venta and sucursal:
        try:
            conn = conectar_db()
            c = conn.cursor()
            c.execute("INSERT INTO venta (id, nombre, venta, sucursal) values (%s, %s, %s, %s)",
            (id, nombre, venta, sucursal))
            conn.commit()
            c.close()
            conn.close()
            messagebox.showinfo("exito","venta registrada correctamenta")
            limpiar_formulario()
        except psycopg2.error as e:
            messagebox.showerror("error",f"error al agregar la venta: {e}")
    else:
        messagebox.showarning("advertencia", "por favor, completar todos los campos")

def limpiar_formulario():
    entry_id.delete(0,tk.END)
    entry_nombre.delete(0,tk.END)
    entry_venta.delete(0, tk.END)
    entry_sucursal.delete(0, tk.END)

def abrir_venta_consulta():
    consulta_ventana = tk.Toplevel(root)
    consulta_ventana.title("consulta de ventas por ID")
    consulta_ventana.geometry("300x200")
    consulta_ventana.config(
        fg="purple",
        bg="red"
    )
def actualizar_venta():
    messagebox.showinfo("actualizar venta","funcionalidad de actualizar venta aun no implementada.")

def eliminar_venta():
    messagebox.showinfo("eliminar venta","funcionalidad de eliminar venta aun no implementada.")

    tk.Label(consulta_ventana, text="ingrese el ID").pack(pady=10)
    entry_id_consulta = tk.Entry(conectar_ventana)
    entry_id_consulta.pack()

    def consultar():
        id_consultar = tk.entry_id_consulta.get()
        if id_consulta:
            try:
                conn = conectar_db()  
                c = conn.cursor()
                c.execute('SELECT * FROM ventas WHERE id = %s', (id_consulta,))
                resultados = c.fetchall()
               
                c.close()
                conn.close()
            except psycopg2.Error as e:
                messagebox.showerror('Error', f'Error al consultar: {e}')

root = tk.Tk
root.title("registro de venta")
root.geometry("700x500")

tk.Label(root, text='ID').pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text='Nombre').pack(pady=5) 
entry_nombre = tk.Entry(root)  
entry_nombre.pack()

tk.Label(root, text='Venta').pack(pady=5)    
entry_venta = tk.Entry(root)
entry_venta.pack()

tk.Label(root, text='Sucursal').pack(pady=5)   
entry_sucursal = tk.Entry(root)
entry_sucursal.pack()

btn_agregar = tk.Button(root, text='Agregar Venta', command=agregar_venta)
btn_agregar.pack(pady=10)


btn_consultar = tk.Button(root, text='Consultar Venta por ID', command=abrir_ventana_consulta)
btn_consultar.pack(pady=10)

btn_actualizar = tk.Button(root, text='Actualizar Venta', command=actualizar_venta)
btn_actualizar.pack(pady=10)

btn_eliminar = tk.Button(root, text='Eliminar Venta', command=eliminar_venta)
btn_eliminar.pack(pady=10)


root.mainloop()

