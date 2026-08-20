---
title: Workaround for Asynchronous SCSIAction Crashes
apple_id: DTS10001676
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-03-21'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1129.html
archived_at: '2026-07-18T02:38:14.935166Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [SCSI](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxSCSI-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A QA1129Workaround for Asynchronous SCSIAction Crashes |

|  |  |  |
| --- | --- | --- |
| ---   Q: In Mac OS X 10.1.x, why does my CFM application crash when attempting to use the asynchrounous `SCSIAction` calls?  A: Because of a bug (r. 2649048), the proper Mach-O to CFM glue is not being created which will cause your application to crash when `SCSIAction` attempts to call your CFM callback function. To workaround this problem, simply implement the code shown below instead of calling `NewSCSICallbackUPP` and `DisposeSCSICallbackUPP`. Remember to check the Tech Notes released with System Updates and major OS releases so you can remove this workaround after the underlying bug is fixed.     |  | | --- | | ``` SCSICallbackUPP MyNewSCSICallbackUPP(SCSICallbackProcPtr cfmfp) {  #if TARGET_RT_MAC_CFM       long systemVersion = 0;       if (Gestalt(gestaltSystemVersion, &systemVersion) == noErr && systemVersion >= 0x1010)     {         UInt32 temp[6] = {0x3D800000, 0x618C0000, 0x800C0000,                           0x804C0004, 0x7C0903A6, 0x4E800420};          // Must later dispose of allocated memory         UInt32 * mfp = (UInt32*) NewPtr(sizeof(temp));         mfp[0] = temp[0] | ((UInt32)cfmfp >> 16);         mfp[1] = temp[1] | ((UInt32)cfmfp & 0xFFFF);         mfp[2] = temp[2];         mfp[3] = temp[3];         mfp[4] = temp[4];         mfp[5] = temp[5];          MakeDataExecutable(mfp, sizeof(temp));          return ((SCSICallbackUPP)mfp);     }     else     {         return (NewSCSICallbackUPP(cfmfp));     }  #else      return (NewSCSICallbackUPP(cfmfp));  #endif  }    void MyDisposeSCSICallbackUPP(SCSICallbackUPP fp) {  #if TARGET_RT_MAC_CFM      long systemVersion = 0;      if (Gestalt(gestaltSystemVersion, &systemVersion) == noErr && systemVersion >= 0x1010)     {         DisposePtr((char *)fp);     }     else     {         DisposeSCSICallbackUPP(fp);     }  #else      DisposeSCSICallbackUPP(fp);  #endif  } ``` | | __Listing 1.__ Code to create Mach-O to CFM glue. |        ---  [Mar 18 2002] |

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
