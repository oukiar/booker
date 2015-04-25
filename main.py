from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty, ObjectProperty, NumericProperty

from kivy.clock import Clock

class Booker(FloatLayout):
    paragraphs = ListProperty()
    bookname = StringProperty()
    textview = ObjectProperty()
    current = NumericProperty(0)
    padding = NumericProperty(100)
    
    def on_bookname(self, w, val):
        with open(val) as f:
            self.paragraphs = f.read().split("\n\n")
            
    def on_paragraphs(self, w, val):
        if self.textview == None:
            Clock.schedule_once(self.update_paragraph, .1)
        else:
            self.textview.text = self.paragraphs[self.current]
            
    def on_current(self, w, val):
        if val >= 0 and val < len(self.paragraphs):
            self.update_paragraph()

    def update_paragraph(self, dt=None):
        if len(self.paragraphs)>0 and self.current < len(self.paragraphs):
            self.textview.font_size = 10
            self.textview.text = self.paragraphs[self.current]
            self.textview.bind(texture_size=self.checktextsize)
    
    def checktextsize(self, w, val):
        
        #the better text size for optimal visualization
        if self.textview.width > self.textview.texture_size[0]+self.padding and self.textview.height > self.textview.texture_size[1]+self.padding:
            Clock.schedule_once(self.addfontsize, 0)
            
    def addfontsize(self, dt):
        self.textview.font_size += 1
            
        

if __name__ == "__main__":
    from kivy.app import App
    
    class BookerApp(App):
        def build(self):
            return Booker(bookname="El sendero de los maestros")
    
    BookerApp().run()
