---
title: PlayTune
apple_id: DTS10000976
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/PlayTune/Introduction/Intro.html
archived_at: '2026-07-18T03:19:09.632295Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-PlayTune.java.md)

# PlayTune

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-05-11 Cleaned up code, updated for new Java and QTJava API, and cleaned up project layout. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydaojxgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

The user is shown a small window with a button on it - click the button to play the tune.

NoteChannels are constructed and given to the TunePlayer to play the tune with. The tune is then constructed using the static methods of the MusicData class to stuff the desired notes/rests/etc. into the data format that the TunePlayer expects.

An AtomicInstrument is used as the instrument for the second part of the tune. It uses a Sin Wave at 440KHz stored in an AIFF file as the sample data.

The sample also shows you how to make a Movie from the Tune that has been constructed.

[Next](src-PlayTune.java.md)

