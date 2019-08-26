#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#This code will enable the manipulation of the Drone from a User Interface created with Glade

# We import PYGTK Module V 2.0
import pygtk
pygtk.require("2.0")

# Next, we import gtk module
import gtk
import gtk.glade

# We create the Class for the main Window
class MainWin:
    
    def __init__(self):

        self.widgets = gtk.glade.XML("gui_drone.glade")
                
        # We create a dictionary with the glade defined signals and their method
        signals = { "on_b_on_clicked" : self.on_b_on_clicked,
                    "on_b_off_clicked" : self.on_b_off_clicked,
                    "on_b_ade_clicked" : self.on_b_ade_clicked,
                    "on_b_izq_clicked" : self.on_b_izq_clicked,
                    "on_b_atr_clicked" : self.on_b_atr_clicked,
                    "on_b_der_clicked" : self.on_b_der_clicked,
                    "on_b_arr_clicked" : self.on_b_arr_clicked,
                    "on_b_aba_clicked" : self.on_b_aba_clicked,
                    "gtk_main_quit" : gtk.main_quit }
        
        # Autoconnect Signals
        self.widgets.signal_autoconnect(signals)
        
        # Obtain Widgets from Glade file, use them (label1 and entry 1)
        
        self.status = self.widgets.get_widget("status")
            # Define methods for the Action On Clicked
    def on_b_on_clicked(self, widget):
        self.status.set_text("Encendiendo")
    def on_b_off_clicked(self, widget):
        self.status.set_text("Apagando")
    def on_b_ade_clicked(self, widget):
        self.status.set_text("Adelante")
    def on_b_izq_clicked(self, widget):
        self.status.set_text("Izquierda")
    def on_b_der_clicked(self, widget):
        self.status.set_text("Derecha")
    def on_b_arr_clicked(self, widget):
        self.status.set_text("Arriba")
    def on_b_aba_clicked(self, widget):
        self.status.set_text("Abajo")
    def on_b_atr_clicked(self, widget):
        self.status.set_text("Atras")
    

# Start the program
if __name__ == "__main__":
    MainWin()
    gtk.main()
