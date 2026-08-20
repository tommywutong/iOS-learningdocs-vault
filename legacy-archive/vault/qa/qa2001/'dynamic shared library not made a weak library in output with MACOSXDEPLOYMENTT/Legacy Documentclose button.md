---
title: '''dynamic shared library not made a weak library in output with MACOSX_DEPLOYMENT_TARGET...''
  bug'
apple_id: DTS10002282
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1233.html
archived_at: '2026-07-18T02:38:20.224470Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Tools > Compiling & Debugging](https://developer.apple.com/referencelibrary/DeveloperTools/idxCompilersDebuggers-date.html)

|  |
| --- |
| Technical Q&A QA1233'dynamic shared library not made a weak library in output with MACOSX_DEPLOYMENT_TARGET...' bug |

|  |
| --- |
| ---   Q: Why does 'ld' give me a warning about my MACOSX_DEPLOYMENT_TARGET environment variable and failing to weak link when I try to build?  A: When building in Project Builder using the December 2002 Mac OS X Developer Tools, you may get the following warning:  `ld: warning dynamic shared library:`  `/path/to/a/library/or/framework/that/you/link/against not made a weak library in output with MACOSX_DEPLOYMENT_TARGET environment variable set to: 10.1`  This is most likely due to bug #3094497, which should be fixed in the next major release of the Mac OS X Developer Tools. Here is what is happening: the framework or library (call it library A) listed by ld is linked by your application, but you use no symbols directly from it. Another framework or library (call it library B) that you link against and use DOES use symbols from library A. The linker gets confused, and tries to weak link library A, when it should instead be linking it strongly. Since by default the MACOSX_DEPLOYMENT_TARGET environment variable (which controls binary features introduced in specific OS versions) is set to 10.1, and weak linking was introduced in 10.2, the warning is generated.  Here are two suggested workarounds in the meantime:  1) If you do not mind weak linking against library A and do not mind requiring Mac OS X 10.2 or higher to run, you can set the MACOSX_DEPLOYMENT_TARGET to 10.2 in a target build setting in Project Builder. Note that after doing this, if you are using cpp-precomp precompiled header technology (instead of newer precompiled header technology like the PFE) you may see lots of warnings about your precompiled headers being broken. To fix this, you need to rebuild your precompiled headers like so from Terminal:  setenv MACOSX_DEPLOYMENT_TARGET 10.2  sudo fixPrecomps -force  2) If you do in fact need to continue building for Mac OS X 10.1 and higher, or don't wish to start weak linking against library A, then you can make a gratuitous reference to a symbol in the library to get the linker to strongly link against it.   ---  [Apr 01, 2003] |

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
