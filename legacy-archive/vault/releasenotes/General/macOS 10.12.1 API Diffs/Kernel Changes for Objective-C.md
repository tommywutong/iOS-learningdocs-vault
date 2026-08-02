---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Objective-C/Kernel.html
archived_at: '2026-07-18T02:51:43.553779Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# Kernel Changes for Objective-C

### Kernel

#### IOKit/bluetooth/Bluetooth.h

Added [kBluetoothL2CAPChannelMagicPairing](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelmagicpairing)

#### IOKit/bluetooth/BluetoothAssignedNumbers.h

Added [kBluetoothHCIExtendedInquiryResponseDataTypeIndoorPositioning](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeindoorpositioning)Added [kBluetoothHCIExtendedInquiryResponseDataTypeTransportDiscoveryData](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypetransportdiscoverydata)Added [kBluetoothHCIExtendedInquiryResponseDataTypeURI](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeuri)

#### IOKit/hid/IOHIDDevice.h

Removed IOHIDDevice::newUserClientGated()Added IOHIDDevice::newUserClientInternal()

#### IOKit/hid/IOHIDKeys.h

Added [kIOHIDValueOptionsUpdateElementValues](https://developer.apple.com/documentation/iokit/1556610-anonymous/kiohidvalueoptionsupdateelementvalues)

#### IOKit/hid/IOHIDProperties.h

Removed #def kIOHIDUserUsageMapKeyAdded #def kIOHIDUserKeyUsageMapKey

#### IOKit/hid/IOHIDUsageTables.h

Added [kHIDUsage_Snsr_Light_Illuminance](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light_illuminance)

#### IOKit/hidsystem/IOHIDParameter.h

Removed #def kIOHIDMouseClickNotificationAdded #def kHIDPointerReportRateKeyAdded #def kIOHIDResetStickyKeyNotification

#### IOKit/hidsystem/IOHIDSystem.h

Added IOHIDSystem::powerStateHandler()Added IOHIDSystem::sleepDisplayTickle()Added IOHIDSystem::updatePowerState()

#### IOKit/hidsystem/IOHIDUsageTables.h

Added [kHIDUsage_Snsr_Light_Illuminance](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light_illuminance)

#### IOKit/IOTimeStamp.h

Added #def IODBG_IOREGISTRYAdded #def IOREGISTRYENTRY_NAMEAdded #def IOREGISTRYENTRY_NAME_STRING

#### IOKit/usb/IOUSBHostFamily.h

Removed #def kUSBHostControllerPropertyCompanionPresentRemoved #def kUSBHostPortPropertyCompanionPresentAdded #def kUSBHostBillboardDevicePropertydwAlternateModeVdo

#### kern/task.h

Added #def TF_LRETURNWAITAdded #def TF_LRETURNWAITERAdded #def TPF_EXEC_COPYAdded #def TPF_NONE

#### mach/vm_statistics.h

Added #def VM_MEMORY_DFR

#### security/mac_policy.h

Added mpo_vnode_check_getattr_t

#### sys/imgact.h

Added #def IMGPF_EXEC

#### sys/kdebug.h

Added #def DBG_APP_EOSSUPPORTAdded #def DBG_IOREGISTRY

#### sys/ucred.h

Added [set_security_token_task_internal()](https://developer.apple.com/documentation/kernel/2646915-set_security_token_task_internal)

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
