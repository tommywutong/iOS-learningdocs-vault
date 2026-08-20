---
title: System Error 29
apple_id: DTS10001497
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-09-12'
source_url: https://developer.apple.com/library/archive/qa/ops/ops16.html
archived_at: '2026-07-18T02:29:49.711852Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS16System Error 29 |

|  |
| --- |
| Q My customers report my application crashing with system error 29, but that error is not documented in "Errors.h". What does it mean?    A While system error 29 is not documented in any of the standard places, it is possible to get it in a roundabout fashion. On the original (pre-System 7) Mac OS, the Package Manager was allocated system error numbers 17 to 24 for use when it failed to load a package. The Package Manager raises the error based on the equation `17 + packNum`, where `packNum` was the package number that it couldn't load, ranging from 0 to 7.  __Note:__ For more information about packages, see ["_Inside Macintosh: Operating System Utilities_," Chapter 10](https://developer.apple.com/documentation/mac/OSUtilities/OSUtilities-212.html).  System 7 extended the Mac OS to have more packages; package numbers now range from 0 to 15. Unfortunately the error handler in the Package Manager was not updated to reflect this change, which means it still raises the error based on the equation `17 + packNum`. This produces a number of undocumented error codes, and aliases to existing error codes. The table below gives the exact mapping.   ``` Error  Standard Meaning    Package -----  ----------------    ------- 25     Out of memory         8 AppleEvents 26     Can't launch file     9 PPC Browser 27     File system trashed  10 -- 28     Heap/stack collision 11 Edition Manager 29     --                   12 Color Picker 30     --                   13 Database Access Manager 31     --                   14 Help Manager 32     --                   15 Picture Utils ```   So you can see that System Error 28 can mean either "heap/stack collision", or "could not load the Edition Manager package". And system error 29 almost certainly means "could not load the Color Picker package".  There are a variety of reasons why the Package Manager might fail to load a package, and thus raise this system error. The most common one is that the system heap is too full to load the package's code. Another possibility is that the package is not installed. Finally, it could be that the system resource file is corrupt (either on disk, or maybe just the resource map in memory), and so the Package Manager can't find the PACK resource to load.  You can debug this problem with MacsBug. When you get the error, you will drop into MacsBug. You can then use the "hx" command to switch to the system heap, and the "ht" command to find out how much space is free in the system heap. While you're at it, you should most probably use "hc all" to check all heaps for corruption. Finally, you can also use the command "rd -f 2 -t 'PACK'" to get a dump of `'PACK'` resources in the resource map of the system file, to see if they are all present and loaded. Updated: 12-September-97 |

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
