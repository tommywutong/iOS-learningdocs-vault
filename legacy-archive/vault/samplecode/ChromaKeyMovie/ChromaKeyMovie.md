---
title: ChromaKeyMovie
apple_id: DTS10000844
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ChromaKeyMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:03:19.317009Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ChromaKeyMovie.h.md)

# ChromaKeyMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates alternative approaches to removing a color from a QuickTime movie. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon 68k or PowerPC (or newer) machines running System 8.5 or later. PC with Intel Pentium or compatible processor. QuickTime 4.0 or later. CodeWarrior Pro 2 or later or Visual C++ 5.0 or later. |

Chromakey Movie is a simple application which is designed to show alternative approaches to removing a color from a QuickTime movie while it is playing and allowing a separate image to be displayed in the removed regions. It demonstrates several features available in QuickTime and Color QuickDraw: Color Quickdraw - The use of GWorlds to store the current QuickTime movie frame, the background image and the composite (movie frame and background) image. - Various arithmetic transfer modes with CopyBits() to manipulate image data between offscreen graphics ports and a visible window. QuickTime - The playing of a movie into an offscreen port and transfer to a visible window. - The use of a modifier track to provide additional information as to the display characteristics of the video tracks in the movie. - Operation of the SetVideoMediaGraphicsMode() function to provide a Chromakeying effect. - The use of the movie controller to manipulate the playback of the movie. Additional features demonstrated - Checking in a PowerPC native application if a system feature is available from a weak linked shared library as Gestalt() doesn't always provide the correct response. - The implementation of the Dialog manager GetStdFilterProc() and SetDialogDefaultItem() functions to provide default alert and warning dialogs with highlighting of the default button. These functions are not documented within Inside Macintosh, but have been available since System 7.0 and are fully explained in the Technical Note "Toolbox - TB 37 - Pending Update Perils". Requirements: 68k or PowerPC (or newer) machines running System 8.5 or later. PC with Intel Pentium or compatible processor. QuickTime 4.0 or later. CodeWarrior Pro 2 or later or Visual C++ 5.0 or later. Keywords: QuickTime, AIFF, Sound, Mixer, Output, Device, Component

[Next](ChromaKeyMovie.h.md)

