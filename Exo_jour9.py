# pip install meteofrance-api

from meteofrance_api import MeteoFranceClient
from meteofrance_api.helpers import readeable_phenomenoms_dict
from datetime import date


def test_workflow(city: str) -> None:
    """Test classical workflow usage with the Python library."""
    # Init client
    client = MeteoFranceClient()

    # Search a location from name.
    list_places = client.search_places(city)
    if (len(list_places) > 0) :
        my_place = list_places[0]
    else :
        print("Rien trouvé")
        return ""

    # Fetch weather forecast for the location
    my_place_weather_forecast = client.get_forecast_for_place(my_place)

    # Get the daily forecast
    my_place_daily_forecast = my_place_weather_forecast.daily_forecast

    # Fetch weather alerts.
    if my_place.admin2:
        my_place_weather_alerts = client.get_warning_current_phenomenoms(
            my_place.admin2
        )
        readable_warnings = readeable_phenomenoms_dict(
            my_place_weather_alerts.phenomenons_max_colors
        )

    return [my_place, readable_warnings["Neige-verglas"], my_place_daily_forecast]

import tkinter as tk

def tagChanger(tag, id): # Fonction qui prend un "tag" donné et l'applique au label donné
    id.config(text=tag)

class Application(tk.Frame):                         # Crée la fenetre de l'application
    def __init__(self, master=None):                 # Initialisation
        super().__init__(master)                     # Initialisation automatique
        self.master = master
        self.master.title("Météo")   # titre de la fenêtre
        self.pack()                                  # Package (anglicisme) de la fenêtre
        self.create_widgets()                        # Execution du contenue

    def found(self):
        self.element = self.entrySearch.get()
        output = ""
        result = test_workflow(self.element)
        a = result[0]
        b = result[1]
        c = result[2]
        output += "Ville : " + str(a) +"\n"
        output += "Neige-verglas : " + str(b) + "\n"+"\n"
        for i in c :
            #print(i["T"]["min"], i["T"]["max"], i["weather12H"]["desc"])
            timestamp = date.fromtimestamp(i["dt"])
            output += "------------------------- " + str(timestamp) + " -------------------------" + "\n"
            output += "      * " + "Températures :  max -> "+str(i["T"]["max"])+" et min -> " +str(i["T"]["min"])+"\n"
            output += "      * " + "Météo :  " + i["weather12H"]["desc"] + "\n"
        self.labelResult.config(text=output)

    def create_widgets(self):
        self.labelInput  = tk.Label(root,  text="Entrez votre recherche et choisissez votre catégorie :", pady=20)       # Crée un "titre"
        self.entrySearch = tk.Entry(root,  width=20)                                                                     # Crée une boîte de texte
        self.executeBT   = tk.Button(root, text="CHERCHER", fg="green", command=self.found, pady=7)                  # Crée un bouton pour executer la recherche
        self.labelResult = tk.Label(root, height=90)                     # Crée un text pour le résultat

        self.labelInput. pack(side="top") # Pack le texte (et donc l'affiche)
        self.entrySearch.pack(side="top") # Pack la boîte de texte
        self.executeBT.  pack(side="top") # Pack le bouton
        self.labelResult.pack(side="top") # Pack le texte


root = tk.Tk()
root.geometry("500x1000")       # Taille de la fenêtre
app = Application(master=root) # Lance l'application
app.mainloop()                 # Repète en boucle l'application