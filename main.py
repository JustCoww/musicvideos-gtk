#!/usr/bin/env python3

import os
import gi
import time
import signal
import threading
from musicvideos_extras import build

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def progressbar_modify(bar, fraction, text):
    thread_frac = threading.Thread(target=bar.set_fraction, args=[fraction])
    thread_text = threading.Thread(target=bar.set_text, args=[text])
    thread_frac.start()
    thread_text.start()
    return 0


def build(self, widget):
    # Get info from the gui things
    client_secrets = self.builder.get_object('youtube_entry_box').get_text()
    cover = self.builder.get_object('cover_entry_box').get_text()
    audio = self.builder.get_object('audio_entry_box').get_text()
    artists = self.builder.get_object('artists_entry_box').get_text()
    song = self.builder.get_object('song_entry_box').get_text()
    reverb = self.builder.get_object('reverb_slide').get_value()
    speed = self.builder.get_object('speed_slide').get_value()
    custom_toptext = self.builder.get_object('toptext_entry_box').get_text()
    compress = self.builder.get_object('compress_toggle').get_active()
    upload = self.builder.get_object('upload_toggle').get_active()
    remove_toptext = not self.builder.get_object('toptext_toggle').get_active()

    # If audio or cover not specified error out and cancel the building process
    if audio == '' or cover == '':
        self.building = False
        return print('Audio or Cover not specified!')

    # If audio and cover are specified start the building process :)
    progressbar_modify(self.loading, 0.0, 'Setting up')
    video = build.BuildVideo(song=song,
                        artists=artists,
                        audio=audio,
                        cover=cover,
                        speed=speed,
                        reverb=reverb,
                        remove_toptext=remove_toptext)
    if custom_toptext != '' and not remove_toptext:
        video.custom_toptext(custom_toptext)

    # Exports
    progressbar_modify(self.loading, 0.3, 'Exporting audio')
    video.export_audio()
    progressbar_modify(self.loading, 0.4, 'Exporting images')
    video.export_images()
    progressbar_modify(self.loading, 0.6, 'Exporting Video')
    video.export_video()
    progressbar_modify(self.loading, 0.7, 'Video Exported')
    if upload:
        progressbar_modify(self.loading, 0.8, 'Uploading')
        video.upload_youtube(client_secrets=client_secrets)
    progressbar_modify(self.loading, 0.9, 'Finishing')
    video.finish(compress=compress)
    progressbar_modify(self.loading, 1.0, 'Finished')

    # At the end remove the loading bar and set the building status to False
    time.sleep(1)
    widget.remove(self.loading)
    widget.add(self.build_label)
    self.building = False
    return 0


class Application:
    def __init__(self):
        # ----- Variables ----- #
        self.compress = True
        self.upload = False
        self.toptext = True
        self.building = False
        # ----- Window ----- #
        self.builder = Gtk.Builder()
        self.builder.add_from_file('app.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('main_window')
        self.window.show()
        # ----- Progress Bar ----- #
        self.loading = Gtk.ProgressBar()
        self.loading.show()
        self.loading.set_show_text(True)
        self.loading.set_vexpand(False)
        self.loading.set_valign(Gtk.Align.CENTER)
        # ----- Build Button Label ----- #
        self.build_label = Gtk.Label()
        self.build_label.set_text('Build')
        self.build_label.show()
        self.build_label.set_vexpand(False)
        self.build_label.set_valign(Gtk.Align.CENTER)
        self.builder.get_object('build_button ').add(self.build_label)

    def on_main_window_delete_event(self, idk, crazy):
        if not self.building: return Gtk.main_quit()
        dialog = self.builder.get_object('close_dialog_window')
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            dialog.hide()
            Gtk.main_quit()
            os.kill(os.getpid(), signal.SIGTERM)
            exit()
            return False
        else:
            dialog.hide()
            return True


    def on_audio_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            filename = file_chooser.get_filename()
            self.builder.get_object('audio_entry_box').set_text(filename)
        else:
            file_chooser.hide()

    def on_cover_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            filename = file_chooser.get_filename()
            self.builder.get_object('cover_entry_box').set_text(filename)
        else:
            file_chooser.hide()

    def on_yt_open_button(self, widget):
        file_chooser = self.builder.get_object('file_chooser_window')
        response = file_chooser.run()
        if response == Gtk.ResponseType.YES:
            file_chooser.hide()
            filename = file_chooser.get_filename()
            self.builder.get_object('youtube_entry_box').set_text(filename)
        else:
            file_chooser.hide()

    def on_slowed_default_click(self, widget):
        self.builder.get_object('reverb_slide').set_value(2.0)
        self.builder.get_object('speed_slide').set_value(-4.0)

    def on_nightcore_default_click(self, widget):
        self.builder.get_object('reverb_slide').set_value(2.0)
        self.builder.get_object('speed_slide').set_value(5.0)

    def on_build_click(self, widget):
        if not self.building:
            self.building = True
            widget.remove(self.build_label)
            widget.add(self.loading)
            self.build_thread = threading.Thread(target=build, args=[self, widget])
            self.build_thread.start()


Application()
Gtk.main()
