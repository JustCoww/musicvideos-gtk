#!/usr/bin/env python3

import os
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from musicvideos.extras import PublishVideo

class Application:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('app.glade')
        self.builder.connect_signals(self)
        self.builder.get_object('main_window').show()
        self.compress = True
        self.upload = False

    def on_main_window_destroy(self, widget):
        exit()

    def on_audio_input_draw(self, widget, cr):
        self.song_input_widget = widget

    def on_audio_input_changed(self, widget):
        self.song = widget.get_text()

    def on_audio_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            self.song = file_chooser.get_filename().replace(' ', '\ ')
            self.song_input_widget.set_text(self.song)
        else:
            file_chooser.hide()

    def on_cover_input_draw(self, widget, cr):
        self.cover_input_widget = widget

    def on_cover_input_changed(self, widget):
        self.cover = widget.get_text()

    def on_cover_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            self.cover = file_chooser.get_filename().replace(' ', '\ ')
            self.cover_input_widget.set_text(self.cover)
        else:
            file_chooser.hide()

    def on_artists_input_changed(self, widget):
        self.artists = widget.get_text()

    def on_song_changed(self, widget):
        self.name = widget.get_text()

    def on_reverb_slide_draw(self, widget, idk):
        self.reverb = widget.get_value()
        self.reverb_widget = widget

    def on_speed_slide_draw(self, widget, idk):
        self.speed = widget.get_value()
        self.speed_widget = widget


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
        else:
            self.upload = True

    
    def on_yt_input_draw(self, widget, cr):
        self.yt_input_widget = widget

    def on_yt_input_changed(self, widget):
        self.client_secrets = widget.get_text()

    def on_yt_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            self.client_secrets = file_chooser.get_filename().replace(' ', '\ ')
            self.yt_input_widget.set_text(self.client_secrets)
        else:
            file_chooser.hide()


    def on_slowed_default_click(self, widget):
        self.reverb_widget.set_value(2.0)
        self.speed_widget.set_value(-4.0)

    def on_nightcore_default_click(self, widget):
        self.reverb_widget.set_value(2.0)
        self.speed_widget.set_value(5.0)

    def on_build_click(self, widget):
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
            new_video.info(artist=self.artists, song=self.name)
        if self.compress:
            new_video.make(compress_files=True)
        else:
            new_video.make()
        if self.upload:
            new_video.upload(client_secrets=self.client_secrets)    

Application()
Gtk.main()