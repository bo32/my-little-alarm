# from playsound import playsound
from vlc import MediaPlayer, MediaList, Media, MediaListPlayer, PlaybackMode, Instance

from src.services.file_service import FileService

DEFAULT_ALARM_FILEPATH = 'src/resources/sounds/alarm_clock.ogg'

class SoundService:

    __instance = None
    # player = None

    def __init__(self):
        # self.player = None
        self.player = None
        self.vlc_instance = Instance
        self.playing_radio = False
        self.playing_alarm = False

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
        self.play_alarm_sound(DEFAULT_ALARM_FILEPATH)

    def play_alarm_sound(self, filepath):
        # here we use a MediaListPlayer instance as it offers the repeat functionality
        self.player = MediaListPlayer()
        self.player.set_playback_mode(PlaybackMode.loop)
        media_player = Media(filepath)
        if not FileService.file_exists(filepath):
            print('The alarm could not be played. Fallback to well known default alarm')
            media_player = Media(DEFAULT_ALARM_FILEPATH)
        media_list = MediaList()
        media_list.add_media(media_player)
        self.player.set_media_list(media_list)

        result = self.player.play()
        if result == -1:
            # TODO test this
            print('Something went wrong')

        self.playing_alarm = True

    def stop_alarm_sound(self):
        self.player.stop()
        self.playing_alarm = False

    def pause_alarm_sound(self):
        self.player.pause()
        self.playing_radio = False

    def play_webradio(self, url):
        self.player = MediaPlayer(url)
        self.player.play()
        self.playing_radio = True

    def pause_webradio(self):
        self.player.pause()
        self.playing_radio = False

    def stop_webradio(self):
        self.player.stop()
        self.playing_radio = False

    def pause_playing(self):
        print('Pausing alarm')
        if self.playing_radio:
            self.pause_webradio()
        else:
            self.pause_alarm_sound()

    def stop_playing(self):
        print('Stopping alarm')
        if self.playing_radio:
            self.stop_webradio()
        else:
            self.stop_alarm_sound()
