import os
import unittest
from pathlib import Path

import pillow_avif
from PIL import Image

rootdir = Path('./items')
typetiers = {
    'shield': {'maxquality': 5, 'maxtier': 9},
    'staff': {'maxquality': 5, 'maxtier': 16}, 
    'glove': {'maxquality': 5, 'maxtier': 12}, 
    'charm': {'maxquality': 3, 'maxtier': 14}, 
    'material': {'maxquality': 3, 'maxtier': 39}, 
    'sword': {'maxquality': 5, 'maxtier': 16}, 
    'box': {'maxquality': 3, 'maxtier': 2}, 
    'ring': {'maxquality': 5, 'maxtier': 11}, 
    'quiver': {'maxquality': 5, 'maxtier': 9}, 
    'bag': {'maxquality': 5, 'maxtier': 4}, 
    'rune': {'maxquality': 3, 'maxtier': 10}, 
    'hammer': {'maxquality': 5, 'maxtier': 16}, 
    #'book': {'maxquality': 3, 'maxtier': 33}, 
    'armor': {'maxquality': 5, 'maxtier': 10}, 
    'amulet': {'maxquality': 5, 'maxtier': 11}, 
    'totem': {'maxquality': 5, 'maxtier': 9}, 
    'bow': {'maxquality': 5, 'maxtier': 16}, 
    'armlet': {'maxquality': 5, 'maxtier': 12}, 
    'orb': {'maxquality': 5, 'maxtier': 9}, 
    'boot': {'maxquality': 5, 'maxtier': 12}, 
    'mount': {'maxquality': 5, 'maxtier': 25}, 
    'pet': {'maxquality': 5, 'maxtier': 15}, 
    'misc': {'maxquality': 3, 'maxtier': 5}
}

class TestFiles(unittest.TestCase):
    def test_existence(self):
        for type in typetiers:
            for tier in range(0, typetiers[type]['maxtier']+1):
                webp_grey = Path(f'{rootdir}/{type}/{type}{tier}_grey.webp')
                avif_grey = Path(f'{rootdir}/{type}/{type}{tier}_grey.avif')
                self.assertTrue(webp_grey.is_file(), f'Failed {webp_grey}')
                self.assertTrue(avif_grey.is_file(), f'Failed {avif_grey}')
                for qual in range(0, typetiers[type]['maxquality']+1):
                    webp = Path(f'{rootdir}/{type}/{type}{tier}_q{qual}.webp')
                    avif = Path(f'{rootdir}/{type}/{type}{tier}_q{qual}.avif')
                    self.assertTrue(webp.is_file(), f'Failed {webp}')
                    self.assertTrue(avif.is_file(), f'Failed {avif}')

    def test_file_corruption(self):
        for type in typetiers:
            for tier in range(0, typetiers[type]['maxtier']+1):
                webp_grey = Path(f'{rootdir}/{type}/{type}{tier}_grey.webp')
                avif_grey = Path(f'{rootdir}/{type}/{type}{tier}_grey.avif')
                with Image.open(webp_grey): pass
                with Image.open(avif_grey): pass
                for qual in range(0, typetiers[type]['maxquality']+1):
                    webp = Path(f'{rootdir}/{type}/{type}{tier}_q{qual}.webp')
                    avif = Path(f'{rootdir}/{type}/{type}{tier}_q{qual}.avif')
                    with Image.open(webp): pass
                    with Image.open(avif): pass
                    
                

if __name__ == "__main__":
    unittest.main()