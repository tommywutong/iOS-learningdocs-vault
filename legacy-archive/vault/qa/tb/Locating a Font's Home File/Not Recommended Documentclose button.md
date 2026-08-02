---
title: Locating a Font's Home File
apple_id: DTS10002204
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-15'
source_url: https://developer.apple.com/library/archive/qa/tb/tb18.html
archived_at: '2026-07-18T02:38:56.217306Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/TextFonts/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/TextFonts/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Text & Fonts > Carbon](https://developer.apple.com/referencelibrary/TextFonts/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A TB18Locating a Font's Home File |

|  |
| --- |
| Q I need to find the home file of a given font. Using the Finder's Find File command doesn't seem to work. Can you provide some code samples to do this?   A Here are some steps that show one way to approach the problem programatically. 1) Find a FOND with the right name (there may be more than one) using GetNamedResource. The first one you find is a good one to start with.  2) On the Handle that's returned, call HomeResFile to find the refnum of the file that contains the resource.  3) Call PBGetFCBInfo on the refnum to determine the location of the file. Note that this won't work if there are multiple refnums for the same file, but in the case of FOND resources, you should be fine.  4) Call GetNextFOND (undocumented, but the function declaration is in Resources.h) with the FOND handle you've just used.  5) If the returned handle is non-nil, go to step 2; otherwise, you're done. [Feb 15 1996] |

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
