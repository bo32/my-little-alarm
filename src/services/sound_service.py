from playsound import playsound
import vlc


class SoundService:
    def __init__(self):
        pass

    def play_default_alarm_sound(self):
        self.play_alarm_sound('src/resources/sounds/alarm_clock.ogg')

    def play_alarm_sound(self, filepath):
        playsound(filepath)

    def play_webradio(self, url):
        player = vlc.MediaPlayer(url)
        player.play()
