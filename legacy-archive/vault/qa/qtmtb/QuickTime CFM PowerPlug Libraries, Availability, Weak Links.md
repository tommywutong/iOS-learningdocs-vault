---
title: QuickTime CFM PowerPlug Libraries, Availability, Weak Links
apple_id: DTS10001990
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb20.html
archived_at: '2026-07-18T02:38:47.847380Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > QuickTime](https://developer.apple.com/referencelibrary/QuickTime/index.html)

|  |
| --- |
| Technical Q&A QTMTB20QuickTime CFM PowerPlug Libraries, Availability, Weak Links |

|  |
| --- |
| The Code Fragment Manager supports the concept of "soft" or "weak" linking. If a library is soft-linked, the Process Manager runs your application, even if the library is missing. This means that the application does not die, even if a particular library is not installed, and the application can disable functionality based on library availability.  MPW PowerPC tools include the MakePEF tool with an additional flag that specifies that the exported symbols are weak. In this case the runtime architecture will try to resolve the CFM library, but won't fail if it can't. You can define that the library has weak linking by adding a magic tilde (~) character at the end of the -l option to MakePEF. For example, to soft link to QuickTimeLib you would do the following:   ```     MakePEF -l QuickTimeLib.xcoff=QuickTimeLib~ ... ```   You could also mark CFM libraries as weak using the Metrowerks PowerPC environment.  In the client program you can test that the CFM library was not loaded and for instance disable all functionality that depends on the CFM library (for example, no QuickTime CFM libraries present so "play movies" gets disabled).  Since the library only registers itself with Gestalt once, there's no way to unregister it if the user moves the library. This particular problem does not have any direct solutions, but there's an alternative way to determine if the library is loaded.  The solution is to check the address of one of the functions in the library before calling the library. The PowerPC Inside Macintosh documentation illustrates the technique:   ``` extern int printf (char *, ...); // ... if (printf == kUnresolvedSymbolAddress)         DebugStr("\printf is not available."); else     printf("Hello, world!\n"); ```   QuickTime has a new Gestalt selector to determine whether it's safe to call the weak-linked library (gestaltQuickTimeFeatures). This function shows how to initialize QuickTime, for 68k and PowerPC:   ``` Boolean    InitQuickTime(void) {     long         qtVersion;     OSErr         anErr; #ifdef powerc     long         qtFeatures; #endif      anErr = Gestalt(gestaltQuickTime, &qtVersion);     if (anErr != noErr)         return false;        // no QT present  #ifdef powerc  // Test if the library is registered.     anErr = Gestalt(gestaltQuickTimeFeatures, &qtFeatures);     if ( !( (anErr == noErr)  &&  (qtFeatures         & (1 << gestaltPPCQuickTimeLibPresent))  )) // not true           return false; #endif      anErr = EnterMovies();     if ( anErr == noErr)         return true;     else         return false;        // problems initializing QuickTime } ```   Both QuickTime Gestalt selectors are being tested for in the PowerPC case. You need to test both that QuickTime is present and that the QuickTime library is present.  A simple test to verify that things work properly is to exclude the PowerPlug CFM library from the extension file, or move it out from the folder while the application that needs the library is running.  If the application is unable to load the CFM library due to lack of space, the application might mysteriously die later, so it's important to always check that the libraries are loaded and available. [May 01 1995] |

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
