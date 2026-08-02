---
title: ATAErrorDetector
apple_id: DTS10000419
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ATAErrorDetector/Introduction/Intro.html
archived_at: '2026-07-18T02:59:44.011781Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ATA%20Error%20Detection.c.md)

# ATAErrorDetector

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon PowerBook with ATA manager (190, 2300, 5300, 1400, 3400, 2400). Later PowerBooks are not affected by these bugs, but the test will run. |

ATAErrorDetector is sample code demonstrating how to test for certain kinds of ATA hard drives which would cause problems for some PowerBooks runnning in SCSI disk mode. The sample demonstrates using the ATA inquiry command and the fields returned by this command to determine information about an ATA drive. It detects an error documented in Technote 1116, "PowerBook HD Upgrades and SCSI Disk Mode Compatibility". Requirements: PowerBook with ATA manager (190, 2300, 5300, 1400, 3400, 2400). Later PowerBooks are not affected by these bugs, but the test will run. Keywords: ATA, PowerBook, SCSI, SCSI disk mode, ATAErrorDetector

[Next](ATA%20Error%20Detection.c.md)

