---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/09_RevisionHistory/MS_RevHistory.html
archived_at: '2026-07-15T07:31:32.913012Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Index.md)[Previous](Developing%20a%20Filter%20Scheme.md)

# Document Revision History

This table describes the changes to _Mass Storage Device Driver Programming Guide_.

| __Date__ | __Notes__ |
| 2007-04-03 | Added guidance for creating CDB commands in a custom logical unit driver. |
| 2006-05-23 | Added a caveat that a filter scheme should not produce an IOCDMedia or IODVDMedia object. |
| 2005-12-06 | Made minor corrections. |
| 2005-11-09 | Added caution against sending READ and WRITE commands from a custom logical unit driver. |
| 2005-09-08 | Added chapter on endian issues for mass storage drivers and filter schemes. Changed title from "Writing Drivers for Mass Storage Devices." |
| 2005-04-08 | Fixed links; updated to refer to Xcode. |
| 2005-02-03 | Fixed quotes in newfs_hfs command. |
| 2005-01-11 | Fixed filter scheme sample code to allow filtering the boot volume. Added -nomount option to hdiutil command (for OS X v. 10.2 and later). |
| 2004-05-27 | Fixed URL for USB Common Class Specification. |
| 2002-01-15 | First version. |

[Next](Index.md)[Previous](Developing%20a%20Filter%20Scheme.md)

