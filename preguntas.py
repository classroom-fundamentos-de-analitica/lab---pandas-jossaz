"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    cantidad_filas = tbl0.shape[0]
    return cantidad_filas

def pregunta_02():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    cantidad_columnas = tbl0.shape[1]
    return cantidad_columnas

def pregunta_03():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    conteo_letras = tbl0["_c1"].value_counts().sort_index()
    return conteo_letras

def pregunta_04():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    promedio_letras = tbl0.groupby("_c1")["_c2"].mean().sort_index()
    return promedio_letras



def pregunta_05():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    maximo_letras = tbl0.groupby("_c1")["_c2"].max().sort_index()
    return maximo_letras


def pregunta_06():
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    valores_unicos = sorted(tbl1["_c4"].astype(str).str.upper().unique())
    return valores_unicos

def pregunta_07():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    suma_por_letra = tbl0.groupby("_c1")["_c2"].sum()
    return suma_por_letra

def pregunta_08():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl0 = tbl0.assign(suma=tbl0["_c0"] + tbl0["_c2"])
    return tbl0


def pregunta_09():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl0 = tbl0.assign(year=tbl0["_c3"].str.split("-").str[0])
    return tbl0


def pregunta_10():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl0_agg = tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(map(str, sorted(x)))).reset_index(name="_c2")
    tbl0_agg.set_index("_c1", inplace=True)
    return tbl0_agg


def pregunta_11():
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl1_grouped = tbl1.groupby("_c0")["_c4"].apply(lambda x: ','.join(sorted(x))).reset_index()
    return tbl1_grouped
  


def pregunta_12():
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
    tbl2_grouped = tbl2.groupby("_c0").apply(lambda x: ','.join(f"{a}:{b}" for a, b in sorted(zip(x["_c5a"], x["_c5b"]))) ).reset_index(name="_c5")
    return tbl2_grouped


def pregunta_13():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
    merged = pd.merge(tbl0, tbl2, on="_c0")
    result = merged.groupby("_c1")["_c5b"].sum()
    return result
  
