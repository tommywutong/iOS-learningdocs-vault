---
title: MP3Player
apple_id: DTS10000365
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MP3Player/Introduction/Intro.html
archived_at: '2026-07-18T03:13:56.107026Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Main.c.md)

# MP3Player

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon CodeWarrior Pro 6 or CodeWarrior Pro 7, Mac OS 9.1+ with CarbonLib 1.4+, QuickTime 5.02 or Mac OS X, Universal Interfaces 3.4. |

This example contains two targets:1) MP3 Player FillBuffer shows how to play VBR and Non-VBR MP3 encoded sound files using the SoundConverterFillBuffer APIs and QuickTime.2) MP3 Player ConvertBuffer shows how to play Non-VBR MP3 encoded sound files using the SoundConverterConvertBuffer APIs.Beyond this obvious difference both targets demonstrate the use of the GetSoundDescriptionExtension, and SoundConverterSetInfo APIs to retrieve and use the siDecompressorSettings atom.Egon's developer safety tip: The SoundConverterFillBuffer APIs available with CarbonLib 1.1 and higher are now the preferred set of APIs to use with the SoundConverter.http://developer.apple.com/techpubs/quicktime/qtdevdocs/RM/sndframe.htm#sound Requirements: CodeWarrior Pro 6 or CodeWarrior Pro 7, Mac OS 9.1+ with CarbonLib 1.4+, QuickTime 5.02 or Mac OS X, Universal Interfaces 3.4. Keywords: MP3, QuickTime Audio, SoundConverterFillBuffer, MP3

[Next](Main.c.md)

