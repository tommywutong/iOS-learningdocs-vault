---
title: AudioDataOutputToAudioUnit
apple_id: DTS40007766
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/AudioDataOutputToAudioUnit/Introduction/Intro.html
archived_at: '2026-07-18T03:01:22.175684Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# AudioDataOutputToAudioUnit

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2010-10-26 Fixed misnamed class. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzwgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 and later |
| __Runtime Requirements:__ | Mac OS X v10.6 and later |

AudioDataOutputToAudioUnit is a short sample that demonstrates how to use the QTSampleBuffer objects vended by QTKit capture's QTCaptureDecompressedAudioOutput API with various CoreAudio APIs. The built application uses a QTCaptureSession with a QTCaptureDecompressedAudioOutput to capture audio from the default system input device, applies an effect to that audio using a simple effect AudioUnit, and writes the modified audio to a file using the CoreAudio ExtAudioFile API.

[Next](main.m.md)

