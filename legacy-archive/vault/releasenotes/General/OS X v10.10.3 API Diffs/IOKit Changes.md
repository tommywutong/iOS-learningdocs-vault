---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/IOKit.html
archived_at: '2026-07-18T02:51:49.630552Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IOKit Changes

## IOKit

audio/IOAudioDefines.hAdded #def kIOAudioEngineDisableClockBoundsCheckgraphics/IOGraphicsTypes.hAdded [kConnectionVBLMultiplier](https://developer.apple.com/documentation/kernel/1645147-anonymous/kconnectionvblmultiplier)Added [kIOWindowServerActiveAttribute](https://developer.apple.com/documentation/kernel/1645144-anonymous/kiowindowserveractiveattribute)IOKitLib.hModified IOMapMemory()

|  | Deprecation |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.10.2 |

pwr_mgt/IOPM.hRemoved kIOPMThermalWarningLevelCrisisRemoved kIOPMThermalWarningLevelDangerRemoved kIOPMThermalWarningLevelNormalAdded [kIOPMThermalLevelCritical](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermallevelcritical)Added [kIOPMThermalLevelDanger](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermalleveldanger)Added [kIOPMThermalLevelNormal](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermallevelnormal)Added [kIOPMThermalLevelTrap](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermalleveltrap)Added [kIOPMThermalLevelUnknown](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermallevelunknown)Added [kIOPMThermalLevelWarning](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermallevelwarning)Added #def kIOPMThermalWarningLevelCrisisAdded #def kIOPMThermalWarningLevelDangerAdded #def kIOPMThermalWarningLevelNormalscsi/SCSICmds_INQUIRY_Definitions.hAdded [kINQUIRY_VERSION_DESCRIPTOR_NVME](https://developer.apple.com/documentation/iokit/1572862-anonymous/kinquiry_version_descriptor_nvme)usb/USB.hAdded #def kIOUSBMessageTDMLowBatteryAdded #def kOverrideAllowLowPowerAdded #def kOverrideAttachedToCPUAdded [kUSBTDMLowBatteryType](https://developer.apple.com/documentation/kernel/1646362-anonymous/kusbtdmlowbatterytype)usb/USBSpec.hAdded [kUSBBillBoardClass](https://developer.apple.com/documentation/iokit/1424988-device_class_codes/kusbbillboardclass)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
