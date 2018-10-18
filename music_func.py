from pygame import mixer
import RPi.GPIO as GPIO

def play_music(channel1, music_lists, music_status, playing_number):
    if music_status == 1:
        if playing_number <= 0:
            playing_number = len(music_lists)
        playing_number = playing_number - 1  #在下方列表循环播放代码会自动播放歌曲，此处不设置
    
    elif music_status == 2:  #last song
        music_status = 1
        if playing_number <= 0:
            playing_number = len(music_lists)
        playing_number = playing_number - 1
        mixer.music.load('music/' + music_lists[playing_number])
        mixer.music.play()
        print('Playing music(last song)... [ ' + music_lists[playing_number] + ' ]')
    
    elif music_status == 3:  #next song
        music_status = 1
        playing_number = playing_number + 1
        if playing_number >= len(music_lists):
            playing_number = 0
        mixer.music.load('music/' + music_lists[playing_number])
        mixer.music.play()
        print('Playing music(next song)... [ ' + music_lists[playing_number] + ' ]')
    
    elif music_status == 4:  # higher volume
        music_status = 1
        volume = mixer.music.get_volume()
        volume = volume + 0.2
        if volume > 0.95:
            volume = 0.95
        mixer.music.set_volume(volume)
        print('Adjusting music volume... [' + str(mixer.music.get_volume()) + ']')
    
    elif music_status == 5:  # lower volume
        music_status = 1
        volume = mixer.music.get_volume()
        volume = volume - 0.2
        if volume < 0.05:
            volume = 0.05
        mixer.music.set_volume(volume)
        print('Adjusting music volume... [' + str(mixer.music.get_volume()) + ']')
    
    else:
        mixer.music.stop()
    
    
    while music_status != 0 and GPIO.input(channel1) == False:  #列表循环播放
        if mixer.music.get_busy() == False:
            playing_number = playing_number + 1
            if playing_number >= len(music_lists):
                playing_number = 0
            mixer.music.load('music/' + music_lists[playing_number])
            mixer.music.play()
            print('Playing music... [ ' + music_lists[playing_number] + ' ]')
    
    return [music_status, playing_number]

