from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.audio import SoundLoader
from kivy.utils import platform
import os
from gtts import gTTS

# caminho Download - funciona no Android e no PC
if platform == 'android':
    from android.storage import primary_external_storage_path
    DOWNLOAD_DIR = primary_external_storage_path()
else:
    DOWNLOAD_DIR = os.path.expanduser("~/Downloads")

DOWNLOAD_FILE = os.path.join(DOWNLOAD_DIR, "aloisio_tts.mp3")

class AloisioTTSApp(App):
    def build(self):
        self.title = "Aloisio TTS"
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        root.add_widget(Label(text="Digite seu texto:", size_hint_y=None, height=30, font_size=18))

        self.caixa = TextInput(hint_text="Cole seu texto grego aqui...", font_size=16, multiline=True)
        root.add_widget(self.caixa)

        # Spinner de idiomas (bem mais leve que 6 RadioButtons)
        self.lang_spinner = Spinner(
            text='Greek - el',
            values=('Portuguese - pt', 'English - en', 'Italian - it', 'Spanish - es', 'French - fr', 'Greek - el'),
            size_hint_y=None,
            height=44
        )
        root.add_widget(self.lang_spinner)

        self.status = Label(text="Pronto", size_hint_y=None, height=30)
        root.add_widget(self.status)

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_layout.add_widget(Button(text="Salvar Audio", on_press=self.salvar_audio))
        btn_layout.add_widget(Button(text="Ouvir", on_press=self.ler_audio))
        root.add_widget(btn_layout)

        btn_layout2 = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_layout2.add_widget(Button(text="Limpar", on_press=self.limpar))
        btn_layout2.add_widget(Button(text="Colar", on_press=self.colar))
        root.add_widget(btn_layout2)

        return root

    def get_lang_code(self):
        # "Greek - el" -> "el"
        return self.lang_spinner.text.split("-")[-1].strip()

    def salvar_audio(self, instance):
        texto = self.caixa.text.strip()
        if not texto:
            self.status.text = "Caixa vazia, criatura!"
            return
        try:
            self.status.text = "Gerando..."
            idioma = self.get_lang_code()
            tts = gTTS(texto, lang=idioma)
            tts.save(DOWNLOAD_FILE)
            self.status.text = f"Salvo em: {DOWNLOAD_FILE}"
        except Exception as e:
            self.status.text = f"Erro: {e}"

    def ler_audio(self, instance):
        if os.path.exists(DOWNLOAD_FILE):
            try:
                sound = SoundLoader.load(DOWNLOAD_FILE)
                if sound:
                    sound.play()
                    self.status.text = "Tocando..."
                else:
                    self.status.text = "Erro ao tocar"
            except Exception as e:
                self.status.text = f"Erro: {e}"
        else:
            self.status.text = "Nenhum audio ainda!"

    def limpar(self, instance):
        self.caixa.text = ""
        self.status.text = "Limpo"

    def colar(self, instance):
        from kivy.core.clipboard import Clipboard
        self.caixa.text += Clipboard.paste()

AloisioTTSApp().run()
