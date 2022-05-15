#!/usr/bin/env python3

import os
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from musicvideos.extras import PublishVideo

app = '''
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.38.2 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <object class="GtkFileChooserDialog" id="file_chooser_window">
    <property name="can-focus">False</property>
    <property name="type-hint">dialog</property>
    <child internal-child="vbox">
      <object class="GtkBox">
        <property name="can-focus">False</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox">
            <property name="can-focus">False</property>
            <property name="layout-style">end</property>
            <child>
              <object class="GtkButton" id="button2">
                <property name="label" translatable="yes">Cancel</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="receives-default">True</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button1">
                <property name="label" translatable="yes">Open</property>
                <property name="visible">True</property>
                <property name="can-focus">True</property>
                <property name="can-default">True</property>
                <property name="receives-default">True</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="-9">button2</action-widget>
      <action-widget response="-8">button1</action-widget>
    </action-widgets>
  </object>
  <object class="GtkPopover" id="menu">
    <property name="can-focus">False</property>
    <child>
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="margin-start">5</property>
        <property name="margin-end">5</property>
        <property name="margin-top">5</property>
        <property name="margin-bottom">5</property>
        <property name="orientation">vertical</property>
        <property name="spacing">3</property>
        <child>
          <object class="GtkButton">
            <property name="label" translatable="yes">Slowed + Reverb</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="on_slowed_default_click" swapped="no"/>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton">
            <property name="label" translatable="yes">Nightcore + Reverb</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="on_nightcore_default_click" swapped="no"/>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkAdjustment" id="reverb">
    <property name="upper">10</property>
    <property name="step-increment">1</property>
    <property name="page-increment">10</property>
  </object>
  <object class="GtkAdjustment" id="speed">
    <property name="lower">-10</property>
    <property name="upper">10</property>
    <property name="step-increment">1</property>
    <property name="page-increment">10</property>
  </object>
  <object class="GtkApplicationWindow" id="main_window">
    <property name="can-focus">False</property>
    <property name="default-width">1280</property>
    <property name="default-height">720</property>
    <signal name="destroy" handler="on_main_window_destroy" swapped="no"/>
    <child>
      <!-- n-columns=4 n-rows=8 -->
      <object class="GtkGrid">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="margin-start">20</property>
        <property name="margin-end">20</property>
        <property name="margin-top">20</property>
        <property name="margin-bottom">20</property>
        <property name="row-spacing">20</property>
        <property name="column-spacing">10</property>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Audio</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry">
            <property name="width-request">300</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="placeholder-text" translatable="yes">https://soundcloud.com/osno1/gone-with-a-knife-given-all-wrong</property>
            <property name="input-purpose">url</property>
            <signal name="changed" handler="on_audio_input_changed" swapped="no"/>
            <signal name="draw" handler="on_audio_input_draw" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton">
            <property name="label">gtk-open</property>
            <property name="width-request">100</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="halign">start</property>
            <property name="use-stock">True</property>
            <property name="always-show-image">True</property>
            <signal name="clicked" handler="on_audio_open_button" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">1</property>
            <property name="top-attach">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry">
            <property name="width-request">300</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="placeholder-text" translatable="yes">https://i1.sndcdn.com/artworks-000186252146-0r7m3p-t500x500.jpg</property>
            <property name="input-purpose">url</property>
            <signal name="changed" handler="on_cover_input_changed" swapped="no"/>
            <signal name="draw" handler="on_cover_input_draw" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Cover</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton">
            <property name="label">gtk-open</property>
            <property name="width-request">100</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="halign">start</property>
            <property name="use-stock">True</property>
            <property name="always-show-image">True</property>
            <signal name="clicked" handler="on_cover_open_button" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">1</property>
            <property name="top-attach">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Reverb</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkScale">
            <property name="width-request">350</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="adjustment">reverb</property>
            <property name="fill-level">100</property>
            <property name="round-digits">1</property>
            <signal name="draw" handler="on_reverb_slide_draw" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Speed</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkScale">
            <property name="width-request">350</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="adjustment">speed</property>
            <property name="fill-level">100</property>
            <property name="round-digits">0</property>
            <property name="digits">0</property>
            <signal name="draw" handler="on_speed_slide_draw" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkCheckButton">
            <property name="label" translatable="yes">Compress?</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">False</property>
            <property name="active">True</property>
            <property name="draw-indicator">True</property>
            <signal name="draw" handler="on_compress_draw" swapped="no"/>
            <signal name="toggled" handler="on_compress_on" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry">
            <property name="width-request">100</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="placeholder-text" translatable="yes">client_secrets.json</property>
            <property name="input-purpose">url</property>
            <signal name="changed" handler="on_yt_input_changed" swapped="no"/>
            <signal name="draw" handler="on_yt_input_draw" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">7</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton">
            <property name="label">gtk-open</property>
            <property name="width-request">100</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="halign">start</property>
            <property name="use-stock">True</property>
            <property name="always-show-image">True</property>
            <signal name="clicked" handler="on_yt_open_button" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">3</property>
            <property name="top-attach">7</property>
          </packing>
        </child>
        <child>
          <object class="GtkCheckButton">
            <property name="label" translatable="yes">Upload to Youtube? </property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">False</property>
            <property name="margin-start">20</property>
            <property name="draw-indicator">True</property>
            <signal name="draw" handler="on_upload_draw" swapped="no"/>
            <signal name="toggled" handler="on_upload_toggle" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">6</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-left">10</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Youtube</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">2</property>
            <property name="top-attach">5</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Artists</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">6</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-left">10</property>
            <property name="margin-start">10</property>
            <property name="label" translatable="yes">Song</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="scale" value="1.8"/>
            </attributes>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry">
            <property name="width-request">300</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">20</property>
            <property name="placeholder-text" translatable="yes">Laura Les, Dylan Brady</property>
            <property name="input-purpose">name</property>
            <signal name="changed" handler="on_artists_input_changed" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">7</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry">
            <property name="width-request">300</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-left">20</property>
            <property name="margin-start">20</property>
            <property name="placeholder-text" translatable="yes">gone with a knife; given all wrong</property>
            <property name="input-purpose">name</property>
            <signal name="changed" handler="on_song_changed" swapped="no"/>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">5</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
    <child type="titlebar">
      <object class="GtkHeaderBar">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <property name="title" translatable="yes">Thaa Crazz VIdeo Macheen</property>
        <property name="spacing">10</property>
        <property name="show-close-button">True</property>
        <child>
          <object class="GtkMenuButton">
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="focus-on-click">False</property>
            <property name="receives-default">True</property>
            <property name="popover">menu</property>
            <child>
              <object class="GtkImage">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <property name="icon-name">open-menu-symbolic</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="pack-type">end</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton">
            <property name="label" translatable="yes">Build</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="on_build_click" swapped="no"/>
          </object>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
'''

class Application:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_string(app)
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