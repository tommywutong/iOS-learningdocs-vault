---
title: MP3 Player
apple_id: DTS10000397
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MP3_Player/Introduction/Intro.html
archived_at: '2026-07-18T03:13:56.651827Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# MP3 Player

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 How to wrap a command-line UNIX/Linux application in a Cocoa GUI, calling a the command-line app through NSTask. |
| __Build Requirements:__ | Project Builder 2.0 or higher |
| __Runtime Requirements:__ | Mac OS X, mpg123 for playing mp3 files |

This sample shows how to wrap a command-line UNIX/Linux application in a Cocoa GUI, calling out to the command-line app through NSTask. MP3 Player is just what its name suggests - an MP3 player, and it calls through to the open-source mpg123 command-line mp3 player to do the real work of playing music. What the Cocoa code provides is a nice window with a tableview for holding MP3s which you can drag-and-drop onto the table from the Finder. The tableview handles double-clicking a song to play it, or you can press the play or stop buttons in the window to play the currently selected song. The custom tableview provided also now shows how to highlight every other row in blue, a la iTunes. See the ReadMe file for information on downloading and building mpg123.

[Next](main.m.md)

