from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class Visualization:
    def __init__(self, parent):
        self.figure = plt.Figure(figsize=(12, 7), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def plot_streams_by_year(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['released_year'] = pd.to_numeric(spotify_songs['released_year'], errors='coerce')
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            spotify_songs.groupby('released_year')['streams'].sum().plot(kind='bar', ax=ax)
            ax.set_title('Total Streams by Release Year')
            ax.set_xlabel('Year')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting streams by year: {e}")

    def plot_top_artists_by_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            top_artists = spotify_songs.groupby('artist(s)_name')['streams'].sum().nlargest(10) / 1e6
            top_artists.plot(kind='bar', ax=ax)
            ax.set_title('Top 10 Artists by Streams')
            ax.set_xlabel('Artist')
            ax.set_ylabel('Streams (in millions)')
            ax.set_xticklabels(top_artists.index, rotation=30, ha='right', fontsize=10)
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting top artists by streams: {e}")

    def plot_danceability_vs_energy(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['danceability_%'] = pd.to_numeric(spotify_songs['danceability_%'], errors='coerce')
            spotify_songs['energy_%'] = pd.to_numeric(spotify_songs['energy_%'], errors='coerce')
            spotify_songs.plot.scatter(x='danceability_%', y='energy_%', ax=ax, alpha=0.5)
            ax.set_title('Danceability vs. Energy')
            ax.set_xlabel('Danceability')
            ax.set_ylabel('Energy')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting danceability vs. energy: {e}")

    def plot_songs_released_by_month(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['released_month'] = pd.to_numeric(spotify_songs['released_month'], errors='coerce')
            spotify_songs['released_month'].value_counts().sort_index().plot(kind='bar', ax=ax)
            ax.set_title('Count of Songs Released by Month')
            ax.set_xlabel('Month')
            ax.set_ylabel('Count of Songs')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting songs released by month: {e}")

    def plot_key_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            spotify_songs.groupby('key')['streams'].sum().plot(kind='bar', ax=ax)
            ax.set_title('Total Streams by Key')
            ax.set_xlabel('Key')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting key vs. streams: {e}")

    def plot_valence_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['valence'] = pd.to_numeric(spotify_songs['valence_%'], errors='coerce')
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            spotify_songs.plot.scatter(x='valence', y='streams', ax=ax, alpha=0.5)
            ax.set_title('Valence vs. Streams')
            ax.set_xlabel('Valence (Musical Positivity)')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting valence vs. streams: {e}")

    def plot_mode_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            spotify_songs.groupby('mode')['streams'].sum().plot(kind='bar', ax=ax)
            ax.set_title('Total Streams by Mode')
            ax.set_xlabel('Mode')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting mode vs. streams: {e}")

    def plot_danceability_vs_bpm(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['danceability_%'] = pd.to_numeric(spotify_songs['danceability_%'], errors='coerce')
            spotify_songs['bpm'] = pd.to_numeric(spotify_songs['bpm'], errors='coerce')
            spotify_songs.plot.scatter(x='danceability_%', y='bpm', ax=ax, alpha=0.5)
            ax.set_title('Danceability vs. BPM')
            ax.set_xlabel('Danceability')
            ax.set_ylabel('BPM')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting danceability vs. BPM: {e}")

    def plot_avg_bpm_vs_release_year(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['released_year'] = pd.to_numeric(spotify_songs['released_year'], errors='coerce')
            spotify_songs['bpm'] = pd.to_numeric(spotify_songs['bpm'], errors='coerce')
            spotify_songs.groupby('released_year')['bpm'].mean().plot(kind='line', marker='o', ax=ax)
            ax.set_title('Average BPM vs. Release Year')
            ax.set_xlabel('Release Year')
            ax.set_ylabel('Average BPM')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting average BPM vs. release year: {e}")

    def plot_pie_chart_of_keys(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            key_counts = spotify_songs['key'].value_counts()
            key_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90, legend=False)
            ax.set_title('Distribution of Keys')
            ax.set_ylabel('')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting pie chart of keys: {e}")

    def plot_collaborative_vs_solo(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs['streams'] = pd.to_numeric(spotify_songs['streams'], errors='coerce')
            spotify_songs['is_collaborative'] = spotify_songs['artist_count'].apply(
                lambda x: 'Collaborative' if x > 1 else 'Solo')
            summary = spotify_songs.groupby('is_collaborative')['streams'].sum().reset_index()
            summary.plot(kind='bar', x='is_collaborative', y='streams', ax=ax, legend=False)
            ax.set_title('Total Streams: Collaborative Tracks vs. Solo Tracks')
            ax.set_xlabel('Track Type')
            ax.set_ylabel('Streams')
            ax.set_xticklabels(summary['is_collaborative'], rotation=0)
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting collaborative vs. solo streams: {e}")

    def plot_danceability_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs.plot.scatter(x='danceability_%', y='streams', ax=ax, alpha=0.5)
            ax.set_title('Danceability vs. Streams')
            ax.set_xlabel('Danceability')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting danceability vs. streams: {e}")

    def plot_acousticness_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs.plot.scatter(x='acousticness_%', y='streams', ax=ax, alpha=0.5)
            ax.set_title('Acousticness vs. Streams')
            ax.set_xlabel('Acousticness')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting acousticness vs. streams: {e}")

    def plot_instrumentalness_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs.plot.scatter(x='instrumentalness_%', y='streams', ax=ax, alpha=0.5)
            ax.set_title('Instrumentalness vs. Streams')
            ax.set_xlabel('Instrumentalness')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting instrumentalness vs. streams: {e}")

    def plot_liveness_vs_streams(self, spotify_songs):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            spotify_songs.plot.scatter(x='liveness_%', y='streams', ax=ax, alpha=0.5)
            ax.set_title('Liveness vs. Streams')
            ax.set_xlabel('Liveness')
            ax.set_ylabel('Streams')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting liveness vs. streams: {e}")
