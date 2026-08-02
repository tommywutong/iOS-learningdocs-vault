---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/IOKit.html
archived_at: '2026-07-18T02:53:07.740206Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOKit Changes for Objective-C

### IOKit

#### hid/IOHIDKeys.h

Added #def kIOHIDBatchIntervalKeyAdded #def kIOHIDSystemButtonPressedDuringDarkBootAdded #def kIOHIDUniqueIDKey

#### hidsystem/IOHIDLib.h

Added IOHIDSetOnScreenCursorBounds()

#### IOInterruptAccounting.h

Added #def kInterruptAccountingGroupName

#### IOKitLib.h

Added [IORegistryEntryCopyFromPath()](https://developer.apple.com/documentation/iokit/1514248-ioregistryentrycopyfrompath)Added [IORegistryEntryCopyPath()](https://developer.apple.com/documentation/iokit/1514853-ioregistryentrycopypath)

#### iokitmig.h

Added io_registry_entry_from_path_ool()Added io_registry_entry_get_path_ool()

#### IOReturn.h

Added #def sub_iokit_basebandAdded #def sub_iokit_HDAAdded #def sub_iokit_platformAdded #def sub_iokit_usbaudio

#### IOTypes.h

Added [kIOMapOverwrite](https://developer.apple.com/documentation/iokit/kiomapoverwrite)

#### network/IONetworkMedium.h

Added [kIOMediumEthernet2500BaseT](https://developer.apple.com/documentation/kernel/1645756-anonymous/kiomediumethernet2500baset)Added [kIOMediumEthernet5000BaseT](https://developer.apple.com/documentation/kernel/1645756-anonymous/kiomediumethernet5000baset)

#### ps/IOPowerSources.h

Added #def kIOPMACPowerKeyAdded #def kIOPMBatteryPowerKeyAdded #def kIOPMUPSPowerKey

#### ps/IOPSKeys.h

Added #def kIOPSCommandSendCurrentStateOfChargeAdded #def kIOPSCommandSetCurrentLimitKeyAdded #def kIOPSCommandSetRequiredVoltageKeyAdded #def kIOPSInternalFailureKeyAdded #def kIOPSNominalCapacityKeyAdded #def kIOPSProductIDKeyAdded #def kIOPSVendorIDKey

#### scsi/SCSICmds_INQUIRY_Definitions.h

Added [SCSICmd_INQUIRY_Page00_Header_SPC_16](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_page00_header_spc_16)Added [SCSICmd_INQUIRY_Page80_Header_SPC_16](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_page80_header_spc_16)

#### serial/ioftdi.h (Removed)

Removed BITMODE_BITBANGRemoved BITMODE_CBUSRemoved BITMODE_FT1284Removed BITMODE_MCURemoved BITMODE_MPSSERemoved BITMODE_OPTORemoved BITMODE_RESETRemoved BITMODE_SYNCBBRemoved BITMODE_SYNCFFRemoved ftdi_mpsse_modeRemoved #def SET_BITMODE

#### storage/IOStorage.h

Added #def kIOStorageFeatureBarrier

#### usb/IOUSBUserClient.h

Removed kIOUSBLibInterfaceUserClientV3NumCommands

#### usb/USB.h

Added #def kIOUSBMessageLegacyReEnumerateDeviceAdded #def kIOUSBMessageLegacyResetDeviceAdded #def kIOUSBMessageLegacySuspendDevice

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
