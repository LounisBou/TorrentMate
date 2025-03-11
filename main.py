#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main entry point for the TorrentMate CLI.
This file allows direct execution of the tool without installing it as a package.
"""

import sys
from torrentmate.torrentmate import main

if __name__ == "__main__":
    sys.exit(main())