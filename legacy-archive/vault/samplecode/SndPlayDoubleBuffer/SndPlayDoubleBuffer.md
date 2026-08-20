---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Introduction/Intro.html
archived_at: '2026-07-18T03:24:54.194941Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](headers-DBFF.h.md)

# SndPlayDoubleBuffer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

The primary purpose of this sample code is to show developers how to use SndPlayDoubleBuffer to play AIFF, WAVE, and .au files asynchronously from disk. To this end this sample can be used to show you how to: 1) parse an AIFF, 'snd ' resource, WAVE, or .au header 2) use PBReadAsync() at interrupt time 3) munge AIFF, WAVE, and .au data into a form the Sound Manager can play 4) set up the sound header to play compressed and uncompressed sounds 5) instantly (well, really quickly) pause a sound 6) stop a sound so you can play from some other part of the sound 7) make it sound like you are playing a sound backwards 8) use completion routines 9) have fun with sounds Requires: Code Warrior Pro 5 (to open the project file), a Mac that's fast enough to play sound from disk. Keywords: sound, play, doublebuffer, SndPlayDoubleBuffer, compress

[Next](headers-DBFF.h.md)

