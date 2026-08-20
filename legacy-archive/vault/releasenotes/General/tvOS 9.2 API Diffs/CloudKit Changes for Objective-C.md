---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Objective-C/CloudKit.html
archived_at: '2026-07-18T02:58:04.072127Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# CloudKit Changes for Objective-C

### CloudKit

#### CKContainer.h

Added [-[CKContainer fetchAllLongLivedOperationIDsWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399160-fetchalllonglivedoperationidswit)Added [-[CKContainer fetchLongLivedOperationWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399164-fetchlonglivedoperationwithid)Added CKContainer(CKLongLivedOperations)

#### CKFetchWebAuthTokenOperation.h

Modified [CKFetchWebAuthTokenOperation](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.2 |

#### CKOperation.h

Removed -[CKOperation activityStart]Added [CKOperation.longLived](https://developer.apple.com/documentation/cloudkit/ckoperation/1452374-longlived)Added [CKOperation.longLivedOperationWasPersistedBlock](https://developer.apple.com/documentation/cloudkit/ckoperation/1452366-longlivedoperationwaspersistedbl)Added [CKOperation.operationID](https://developer.apple.com/documentation/cloudkit/ckoperation/1452362-operationid)

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
