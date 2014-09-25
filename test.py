#!/usr/bin/env python3

from skelt import petrify, rehydrate, IGNORABLES
from shutil import rmtree
from pathlib import Path

def main():

    replacements = {
        'scalafoo': 'name',
        'Scalafoo': 'Name',
        'Jeff Klukas': 'author',
        'jeff@klukas.net': 'email',
    }

    ignorables = IGNORABLES + [
        'target',
        '.ensime_cache',
    ]

    emptiables = [
        'banner.txt'
    ]

    # Should produce a tree identical to 'scalafoo_skeletonized'
    petrify('skelt/scalafoo', 'skelt/test_skeleton', replacements, ignorables)

    replacements = {
        'name': 'scalafoo',
        'Name': 'Scalafoo',
        'author': 'Jeff Klukas',
        'email': 'jeff@klukas.net',
    }

    # Should produce a tree identical to 'scalafoo'
    rehydrate('skelt/scalafoo_skeletonized', 'skelt/test_scalafoo', replacements)

if __name__ == "__main__":
    main()
