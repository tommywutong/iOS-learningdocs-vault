---
title: QuickTime and Native PowerPC
apple_id: DTS10002010
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb40.html
archived_at: '2026-07-18T02:38:48.686297Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A QTMTB40QuickTime and Native PowerPC |

|  |
| --- |
| Q We are calling the DecompressImage() function from QuickTime in native PowerPC code (QuickTime for PowerPC is installed). The graphics compressor is very slow on the PowerPC. It seems that the graphics decompressor may not be ported to the PowerPC and that emulated code is called from native code. Is this true, and if so, what is the solution to this ?   A It's possible that the QuickTime PowerPlug file, which is the CFM library that contains the native codecs, isn't installed in your extension folder. Use the following code to test for availability of this library:  ``` /*  IsQuickTimeCFMInstalled IsQuickTimeInstalled is used to initialize the environment  pascal Boolean    IsQuickTimeCFMInstalled(void)  DESCRIPTION     IsQuickTimeCFMInstalled will test if the CFM QuickTime libraries are     present (QuickTime PowerPlug, for instance), and if the libraries     are still present (this because the libraries are registered once     when Gestalt finds then during runtime, and the end user might     delete these, or move them to another location later)(. */  pascal Boolean IsQuickTimeCFMInstalled(void) {     OSErr     anErr;     long         qtFeatures;  // Test if the library is registered.     anErr = Gestalt(gestaltQuickTimeFeatures, &qtFeatures);      if (!(  (anErr == noErr)  &&     (qtFeatures & (1 << gestaltPPCQuickTimeLibPresent))     )) // not true           return false;  // Test if a function is available (the library is not moved from the // Extension folder), // this is the trick to be used concerning testing if a function // is available via CFM.     if   ( ! EnterMovies )         return false;     else         return true; } ```   You should also be using the QuickTimeLib or QuickTime.xcoff files, which are needed to link together the native code that uses the CFM PowerPlug libraries.  Since the component manager and core parts of QuickTime are not yet native, you will encounter context switches, sometimes frequently (these are usually 50 cycles in length). The gain from using native codecs decreases as the number of context switches increases. However, in the case of the CinePak codecs, we've observed a gain of four times or more during the compression stage. [May 01 1995] |

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
