---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/TWAIN.html
archived_at: '2026-07-18T02:53:54.303198Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# TWAIN Changes for Swift

### TWAIN

Added TW_PENDINGXFERS.init(Count: TW_UINT16, TW_JOBCONTROL: TW_PENDINGXFERS.__Unnamed_union_TW_JOBCONTROL)Added TW_PENDINGXFERS.TW_JOBCONTROLModified TW_PENDINGXFERS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TW_PENDINGXFERS {     var Count: TW_UINT16     init() } ``` |
| To | ``` struct TW_PENDINGXFERS {     struct __Unnamed_union_TW_JOBCONTROL {         var EOJ: TW_UINT32         var Reserved: TW_UINT32         init(EOJ EOJ: TW_UINT32)         init(Reserved Reserved: TW_UINT32)         init()     }     var Count: TW_UINT16     var TW_JOBCONTROL: TW_PENDINGXFERS.__Unnamed_union_TW_JOBCONTROL     init()     init(Count Count: TW_UINT16, TW_JOBCONTROL TW_JOBCONTROL: TW_PENDINGXFERS.__Unnamed_union_TW_JOBCONTROL) } ``` |

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
