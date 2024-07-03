import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()

        anno = self._view._txtAnno.value
        grafo = self._model.get_grafo(int(anno))
        stati_confinanti = self._model.get_stati_connessi()
        num_stati = self._model.connesse()

        self._view._txt_result.controls.append(ft.Text(f"Numero delle componenti connesse:{num_stati}\n"
                                                       f"Elenco degli stati confinanti:\n"
                                                       f"{stati_confinanti}"))
        self._view.update_page()

    def handleStatiConfinanti(self, e):
        self._view._txt_result.controls.clear()
        stato = self._view._txtStato.value
        grafo = self._model.get_grafo(int(2016))
        stati = self._model.get_stati_raggiungibili(stato)
        self._view._txt_result.controls.append(ft.Text(f"Stati raggiungibili a partire da {stato}:\n"
                                                       f"{stati}"))
        self._view.update_page()

    def popolaTendina(self):
        stati = self._model.get_all_stati()
        for element in stati:
            self._view._txtStato.options.append(ft.dropdown.Option(element))
        self._view.update_page()