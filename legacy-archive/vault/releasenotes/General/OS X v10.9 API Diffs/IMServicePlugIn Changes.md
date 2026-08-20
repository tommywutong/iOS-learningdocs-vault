---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/IMServicePlugIn.html
archived_at: '2026-07-18T02:54:13.863401Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# IMServicePlugIn Changes

## IMServicePlugIn

IMServicePlugInFileTransfer.hModified +[IMServicePlugInFileTransfer fileTransferWithPath:type:totalBytes:]

|  | Declaration |
| --- | --- |
| From | + (id)fileTransferWithPath:(NSString \*)path type:(NSString \*)type totalBytes:(unsigned long long)totalBytes |
| To | + (id)fileTransferWithPath:(NSString \*)path type:(NSString \*)type totalBytes:(uint64_t)totalBytes |

Modified -[IMServicePlugInFileTransfer initWithPath:type:totalBytes:]

|  | Declaration |
| --- | --- |
| From | - (id)initWithPath:(NSString \*)path type:(NSString \*)type totalBytes:(unsigned long long)totalBytes |
| To | - (id)initWithPath:(NSString \*)path type:(NSString \*)type totalBytes:(uint64_t)totalBytes |

Modified IMServicePlugInFileTransfer.totalBytes

|  | Declaration |
| --- | --- |
| From | @property(readonly) unsigned long long totalBytes |
| To | @property(readonly) uint64_t totalBytes |

Modified IMServicePlugInFileTransfer.transferredBytes

|  | Declaration |
| --- | --- |
| From | @property(readonly) unsigned long long transferredBytes |
| To | @property(readonly) uint64_t transferredBytes |

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
