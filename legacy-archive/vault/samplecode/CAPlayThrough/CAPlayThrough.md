---
title: CAPlayThrough
apple_id: DTS10004443
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-09-23'
source_url: https://developer.apple.com/library/archive/samplecode/CAPlayThrough/Introduction/Intro.html
archived_at: '2026-07-18T03:02:22.187047Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# CAPlayThrough

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2.2, 2013-09-23 Updated for Xcode 4.6.3. Added v1.0.4 version of required Core Audio Utility Classes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbugmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.7 or later Xcode 4.3 or later |
| __Runtime Requirements:__ | OS X v10.7 or later |

The CAPlayThrough example project provides a Cocoa based sample application for obtaining all possible input and output devices on the system, setting the default device for input and/or output, and playing through audio from the input device to the output. The application uses two instances of the AUHAL audio unit (one for input, one for output) and a varispeed unit in between to compensate for minor sample rate drift. The app also uses a ring buffer to store the captured audio data from input and access it as needed by the output unit.

[Next](ReadMe.txt.md)

