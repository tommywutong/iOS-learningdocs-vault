---
title: Suppressing the Network Configuration Dialog
apple_id: DTS40009293
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/qa/qa1667/_index.html
archived_at: '2026-07-18T02:33:32.781812Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1667

# Suppressing the Network Configuration Dialog

## Q:  When I attach my device, why does a dialog appear asking me to configure it for the network?

A: When I attach my device, why does a dialog appear asking me to configure it for the network?

__Figure 1__  Network Configuration Dialog

!

Starting in Mac OS X 10.5, a dialog prompts the user when a device is connected to the system that could be used for networking, such as a USB Ethernet interface, modem, or serial port adaptor. Two I/O Kit properties are available that device drivers can use to control this dialog.

- The `New Interface Detected Action` property can be added to the I/O Registry properties for the device. Use this property if your device provides a network interface, but you do not want the dialog presented. Devices with this property will still appear in the Network preference pane and will still be usable as networking devices. The property can have the value of `None` or `Prompt`. `None` will prevent the dialog from appearing; while  `Prompt`  will show allow the standard dialog to appear.
- The `HiddenPort`  property can be added to the I/O Registry properties for the device. Use this property if your device will never be used for networking. When this property is set, the device is hidden from the Network preference pane and the System Configuration framework, and cannot be used as a network device. Devices with the  `HiddenPort`  property will never cause the network interface dialog to appear. The value of this property should always be set to `1`.

The `New Interface Detected Action` property is available starting in Mac OS X 10.6 while the  `HiddenPort`  property has been available since Mac OS X 10.2.

Devices that do not require additional drivers to function can use a codeless KEXT to control the dialog. The example KEXTs will merge the correct properties into the `I/O Registry`; however, each KEXT's `Info.plist` file will need to be modified to match the hardware being controlled. For more information on I/O Kit matching dictionaries, as well as KEXT installation, see the document [I/O Kit Fundamentals](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011-CH204). For USB devices, the document [Technical Q&A QA1076, 'Tips on USB driver matching for Mac OS X'](https://developer.apple.com/qa/qa2001/qa1076.html) may also be helpful.

- New Interface Detected Action Example ("qa1667_NewInterfaceDetected.zip", 2.6K)
- HiddenPort Example ("qa1667_HiddenPort.zip", 2.5K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-09 | New document that describes how to suppress the network configuration dialog |

