---
title: AudioFileStreamExample
apple_id: DTS40008648
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-06-29'
source_url: https://developer.apple.com/library/archive/samplecode/AudioFileStreamExample/Introduction/Intro.html
archived_at: '2026-07-18T03:01:24.874750Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AudioFileStreamExample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2013-06-29 Updated Xcode Project [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnruhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.8 SDK or later |
| __Runtime Requirements:__ | Mac OS X v10.8 or later |

The AudioFileStreamExample project provides two targets, a client that receives the streamed data and parses it for the appropriate audio file properties and data, and a server that opens an AudioFile for read and sends the raw bytes over a specified port. The example shows how to utilize the AudioFileStream callback mechanisms to received and process the data provided by the server, and plays the audio data using the AudioQueue API.

[Next](ReadMe.txt.md)

