---
title: SimpleAudioExtraction
apple_id: DTS10003740
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-03'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleAudioExtraction/Introduction/Intro.html
archived_at: '2026-07-18T03:23:52.552478Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# SimpleAudioExtraction

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-01-03 Updated to use AUScheduledSoundPlayer |
| __Build Requirements:__ | Mac OS X 10.4, or Mac OS X 10.3.9 and QuickTime 7.0, Xcode 2.2 |
| __Runtime Requirements:__ | Mac OS X 10.4, or Mac OS X 10.3.9 and QuickTime 7.0 |

Demonstrates how to use the QuickTime 7.0 Audio Extraction APIs: MovieAudioExtractionBegin, MovieAudioExtractionEnd and MovieAudioExtractionFillBuffer and others to extract and mix audio from a QuickTime movie. The extracted movie audio is then scheduled for playback using the AUScheduledSoundPlayer and finally rendered using a Core Audio AUGraph where an audio effect is applied.
(NOTE: The Movie Audio Extraction APIs in QuickTime 7 are now considered the preferred APIs to use for extracting audio from a Movie sound track. Previous techniques involved using the GetMediaSample API to get media sample data from the sound track, as demonstrated by the "SoundPlayer" sample code (and others) on the ADC website. While these techniques still work, they are no longer the preferred method. Use the Movie Audio Extraction APIs instead.)

[Next](main.c.md)

