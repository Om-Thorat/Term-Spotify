from api import Player
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label,Footer,Static

pl = Player()

pl.start()

class nowplaying(Static):
    song = reactive("OOPS")

    def on_mount(self):
        self.set_interval(1 / 60, self.update_song)
    
    def update_song(self):
        self.song = pl.getdata()

    def watch_song(self):
        self.update(f"Now Playing {self.song}")

class MyApp(App[str]):
    CSS_PATH = "final.css"
    TITLE = "SpotiTui"

    def on_mount(self):
        np = self.query_one(nowplaying)
        np.song = pl.read()


    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield nowplaying(id="status")
        yield Button("Back", id="Prev", variant="primary")
        yield Button("Play", id="PlayPause", variant="success")
        yield Button("Next", id="Next",variant="primary")
        yield Button("Repeat", id="Repeat", variant="default")
        yield Button("Shuffle", id="Shuffle", variant="default")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        pl.proc.stdin.write(f"{event.button.id}\n")
        pl.proc.stdin.flush()
        np = self.query_one(nowplaying)
        np.song = pl.read()

ui = MyApp()
ui.run()

