"""Utilidades para parchear TP_MLE.ipynb sin regenerarlo.

Regla: nunca reescribir el notebook completo. Solo reemplazar/insertar
las celdas que se tocan, para no pisar ediciones manuales del notebook.
"""

import nbformat

NB = "TP_MLE.ipynb"


def load():
    return nbformat.read(NB, as_version=4)


def save(nb):
    nbformat.write(nb, NB)


def find(nb, marker, cell_type=None):
    ids = [
        i for i, c in enumerate(nb.cells)
        if marker in c.source and (cell_type is None or c.cell_type == cell_type)
    ]
    return ids


def replace_cell(nb, marker, new_source, cell_type="markdown"):
    ids = find(nb, marker, cell_type)
    if len(ids) != 1:
        raise SystemExit(f"marker {marker!r} matchea {len(ids)} celdas, se esperaba 1")
    nb.cells[ids[0]].source = new_source


def replace_code(nb, marker, new_source):
    replace_cell(nb, marker, new_source, cell_type="code")


def append_cells(nb, cells, before_marker=None):
    """Inserta celdas antes de la celda que contiene before_marker (o al final)."""
    idx = len(nb.cells) if before_marker is None else find(nb, before_marker)[0]
    for offset, cell in enumerate(cells):
        nb.cells.insert(idx + offset, cell)


def md(source):
    return nbformat.v4.new_markdown_cell(source)


def code(source):
    return nbformat.v4.new_code_cell(source)
