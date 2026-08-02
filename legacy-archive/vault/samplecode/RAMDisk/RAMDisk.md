---
title: RAMDisk
apple_id: DTS10000430
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RAMDisk/Introduction/Intro.html
archived_at: '2026-07-18T03:21:46.829658Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](RamCDev.c.md)

# RAMDisk

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon System 7.0 |

RAMDisk is a sample demonstrating how to write a simple Mac OS block device driver, in this case a RAM disk. It also demonstrates how to bundle a system extension (INIT), driver (DRVR) and control panel (cdev) in one file, to achieve maximum functionality while minimising the number of items in the System Folder. This sample is a control panel, which installs a RAM disk. It compiles using Metrowerks C and is written almost entirely in C, along with a small assembly language DRVR header. Requirements: System 7.0 Keywords: disk device driver, RAM disk, Driver Gestalt, INIT, cdev, DRVR, control panel, RAMDisk

[Next](RamCDev.c.md)

