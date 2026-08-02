---
title: PBXGetVolInfo Glue
apple_id: DTS10001193
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-07-30'
source_url: https://developer.apple.com/library/archive/qa/fl/fl07.html
archived_at: '2026-07-18T02:29:28.838264Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Determining volume size](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL07PBXGetVolInfo Glue |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ---   Q: What is the glue for calling `PBXGetVolInfoSync` and `PBXGetVolInfoAsync`?  A: Here is the glue that you need:   |  | | --- | | ``` #if GENERATINGCFM  #include <Traps.h> #include <FSM.h>  // kFSMXGetVolInfo was not introduced until Universal Interfaces 3.0.1.  #if UNIVERSAL_INTERFACES_VERSION < 0x0301     enum {         kFSMXGetVolInfo = 0x0012     }; #endif  // Define the ProcInfoType value for the PBXGetVolInfo routines.  enum {     uppXGetVolInfoProcInfo = kRegisterBased |         RESULT_SIZE(SIZE_CODE(sizeof(OSErr))) |         REGISTER_RESULT_LOCATION(kRegisterD0) |         REGISTER_ROUTINE_PARAMETER(1, kRegisterD0, kFourByteCode) |         REGISTER_ROUTINE_PARAMETER(2, kRegisterD1, kFourByteCode) |         REGISTER_ROUTINE_PARAMETER(3, kRegisterA0, SIZE_CODE(sizeof(XVolumeParamPtr))) };  // Glue for the sync routine.  extern pascal OSErr PBXGetVolInfoSync(XVolumeParamPtr paramBlock) {     return CallOSTrapUniversalProc(GetOSTrapAddress(_FSDispatch), uppXGetVolInfoProcInfo,         kFSMXGetVolInfo,            // selector   in D0         _FSDispatch,                // trap word  in D1         paramBlock                  // paramBlock in A0     ); }  // Glue for the async routine.  extern pascal OSErr PBXGetVolInfoAsync(XVolumeParamPtr paramBlock) {     return CallOSTrapUniversalProc(GetOSTrapAddress(_FSDispatch), uppXGetVolInfoProcInfo,         kFSMXGetVolInfo,            // selector   in D0         _FSDispatch | kAsyncMask,   // trap word  in D1         paramBlock                  // paramBlock in A0     ); }  #endif ``` |  |  | | --- | | __IMPORTANT:__  While the glue in this Q&A has always been correct, DTS has given out incorrect glue for `PBXGetVolInfoSync` to a number of individual developers. This glue appears to work, but there is a distinct chance it will cause the computer to crash eventually. If you are using this incorrect glue, you should update to the glue given above as soon as possible.  You can recognize the incorrect glue by looking at the `ProcInfoType` it constructs. The `ProcInfoType` construction code for the incorrect glue is shown below. |      |  | | --- | | ``` // WARNING: Do not use this code ``` |      |  | | --- | | ``` #define PROCINFO \     kRegisterBased | \     RESULT_SIZE(SIZE_CODE(sizeof(OSErr))) | \     REGISTER_RESULT_LOCATION(kRegisterD0) | \     REGISTER_ROUTINE_PARAMETER(1, kRegisterD0, kTwoByteCode) | \     REGISTER_ROUTINE_PARAMETER(2, kRegisterA0, SIZE_CODE(sizeof(XVolumeParamPtr)))      ``` |    |  | | --- | | ``` // WARNING: Do not use this code ``` |    This `ProcInfoType` is incorrect because it does not describe the use of 68K register D1 as an implicit parameter to `PBXGetVolInfoSync`. Register D1 determines whether the trap runs synchronously or asynchronously. If you fail to set it up, the trap may run asynchronously (based on the previous contents of register D1) which, depending on a variety of circumstances, may crash the computer.  For more information on how to build glue for calling classic 68K code from CFM, including OS traps like `PBXGetVolInfoSync`, read Technote 1127 [In Search of Missing Links](https://developer.apple.com/library/archive/technotes/tn/tn1127.html). |

#### [Jul 30 1998]

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
