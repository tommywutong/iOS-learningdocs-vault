---
title: QTSetMovieAudioDevice
apple_id: DTS10003897
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-03-03'
source_url: https://developer.apple.com/library/archive/samplecode/QTSetMovieAudioDevice/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:21:20.573999Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSetMovieAudioDevice](QTSetMovieAudioDevice.md)


[Next](EnumDevices.cpp.md)[Previous](QTSetMovieAudioDevice.md)

# ReadMe.txt

```
README - QTSETMOVIEAUDIODEVICE
Version 1.0 (2/22/06)

OVERVIEW

QTSetMovieAudioDevice is a simple sample which demonstrates how to create a QTAudioContext for a given audio output device and then target a movie to render to this audio context. 

DETAILS

To accomplish this, first use native Windows DirectX APIs to enumerate a list of all available sound output devices. Next, call the QuickTime QTAudioContextCreateForAudioDevice API to create a QuickTime Audio Context (QTAudioContext) from either a device GUID or device name. 

Note -- you must have QT 7.0.4 or better installed to create a QuickTime Audio Context from a GUID.

Finally, call SetMovieAudioContext to target the movie to render to the QuickTime Audio Context.

HOW THE APPLICATION WORKS

Simply launch the application and do the following:
 - Use the popup to select the desired sound output device
 - Choose a QuickTime movie file to play
 - Select the "Play Movie" button to play the movie through the selected sound output device
```

[Next](EnumDevices.cpp.md)[Previous](QTSetMovieAudioDevice.md)

