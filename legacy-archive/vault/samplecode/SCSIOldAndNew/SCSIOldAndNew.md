---
title: SCSIOldAndNew
apple_id: DTS10000448
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2006-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/SCSIOldAndNew/Introduction/Intro.html
archived_at: '2026-07-18T03:22:28.985298Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](OldMethod.c.md)

# SCSIOldAndNew

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-12-07 Updated to produce a universal binary. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbuhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.2.1 or later |
| __Runtime Requirements:__ | Mac OS X 10.2 or later |

Demonstrates how to communicate with SCSI Parallel devices on Mac OS X. The sample illustrates both the SCSITask User Client and IOSCSIUserClient APIs. The IOSCSIUserClient and SCSIAction APIs were deprecated in Mac OS X 10.2 and removed in Mac OS X 10.3.
Developers who want their applications to run on all versions of Mac OS X including 10.2 and earlier should use both SCSITaskUserClient and SCSIAction/IOSCSIUserClient to discover their device, then use the API which found the device to communicate with it. This sample uses this recommended technique to find devices based on their SCSI peripheral device type and then sends a simple INQUIRY command.
This sample code has been updated to include a project that produces a universal binary.

[Next](OldMethod.c.md)

