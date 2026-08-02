---
title: SCSIHBAEmulator
apple_id: DTS10004195
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-02-20'
source_url: https://developer.apple.com/library/archive/samplecode/SCSIHBAEmulator/Introduction/Intro.html
archived_at: '2026-07-18T03:22:27.564544Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SCSIEmulator.cpp.md)

# SCSIHBAEmulator

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-02-20 Demonstration of how to implement a virtual parallel tasking SCSI host bus adapter (HBA) |
| __Build Requirements:__ | Xcode 2.2.1 with MacOSX10.3.9 SDK for PowerPC-based Macs and MacOSX10.4u SDK for Intel-based Macs |
| __Runtime Requirements:__ | OS X 10.3 or newer for PowerPC-based Macs and 10.4 or newer for Intel-based Macs |

This sample shows how to implement a parallel tasking SCSI host bus adapter (HBA) using IOSCSIParallelInterfaceController. It produces a universal binary KEXT that includes a SCSI target device emulator that is used to create a 20MB RAM disk as a device attached to a virtual HBA.

[Next](SCSIEmulator.cpp.md)

