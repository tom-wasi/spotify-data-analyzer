import tkinter as tk
from tkinter import ttk
import pandas as pd
import chardet
from data_explorer import DataExplorer
from visualization import Visualization


class SpotifyApp:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("Spotify Songs Explorer")

            # Autodetect encoding
            file_path = 'data/Popular_Spotify_Songs.csv'
            with open(file_path, 'rb') as f:
                result = chardet.detect(f.read())
            encoding = result['encoding']

            # Load the dataset
            self.spotify_songs = pd.read_csv(file_path, encoding=encoding)

            # Create DataExplorer
            self.data_explorer = DataExplorer(self.root, self.spotify_songs)

            # Frame for visualization
            self.frame_visualization = ttk.LabelFrame(self.root, text="Data Visualization")
            self.frame_visualization.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # Frame for the dropdown, button, and conclusion
            self.frame_controls = ttk.Frame(self.frame_visualization)
            self.frame_controls.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            # Dropdown for visualization options
            self.visualization_options = [
                "Streams by Release Year",
                "Top 10 Artists by Streams",
                "Danceability vs. Energy",
                "Songs Released by Month",
                "Key vs. Streams",
                "Valence vs. Streams",
                "Mode vs. Streams",
                "Danceability vs. BPM",
                "Average BPM vs. Release Year",
                "Pie Chart of All Keys",
                "Collaborative vs. Solo Streams",
                "Danceability vs. Streams",
                "Acousticness vs. Streams",
                "Instrumentalness vs. Streams",
                "Liveness vs. Streams"
            ]
            self.selected_option = tk.StringVar()
            self.selected_option.set(self.visualization_options[0])
            self.dropdown_visualization = ttk.OptionMenu(self.frame_controls, self.selected_option,
                                                         *self.visualization_options)
            self.dropdown_visualization.grid(row=0, column=0, padx=5, pady=5)

            # Button to create visualization
            self.btn_create_viz = ttk.Button(self.frame_controls, text="Create Visualization",
                                             command=self.create_visualization)
            self.btn_create_viz.grid(row=0, column=1, padx=5, pady=5)

            # Label for conclusions
            self.label_conclusions = ttk.Label(self.frame_controls, text="", wraplength=500)
            self.label_conclusions.grid(row=0, column=2, padx=10, pady=5, sticky="w")

            # Create Visualization instance
            self.visualization = Visualization(self.frame_visualization)
        except FileNotFoundError:
            messagebox.showerror("Error", "The data file was not found.")
        except pd.errors.ParserError:
            messagebox.showerror("Error", "Error parsing the data file.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def create_visualization(self):
        selected_viz = self.selected_option.get()
        if selected_viz == "Streams by Release Year":
            self.visualization.plot_streams_by_year(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The graph clearly demonstrates the increasing trend of music streaming over the years, particularly in the last decade. The dominance of recent years highlights the impact of digital transformation in the music industry, with streaming platforms playing a pivotal role in how people consume music today.\nThe peak was in the 2022.")
        elif selected_viz == "Top 10 Artists by Streams":
            self.visualization.plot_top_artists_by_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion:The artists in the top 10 represent a variety of genres and styles, including pop (Taylor Swift, Ed Sheeran, Harry Styles), hip-hop (Eminem), Latin (Bad Bunny), and alternative/rock (Arctic Monkeys, Imagine Dragons). This diversity indicates that high streaming numbers are not limited to a single genre, reflecting varied musical tastes among listeners.\nArtists like Olivia Rodrigo and Bad Bunny, who have risen to fame more recently compared to some of the others, are also among the top 10. This suggests that newer artists can quickly amass a large number of streams and compete with long-established artists.")
        elif selected_viz == "Danceability vs. Energy":
            self.visualization.plot_danceability_vs_energy(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: Most of the points are concentrated in the range of 40 to 80 for both danceability and energy. This suggests that many popular songs tend to have moderate to high levels of both attributes, making them suitable for dancing and energetic activities.\nThere is no clear correlation between the two factors.")
        elif selected_viz == "Songs Released by Month":
            self.visualization.plot_songs_released_by_month(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The graph shows that most songs are coming out in January and in May. The least amount of songs are published in August. This may be a part of some marketing/pr tactics or strategies regarding publishing songs in music industry.")
        elif selected_viz == "Key vs. Streams":
            self.visualization.plot_key_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The graph illustrates that the key of C# is exceptionally popular, with significantly higher total streams compared to other keys. This trend suggests that songs in this key may have qualities that resonate particularly well with listeners. Other keys like D, E, F, G, and G# also show strong performance, while keys like D# and A are less popular. ")
        elif selected_viz == "Valence vs. Streams":
            self.visualization.plot_valence_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: TThere is no strong correlation between valence and the number of streams. Most songs, regardless of their valence, have streams clustered in the lower range (below 1 billion). A few outliers have much higher streams, but they do not show a clear pattern related to valence.\nHigh-stream songs (above 1 billion streams) are spread across different valence levels, further supporting the idea that musical positivity is not a key determinant of a song's popularity. ")
        elif selected_viz == "Mode vs. Streams":
            self.visualization.plot_mode_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: Despite the preference for Major mode songs, the presence of a considerable number of streams for Minor mode songs indicates that popular music maintains a balance of different emotional tones, catering to a wide range of listener moods and preferences.")
        elif selected_viz == "Danceability vs. BPM":
            self.visualization.plot_danceability_vs_bpm(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: There is a higher concentration of songs with BPM values between 80 and 140. This range is typical for many popular genres such as pop, rock, and electronic dance music, which tend to dominate streaming platforms.\nThere is no clear correlation between BPM and danceability. The points are widely scattered across the plot, indicating that a song can be highly danceable regardless of its BPM, and vice versa.")
        elif selected_viz == "Average BPM vs. Release Year":
            self.visualization.plot_avg_bpm_vs_release_year(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: There are noticeable peaks in average BPM during the early years (around the 1940s and 1950s) and in the 1980s. The peaks from 1980 and 2000 suggest periods when faster-tempo music was particularly popular. In the most recent years (2010s and 2020s), the average BPM appears to have stabilized at a lower range compared to earlier decades. This suggests a trend towards slower-tempo music in recent times.")
        elif selected_viz == "Pie Chart of All Keys":
            self.visualization.plot_pie_chart_of_keys(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The pie chart illustrates a relatively balanced distribution of songs across different keys, with C# being the most popular and D# - the least popular.")
        elif selected_viz == "Collaborative vs. Solo Streams":
            self.visualization.plot_collaborative_vs_solo(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The analysis shows, that the sum of total streams of Solo songs is more than 2 times greater than those which are collaborative. This may be also due to the dataset records as a whole.")
        elif selected_viz == "Danceability vs. Streams":
            self.visualization.plot_danceability_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The scatter plot shows a concentration of songs with mid to high danceability values having a wide range of streams, indicating that while danceability is a factor, it does not solely determine the popularity of a song. Most of the records tend to keep moderate danceability, between 40-90%.")
        elif selected_viz == "Acousticness vs. Streams":
            self.visualization.plot_acousticness_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The scatter plot indicates that in the dataset there is more records with low percentage (0-20%) of acousticnesss. There is no visible correlation between acousticness and streams, indicating that fully acoustic songs can also be popular. ")
        elif selected_viz == "Instrumentalness vs. Streams":
            self.visualization.plot_instrumentalness_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: Most high-stream songs have 0% or low instrumentalness percentage, indicating that purely instrumental tracks are less popular in terms of streaming.")
        elif selected_viz == "Liveness vs. Streams":
            self.visualization.plot_liveness_vs_streams(self.spotify_songs)
            self.label_conclusions.config(
                text="Conclusion: The scatter plot shows a wide distribution of liveness values that favor less liveness according to amount of streams. There is also significantly more records with liveness in a range between 20-40%.")
