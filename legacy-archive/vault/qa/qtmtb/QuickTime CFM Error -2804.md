---
title: QuickTime CFM Error -2804
apple_id: DTS10002007
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb37.html
archived_at: '2026-07-18T02:38:48.520489Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB37QuickTime CFM Error -2804 |

|  |
| --- |
| Q I am using MPW on a PowerMac 8100/80 AV with System 7.5 and QuickTime 2.0, and I am developing a component which uses the MovieToolbox's TransformRect routine. The linker flags unresolved external symbols for the TransformRect function. Linking the component with the import-library QuickTimeLib.xcoff (from ETO #15) satisfies the linker. I get a CFM error of - 2804, with an error string of "QuickTimeLib.xcoff", which I believe suggests that the CFM cannot find the implementation of the QuickTimeLib. What's causing this error, and what can I do to eliminate it? A It's possible that this is happening because you don't have the QuickTime PowerPlug extension installed. PowerPlug is actually the CFM for the few native functions we have for QuickTime (mostly codecs and compression/decompression functions). PowerPlug is included with QuickTime 2.0, so you should have it available. The following is a note relating to weak linking and QuickTime. It includes code that shows how to query for the availability of the library from within the application itself.  QuickTime CFM PowerPlug Libraries, Availability, Weak Links  The Code Fragment Manager supports the concept of "soft" or "weak" linking. If a library is soft-linked, the Process Manager runs your application, even if the library is missing. As a result, the application continues to function when a particular library it calls is not installed. The application can disable areas of functionality based on the current availability of libraries.  MPW PowerPC tools includes MakePEF, a tool with an additional flag that specifies when exported symbols are weak. In this case, the runtime architecture tries to resolve the CFM library, but it doesn't fail if it can't. You can specify that the library has weak linking by adding a tilde (~) character at the end of the - l option to MakePEF. For example, to soft-link to QuickTimeLib, do this:   ```     MakePEF - l QuickTimeLib.xcoff=QuickTimeLib~ ... ```   You can also mark CFM libraries that have weak linking in the Metrowerks PowerPC environment.  Your client program can test for the presence of the CFM library and disable all functionality that depends on it. (for example, if no QuickTime CFM libraries are present, you can disable "Play Movies").  This technique has one drawback -- it does not prevent a problem when a user moves the library after it registers with Gestalt, since the library registers only once, and there is no way to de-register it. There is no direct solution to this problem, but there is an alternative way to determine if the library is loaded -- check the address of one of the library's functions before calling it. In _Inside Macintosh_, this technique is illustrated in the following example:   ``` extern int printf (char *, ...); // ... if (printf == kUnresolvedSymbolAddress)         DebugStr("\printf is not available."); else     printf("Hello, world!\n");  QuickTime also has a new Gestalt selector to determine whether it's safe to call a weak- linked library (gestaltQuickTimeFeatures). This function shows how to initialize QuickTime for 68K and PowerPC Macs:  Boolean    InitQuickTime(void) {     long         qtVersion;     OSErr         anErr; #ifdef powerc     long         qtFeatures; #endif      anErr = Gestalt(gestaltQuickTime, &qtVersion);     if (anErr != noErr)         return false;        // no QT present  #ifdef powerc  // Test if the library is registered.     anErr = Gestalt(gestaltQuickTimeFeatures, &qtFeatures);     if ( !( (anErr == noErr)  &&  (qtFeatures &     (1 << gestaltPPCQuickTimeLibPresent))       )) // not true           return false; #endif      anErr = EnterMovies();     if ( anErr == noErr)         return true;     else         return false;        // problems initializing QuickTime } ```   Both QuickTime Gestalt selectors are tested for in the PowerPC case. You need to test for the presence of both QuickTime and the QuickTime library. If the application is unable to load the CFM library due to lack of space, the application might mysteriously die later, so it's important to always check that the libraries are loaded and available. [May 01 1995] |

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
