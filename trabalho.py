import numpy as np
from sympy import symbols, Function, sympify, lambdify
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk


def runge_kutta_4th_order(f, x0, y0, x_max, n):
    try:
        h = (x_max - x0) / n
        x_values = np.linspace(x0, x_max, n+1)
        y_values = np.zeros(n+1)
        y_values[0] = y0

        for i in range(n):
            x = x_values[i]
            y = y_values[i]
            k1 = h * f(x, y)
            k2 = h * f(x + h/2, y + k1/2)
            k3 = h * f(x + h/2, y + k2/2)
            k4 = h * f(x + h, y + k3)
            y_values[i+1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6

        return x_values, y_values
    except ValueError or TypeError or SyntaxError:
        messagebox.showerror("ERRO", "Invalido")

def runge_kutta_2nd_order(f, x0, y0, x_max, n):
    h = (x_max - x0)/n
    x_values = np.linspace(x0, x_max,n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x,y)
        k2 = h * f(x + h, y + k1)
        y_values[i+1] = y + (h/2)*(k1+k2)
    
    return x_values, y_values

def runge_kutta_6th_order(f, x0, y0, x_max, n):
    h =(x_max- x0)/n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x,y)
        k2 = h * f(x + h/3, y + k1/3)
        k3 = h * f(x + (2*h/3), y + 2*k2/3)
        k4 = h * f(x + h/3, y + k1/12 + k2/3 - k3/12)
        k5 = h * f(x + h/2, y - k1/12 + (9*k2/8) - (3*k3/16) - (3*k4/8))
        k6 = h * f(x + h/2, y - (9*k2/8) - (3*k3/8) - (3*k4/4) + k5/2)
        k7 = h * f(x + h, y + (9*k1/44) - (9*k2/11) + (63*k3/44) + (18*k4/11) - (16*k6/11))
        y_values[i+1] = y + ((11*k1/120) + (27*k3/40) + (27*k4/40) - (4*k5/15) - (4*k6/15) + (11*k7/120))

    return x_values, y_values

def euler(f, x0, y0, x_max, n):
    h = (x_max - x0)/n
    x_values = np.linspace(x0,x_max,n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        y_values[i+1] = y + h*f(x,y)

    return x_values, y_values

def heun(f, x0, y0, x_max, n):
    h = (x_max - x0)/n
    x_values = np.linspace(x0, x_max, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        y_values[i+1] = y + (1/2) * (f(x,y)+f(x+h, y + h*f(x,y)))

    return x_values, y_values

'''def rkf45(f, x0, y0, x_max, tol):
    h = 0.01  # Initial step size
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    while x < x_max:
        if x + h > x_max:
            h = x_max - x
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/4, y + k1/4)
        k3 = h * f(x + 3*h/8, y + 3*k1/32 + 9*k2/32)
        k4 = h * f(x + 12*h/13, y + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
        k5 = h * f(x + h, y + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
        k6 = h * f(x + h/2, y - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)
        
        y_rk4 = y + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5
        y_rk5 = y + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55

        error = np.abs(y_rk5 - y_rk4)
        
        if error <= tol:
            x += h
            y = y_rk5
            x_values.append(x)
            y_values.append(y)
        
        h = h * min(max(0.84 * (tol / error)**0.25, 0.1), 4.0)
    
    return np.array(x_values), np.array(y_values)'''

def solve_edo1(equation_str, x0, y0, x_final, n, method, tol=None):
    try:
        x, y = symbols('x y')
        derivative_expr = sympify(equation_str)
        f = lambdify((x, y), derivative_expr, modules=['numpy'])

        if method == 'RK4':
            return runge_kutta_4th_order(f, x0, y0, x_final, n)
        elif method == 'RK2':
            return runge_kutta_2nd_order(f, x0, y0, x_final, n)
        elif method == 'RK6':
            return runge_kutta_6th_order(f, x0, y0, x_final, n)
        elif method == 'Euler':
            return euler(f, x0, y0, x_final, n)
        elif method == 'Heun':
            return heun(f, x0, y0, x_final, n)
        else:
            raise ValueError("Método desconhecido")
    except ValueError or TypeError or SyntaxError:
        messagebox.showerror("Error", "Invalido")

def save_to_csv(x_values, y_values):
    df = pd.DataFrame({'x': x_values, 'y': y_values})
    df.to_csv('valores_x_y.csv', index=False)
    messagebox.showinfo("Salvar", "Dados salvos em 'valores_x_y.csv'")

def calcular_erros_globais(true_solution, x_values, y_values):
    real_y_values = true_solution(x_values)
    error = np.abs(real_y_values - y_values)
    global_error = np.sum(error)
    return global_error

def comparar_erros(equation_str, x0, y0, x_final, n):
    x, y = symbols('x y')
    derivate_expr = sympify(equation_str)
    f = lambdify((x,y), derivate_expr, modules = ['numpy'])

    try:
        true_solution_expr = sympify(true_solution_entry.get())
        true_solution = lambdify(x, true_solution_expr, modules=['numpy'])
    except (SyntaxError, ValueError):
        messagebox.showerror("Erro", "Solução exata inválida")
        return None

    methods = ['RK4', 'RK2', 'RK6', 'Euler', 'Heun']
    errors = {}

    for method in methods:
        x_values, y_values = solve_edo1(equation_str, x0, y0, x_final, n, method)
        error = calcular_erros_globais(true_solution, x_values, y_values)
        errors[method] = error

    return errors

def plot_graph(x_values, y_values):
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label="y(x)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico de y em função de x")
        plt.legend()
        plt.grid(True)
        plt.show()

def run():
        equation_str = equation_entry.get()
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        x_final = float(x_final_entry.get())
        n = int(n_entry.get())
        method = method_var.get()
        #tol = float(tol_entry.get()) if method == 'RKF45' else None

        x_values, y_values = solve_edo1(equation_str, x0, y0, x_final, n, method)
        plot_graph(x_values, y_values)

        if save_var.get():
            save_to_csv(x_values, y_values)

        if error_var.get():
            errors = comparar_erros(equation_str, x0, y0, x_final, n)
            error_message = "Erros globais:\n"
            for method, error in errors.items():
                error_message += f"{method}: {error}\n"
            messagebox.showinfo("Erro Global", error_message)
    

root = ctk.CTk()
root.title("Método de Runge-Kutta para EDOs")


ctk.CTkLabel(root, text="'COLOQUE VALORES QUE ESTÃO MULTIPLICANDO ENTRE SI COM UM *. Ex: 4*x + 2*y'").pack()


ctk.CTkLabel(root, text="Digite a derivada de y (y'):").pack()
equation_entry = ctk.CTkEntry(root)
equation_entry.pack()

ctk.CTkLabel(root, text="Solução exata (y(x)):").pack()
true_solution_entry = ctk.CTkEntry(root)
true_solution_entry.pack()


ctk.CTkLabel(root, text="x0:").pack()
x0_entry = ctk.CTkEntry(root)
x0_entry.pack()

ctk.CTkLabel(root, text="y0:").pack()
y0_entry = ctk.CTkEntry(root)
y0_entry.pack()

ctk.CTkLabel(root, text="x final:").pack()
x_final_entry = ctk.CTkEntry(root)
x_final_entry.pack()

ctk.CTkLabel(root, text="Número de pontos (n):").pack()
n_entry = ctk.CTkEntry(root)
n_entry.pack()

'''ctk.CTkLabel(root, text="Tolerância (para RKF45):").pack()
tol_entry = ctk.CTkEntry(root)
tol_entry.pack()'''

method_var = ctk.StringVar(value=' ')

R4 = ctk.CTkRadioButton(root, text="Runge-Kutta 4ª Ordem", variable=method_var, value='RK4')
R2 = ctk.CTkRadioButton(root, text="Runge-Kutta 2ª Ordem", variable=method_var, value='RK2')
R6 = ctk.CTkRadioButton(root, text="Runge-Kutta 6ª Ordem", variable=method_var, value='RK6')
Euler = ctk.CTkRadioButton(root, text="Método de Euler", variable=method_var, value='Euler')
Heun = ctk.CTkRadioButton(root, text="Método de Heun", variable=method_var, value='Heun')
RFK45 = ctk.CTkRadioButton(root, text="RFK45", variable=method_var, value='RFK45')

ctk.CTkLabel(root, text="Métodos:").pack()
#ctk.CTkComboBox(root,values=methods, font=('Arial', 12)).pack()
R2.pack()
R4.pack()
R6.pack()
Euler.pack()
Heun.pack()
#RFK45.pack()

ctk.CTkLabel(root, text=" ").pack()

ctk.CTkButton(root, text="Resolver e Plotar", command=run).pack()

ctk.CTkLabel(root, text=" ").pack()

save_var = ctk.BooleanVar()
save_checkbox = ctk.CTkCheckBox(root, text="Salvar em CSV", variable=save_var)
save_checkbox.pack()

ctk.CTkLabel(root, text=" ").pack()

error_var = ctk.BooleanVar()
error_checkbox = ctk.CTkCheckBox(root, text="Calcular e comparar erro global", variable=error_var)
error_checkbox.pack()



root.geometry('500x500')

root._set_appearance_mode("dark")

#root.resizable(width=False, height=False)


root.mainloop()
