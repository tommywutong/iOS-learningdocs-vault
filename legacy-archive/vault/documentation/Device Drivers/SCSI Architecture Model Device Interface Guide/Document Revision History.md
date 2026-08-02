---
title: SCSI Architecture Model Device Interface Guide
apple_id: TP40000971
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWithSAM/WWS_RevHistory/WWS_RevHistory.html
archived_at: '2026-07-15T07:31:39.067070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SCSI Architecture Model Device Interface Guide](Introduction%20to%20SCSI%20Architecture%20Model%20Device%20Interface%20Guide.md)


[Previous](Accessing%20SCSI%20Architecture%20Model%20Devices.md)

# Document Revision History

This table describes the changes to _SCSI Architecture Model Device Interface Guide_.

| __Date__ | __Notes__ |
| 2007-02-08 | Made minor corrections. |
| 2005-11-09 | Added information to emphasize what types of commands applications can and cannot send to storage devices. |
| 2005-09-08 | Added information about endian issues. Changed title from "Working With SCSI Architecture Model Devices." |
| 2003-06-12 | The chapter [Accessing SCSI Parallel Devices](Accessing%20SCSI%20Parallel%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobwfvbecsseiffeisq) was revised to use a new code sample (the `SCSIOldAndNew` project, available at [http://developer.apple.com/samplecode/Sample_Code/Devices_and_Hardware.htm](https://developer.apple.com/samplecode/Sample_Code/Devices_and_Hardware.htm)) that demonstrates how to use the APIs of both the deprecated SCSI family and the SCSI Architecture Model family to find and access devices. |
| 2003-05-01 | Preliminary version of _Working With SCSI Parallel and SCSI Architecture Model Devices_. This document comprises two chapters from an earlier version of _Accessing Hardware From Applications_ and includes additional information on how to choose the correct API to work with SCSI Parallel devices. |

[Previous](Accessing%20SCSI%20Architecture%20Model%20Devices.md)

