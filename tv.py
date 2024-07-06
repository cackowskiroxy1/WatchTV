from channel import Channel

class TV:
    def __init__(self):
        self.channels = [
            Channel(1, "News Channel", "All day news coverage."),
            Channel(2, "Sports Channel", "Live sports events."),
            Channel(3, "Movie Channel", "Latest movies and classics."),
        ]
        self.current_channel = self.channels[0]
    
    def start(self):
        print("Welcome to WatchTV!")
        self.main_loop()
    
    def main_loop(self):
        while True:
            print(f"You are watching: {self.current_channel.name} - {self.current_channel.description}")
            action = input("Enter 'c' to change channel, 'q' to quit: ").lower()
            if action == 'q':
                print("Thank you for watching!")
                break
            elif action == 'c':
                self.change_channel()
            else:
                print("Invalid input, please try again.")
    
    def change_channel(self):
        print("Available channels:")
        for channel in self.channels:
            print(f"{channel.number}. {channel.name}")
        try:
            choice = int(input("Enter channel number: "))
            self.current_channel = next((ch for ch in self.channels if ch.number == choice), self.current_channel)
        except ValueError:
            print("Invalid input, please enter a valid channel number.")

