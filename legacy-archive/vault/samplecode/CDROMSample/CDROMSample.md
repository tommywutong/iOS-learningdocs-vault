---
title: CDROMSample
apple_id: DTS10000423
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2011-05-05'
source_url: https://developer.apple.com/library/archive/samplecode/CDROMSample/Introduction/Intro.html
archived_at: '2026-07-18T03:02:24.786882Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# CDROMSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2011-05-05 Now builds with Xcode 4. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbsgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

This command-line tool demonstrates how to find and read sectors from CD-ROM media on Mac OS X. Techniques shown are: finding ejectable CD-ROM media, locating the BSD /dev/rdisk\* node name corresponding to that media, opening the /dev/rdisk\* node, retrieving the media's preferred block size, reading a sector from the media, and closing the device.

[Next](Readme.txt.md)

