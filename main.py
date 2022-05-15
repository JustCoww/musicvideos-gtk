from musicvideos.extras import PublishVideo
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Application:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('app.glade')
        self.builder.connect_signals(self)
        self.builder.get_object('main_window').show()
        self.compress = True
        self.upload = False

    def on_song_input_draw(self, widget, cr):
        self.song_input_widget = widget

    def on_song_input_insert(self, widget):
        self.song = widget.get_text()

    def on_song_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            self.song = f'"{file_chooser.get_filename()}"'
            self.song_input_widget.set_text(self.song)
        elif response == Gtk.ResponseType.NO:
            file_chooser.hide()

    def on_cover_input_draw(self, widget, cr):
        self.cover_input_widget = widget

    def on_cover_input_insert(self, widget):
        self.cover = widget.get_text()

    def on_cover_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            self.cover = f'"{file_chooser.get_filename()}"'
            self.cover_input_widget.set_text(self.cover)
        elif response == Gtk.ResponseType.NO:
            file_chooser.hide()

    def on_artists_input_insert(self, widget):
        self.artists = widget.get_text()

    def on_reverb_slide_draw(self, widget, idk):
        self.reverb = widget.get_value()
        self.reverb_widget = widget

    def on_speed_slide_draw(self, widget, idk):
        self.speed = widget.get_value()
        self.speed_widget = widget

    def on_song_name_insert(self, widget):
        self.name = widget.get_text()

    def on_build_click(self, widget):
        original_dir = os.curdir()
        new_video = PublishVideo()
        new_video.files(audio=self.song, cover=self.cover)
        new_video.speed(int(self.speed))
        new_video.reverb(dry=60, wet=int(self.reverb*10))
        if ',' in self.artists:
            self.features = self.artists.split(', ')
            self.artist = self.features[0]
            self.features = self.features[1:]
            new_video.info(artist=self.artist, song=self.name, features=self.features)
        else:
            new_video.info(artist=self.artist, song=self.name)
        if self.compress:
            new_video.make(compress_files=True)
        else:
            new_video.make()
        if self.upload:
            new_video.upload(client_secrets=f'{__file__[:-7]}/client_secrets.json')
        os.chdir(original_dir)

    def on_compress_draw(self, widget, cr):
        self.compress_widget = widget

    def on_compress_on(self, widget):
        if self.compress:
            self.compress = False
        else:
            self.compress = True

    def on_upload_draw(self, widget, cr):
        self.upload_widget = widget

    def on_upload_toggle(self, widget):
        if self.upload:
            self.upload = False
            return

        warning = self.builder.get_object('warning_client_secrets')
        response = warning.run()
        if response == Gtk.ResponseType.YES:
            warning.hide()
            self.upload = True
            self.upload_widget.set_mode(True)
        elif response == Gtk.ResponseType.NO:
            warning.hide()
            self.upload = False
            self.upload_widget.set_mode(False)

    def on_slowed_default_click(self, widget):
        self.reverb_widget.set_value(2.5)
        self.speed_widget.set_value(-4.0)

    def on_nightcore_default_click(self, widget):
        self.reverb_widget.set_value(2.5)
        self.speed_widget.set_value(5.0)


Application()
Gtk.main()