---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Objective-C/Kernel.html
archived_at: '2026-07-18T02:53:49.000412Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Kernel Changes for Objective-C

### Kernel

#### bank/bank_types.h

Added #def BANK_PERSONA_TOKENAdded [persona_token](https://developer.apple.com/documentation/kernel/persona_token)Added [proc_persona_info](https://developer.apple.com/documentation/kernel/proc_persona_info)

#### console/video_console.h (Added)

Added [kVCAcquireImmediate](https://developer.apple.com/documentation/kernel/1645948-anonymous/kvcacquireimmediate)Added [kVCDarkBackground](https://developer.apple.com/documentation/kernel/1645948-anonymous/kvcdarkbackground)Added [kVCDarkReboot](https://developer.apple.com/documentation/kernel/1645948-anonymous/kvcdarkreboot)Added [kVCLightBackground](https://developer.apple.com/documentation/kernel/1645948-anonymous/kvclightbackground)Added #def kVCSysctlConsoleOptionsAdded #def kVCSysctlProgressMeterAdded #def kVCSysctlProgressMeterEnableAdded #def kVCSysctlProgressOptionsAdded [kVCUsePosition](https://developer.apple.com/documentation/kernel/1645948-anonymous/kvcuseposition)Added [vc_progress_user_options](https://developer.apple.com/documentation/kernel/vc_progress_user_options)

#### IOKit/bluetooth/BluetoothAssignedNumbers.h

Added [kBluetoothHCIVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciversioncorespecification4_2)Added [kBluetoothLMPVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification4_2)

#### IOKit/hid/IOHIDKeys.h

Added #def kIOHIDPhysicalDeviceUniqueIDKey

#### IOKit/IOService.h

Removed IOService::scheduleFinalize()

#### IOKit/pci/IOPCIDevice.h

Added #def IOPCIPMCSPMEDISABLEINS3_DEFINEDAdded [kPCIPMCSPMEDisableInS3](https://developer.apple.com/documentation/kernel/1640321-anonymous/kpcipmcspmedisableins3)

#### IOKit/scsi/IOSCSIProtocolInterface.h

Removed IOSCSIProtocolInterface::stop()

#### IOKit/usb/IOUSBHostFamily.h

Removed [#def kUSBExpressCardCantWake](https://developer.apple.com/documentation/iokit/kusbexpresscardcantwake)Removed #def kUSBHostPropertyDataToggleResetOverrideAdded #def kUSBHostPortPropertyDisconnectIntervalAdded [kUSBHostPortTypeExpressCard](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypeexpresscard)

#### IOKit/usb/IOUSBHostInterface.h

Added IOUSBHostInterface::destroyPipes()Added IOUSBHostInterface::destroyPipesGated()

#### IOKit/usb/IOUSBHostIOSource.h

Added IOUSBHostIOSource::destroy()Added IOUSBHostIOSource::destroyGated()Added IOUSBHostIOSource::open()Added IOUSBHostIOSource::openGated()

#### IOKit/usb/IOUSBHostPipe.h

Added IOUSBHostPipe::destroyGated()Added IOUSBHostPipe::openGated()

#### kern/assert.h

Added #def assertf

#### mach/mach_host.h

Added [host_set_multiuser_config_flags()](https://developer.apple.com/documentation/kernel/1502470-host_set_multiuser_config_flags)

#### mach/mach_voucher_types.h

Added #def MACH_VOUCHER_ATTR_AUTO_REDEEMAdded #def MACH_VOUCHER_ATTR_SEND_PREPROCESSAdded #def MACH_VOUCHER_ATTR_VALUE_FLAGS_NONEAdded #def MACH_VOUCHER_ATTR_VALUE_FLAGS_PERSISTAdded [mach_voucher_attr_value_flags_t](https://developer.apple.com/documentation/kernel/mach_voucher_attr_value_flags_t)

#### os/overflow.h (Added)

Added #def os_add3_overflowAdded #def os_add_overflowAdded #def os_mul_overflowAdded #def os_sub_overflow

#### sys/kdebug.h

Added #def BANK_SECURE_ORIGINATOR_CHANGEDAdded #def DBG_IMGAdded #def MACH_REC_CORES_FAILSAFEAdded #def MACH_SCHED_LOADAdded #def MACH_SCHED_QUANTUM_EXPIRED

#### sys/mount.h

Removed #def VQ_FLAG1000Added #def VQ_QUOTA

#### sys/proc.h

Added [proc_selfcsflags()](https://developer.apple.com/documentation/kernel/1488989-proc_selfcsflags)

#### sys/syscall.h

Added #def SYS_personaAdded #def SYS_usrctl

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
