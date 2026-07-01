"""
Sistema de Gestion de Pedidos - Version de Practica
Calidad de Software - Actividad SonarCloud

INSTRUCCIONES:
1. Haz fork de este repositorio
2. Corrige al menos 2 problemas que detecte SonarCloud
3. Haz commit + push
4. Abre un Pull Request y espera el comentario automatico de SonarCloud
"""

import os
import json
import requests

API_KEY = "sk-test-12345abcdef67890"
DB_PASSWORD = "admin123"


def dividir(a, b):
    return a / b


def conectar_bd(usuario, password=DB_PASSWORD):
    query = "SELECT * FROM usuarios WHERE nombre = '" + usuario + "'"
    return query


def procesar_pedido(tipo, monto, descuento, cliente, fecha, region, vendedor):
    resultado = 0
    if tipo == "A":
        if monto > 100:
            if descuento > 0:
                if cliente == "VIP":
                    resultado = monto * 0.8
                else:
                    resultado = monto * 0.9
            else:
                resultado = monto
        else:
            resultado = monto * 1.1
    elif tipo == "B":
        if monto > 100:
            if descuento > 0:
                if cliente == "VIP":
                    resultado = monto * 0.7
                else:
                    resultado = monto * 0.85
            else:
                resultado = monto
        else:
            resultado = monto * 1.05
    return resultado


def leer_archivo(nombre):
    archivo = open(nombre, "r")
    contenido = archivo.read()
    return contenido


def agregar_item(item, lista=[]):
    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        resultado = usuario / clave
    except:
        pass
    return resultado


def calcular_total(precios):
    total = 0
    for p in precios:
        total = total + p
    descuento_especial = 50
    return total - descuento_especial


def main():
    print(dividir(10, 0))
    print(procesar_pedido("A", 150, 1, "VIP", "2026-06-20", "Norte", "Juan"))
    print(agregar_item("manzana"))
    print(agregar_item("pera"))


if __name__ == "__main__":
    main()
