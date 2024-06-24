import unittest
import pandas as pd
from tkinter import Tk
from ..data_explorer import DataExplorer


class TestDataExplorer(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.data = pd.DataFrame({
            'artist(s)_name': ['Artist 1', 'Artist 2', 'Artist 1', 'Artist 3'],
            'track_name': ['Track 1', 'Track 2', 'Track 3', 'Track 4'],
            'released_year': [2020, 2021, 2020, 2021],
            'streams': [1000, 2000, 1500, 2500],
            'artist_count': [1, 2, 1, 2]
        })
        self.data_explorer = DataExplorer(self.root, self.data)

    def tearDown(self):
        self.root.destroy()

    def test_load_data(self):
        self.data_explorer.load_data(self.data)
        self.assertEqual(len(self.data_explorer.tree.get_children()), len(self.data))

    def test_apply_filter(self):
        self.data_explorer.filter_entry.insert(0, 'Artist 1')
        self.data_explorer.selected_filter_option.set('artist(s)_name')
        self.data_explorer.apply_filter()
        self.assertEqual(len(self.data_explorer.tree.get_children()), 2)

    def test_clear_filter(self):
        self.data_explorer.filter_entry.insert(0, 'Artist 1')
        self.data_explorer.selected_filter_option.set('artist(s)_name')
        self.data_explorer.apply_filter()
        self.data_explorer.clear_filter()
        self.assertEqual(len(self.data_explorer.tree.get_children()), len(self.data))

    def test_classify_tracks(self):
        self.data_explorer.classify_tracks()
        self.assertIn('is_collaborative', self.data_explorer.spotify_songs.columns)
        self.assertEqual(self.data_explorer.spotify_songs['is_collaborative'].iloc[0], 'Solo')
        self.assertEqual(self.data_explorer.spotify_songs['is_collaborative'].iloc[1], 'Collaborative')


if __name__ == '__main__':
    unittest.main()
