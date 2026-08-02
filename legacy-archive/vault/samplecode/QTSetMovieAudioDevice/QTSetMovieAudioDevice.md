---
title: QTSetMovieAudioDevice
apple_id: DTS10003897
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-03-03'
source_url: https://developer.apple.com/library/archive/samplecode/QTSetMovieAudioDevice/Introduction/Intro.html
archived_at: '2026-07-18T03:21:20.212018Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# QTSetMovieAudioDevice

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-03-03 Create a QT audio context for an audio output device and target a movie to render to the context |
| __Build Requirements:__ | Microsoft Visual Studio .NET 2003, Microsoft .NET Framework, DirectX 9 SDK |
| __Runtime Requirements:__ | QuickTime 7 for Windows, Windows 2000 or XP |

QTSetMovieAudioDevice is a simple sample which demonstrates how to create a QTAudioContext for a given audio output device and then target a movie to render to this audio context.
To accomplish this, first use native Windows DirectX APIs to enumerate a list of all available sound output devices. Next, call the QuickTime QTAudioContextCreateForAudioDevice API to create a QuickTime Audio Context (QTAudioContext) from either a device GUID or device name.
Note -- you must have QT 7.0.4 or better installed to create a QuickTime Audio Context from a GUID.
Finally, call SetMovieAudioContext to target the movie to render to the QuickTime Audio Context.

[Next](ReadMe.txt.md)

