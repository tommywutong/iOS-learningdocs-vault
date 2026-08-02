---
title: DataBurn
apple_id: DTS10000465
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-05-09'
source_url: https://developer.apple.com/library/archive/samplecode/DataBurn/Introduction/Intro.html
archived_at: '2026-07-18T03:06:01.468734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# DataBurn

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2012-05-09 Updated for OS X v10.8 and ARC. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbwguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.8 or later, Xcode 4.4 or later. |
| __Runtime Requirements:__ | OS X v10.7 or later. |

DataBurn demonstrates basic features of the DiscRecording framework, and in particular the DRTrack object. The sample shows how to create a DRFolder from an existing folder on a source disk and burn it to disc creating a hybrid ISO9660/Joliet/HFS+ data CD.

The sample also uses the DiscRecordingUI framework to present the standard burn setup and progress user interfaces.

The main functionality is provided in the AppController class. It illustrates how to setup and start a simple single folder data burn.

[Next](README.txt.md)

