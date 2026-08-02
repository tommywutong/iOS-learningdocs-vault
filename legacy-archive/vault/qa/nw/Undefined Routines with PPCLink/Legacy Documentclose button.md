---
title: Undefined Routines with PPCLink?
apple_id: DTS10001445
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw33.html
archived_at: '2026-07-18T02:29:45.963715Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW33Undefined Routines with PPCLink? |

|  |  |
| --- | --- |
| ---   Q: I'm trying to use Open Transport from Symantec C++ using PPCLink but it complains that a bunch of routines (`InitOpenTransportPriv`, `OTExitPatchPriv`, etc) are undefined. What's going on?  A: Using SPM 8.0.3 and PPCLink 1.3 from ETO 19, the following things had to be done to get SPM to link an Open Transport program using the external linker:   1. Add "-outputformat xcoff" to your PPCLink settings. This forces PPCLink to    generate an XCOFF file instead of a PEF application. 2. Use the "PPCRuntime.o" from the MPW Libraries folder instead of the default    one provided by SPM. Do this by removing "PPCRuntime.o" from your project and    then adding in the one from ":MPW:Libraries:PPCLibraries:". 3. Add the "OpenTransportAppPPC.o" file to your project in the usual manner. 4. Add the "OpenTransportLib" file to your project by adding it to the PPCLink    settings text field. Simply add the path to the library, enclosed in single    quotes. For example...   'Guy Smiley:Open Transport:Open Transport SDK:Open Tpt Client Developer:PPC Libraries:OpenTransportLib'    |  | | --- | | __Note:__  The single quotes are important! |    For statically linked libraries SPM automatically generates the appropriate arguments for PPCLink, but for shared libraries you have to do it by hand.  Note that you will also have to supply the "-weaklib OpenTransportLib" if you want to import the library weakly. |

#### [May 14 1996]

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
