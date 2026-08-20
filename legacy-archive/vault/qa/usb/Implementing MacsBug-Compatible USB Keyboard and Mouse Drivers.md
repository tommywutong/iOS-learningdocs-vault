---
title: Implementing MacsBug-Compatible USB Keyboard and Mouse Drivers
apple_id: DTS10002272
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-05-31'
source_url: https://developer.apple.com/library/archive/qa/usb/usb06.html
archived_at: '2026-07-18T02:38:59.671248Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)

|  |
| --- |
| Technical Q&A USB06Implementing MacsBug-Compatible USB Keyboard and Mouse Drivers |

|  |  |
| --- | --- |
| ---   Q: Under MacOS USB 1.4.x, the Apple USB Mouse and Keyboard drivers work better with MacsBug. How can I implement similar functionality in my vendor-specific Mouse and Keyboard driver?  A: MacOS USB 1.4.x implements modifications within the USB Services Library so that when MacsBug is active, the USB Interrupt Service Routine (ISR) limits the processing of data to those devices whose drivers support MacsBug. In prior versions of MacOS USB, the USB ISR continued to process incoming data requests, such that all USB devices would still function within the MacsBug context. To support MacsBug, the following conditions must be true:   - The USB parameter block request must have the   `kUSBDebugAwareFlag` bit set in   the `usbFlags` field. - The `ADBShim` implemented in MacOS 9.0.4 or greater   must be present. - The `ADBShim` must be actively supporting a keyboard   attached to the system.   The `ADBShim` that ships as part of the MacOS ROM file for MacOS 9.0.4 was modified to provide MacsBug support for USB keyboards and mice. The MacOS ROM file is only present on Power Macintosh systems with USB built-in. As of the writing of this Q&A, there is no support for MacsBug for USB keyboards and mice on older Power Macintosh G3 systems.  To support MacsBug, the USB ISR must be aware that MacsBug has been entered. This is handled by the `ADBShim`, when it loads to support a dependent USB Keyboard. The `ADBShim` is also activated for a Blue&White G3 with an ADB keyboard and for keyboards on PowerBook G3 systems with USB built-in. If the `ADBShim` is active only to support a USB mouse, the mouse will not work within MacsBug. Setting the `kUSBDebugAwareFlag` Bit In the [MacOS USB DDK 1.4.1](https://developer.apple.com/hardware/usb/download.htm) and greater, both the Keyboard and Mouse examples demonstrate the use of the `kUSBDebugAwareFlag`. The flag bit is set in the `USBIntRead` parameter block call. When MacsBug is entered, the USB scans each incoming request to check if the `kUSBDebugAwareFlag` bit is set in the usbFlags field. If so, then the `usbCompletion` routine is executed, which normally chains to another `USBIntRead` call. If the bit is not set, the USB ISR queues the request for later processing, after the user leaves MacsBug. The following is an example of setting the `kUSBDebugAwareFlag` bit from code modified from the keyboard sample.   |  | | --- | | ```     // initialize the parameter block     InitParamBlock(pKeyboardPB->pipeRef, &pKeyboardPB->pb);      // specify where the response buffer     pKeyboardPB->pb.usbBuffer = (Ptr)response;      // 8 bytes of data requested for a keyboard read     pKeyboardPB->pb.usbReqCount = 0x08;      // set the interfaceNumber of the keyboard     pKeyboardPB->pb.usb.cntl.WIndex = interfaceNumber;      // set the completion proc     pKeyboardPB->pb.usbCompletion = (USBCompletion)KeyboardCompletionProc;      // user sets the usbRefcon field which remains unchanged     // across the call     pKeyboardPB->pb.usbRefcon |= kCompletionPending;      // Get USB Version to see if we support the     // debug aware flag ( version > 1.4 )     if ( pKeyboardPB->usbVersion >=  kUSBVersion14 )     {         pKeyboardPB->pb.usbFlags |= kUSBDebugAwareFlag;     }      // post the USBIntRead call     myErr = USBIntRead(&pKeyboardPB->pb); ``` |  Supporting the ADBShim When the mouse or keyboard device is attached, the `ADBShim` is notified and it searches for an exported `TheHIDModuleDispatchTable` symbol associated with the device driver. If the symbol is found, then the `USBHIDInstallInterruptProcPtr` field is checked to make sure that it is not nil. The `ADBShim` passes the driver its ISR to be used to process all incoming data. If there is no `TheHIDModuleDispatchTable` or if the `USBHIDInstallInterruptProcPtr` is nil, the `ADBShim` does not support the device. An example of implementing the `TheHIDModuleDispatchTable`, is demonstrated in the Keyboard and Mouse module driver samples which are part of the [MacOS USB DDK 1.4.1.](https://developer.apple.com/hardware/usb/download.htm)  A vendor specific keyboard or mouse driver may implement support for the `kUSBDebugAwareFlag` bit, but not export the `TheHIDModuleDispatchTable`, and still work with MacsBug. For this to happen, a keyboard that is supported by the `ADBShim` must be attached. For this reason, developers find that their keyboards and mice that are supported by vendor-specific drivers work within MacsBug with an Apple USB keyboard attached, but not without it.  A vendor-specific keyboard or mouse driver can implement support for the `TheHIDModuleDispatchTable` as well as the `USBHIDInstallInterruptProcPtr` and still selectively support additional functionality which their product provides. When processing each event, determine which events should be passed to the `ADBShim`. If the event is to be handled by your own code, be aware that the driver may be operating within the MacsBug context. Consider using a [Deferred Task](https://developer.apple.com/documentation/mac/Processes/Processes-120.html#HEADING120-0) to execute your code, in this case. [May 31 2000] |

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
