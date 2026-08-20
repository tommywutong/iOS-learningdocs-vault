---
title: NPAPI Core Animation Movie Plugin
apple_id: DTS40011209
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/NPAPI_Core_Animation_Movie_Plugin/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:16:44.894476Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NPAPI Core Animation Movie Plugin](NPAPI%20Core%20Animation%20Movie%20Plugin.md)


[Next](main.m.md)[Previous](NPAPI%20Core%20Animation%20Movie%20Plugin.md)

# ReadMe.txt

```
### NPAPI Core Animation Movie Plugin ###

===========================================================================
DESCRIPTION:

This sample illustrates how to create a modern Netscape-style plugin using NPAPI.  It queries for the Core Animation drawing model and the Cocoa Event model, and enables those technologies if available.  This sample includes an HTML page which embeds the included plug-in to play a movie.  The movie can be played and paused by clicking HTML buttons that script into the plugin.  This plugin also captures keyboard events, so the playback state can also be toggled by pressing the space bar.

This plugin is provided for instructional purpose only.  If you need to play video in a web page, you should consider an HTML5 <video> solution.

For more information about the Core Animation Drawing Model, and the Cocoa Event Model, see:
https://wiki.mozilla.org/NPAPI:CocoaEventModel
https://wiki.mozilla.org/NPAPI:CoreAnimationDrawingModel


===========================================================================
BUILD REQUIREMENTS:

- Xcode 4 or later
- Safari 5.0 and later 

===========================================================================
RUNTIME REQUIREMENTS:

- Safari 5.0 and later

===========================================================================
PACKAGING LIST:

test.html 
    - Sample HTML file that embeds this plugin to play a movie, and has play/pause buttons that script the plugin.

main.m
    - Main file.  Includes code that queries for Core Animation and Cocoa Event support.

MovieNPObject.h
MovieNPObject.m
    - Files to define our movie object.  Initialize our method identifiers and set up functions to invoke them.

MovieControllerLayer.h
MovieControllerLayer.m
    - Set up our movie layer, draw our movie controls and handle mouse events on these controls.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](NPAPI%20Core%20Animation%20Movie%20Plugin.md)

