from playsound import playsound
import vlc


class SoundService:

    __instance = None
    # player = None

    def __init__(self):
        # self.player = None
        self.player = None
        # pass

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    @staticmethod
    def get_instance():
        if SoundService.__instance is None:
            SoundService.__instance = SoundService()
        return SoundService.__instance

    def play_default_alarm_sound(self):
        self.play_alarm_sound('src/resources/sounds/alarm_clock.ogg')

    def play_alarm_sound(self, filepath):
        playsound(filepath)

    def play_webradio(self, url):
        self.player = vlc.MediaPlayer(url)
        self.player.play()

    def pause_webradio(self):
        self.player.pause()

    def stop_webradio(self):
        self.player.stop()
