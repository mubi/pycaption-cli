pycaption-cli
=============

A command line interface for the pycaption module. Forked to add WebVTT support, courtesy of [this Brightcove guide](docs.brightcove.com/en/perform/brightcove-player/guides/webvtt-converter.html).

Setup
=====

    python setup.py install

Usage
=====

From your command line:

    pycaption <path to caption file> [--sami --dfxp --srt --transcript --webvtt]
    
e.g.

    pycaption ../jnorton-caption.scc --dfxp --transcript

Output is written to the screen. To write to a file, use something like this:

    pycaption ../jnorton-caption.xml --webvtt > jnorton.vtt

Supported Formats
=================

 - SCC (read)
 - SRT (read/write)
 - SAMI (read/write)
 - DFXP (read/write)
 - Transcript (write)
 - VTT (read/write)
 
License
=======

This module is Copyright 2012 Joe Norton and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0
