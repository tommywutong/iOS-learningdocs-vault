---
title: SoundPlayer
apple_id: DTS10000922
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundPlayer/Introduction/Intro.html
archived_at: '2026-07-18T03:25:08.699008Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Main.c.md)

# SoundPlayer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Shows how to play VBR and Non-VBR encoded audio using the SoundConverterFillBuffer API and QuickTime. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X QuickTime 6.0+, Mac OS X 10.1.5+, CodeWarrior Pro 8+, Project Builder 1.1.1+ |

SoundPlayer is based on PlaySoundFillBuffer.c originally part of the MP3 Player sample. It has now been updated and shows how to play VBR / Non-VBR encoded audio using the SoundConverterFillBuffer API and QuickTime. This includes VBR formats like MP3 and AAC encoded audio. SoundConverterFillBuffer is the preferred API to use with the SoundConverter. SoundConverterConvertBuffer should no longer be used as it does not support VBR formats and cannot be used with MPEG4 Audio. http://developer.apple.com/techpubs/quicktime/qtdevdocs/RM/sndframe.htm#sound Requirements: QuickTime 6.0+, Mac OS X 10.1.5+, CodeWarrior Pro 8+, Project Builder 1.1.1+ Keywords: QuickTime Audio, SoundConverterFillBuffer, MP3, AAC, MPEG-4 Audio

[Next](Main.c.md)

