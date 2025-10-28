import flet as ft
from UI import User
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra(self,e):
        U=User()
        macchine=U.get_list_automobili()
        self._view.lista_auto.controls.clear()
        for auto in macchine:
            self._view.lista_auto.controls.append(
                ft.Text(f"{auto[0]} - {auto[1]} - {auto[2]} - {auto[3]} - {auto[4]} - {auto[5]}"))
        self._view.update()

    def cerca (self, e):
        modello = self._view.input_modello_auto.value
        U=User()
        trovate= U.ricerca(modello)
        self._view.lista_auto_ricerca.controls.clear()
        for auto in trovate:
            self._view.lista_auto_ricerca.controls.append(
                ft.Text(f"{auto[0]}- {auto[1]} - {auto[2]} - {auto[3]} - {auto[4]} - {auto[5]}")
            )

        self._view.input_modello_auto.value = ""
        self._view.update()