#!/usr/bin/python

import os
import webbrowser
import sys
import re

from gi.repository import Gtk, GObject
from pysqlite2 import dbapi2 as sqlite
from notifylib.add_url import Add_Series
from notifylib.about import About
from notifylib.confirm import Confirm

sqlite_file='/home/zeref/Coding/Python/letmenotifyu/letmenotifyu-1.2/notifylib/letmenotifyu.sqlite'


def open_child_series(connection,cursor):
    print "Print children"


    
class Base:
    """Font end for letmenotifyu"""
    def __init__(self,gladefile,pic):
        self.connection=sqlite.connect(sqlite_file)
        self.cursor=self.connection.cursor()
        self.builder=Gtk.Builder()
        
        self.builder.add_from_file(gladefile)
        dict={'on_btnmovies_clicked':self.on_btnmovies_clicked,
              'on_winlet_destroy':self.on_winlet_destroy,
              'on_treeview1_button_press_event':self.on_treeview1_button_press_event,
              'on_btnSeries_clicked':self.on_btnSeries_clicked,
              'on_additem_button_press_event':self.on_additem_button_press_event,
              'on_closeitem_button_press_event':self.on_closeitem_button_press_event,
              'on_aboutitem_button_press_event':self.on_aboutitem_button_press_event}
        self.builder.connect_signals(dict)
        self.window=self.builder.get_object('winlet')
        self.window.set_icon_from_file(pic)

        self.window.show()
        
    def on_winlet_destroy(self,widget):
        Gtk.main_quit()

    def on_btnSeries_clicked(self,widget):
        self.builder.get_object('listmovies').clear() 
        series_list=self.builder.get_object('listmovies')
        self.cursor.execute("SELECT title from series")
        for links in self.cursor.fetchall():
            series_list.append([links[0]])
        
    def on_btnmovies_clicked(self,widget):
        self.builder.get_object('listmovies').clear()
        movie_list=self.builder.get_object('listmovies')
        self.cursor.execute("SELECT title FROM movies")
        for title in self.cursor.fetchall():
            movie_list.append([title[0]])

    def on_treeview1_button_press_event(self,widget,event):
        if event.button==1:
            choosen=self.builder.get_object('treeview1').get_selection()
            movie,name=choosen.get_selected()
            title=movie[name][0]
            if  re.findall(r"\d{4}$",title):
                self.cursor.execute("SELECT link FROM movies WHERE title=?",(title,))
            else:
                self.cursor.execute("SELECT episode_link FROM episodes WHERE title=?", (title,))
            #for link in self.cursor.fetchall():
             #   webbrowser.open_new(link[0])
                
        elif event.button==3:
            choosen=self.builder.get_object('treeview1').get_selection()
            series,name=choosen.get_selected()
            url=series[name][0]
            if re.findall(r"\d{4}$",url):
                load=Confirm('confirm.glade',url,self.cursor,self.connection)

    def on_additem_button_press_event(self,widget,event):
        load=Add_Series('inputDialog.glade',self.cursor)
        
    def on_closeitem_button_press_event(self,widget,event):
        Gtk.main_quit()
        
    def on_aboutitem_button_press_event(self,widget,event):
        load=About('about.glade')




