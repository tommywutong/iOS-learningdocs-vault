---
title: ColorSyncDevices
apple_id: DTS10000724
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorSyncDevices/Introduction/Intro.html
archived_at: '2026-07-18T03:04:01.650012Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# ColorSyncDevices

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to use the new ColorSync Device Support APIs introduced with Mac OS X. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon OS X |

README document ColorSyncDevices Sample Code September 10, 2002 Version 1.0 This code demonstrates how to use the new ColorSync Device Support API's introduced with Mac OS X. More specifically, this sample demonstrates how to use the following API's: CMGetDefaultDevice CMGetDeviceProfile CMIterateColorDevices CMIterateDeviceProfiles The program first displays the default display device and profile using CMGetDefaultDevice and CMGetDeviceProfile. Next, it iterates over and displays all ColorSync devices using CMIterateColorDevices. Lastly, CMIterateDeviceProfiles is used to iterate over the current, custom and factory profiles for each device. Note all output is directed to the console. Requirements: OS X Keywords: ColorSync

[Next](main.c.md)

