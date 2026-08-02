---
title: Accessing the Geographical Database in Apple's Map Control Panel
apple_id: DTS10001506
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/ops/ops25.html
archived_at: '2026-07-18T02:29:50.275164Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS25Accessing the Geographical Database in Apple's Map Control Panel |

|  |
| --- |
| ---   Q: How can I provide my users with a “hook” to access the geographical database in Apple’s “Map” Control Panel from my application?  A: There’s no supported way of accessing the geographical database contained in the “Map” Control Panel. Here are some hints, however (just to satisfy your curiosity):  The data are stored in a resource of type `'CTY#'`, ID=-4064, in the Map cdev. The resource format is a list of word-aligned (variable length) city entries, preceded by an integer indicating the number of entries. Each entry has the format:  [`Integer`] length in bytes of the entry  [`Longint`] latitude in `Fract`; north = +  [`Longint`] longitude in `Fract`; east = +  [`Longint`] GMT difference in seconds; east = +  [`Longint`] (reserved; set to 0)  [`PascalString`] name of the city. Updated: 17-May-1999 |

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
