---
title: SMARTQuery
apple_id: DTS10004291
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-05-30'
source_url: https://developer.apple.com/library/archive/samplecode/SMARTQuery/Introduction/Intro.html
archived_at: '2026-07-18T03:22:42.029987Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# SMARTQuery

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-05-30 Demonstration of how to access and use S.M.A.R.T. disk monitoring functionality |
| __Build Requirements:__ | Xcode 2.2.1 or newer |
| __Runtime Requirements:__ | Mac OS X 10.4.0 or newer |

S.M.A.R.T. is a technology embedded in most modern ATA and Serial-ATA storage devices. It's purpose is to collect statistical information about the device while in operation and determine when it is approaching a failure. Often it is able to do this early enough to allow for the recovery of most or all of the data contained on that device.

This sample code demonstrates how to extract both the overall pass/fail result from a given device, but also how to access the raw vendor-specific data and thresholds used by the device in calculating this.

[Next](main.m.md)

