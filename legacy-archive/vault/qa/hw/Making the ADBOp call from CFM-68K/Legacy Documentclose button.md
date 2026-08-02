---
title: Making the ADBOp call from CFM-68K
apple_id: DTS10001302
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-05-11'
source_url: https://developer.apple.com/library/archive/qa/hw/hw30.html
archived_at: '2026-07-18T02:29:36.605401Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Accessibility](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAccessibility-date.html)
- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)
- [Hardware & Drivers > Human Interface Device & Force Feedback](https://developer.apple.com/referencelibrary/HardwareDrivers/idxHumanInterfaceDeviceForceFeedback-date.html)

|  |
| --- |
| Technical Q&A HW30Making the ADBOp call from CFM-68K |

|  |  |
| --- | --- |
| ---   Q: When I make the `ADBOp` call from a CFM-68K process, I crash with a bus error. How can I get around this problem?  A: This is a known issue with the glue code implemented in the CFM-68K `InterfaceLib` file. The solution is to implement your own glue code (presented below) to perform the call directly to the 68K trap. You will need to make some minor changes to your program to accommodate the glue code as documented here.   1. Include the code below and change your call from `ADBOp` to `MyADBOp`. 2. If you implement a completion routine, instead of accessing the register parameters directly (the optional `refCon` buffer and the data buffer), you'll need to access them as globals to the fragment. You can find a sample program demonstrating this code on the Developer CD - "SetLED."   For more information on implementing glue code for calls from PowerPC code to 68K code, refer to [Technote 1127: "In Search of Missing Links."](https://developer.apple.com/technotes/tn/tn1127.html) This problem was identified with System Software 8.1. The bug report number is 2227159.   |  | | --- | | ``` #include <Types.h> #include <DeskBus.h> #include <MixedMode.h>   // Instead of making the ADBOp directly, call MyADBOp which makes the appropriate // call depending on the target architecture. For CFM68K, the ADBOpBlock structure // is filled in and the ADBGlue routine above is called. For regular 68K and PPC, // the ADBOp call is made straightaway.   pascal OSErr MyADBOp( Ptr refCon, ADBServiceRoutineUPP compRout, Ptr buffer, short commandNum) { #if TARGET_CPU_68K && TARGET_RT_MAC_CFM     ADBOpBlock adbOpBlock;     adbOpBlock.dataBuffPtr = buffer;     adbOpBlock.opServiceRtPtr = compRout;     adbOpBlock.opDataAreaPtr = refCon;      // Important note: In this sample, we declare the adbOpBlock structure     // as a stack variable. Normally this is a bad practice to use a stack     // parameter for any asynchronous call. ADBOp makes a copy of the     // contents of the structure, so the structure does not need to exist     // for the life of the asynchronous call.      // Note that the refCon value is placed into the ADBOpBlock structure     // for completeness. This program sample assumes that a completion     // routine will access the refCon and the data buffer as globals     // to the process, which is possible under CFM.     return (OSErr) CallUniversalProc((UniversalProcPtr)NGetTrapAddress(0xA07C,0),          kRegisterBased |          RESULT_SIZE(SIZE_CODE(sizeof(OSErr))) |         REGISTER_RESULT_LOCATION(kRegisterD0) |         REGISTER_ROUTINE_PARAMETER(1,         kRegisterA0,         SIZE_CODE(sizeof(&gADBOpBlock)))  |         REGISTER_ROUTINE_PARAMETER(2,         kRegisterD0,         SIZE_CODE(sizeof(commandNum))),         &gADBOpBlock,         commandNum); #else // TARGET_CPU_68K && TARGET_RT_MAC_CFM     return (ADBOp(refCon, compRout, buffer, commandNum)); #endif // TARGET_CPU_68K && TARGET_RT_MAC_CFM } ``` | |

#### [May 11 1998]

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

---
