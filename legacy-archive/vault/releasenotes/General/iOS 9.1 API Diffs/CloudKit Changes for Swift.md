---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CloudKit.html
archived_at: '2026-07-18T02:57:06.221434Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CloudKit Changes for Swift

### CloudKit

Modified [CKAccountStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckaccountstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKApplicationPermissionStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset)

|  | Protocols |
| --- | --- |
| From | AnyObject, CKRecordValue, NSObjectProtocol |
| To | CKRecordValue |

Modified [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKDatabaseOperation](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKDiscoverAllContactsOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKDiscoveredUserInfo](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKDiscoverUserInfosOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKErrorCode [enum]](https://developer.apple.com/documentation/cloudkit/ckerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CKErrorCode : Int {     case InternalError     case PartialFailure     case NetworkUnavailable     case NetworkFailure     case BadContainer     case ServiceUnavailable     case RequestRateLimited     case MissingEntitlement     case NotAuthenticated     case PermissionFailure     case UnknownItem     case InvalidArguments     case ResultsTruncated     case ServerRecordChanged     case ServerRejectedRequest     case AssetFileNotFound     case AssetFileModified     case IncompatibleVersion     case ConstraintViolation     case OperationCancelled     case ChangeTokenExpired     case BatchRequestFailed     case ZoneBusy     case BadDatabase     case QuotaExceeded     case ZoneNotFound     case LimitExceeded     case UserDeletedZone } extension CKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum CKErrorCode : Int {     case InternalError     case PartialFailure     case NetworkUnavailable     case NetworkFailure     case BadContainer     case ServiceUnavailable     case RequestRateLimited     case MissingEntitlement     case NotAuthenticated     case PermissionFailure     case UnknownItem     case InvalidArguments     case ResultsTruncated     case ServerRecordChanged     case ServerRejectedRequest     case AssetFileNotFound     case AssetFileModified     case IncompatibleVersion     case ConstraintViolation     case OperationCancelled     case ChangeTokenExpired     case BatchRequestFailed     case ZoneBusy     case BadDatabase     case QuotaExceeded     case ZoneNotFound     case LimitExceeded     case UserDeletedZone } extension CKErrorCode : _BridgedNSError { } extension CKErrorCode : _BridgedNSError { } ``` | -- |

Modified [CKFetchNotificationChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKFetchRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKFetchRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKFetchSubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKLocationSortDescriptor](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKLocationSortDescriptor : NSSortDescriptor {     convenience init()     init(key key: String, relativeLocation relativeLocation: CLLocation)     init(coder aDecoder: NSCoder)     @NSCopying var relativeLocation: CLLocation { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class CKLocationSortDescriptor : NSSortDescriptor, NSSecureCoding {     convenience init()     init(key key: String, relativeLocation relativeLocation: CLLocation)     init(coder aDecoder: NSCoder)     @NSCopying var relativeLocation: CLLocation { get } } ``` | NSSecureCoding |

Modified [CKMarkNotificationsReadOperation](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKModifyBadgeOperation](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKModifyRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKModifyRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKModifySubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKNotification](https://developer.apple.com/documentation/cloudkit/cknotification)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKNotificationID](https://developer.apple.com/documentation/cloudkit/cknotification/id)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKNotificationID : NSObject, NSCopying, NSSecureCoding, NSCoding { } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKNotificationID : NSObject, NSCopying, NSSecureCoding { } ``` | NSCopying, NSSecureCoding |

Modified [CKNotificationInfo](https://developer.apple.com/documentation/cloudkit/cknotificationinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCoding, NSCopying {     var alertBody: String?     var alertLocalizationKey: String?     var alertLocalizationArgs: [String]?     var alertActionLocalizationKey: String?     var alertLaunchImage: String?     var soundName: String?     var desiredKeys: [String]?     var shouldBadge: Bool     var shouldSendContentAvailable: Bool     var category: String? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCopying {     var alertBody: String?     var alertLocalizationKey: String?     var alertLocalizationArgs: [String]?     var alertActionLocalizationKey: String?     var alertLaunchImage: String?     var soundName: String?     var desiredKeys: [String]?     var shouldBadge: Bool     var shouldSendContentAvailable: Bool     var category: String? } ``` | NSCopying, NSSecureCoding |

Modified [CKNotificationType [enum]](https://developer.apple.com/documentation/cloudkit/cknotificationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKOperation](https://developer.apple.com/documentation/cloudkit/ckoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKQuery](https://developer.apple.com/documentation/cloudkit/ckquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     init(recordType recordType: String, predicate predicate: NSPredicate)     var recordType: String { get }     @NSCopying var predicate: NSPredicate { get }     var sortDescriptors: [NSSortDescriptor]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKQuery : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     init(recordType recordType: String, predicate predicate: NSPredicate)     var recordType: String { get }     @NSCopying var predicate: NSPredicate { get }     var sortDescriptors: [NSSortDescriptor]? } ``` | NSCopying, NSSecureCoding |

Modified [CKQueryCursor](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding, NSCoding {     init() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding {     init() } ``` | NSCopying, NSSecureCoding |

Modified [CKQueryNotification](https://developer.apple.com/documentation/cloudkit/ckquerynotification)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKQueryNotificationReason [enum]](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecord : NSObject, NSSecureCoding, NSCoding, NSCopying {     init()     init(recordType recordType: String)     init(recordType recordType: String, recordID recordID: CKRecordID)     init(recordType recordType: String, zoneID zoneID: CKRecordZoneID)     var recordType: String { get }     @NSCopying var recordID: CKRecordID { get }     var recordChangeTag: String? { get }     @NSCopying var creatorUserRecordID: CKRecordID? { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID? { get }     @NSCopying var modificationDate: NSDate? { get }     func objectForKey(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKey key: String)     func allKeys() -> [String]     func allTokens() -> [String]     subscript (_ key: String) -> CKRecordValue?     func objectForKeyedSubscript(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKeyedSubscript key: String)     func changedKeys() -> [String]     func encodeSystemFieldsWithCoder(_ coder: NSCoder) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKRecord : NSObject, NSSecureCoding, NSCopying {     init()     init(recordType recordType: String)     init(recordType recordType: String, recordID recordID: CKRecordID)     init(recordType recordType: String, zoneID zoneID: CKRecordZoneID)     var recordType: String { get }     @NSCopying var recordID: CKRecordID { get }     var recordChangeTag: String? { get }     @NSCopying var creatorUserRecordID: CKRecordID? { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID? { get }     @NSCopying var modificationDate: NSDate? { get }     func objectForKey(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKey key: String)     func allKeys() -> [String]     func allTokens() -> [String]     subscript (_ key: String) -> CKRecordValue?     func objectForKeyedSubscript(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKeyedSubscript key: String)     func changedKeys() -> [String]     func encodeSystemFieldsWithCoder(_ coder: NSCoder) } ``` | NSCopying, NSSecureCoding |

Modified [CKRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/id)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     convenience init(recordName recordName: String)     init(recordName recordName: String, zoneID zoneID: CKRecordZoneID)     var recordName: String { get }     var zoneID: CKRecordZoneID { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKRecordID : NSObject, NSSecureCoding, NSCopying {     convenience init()     convenience init(recordName recordName: String)     init(recordName recordName: String, zoneID zoneID: CKRecordZoneID)     var recordName: String { get }     var zoneID: CKRecordZoneID { get } } ``` | NSCopying, NSSecureCoding |

Modified [CKRecordSavePolicy [enum]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKRecordZone](https://developer.apple.com/documentation/cloudkit/ckrecordzone)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCoding, NSCopying {     class func defaultRecordZone() -> CKRecordZone     init()     init(zoneName zoneName: String)     init(zoneID zoneID: CKRecordZoneID)     var zoneID: CKRecordZoneID { get }     var capabilities: CKRecordZoneCapabilities { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCopying {     class func defaultRecordZone() -> CKRecordZone     init()     init(zoneName zoneName: String)     init(zoneID zoneID: CKRecordZoneID)     var zoneID: CKRecordZoneID { get }     var capabilities: CKRecordZoneCapabilities { get } } ``` | NSCopying, NSSecureCoding |

Modified [CKRecordZoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzoneid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(zoneName zoneName: String, ownerName ownerName: String)     var zoneName: String { get }     var ownerName: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(zoneName zoneName: String, ownerName ownerName: String)     var zoneName: String { get }     var ownerName: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [CKRecordZoneNotification](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CKReference](https://developer.apple.com/documentation/cloudkit/ckreference)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKReference : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(recordID recordID: CKRecordID, action action: CKReferenceAction)     convenience init(record record: CKRecord, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID { get } } extension CKReference : CKRecordValue { } ``` | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding |
| To | ``` class CKReference : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(recordID recordID: CKRecordID, action action: CKReferenceAction)     convenience init(record record: CKRecord, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID { get } } extension CKReference : CKRecordValue { } ``` | CKRecordValue, NSCopying, NSSecureCoding |

Modified [CKReferenceAction [enum]](https://developer.apple.com/documentation/cloudkit/ckrecord_reference_action)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CKServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckserverchangetoken)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding, NSCoding {     init() } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding {     init() } ``` | NSCopying, NSSecureCoding |

Modified [CKSubscription](https://developer.apple.com/documentation/cloudkit/cksubscription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKSubscription : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions)     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions)     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     var subscriptionID: String { get }     var subscriptionType: CKSubscriptionType { get }     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     @NSCopying var notificationInfo: CKNotificationInfo?     @NSCopying var zoneID: CKRecordZoneID? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CKSubscription : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions)     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions)     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     var subscriptionID: String { get }     var subscriptionType: CKSubscriptionType { get }     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     @NSCopying var notificationInfo: CKNotificationInfo?     @NSCopying var zoneID: CKRecordZoneID? } ``` | NSCopying, NSSecureCoding |

Modified [CKSubscriptionType [enum]](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
