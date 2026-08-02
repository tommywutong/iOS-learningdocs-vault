---
title: Sending SCSI or ATA commands to storage devices
apple_id: DTS10001708
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2005-05-10'
source_url: https://developer.apple.com/library/archive/qa/qa1179/_index.html
archived_at: '2026-07-18T02:30:12.147284Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1179

# Sending SCSI or ATA commands to storage devices

## Q:  I'd like to send a SCSI or ATA command to my hard drive, flash memory reader, or other storage device. The SCSITask User Client seems to be the right API for sending SCSI commands, but it doesn't work when I try to use it with these devices. Plus, I can't find an API for sending ATA commands similar to the SCSITask User Client API. What are my options here?

A: I'd like to send a SCSI or ATA command to my hard drive, flash memory reader, or other storage device.

The SCSITask User Client seems to be the right API for sending SCSI commands, but it doesn't work when I try to use it with these devices.

Plus, I can't find an API for sending ATA commands similar to the SCSITask User Client API.

What are my options here?

Mac OS X by design does not support sending SCSI or ATA commands from an application to most storage devices unless the developer provides a custom kernel driver for the device.

The SCSI Architecture Model (SAM) family provides in-kernel logical unit drivers that translate generic I/O requests into device-specific commands for devices that return one of the following four peripheral device types from an INQUIRY command:

- $00 for direct access block devices that comply with the SCSI Block Commands (SBC) specification
- $05 for CD/DVD devices that comply with the SCSI Multimedia Commands (MMC) specification
- $07 for optical memory devices that comply with the SCSI Block Commands specification
- $0E for simplified direct-access devices that comply with the SCSI Reduced Block Commands (RBC) specification

The design of the SAM family only allows one logical unit driver at a time to control a device. This architecture has two significant advantages. First, the integrity of the operating system and the user's data is protected because applications cannot directly change the state of a device without the cooperation of an in-kernel logical unit driver provided by the developer. Second, the security of the user's data is enhanced because applications cannot arbitrarily bypass file system permissions by sending I/O commands directly to a storage device.

The SCSITask User Client implements a device interface that allows an application to become the logical unit driver for supported devices and thus send SCSI commands to those devices. The SCSITask User Client API is supported for devices such as printers, scanners, tape drives, and medium changers which have peripheral device types other than those listed above. This API is also supported for peripheral device type $05 authoring devices that comply with the MMC specification, such as CD and DVD burners.

The same design applies to the ATA family as well: sending commands directly to ATA and Serial ATA (SATA) devices is unsupported. However, the ATA family does provide a device interface that allows applications to read SMART (Self-Monitoring, Analysis, and Reporting Technology) data from ATA and SATA devices that implement the SMART feature set.

If you're just interested in the information you'd get from a SCSI INQUIRY or an ATA IDENTIFY DEVICE command, much of that information is already published in the I/O Registry and thus is readable by applications without sending commands to the device in question. You can use the application `/Developer/Applications/IORegistryExplorer` or the command line tool `ioreg` to see if the information you need is in the I/O Registry. There are a number of code samples showing how to search and retrieve properties from the I/O Registry such as [CDROMSample](https://developer.apple.com/samplecode/CDROMSample/CDROMSample.html) and the samples in `/Developer/Examples/IOKit.`

To perform block-level I/O operations from an application, you can use the BSD raw disk device in `/dev.` This is described in [Working with Device Files for Storage Devices](https://developer.apple.com/documentation/DeviceDrivers/Conceptual/WorkingWStorage/index.html). An example of this is [AudioCDSample](https://developer.apple.com/samplecode/AudioCDSample/AudioCDSample.html).

As was mentioned earlier, you will need to implement your own custom subclass of Apple's logical unit drivers to allow your application to send SCSI or ATA commands to devices not supported by the SCSITask User Client or the SMART device interface. Guidance for writing such a driver can be found in [Writing Drivers for Mass Storage Devices](https://developer.apple.com/documentation/DeviceDrivers/Conceptual/MassStorage/index.html). A simple example is [VendorSpecificType00](https://developer.apple.com/samplecode/VendorSpecificType00/VendorSpecificType00.html).

Be sure not to send READ or WRITE commands from your custom driver. If you do, you will open a security hole by which malicious code can use your driver to read or destroy data on a device that the user has protected by setting access permissions. Again, if your application needs to perform block-level reads or writes, use the BSD raw disk device instead.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-05-10 | Expanded discussion of Mac OS X storage architecture. Added specific guidance regarding vendor-specific drivers. Updated documentation links. Expanded coverage of ATA commands. |
| 2002-08-06 | New document that explains that Mac OS X does not implement SCSI or ATA pass-through for many mass storage devices. |

