---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Objective-C/CloudKit.html
archived_at: '2026-07-18T02:57:04.723397Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CloudKit Changes for Objective-C

### CloudKit

#### CKRecord.h

Modified [-[CKRecord objectForKey:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462216-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof id<CKRecordValue> _Nullable)objectForKey:(NSString * _Nonnull)key ``` |
| To | ``` - (id<CKRecordValue>)objectForKey:(NSString *)key ``` |

Modified [-[CKRecord objectForKeyedSubscript:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462210-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` - (__kindof id<CKRecordValue> _Nullable)objectForKeyedSubscript:(NSString * _Nonnull)key ``` |
| To | ``` - (id<CKRecordValue>)objectForKeyedSubscript:(NSString *)key ``` |

Modified [-[CKRecord setObject:forKey:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462231-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(__kindof id<CKRecordValue> _Nullable)object forKey:(NSString * _Nonnull)key ``` |
| To | ``` - (void)setObject:(id<CKRecordValue>)object forKey:(NSString *)key ``` |

Modified [-[CKRecord setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462221-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(__kindof id<CKRecordValue> _Nullable)object forKeyedSubscript:(NSString * _Nonnull)key ``` |
| To | ``` - (void)setObject:(id<CKRecordValue>)object forKeyedSubscript:(NSString *)key ``` |

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
