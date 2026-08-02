---
title: MyMediaPlayer
apple_id: DTS40009203
resource_type: Sample Code
platform: macOS
topic: null
technology: QTKit
published: '2011-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/MyMediaPlayer/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:16:39.113579Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyMediaPlayer](MyMediaPlayer.md)


[Next](main.m.md)[Previous](MyMediaPlayer.md)

# ReadMe.txt

```
### MyMediaPlayer ###

===========================================================================
DESCRIPTION:

Demonstrates how to play a movie fullscreen using QTKit on Mac OS X 10.6. Handles movie load states. Implements play, pause and fullscreen functionality. Provides an overly window with exit and pause buttons during fullscreen playback.

===========================================================================
BUILD REQUIREMENTS:

Xcode 4

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X 10.6

===========================================================================
PACKAGING LIST:

MyDocument.m
MyDocument.h
- NSDocument subclass that implements a fullscreen movie player. Displays a movie in a document window. Handles movie load states as they change. Implements Play, Pause and Fullscreen buttons.

FullScreenWindow.m
FullScreenWindow.h
- Implements the fullscreen player window functionality. Handles ESC key or Cmd-period keys while in fullscreen mode.

FullScreenOverlayWindowController.m
FullScreenOverlayWindowController.h
- Window controller for the fullscreen overlay window, handles the Play/Pause button.

FullScreen.xib
- The nib file containing the fullscreen window

MyDocument.xib
- The nib file that implements the NSDocument subclass

MainMenu.xib
- The nib file containing the main window.



===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 2.1
- Update for Xcode 4

Version 2.0
- Now handles screen resolution changes on the fly while in fullscreen mode. Command-F key toggles fullscreen. Updated to better demonstrate Cocoa coding best practices.

Version 1.0
- First version.

===========================================================================
Copyright (C) 2009 - 2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](MyMediaPlayer.md)

