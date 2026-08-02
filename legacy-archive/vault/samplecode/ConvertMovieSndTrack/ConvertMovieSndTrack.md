---
title: ConvertMovieSndTrack
apple_id: DTS10000908
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ConvertMovieSndTrack/Introduction/Intro.html
archived_at: '2026-07-18T03:04:17.867782Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Main.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/ios/#documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html](https://developer.apple.com/library/ios/#documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html)

# ConvertMovieSndTrack

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates using the Sound Converter to transcode a Sound Track from one audio encoding format to another. |
| __Build Requirements:__ | NOTE: Requires QuickTime 6.0 or greater and Mac OS X. There is no CFM target provided. Requirements: QuickTime 6.0+, Mac OS X 10.1.5+, CodeWarrior Pro 8+, Project Builder 1.1.1+ Keywords: QuickTime Audio, SoundConverterFillBuffer, Sound Converter |
| __Runtime Requirements:__ | Mac OS X QuickTime 6.0+, Mac OS X 10.1.5+, CodeWarrior Pro 8+, Project Builder 1.1.1+ |

This sample demonstrates how to use the Sound Converter to transcode a Movies Sound Track from one audio encoding format to another. It uses Standard Compression to configure the audio compressor and creates a QuickTime Movie containing the newly encoded Sound Track. It also demonstrates the preferred way to use the Sound Converter - using SoundConverterFillBuffer - and shows what you need to do to support VBR compression formats - in QuickTime 6, an example is the AAC format, part of MPEG4 audio support. This Sample will also work with any audio file format QuickTime can import as a Movie such as AIFF, WAVE and MP3.

[Next](Main.c.md)

