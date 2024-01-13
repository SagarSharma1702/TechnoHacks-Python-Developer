'''Task 8 : Music Player
Create a simple music player that can play
MP3 files and allows the user to create and
manage playlists.'''
#Step 1 : pip install pygame
import pygame
import os


class MusicPlayer:

  def __init__(self):
    pygame.mixer.init()  # Initialize the mixer
    self.playlist = []
    self.current_index = 0

  def add_to_playlist(self, song_path):
    self.playlist.append(song_path)
    print(f"Added '{os.path.basename(song_path)}' to the playlist.")

  def play(self):
    if self.playlist:
      pygame.mixer.music.load(self.playlist[self.current_index])
      pygame.mixer.music.play()
      print(
          f"Now playing: {os.path.basename(self.playlist[self.current_index])}"
      )
    else:
      print("Playlist is empty. Add songs to the playlist.")

  def next_song(self):
    if self.playlist:
      self.current_index = (self.current_index + 1) % len(self.playlist)
      self.play()
    else:
      print("Playlist is empty. Add songs to the playlist.")

  def previous_song(self):
    if self.playlist:
      self.current_index = (self.current_index - 1) % len(self.playlist)
      self.play()
    else:
      print("Playlist is empty. Add songs to the playlist.")

  def display_playlist(self):
    if self.playlist:
      print("\nPlaylist:")
      for index, song_path in enumerate(self.playlist, start=1):
        print(f"{index}. {os.path.basename(song_path)}")
    else:
      print("Playlist is empty. Add songs to the playlist.")


def music_player():
  player = MusicPlayer()

  while True:
    print("\nMusic Player")
    print("1. Add to Playlist")
    print("2. Play")
    print("3. Next Song")
    print("4. Previous Song")
    print("5. Display Playlist")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
      song_path = input("Enter the path of the song (MP3 file): ")
      player.add_to_playlist(song_path)
    elif choice == '2':
      player.play()
    elif choice == '3':
      player.next_song()
    elif choice == '4':
      player.previous_song()
    elif choice == '5':
      player.display_playlist()
    elif choice == '6':
      print("Thank you for using the Music Player. Have a great day!")
      pygame.mixer.quit()
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 6.")


# Call the music_player function to start the music player
music_player()
