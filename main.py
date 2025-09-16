import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('2.0.0')

class CounterApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Title
        title = Label(text='Counter App', font_size=30)
        layout.add_widget(title)
        
        # Counter display
        self.counter_label = Label(text='0', font_size=50)
        layout.add_widget(self.counter_label)
        
        # Counter variable
        self.count = 0
        
        # Increment button
        increment_button = Button(text='Increment', font_size=20)
        increment_button.bind(on_press=self.increment)
        layout.add_widget(increment_button)
        
        # Reset button
        reset_button = Button(text='Reset', font_size=20)
        reset_button.bind(on_press=self.reset)
        layout.add_widget(reset_button)
        
        return layout
    
    def increment(self, instance):
        self.count += 1
        self.counter_label.text = str(self.count)
    
    def reset(self, instance):
        self.count = 0
        self.counter_label.text = str(self.count)

if __name__ == '__main__':
    CounterApp().run()