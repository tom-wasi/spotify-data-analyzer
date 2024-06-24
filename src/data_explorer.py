import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk, Tk, messagebox
import chardet


class DataExplorer:
    def __init__(self, parent, spotify_songs):
        self.frame_overview = ttk.LabelFrame(parent, text="Dataset Overview")
        self.frame_overview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Store the dataset
        self.spotify_songs = spotify_songs

        # Treeview widget for displaying the dataset
        self.tree = ttk.Treeview(self.frame_overview, columns=list(spotify_songs.columns), show='headings')
        for col in spotify_songs.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Vertical scrollbar
        self.vsb = ttk.Scrollbar(self.frame_overview, orient="vertical", command=self.tree.yview)
        self.vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.vsb.set)

        # Horizontal scrollbar
        self.hsb = ttk.Scrollbar(self.frame_overview, orient="horizontal", command=self.tree.xview)
        self.hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=self.hsb.set)

        self.tree.pack(side='left', fill='both', expand=True)

        self.load_data(spotify_songs)

        # Entry and button for filtering
        self.filter_frame = ttk.Frame(parent)
        self.filter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.filter_label = ttk.Label(self.filter_frame, text="Filter by:")
        self.filter_label.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown for filter options
        self.filter_options = ["artist(s)_name", "track_name", "released_year", "streams"]  # Add more as needed
        self.selected_filter_option = ttk.Combobox(self.filter_frame, values=self.filter_options)
        self.selected_filter_option.grid(row=0, column=1, padx=5, pady=5)
        self.selected_filter_option.current(0)

        self.filter_entry = ttk.Entry(self.filter_frame)
        self.filter_entry.grid(row=0, column=2, padx=5, pady=5)
        self.filter_button = ttk.Button(self.filter_frame, text="Apply Filter", command=self.apply_filter)
        self.filter_button.grid(row=0, column=3, padx=5, pady=5)
        self.clear_button = ttk.Button(self.filter_frame, text="Clear Filter", command=self.clear_filter)
        self.clear_button.grid(row=0, column=4, padx=5, pady=5)

        # Additional buttons for classification and plotting
        self.extra_frame = ttk.Frame(parent)
        self.extra_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.classify_button = ttk.Button(self.extra_frame, text="Classify Tracks", command=self.classify_tracks)
        self.classify_button.grid(row=0, column=0, padx=5, pady=5)
        self.plot_button = ttk.Button(self.extra_frame, text="Plot Collaborative vs Solo",
                                      command=self.plot_collaborative_vs_solo)
        self.plot_button.grid(row=0, column=1, padx=5, pady=5)

    def load_data(self, data):
        try:
            for row in self.tree.get_children():
                self.tree.delete(row)
            for index, row in data.iterrows():
                self.tree.insert("", "end", values=list(row))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading data: {e}")

    def apply_filter(self):
        try:
            filter_column = self.selected_filter_option.get()
            filter_text = self.filter_entry.get()
            filtered_data = self.spotify_songs[
                self.spotify_songs[filter_column].astype(str).str.contains(filter_text, case=False, na=False)]
            self.load_data(filtered_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while applying filter: {e}")

    def clear_filter(self):
        try:
            self.filter_entry.delete(0, 'end')
            self.load_data(self.spotify_songs)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while clearing filter: {e}")

    def classify_tracks(self):
        try:
            self.spotify_songs['is_collaborative'] = self.spotify_songs['artist_count'].apply(
                lambda x: 'Collaborative' if x > 1 else 'Solo')
            self.load_data(self.spotify_songs)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while classifying tracks: {e}")

    def get_collaboration_streams_summary(self):
        try:
            summary = self.spotify_songs.groupby('is_collaborative')['streams'].sum().reset_index()
            return summary
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while summarizing data: {e}")
            return pd.DataFrame()

    def plot_collaborative_vs_solo(self):
        try:
            summary = self.get_collaboration_streams_summary()
            plt.figure(figsize=(10, 6))
            plt.bar(summary['is_collaborative'],
                    summary['streams'] / 1e9)  # convert streams to billions for readability
            plt.title('Total Streams: Collaborative Tracks vs. Solo Tracks')
            plt.xlabel('Track Type')
            plt.ylabel('Streams (in billions)')
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while plotting data: {e}")


if __name__ == "__main__":
    try:
        root = Tk()
        with open('data/Popular_Spotify_Songs.csv', 'rb') as f:
            result = chardet.detect(f.read())
        encoding = result['encoding']
        spotify_songs = pd.read_csv('data/Popular_Spotify_Songs.csv', encoding=encoding)
        app = DataExplorer(root, spotify_songs)
        root.mainloop()
    except FileNotFoundError:
        messagebox.showerror("Error", "The data file was not found.")
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Error parsing the data file.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
