---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/CloudKit.html
archived_at: '2026-07-18T02:51:48.666922Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CloudKit Changes

## CloudKit

CKDefines.hAdded #def CK_UNIT_TESTS_AVAILABLEAdded #def CK_UNIT_TESTS_EXTERNCKDiscoverAllContactsOperation.hModified [-[CKDiscoverAllContactsOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1514998-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKDiscoverUserInfosOperation.hModified [-[CKDiscoverUserInfosOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403380-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKFetchRecordZonesOperation.hModified [-[CKFetchRecordZonesOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515256-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKFetchRecordsOperation.hModified [-[CKFetchRecordsOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476072-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKFetchSubscriptionsOperation.hModified [-[CKFetchSubscriptionsOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515123-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKLocationSortDescriptor.hModified [-[CKLocationSortDescriptor initWithCoder:]](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515257-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CKLocationSortDescriptor initWithKey:relativeLocation:]](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515071-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKMarkNotificationsReadOperation.hModified [-[CKMarkNotificationsReadOperation initWithNotificationIDsToMarkRead:]](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515228-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKModifyBadgeOperation.hModified [-[CKModifyBadgeOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391678-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKModifyRecordZonesOperation.hModified [-[CKModifyRecordZonesOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415169-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKModifyRecordsOperation.hModified [-[CKModifyRecordsOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447466-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKModifySubscriptionsOperation.hModified [-[CKModifySubscriptionsOperation initWithSubscriptionsToSave:subscriptionIDsToDelete:]](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515015-initwithsubscriptionstosave)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKOperation.hModified [-[CKOperation init]](https://developer.apple.com/documentation/cloudkit/ckoperation/1452370-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKQuery.hModified [-[CKQuery initWithCoder:]](https://developer.apple.com/documentation/cloudkit/ckquery/1413111-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CKQuery initWithRecordType:predicate:]](https://developer.apple.com/documentation/cloudkit/ckquery/1413119-initwithrecordtype)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKQueryOperation.hModified [-[CKQueryOperation init]](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515115-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKRecordID.hModified [-[CKRecordID initWithRecordName:zoneID:]](https://developer.apple.com/documentation/cloudkit/ckrecord/id/1500967-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKRecordZoneID.hModified [-[CKRecordZoneID initWithZoneName:ownerName:]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508089-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKReference.hModified [-[CKReference initWithRecordID:action:]](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1515280-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

CKServerChangeToken.h (Added)Modified [CKServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckserverchangetoken)

|  | Header |
| --- | --- |
| From | CloudKit/CKFetchRecordChangesOperation.h |
| To | CloudKit/CKServerChangeToken.h |

CKSubscription.hModified [-[CKSubscription initWithCoder:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515004-initwithcoder)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CKSubscription initWithRecordType:predicate:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515265-initwithrecordtype)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CKSubscription initWithZoneID:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515215-initwithzoneid)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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
