---
title: Find Documents Folder
apple_id: DTS10001498
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-03-26'
source_url: https://developer.apple.com/library/archive/qa/ops/ops17.html
archived_at: '2026-07-18T02:29:49.792121Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A OPS17Find Documents Folder |

|  |
| --- |
| Q The General control panel (GCP) in 7.6, 7.6.1 and 8.0 has the document options: Last folder, Application set folder, and Documents folder. How can my application determine where this folder is?   A The General control panel (GCP) patches `FindFolder` so it will return the correct document folder given the current GCP options. Pass `FindFolder` a `folderType` of '`docs`'. One quick note: Because the GCP patches `FindFolder`, the createFolder option doesn't work. If the folder doesn't exist you won't get an error and it won't be created. You have to write code to determine if the folder actually exist: if it doesn't, you'll have to create it yourself.   [Mar 26 2001] |

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
