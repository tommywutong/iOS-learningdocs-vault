---
title: PowerPC & Writing Info to the Data Fork
apple_id: DTS10001548
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ppcsys/ppcsys07.html
archived_at: '2026-07-18T02:29:54.441972Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A PPCSYS07PowerPC & Writing Info to the Data Fork |

|  |
| --- |
| ---   Q: I'm developing a PowerPC version of my application. In the current version of my app, I write info into the data fork. What is the recommended way to do this for the Power PC?  In the documentation it talks about offsetting the data using the cfrg resource. Would this help? If so, can this be done using Metrowerks CodeWarrior?  A: Yes. Writing information to the data fork of a PowerPC-native application is supported. You can actually write the code fragment and update the `'cfrg'` using `MergeFragment`. `MergeFragment` takes two files and catenates them. It also updates the offset and length fields for the code fragment's `'cfrg'` resource, which doesn't necessarily have to start at the beginning of the fork. In fact, it's easier to read the serial information if you write the code fragment after the serial information.  A caveat: You need to make sure the offset written to the `'cfrg'` is an even value, and optimally, a multiple of four. `MergeFragment` should take care of this, but we recommend checking it in your final build to make sure your `'cfrg'` and data fork are correct. If the offset is not an even value, VM's file-mapping won't work, and you won't notice a problem unless running your application on a system with VM enabled.  You can use `MergeFragment` with Metrowerks' Toolserver interface. Check out the Metrowerks documentation for more details. |

#### [May 01 1995]

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
