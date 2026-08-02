---
title: sndequalizer
apple_id: DTS10000918
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/sndequalizer/Introduction/Intro.html
archived_at: '2026-07-26T19:52:51.760100Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Application%20Files-ComApplication.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sndequalizer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Manage a dialog window containing a graphical equalizer display. |
| __Build Requirements:__ | QuickTime 5 |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample creates and manages a dialog window containing a graphic equalizer display, similar to the one in the "LCD panel" in QuickTime Player. Really there are just two key functions that you use to make this happen, MediaSetSoundEqualizerBands and MediaGetSoundEqualizerBandLevels.
Important Note: While this sample still functions with QuickTime 7, the APIs being demonstrated; MediaSetSoundEqualizerBands and MediaGetSoundEqualizerBandLevel are no longer preferred. Developers should use the new Movie level APIs SetMovieAudioFrequencyMeteringNumBands and GetMovieAudioFrequencyLevels. See the Audio Playback Enhancements section of the QuickTime 7 Update Guide for more information.

[Next](Application%20Files-ComApplication.c.md)

