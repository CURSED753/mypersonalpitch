import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



class FirstWindow(Screen):

	def scheda_press(self):
		self.ids.per_scheda.background_color = "#000000"

	def scheda(self):
		self.ids.per_scheda.background_color = "#333333"

	def statistiche_press(self):
		self.ids.per_statistiche.background_color = "#000000"

	def statistiche(self):
		self.ids.per_statistiche.background_color = "#333333"

	def color(self):
		self.ids.inviata.background_color = "#000000"

	def spinner1(self):
		self.ids.spinner_ente.background_color = "#000000"

	def spinner1_release(self):
		self.ids.spinner_ente.background_color = "#333333"

	def spinner2(self):
		self.ids.spinner_qualita.background_color = "#000000"

	def spinner2_release(self):
		self.ids.spinner_qualita.background_color = "#333333"

	def spinner3(self):
		self.ids.spinner_periodo.background_color = "#000000"

	def spinner3_release(self):
		self.ids.spinner_periodo.background_color = "#333333"

	def spinner4(self):
		self.ids.spinner_numero_adesioni.background_color = "#000000"

	def spinner4_release(self):
		self.ids.spinner_numero_adesioni.background_color = "#333333"

	def invia(self):

		adesioni = App.get_running_app().root.ids.screen2.ids.numero_adesioni
		guadagno = App.get_running_app().root.ids.screen2.ids.numero_guadagno
		ente = self.ids.spinner_ente
		qualita = self.ids.spinner_qualita
		periodo = self.ids.spinner_periodo
		quantita = self.ids.spinner_numero_adesioni

		stc_15 = App.get_running_app().root.ids.screen3.ids.stc_15
		stc_20 = App.get_running_app().root.ids.screen3.ids.stc_20
		stc_25 = App.get_running_app().root.ids.screen3.ids.stc_25
		stc_30 = App.get_running_app().root.ids.screen3.ids.stc_30

		unhcr_15 = App.get_running_app().root.ids.screen3.ids.unhcr_15
		unhcr_20 = App.get_running_app().root.ids.screen3.ids.unhcr_20
		unhcr_30 = App.get_running_app().root.ids.screen3.ids.unhcr_30
		unhcr_40 = App.get_running_app().root.ids.screen3.ids.unhcr_40
		unhcr_50 = App.get_running_app().root.ids.screen3.ids.unhcr_50

		wwf_15 = App.get_running_app().root.ids.screen3.ids.wwf_15
		wwf_20 = App.get_running_app().root.ids.screen3.ids.wwf_20
		wwf_25 = App.get_running_app().root.ids.screen3.ids.wwf_25
		wwf_30 = App.get_running_app().root.ids.screen3.ids.wwf_30

		telethon_15 = App.get_running_app().root.ids.screen3.ids.telethon_15
		telethon_20 = App.get_running_app().root.ids.screen3.ids.telethon_20
		telethon_30 = App.get_running_app().root.ids.screen3.ids.telethon_30

		self.ids.inviata.background_color = "#333333"

		#ADESIONI STC MENSILI

		if (ente.text=="Save The Children") and (qualita.text=="15") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text) + 18) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_15.text = f"{int(stc_15.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="20") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text) + 27) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_20.text = f"{int(stc_20.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="25") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text) + 29) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_25.text = f"{int(stc_25.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="30") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text) + 30) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_30.text = f"{int(stc_30.text) + int(quantita.text)}"
		#ADESIONI STC ANNUALI

		if (ente.text=="Save The Children") and (qualita.text=="180") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + ((int(qualita.text)/12) + 18) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_15.text = f"{int(stc_15.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="240") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + ((int(qualita.text)/12) + 27) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_20.text = f"{int(stc_20.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="300") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + ((int(qualita.text)/12) + 29) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_25.text = f"{int(stc_25.text) + int(quantita.text)}"

		if (ente.text=="Save The Children") and (qualita.text=="360") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + ((int(qualita.text)/12) + 30) * int(quantita.text))}"
			adesioni.text = f"{int(adesioni.text) + int(quantita.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			stc_30.text = f"{int(stc_30.text) + int(quantita.text)}"

		#ADESIONI UNHCR MENSILI

		if (ente.text=="UNHCR") and (qualita.text=="15") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_15.text = f"{int(unhcr_15.text) + int(quantita.text)}"

		if (ente.text=="UNHCR") and (qualita.text=="20") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_20.text = f"{int(unhcr_20.text) + int(quantita.text)}"


		if (ente.text=="UNHCR") and (qualita.text=="30") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_30.text = f"{int(unhcr_30.text) + int(quantita.text)}"

		if (ente.text=="UNHCR") and (qualita.text=="40") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_40.text = f"{int(unhcr_40.text) + int(quantita.text)}"


		if (ente.text=="UNHCR") and (qualita.text=="50") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_50.text = f"{int(unhcr_50.text) + int(quantita.text)}"


		#ADESIONI UNHCR ANNUALI

		if (ente.text=="UNHCR") and (qualita.text=="180") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_15.text = f"{int(unhcr_15.text) + int(quantita.text)}"


		if (ente.text=="UNHCR") and (qualita.text=="240") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_20.text = f"{int(unhcr_20.text) + int(quantita.text)}"


		if (ente.text=="UNHCR") and (qualita.text=="360") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_30.text = f"{int(unhcr_30.text) + int(quantita.text)}"


		if (ente.text=="UNHCR") and (qualita.text=="480") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_40.text = f"{int(unhcr_40.text) + int(quantita.text)}"

		if (ente.text=="UNHCR") and (qualita.text=="600") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 30)}"
			adesioni.text = f"{int(adesioni.text)}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			unhcr_50.text = f"{int(unhcr_50.text) + int(quantita.text)}"


		#ADESIONI WWF MENSILI

		if (ente.text=="WWF") and (qualita.text=="15") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_15.text = f"{int(wwf_15.text) + int(quantita.text)}"


		if (ente.text=="WWF") and (qualita.text=="20") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_20.text = f"{int(wwf_20.text) + int(quantita.text)}"



		if (ente.text=="WWF") and (qualita.text=="25") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 29)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_25.text = f"{int(wwf_25.text) + int(quantita.text)}"



		if (ente.text=="WWF") and (qualita.text=="30") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + int(qualita.text) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_30.text = f"{int(wwf_30.text) + int(quantita.text)}"


		#ADESIONI WWF ANNUALI

		if (ente.text=="WWF") and (qualita.text=="180") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_15.text = f"{int(wwf_15.text) + int(quantita.text)}"


		if (ente.text=="WWF") and (qualita.text=="240") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_20.text = f"{int(wwf_20.text) + int(quantita.text)}"


		if (ente.text=="WWF") and (qualita.text=="300") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 29)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_25.text = f"{int(wwf_25.text) + int(quantita.text)}"


		if (ente.text=="WWF") and (qualita.text=="360") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			wwf_30.text = f"{int(wwf_30.text) + int(quantita.text)}"



		#ADESIONI TELETHON MENSILI

		if (ente.text=="Telethon") and (qualita.text=="15") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_15.text = f"{int(telethon_15.text) + int(quantita.text)}"



		if (ente.text=="Telethon") and (qualita.text=="20") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_20.text = f"{int(telethon_20.text) + int(quantita.text)}"


		if (ente.text=="Telethon") and (qualita.text=="30") and (periodo.text=="Mensile"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_30.text = f"{int(telethon_30.text) + int(quantita.text)}"


		#ADESIONI TELETHON ANNUALI

		if (ente.text=="Telethon") and (qualita.text=="180") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 18)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_15.text = f"{int(telethon_15.text) + int(quantita.text)}"


		if (ente.text=="Telethon") and (qualita.text=="240") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 27)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_20.text = f"{int(telethon_20.text) + int(quantita.text)}"


		if (ente.text=="Telethon") and (qualita.text=="360") and (periodo.text=="Annuale"):
			guadagno.text = f"{(int(float(guadagno.text)) + (int(qualita.text)/12) + 30)}"
			adesioni.text = f"{int(adesioni.text) + 1}"
			self.ids.avviso.text = "La tua adesione \ne' stata caricata! \nControlla nelle statistiche!"
			telethon_30.text = f"{int(telethon_30.text) + int(quantita.text)}"


class SecondWindow(Screen):

	def color_azzera_release(self):
		self.ids.azzera.background_color = "#333333"

	def color_azzera(self):
		self.ids.azzera.background_color = "#000000"

	def per_adesioni(self):
		self.ids.per_adesioni.background_color = "#000000"

	def adesioni(self):
		self.ids.per_adesioni.background_color = "#333333"


	def azzera(self):

		adesioni = self.ids.numero_adesioni
		guadagno = self.ids.numero_guadagno
		ente = App.get_running_app().root.ids.screen1.ids.spinner_ente
		qualita = App.get_running_app().root.ids.screen1.ids.spinner_qualita
		periodo = App.get_running_app().root.ids.screen1.ids.spinner_periodo
		quantita = App.get_running_app().root.ids.screen1.ids.spinner_numero_adesioni

		adesioni.text = "0"
		guadagno.text = "0"

		ente.text = "Seleziona un ente"
		qualita.text = "Seleziona una qualità"
		periodo.text = "Seleziona un periodo"
		quantita.text = "Quante ne hai fatte?"

class ThirdWindow(Screen):

	def home_press(self):
		self.ids.per_home.background_color = "#000000"

	def home(self):
		self.ids.per_home.background_color = "#333333"

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file("funziona.kv")

class MyPersonalPitch(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MyPersonalPitch().run()