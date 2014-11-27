from distutils.core import setup
if __name__=='__main__':
    setup(name='letmenotifyu',
          version='2.0.6',
          description='Program to notify users of new movie and series episode release from http://www.primewire.ag/',
          author='Lunga Mthembu',
          author_email='shellcomplex7@gmail.com',
          url='https://github.com/shellcomplex/letmenotifyu',
          license='GPL',
          scripts=['letmenotifyu'],
          packages=['notifylib'],
          data_files=[('share/applications',['ui/letmenotifyu.desktop']),
                      ('share/letmenotifyu/ui',['ui/about.glade','ui/confirm.glade','ui/main.glade','ui/stats.glade','ui/error.glade','ui/preferences.glade','ui/set_season.glade','ui/add_series.glade']),
                      ('share/letmenotifyu/ui',['ui/letmenotifyu.png','ui/letmenotifyu.xpm','ui/movies.png']),
                      ('share/letmenotifyu/icons',['icons/128.png','icons/16.png','icons/24.png','icons/32.png','icons/64.png','icons/invert-32.png','icons/invert-television.png','icons/invert-visible.png','icons/television.png','ui/visible.png'])]
                      
          )
            





