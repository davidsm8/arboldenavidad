# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:21:11 2023

@author: david
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def conical_spiral_arc_length(phi, a, m, phi_1, phi_2):
    integrand = lambda phi: np.sqrt((1 + m**2) * (a**2 * phi**2 + 1))
    result, _ = quad(integrand, phi_1, phi_2)
    return result

def generate_conical_spiral(phi, a, m, height, phi_1, phi_2):
    z = np.linspace(phi_1, phi_2, len(phi))
    x = a * z * np.cos(z)
    y = a * z * np.sin(z)
    z = height - m * z  # Height - m * phi to decrease as Z decreases
    return x, y, z

def derive_parameters(largest_radius, height, turns):
    a = largest_radius / (2 * np.pi * turns)
    m = height / (2 * np.pi * turns)
    spacing_z = height / turns  # Calculate the spacing between turns in Z-axis
    spacing_phi = 2 * np.pi * largest_radius / turns  # Calculate the spacing between turns in phi
    return a, m, spacing_z, spacing_phi
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        # Solicitar parámetros al usuario
        largest_radius = get_float_input("Ingrese el radio del arbol en metros: ")
        height = get_float_input("Ingrese la altura del arbol en metros: ")
        turns = get_float_input("Ingrese el número de vueltas de luces que desea: ")

        # Derivar parámetros adicionales
        a, m, spacing_z, spacing_phi = derive_parameters(largest_radius, height, turns)

        # Calcular longitud del arco
        total_length = conical_spiral_arc_length(np.linspace(0, 2 * np.pi * turns, 1000), a, m, 0, 2 * np.pi * turns)

        print(f"\nTotal longitud de luces requerida: {total_length:.4f} m")
        print(f"Espaciado entre vueltas: {spacing_z:.4f} m")

        # Generar coordenadas de la espiral cónica
        phi_values = np.linspace(0, 2 * np.pi * turns, 1000)
        x, y, z = generate_conical_spiral(phi_values, a, m, height, 0, 2 * np.pi * turns)

        # Graficar la espiral cónica
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, label='Luces de arbol navideño')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()

        # Preguntar si se desea realizar otra visualización
        repeat = input("¿Desea realizar otra visualización? (Sí/No): ").lower()
        if repeat != 'si' and repeat != 'sí':
            break

if __name__ == "__main__":
    main()
