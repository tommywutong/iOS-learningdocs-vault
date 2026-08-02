---
title: TbltDrvr
apple_id: DTS10000007
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TbltDrvr/Introduction/Intro.html
archived_at: '2026-07-18T03:26:23.239647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](TbltDrvr.a.md)

# TbltDrvr

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

'ADBS' resources are loaded and executed at boot time (before INIT 31), and they are made of two main parts, the installation or initialization code and the the actual driver. In this example, the installation portion allocates memory in the system heap for the service routine and the "optional data area." It installs the driver using the Apple Desktop Bus (ADB) Manager call _SetADBInfo. Requires: System 7.0 Keywords: ADB

[Next](TbltDrvr.a.md)

