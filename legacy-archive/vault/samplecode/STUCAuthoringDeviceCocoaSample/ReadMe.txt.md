---
title: STUCAuthoringDeviceCocoaSample
apple_id: DTS40009061
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/STUCAuthoringDeviceCocoaSample/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:22:50.850770Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STUCAuthoringDeviceCocoaSample](STUCAuthoringDeviceCocoaSample.md)


[Next](main.m.md)[Previous](STUCAuthoringDeviceCocoaSample.md)

# ReadMe.txt

```
### STUCAuthoringDeviceCocoaSample ###

===========================================================================
DESCRIPTION:

Finds all attached storage devices that use SCSI Multimedia Commands (MMC) and are authoring devices, such as DVD-RW drives. Sends SCSI commands to these devices using the SCSITask User Client (STUC) API.

===========================================================================
BUILD REQUIREMENTS:

Xcode 3.1 or later, Mac OS X Leopard v10.5 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X Leopard v10.5 or later

===========================================================================
PACKAGING LIST:

AuthoringDevice.{h,m}
Class representing an authoring device attached to the system.

AuthoringDeviceTester.{h,m}
Sends commands to an instance of AuthoringDevice.

DeviceDataSource.{h,m}
Table view data source that tracks devices being attached and removed.

InterfaceController.{h,m}
Controller class for the main view.

MyDocument.{h,m}
Main view for the application.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2009 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](STUCAuthoringDeviceCocoaSample.md)

