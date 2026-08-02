---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CloudKit.html
archived_at: '2026-07-18T02:52:09.587972Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CloudKit Changes

## CloudKit

Removed CKApplicationPermissions.valueRemoved CKRecordZoneCapabilities.valueRemoved CKSubscriptionOptions.valueAdded CKApplicationPermissions.init(rawValue: UInt)Added CKRecordZoneCapabilities.init(rawValue: UInt)Added CKSubscriptionOptions.init(rawValue: UInt)Modified CKApplicationPermissions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKApplicationPermissions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var PermissionUserDiscoverability: CKApplicationPermissions { get } } ``` | RawOptionSet |
| To | ``` struct CKApplicationPermissions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PermissionUserDiscoverability: CKApplicationPermissions { get } } ``` | RawOptionSetType |

Modified CKApplicationPermissions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CKAsset.fileURL

|  | Declaration |
| --- | --- |
| From | ``` var fileURL: NSURL! { get } ``` |
| To | ``` @NSCopying var fileURL: NSURL! { get } ``` |

Modified CKAsset.init(fileURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(fileURL fileURL: NSURL!) ``` |
| To | ``` init!(fileURL fileURL: NSURL!) ``` |

Modified CKContainer.init(identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier containerIdentifier: String!) -> CKContainer ``` |
| To | ``` init!(identifier containerIdentifier: String!) -> CKContainer ``` |

Modified CKDiscoverAllContactsOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKDiscoverUserInfosOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKDiscoverUserInfosOperation.init(emailAddresses: [AnyObject]!, userRecordIDs:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(emailAddresses emailAddresses: [AnyObject]!, userRecordIDs userRecordIDs: [AnyObject]!) ``` |
| To | ``` convenience init!(emailAddresses emailAddresses: [AnyObject]!, userRecordIDs userRecordIDs: [AnyObject]!) ``` |

Modified CKDiscoveredUserInfo.userRecordID

|  | Declaration |
| --- | --- |
| From | ``` var userRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var userRecordID: CKRecordID! { get } ``` |

Modified CKFetchNotificationChangesOperation.previousServerChangeToken

|  | Declaration |
| --- | --- |
| From | ``` var previousServerChangeToken: CKServerChangeToken! ``` |
| To | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken! ``` |

Modified CKFetchNotificationChangesOperation.init(previousServerChangeToken: CKServerChangeToken!)

|  | Declaration |
| --- | --- |
| From | ``` init(previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |
| To | ``` init!(previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |

Modified CKFetchRecordChangesOperation.previousServerChangeToken

|  | Declaration |
| --- | --- |
| From | ``` var previousServerChangeToken: CKServerChangeToken! ``` |
| To | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken! ``` |

Modified CKFetchRecordChangesOperation.recordZoneID

|  | Declaration |
| --- | --- |
| From | ``` var recordZoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var recordZoneID: CKRecordZoneID! ``` |

Modified CKFetchRecordChangesOperation.init(recordZoneID: CKRecordZoneID!, previousServerChangeToken: CKServerChangeToken!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordZoneID recordZoneID: CKRecordZoneID!, previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |
| To | ``` init!(recordZoneID recordZoneID: CKRecordZoneID!, previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |

Modified CKFetchRecordZonesOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKFetchRecordZonesOperation.init(recordZoneIDs: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordZoneIDs zoneIDs: [AnyObject]!) ``` |
| To | ``` convenience init!(recordZoneIDs zoneIDs: [AnyObject]!) ``` |

Modified CKFetchRecordsOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKFetchRecordsOperation.init(recordIDs: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordIDs recordIDs: [AnyObject]!) ``` |
| To | ``` convenience init!(recordIDs recordIDs: [AnyObject]!) ``` |

Modified CKFetchSubscriptionsOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKFetchSubscriptionsOperation.init(subscriptionIDs: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(subscriptionIDs subscriptionIDs: [AnyObject]!) ``` |
| To | ``` convenience init!(subscriptionIDs subscriptionIDs: [AnyObject]!) ``` |

Modified CKLocationSortDescriptor.init(coder: NSCoder!)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init!(coder aDecoder: NSCoder!) ``` |

Modified CKLocationSortDescriptor.init(key: String!, relativeLocation: CLLocation!)

|  | Declaration |
| --- | --- |
| From | ``` init(key key: String!, relativeLocation relativeLocation: CLLocation!) ``` |
| To | ``` init!(key key: String!, relativeLocation relativeLocation: CLLocation!) ``` |

Modified CKLocationSortDescriptor.relativeLocation

|  | Declaration |
| --- | --- |
| From | ``` var relativeLocation: CLLocation! { get } ``` |
| To | ``` @NSCopying var relativeLocation: CLLocation! { get } ``` |

Modified CKMarkNotificationsReadOperation.init(notificationIDsToMarkRead: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(notificationIDsToMarkRead notificationIDs: [AnyObject]!) ``` |
| To | ``` init!(notificationIDsToMarkRead notificationIDs: [AnyObject]!) ``` |

Modified CKModifyBadgeOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKModifyBadgeOperation.init(badgeValue: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(badgeValue badgeValue: Int) ``` |
| To | ``` convenience init!(badgeValue badgeValue: Int) ``` |

Modified CKModifyRecordZonesOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKModifyRecordZonesOperation.init(recordZonesToSave: [AnyObject]!, recordZoneIDsToDelete:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordZonesToSave recordZonesToSave: [AnyObject]!, recordZoneIDsToDelete recordZoneIDsToDelete: [AnyObject]!) ``` |
| To | ``` convenience init!(recordZonesToSave recordZonesToSave: [AnyObject]!, recordZoneIDsToDelete recordZoneIDsToDelete: [AnyObject]!) ``` |

Modified CKModifyRecordsOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKModifyRecordsOperation.clientChangeTokenData

|  | Declaration |
| --- | --- |
| From | ``` var clientChangeTokenData: NSData! ``` |
| To | ``` @NSCopying var clientChangeTokenData: NSData! ``` |

Modified CKModifyRecordsOperation.init(recordsToSave: [AnyObject]!, recordIDsToDelete:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordsToSave records: [AnyObject]!, recordIDsToDelete recordIDs: [AnyObject]!) ``` |
| To | ``` convenience init!(recordsToSave records: [AnyObject]!, recordIDsToDelete recordIDs: [AnyObject]!) ``` |

Modified CKModifySubscriptionsOperation.init(subscriptionsToSave: [AnyObject]!, subscriptionIDsToDelete:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(subscriptionsToSave subscriptionsToSave: [AnyObject]!, subscriptionIDsToDelete subscriptionIDsToDelete: [AnyObject]!) ``` |
| To | ``` init!(subscriptionsToSave subscriptionsToSave: [AnyObject]!, subscriptionIDsToDelete subscriptionIDsToDelete: [AnyObject]!) ``` |

Modified CKNotification.badge

|  | Declaration |
| --- | --- |
| From | ``` var badge: NSNumber! { get } ``` |
| To | ``` @NSCopying var badge: NSNumber! { get } ``` |

Modified CKNotification.init(fromRemoteNotificationDictionary: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromRemoteNotificationDictionary notificationDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init!(fromRemoteNotificationDictionary notificationDictionary: [NSObject : AnyObject]!) ``` |

Modified CKNotification.notificationID

|  | Declaration |
| --- | --- |
| From | ``` var notificationID: CKNotificationID! { get } ``` |
| To | ``` @NSCopying var notificationID: CKNotificationID! { get } ``` |

Modified CKOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKQuery.init(coder: NSCoder!)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init!(coder aDecoder: NSCoder!) ``` |

Modified CKQuery.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! { get } ``` |
| To | ``` @NSCopying var predicate: NSPredicate! { get } ``` |

Modified CKQuery.init(recordType: String!, predicate: NSPredicate!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordType recordType: String!, predicate predicate: NSPredicate!) ``` |
| To | ``` init!(recordType recordType: String!, predicate predicate: NSPredicate!) ``` |

Modified CKQueryNotification.recordID

|  | Declaration |
| --- | --- |
| From | ``` var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID! { get } ``` |

Modified CKQueryOperation.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CKQueryOperation.cursor

|  | Declaration |
| --- | --- |
| From | ``` var cursor: CKQueryCursor! ``` |
| To | ``` @NSCopying var cursor: CKQueryCursor! ``` |

Modified CKQueryOperation.init(cursor: CKQueryCursor!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(cursor cursor: CKQueryCursor!) ``` |
| To | ``` convenience init!(cursor cursor: CKQueryCursor!) ``` |

Modified CKQueryOperation.query

|  | Declaration |
| --- | --- |
| From | ``` var query: CKQuery! ``` |
| To | ``` @NSCopying var query: CKQuery! ``` |

Modified CKQueryOperation.init(query: CKQuery!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(query query: CKQuery!) ``` |
| To | ``` convenience init!(query query: CKQuery!) ``` |

Modified CKQueryOperation.zoneID

|  | Declaration |
| --- | --- |
| From | ``` var zoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var zoneID: CKRecordZoneID! ``` |

Modified CKRecord.creationDate

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var creationDate: NSDate! { get } ``` |

Modified CKRecord.creatorUserRecordID

|  | Declaration |
| --- | --- |
| From | ``` var creatorUserRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var creatorUserRecordID: CKRecordID! { get } ``` |

Modified CKRecord.lastModifiedUserRecordID

|  | Declaration |
| --- | --- |
| From | ``` var lastModifiedUserRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var lastModifiedUserRecordID: CKRecordID! { get } ``` |

Modified CKRecord.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate! { get } ``` |

Modified CKRecord.recordID

|  | Declaration |
| --- | --- |
| From | ``` var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID! { get } ``` |

Modified CKRecord.init(recordType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordType recordType: String!) ``` |
| To | ``` init!(recordType recordType: String!) ``` |

Modified CKRecord.init(recordType: String!, recordID: CKRecordID!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordType recordType: String!, recordID recordID: CKRecordID!) ``` |
| To | ``` init!(recordType recordType: String!, recordID recordID: CKRecordID!) ``` |

Modified CKRecord.init(recordType: String!, zoneID: CKRecordZoneID!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordType recordType: String!, zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init!(recordType recordType: String!, zoneID zoneID: CKRecordZoneID!) ``` |

Modified CKRecordID.init(recordName: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordName recordName: String!) ``` |
| To | ``` convenience init!(recordName recordName: String!) ``` |

Modified CKRecordID.init(recordName: String!, zoneID: CKRecordZoneID!)

|  | Declaration |
| --- | --- |
| From | ``` init(recordName recordName: String!, zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init!(recordName recordName: String!, zoneID zoneID: CKRecordZoneID!) ``` |

Modified CKRecordZone.init(zoneID: CKRecordZoneID!)

|  | Declaration |
| --- | --- |
| From | ``` init(zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init!(zoneID zoneID: CKRecordZoneID!) ``` |

Modified CKRecordZone.init(zoneName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(zoneName zoneName: String!) ``` |
| To | ``` init!(zoneName zoneName: String!) ``` |

Modified CKRecordZoneCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKRecordZoneCapabilities : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var FetchChanges: CKRecordZoneCapabilities { get }     static var Atomic: CKRecordZoneCapabilities { get } } ``` | RawOptionSet |
| To | ``` struct CKRecordZoneCapabilities : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FetchChanges: CKRecordZoneCapabilities { get }     static var Atomic: CKRecordZoneCapabilities { get } } ``` | RawOptionSetType |

Modified CKRecordZoneCapabilities.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CKRecordZoneID.init(zoneName: String!, ownerName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(zoneName zoneName: String!, ownerName ownerName: String!) ``` |
| To | ``` init!(zoneName zoneName: String!, ownerName ownerName: String!) ``` |

Modified CKRecordZoneNotification.recordZoneID

|  | Declaration |
| --- | --- |
| From | ``` var recordZoneID: CKRecordZoneID! { get } ``` |
| To | ``` @NSCopying var recordZoneID: CKRecordZoneID! { get } ``` |

Modified CKReference.init(record: CKRecord!, action: CKReferenceAction)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(record record: CKRecord!, action action: CKReferenceAction) ``` |
| To | ``` convenience init!(record record: CKRecord!, action action: CKReferenceAction) ``` |

Modified CKReference.recordID

|  | Declaration |
| --- | --- |
| From | ``` var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID! { get } ``` |

Modified CKReference.init(recordID: CKRecordID!, action: CKReferenceAction)

|  | Declaration |
| --- | --- |
| From | ``` init(recordID recordID: CKRecordID!, action action: CKReferenceAction) ``` |
| To | ``` init!(recordID recordID: CKRecordID!, action action: CKReferenceAction) ``` |

Modified CKSubscription.init(coder: NSCoder!)

|  | Declaration |
| --- | --- |
| From | ``` init(coder aDecoder: NSCoder!) ``` |
| To | ``` init!(coder aDecoder: NSCoder!) ``` |

Modified CKSubscription.notificationInfo

|  | Declaration |
| --- | --- |
| From | ``` var notificationInfo: CKNotificationInfo! ``` |
| To | ``` @NSCopying var notificationInfo: CKNotificationInfo! ``` |

Modified CKSubscription.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! { get } ``` |
| To | ``` @NSCopying var predicate: NSPredicate! { get } ``` |

Modified CKSubscription.init(recordType: String!, predicate: NSPredicate!, options: CKSubscriptionOptions)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(recordType recordType: String!, predicate predicate: NSPredicate!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` convenience init!(recordType recordType: String!, predicate predicate: NSPredicate!, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified CKSubscription.init(recordType: String!, predicate: NSPredicate!, subscriptionID: String!, options: CKSubscriptionOptions)

|  | Declaration |
| --- | --- |
| From | ``` init(recordType recordType: String!, predicate predicate: NSPredicate!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` init!(recordType recordType: String!, predicate predicate: NSPredicate!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified CKSubscription.zoneID

|  | Declaration |
| --- | --- |
| From | ``` var zoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var zoneID: CKRecordZoneID! ``` |

Modified CKSubscription.init(zoneID: CKRecordZoneID!, options: CKSubscriptionOptions)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(zoneID zoneID: CKRecordZoneID!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` convenience init!(zoneID zoneID: CKRecordZoneID!, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified CKSubscription.init(zoneID: CKRecordZoneID!, subscriptionID: String!, options: CKSubscriptionOptions)

|  | Declaration |
| --- | --- |
| From | ``` init(zoneID zoneID: CKRecordZoneID!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` init!(zoneID zoneID: CKRecordZoneID!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified CKSubscriptionOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKSubscriptionOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var FiresOnRecordCreation: CKSubscriptionOptions { get }     static var FiresOnRecordUpdate: CKSubscriptionOptions { get }     static var FiresOnRecordDeletion: CKSubscriptionOptions { get }     static var FiresOnce: CKSubscriptionOptions { get } } ``` | RawOptionSet |
| To | ``` struct CKSubscriptionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FiresOnRecordCreation: CKSubscriptionOptions { get }     static var FiresOnRecordUpdate: CKSubscriptionOptions { get }     static var FiresOnRecordDeletion: CKSubscriptionOptions { get }     static var FiresOnce: CKSubscriptionOptions { get } } ``` | RawOptionSetType |

Modified CKSubscriptionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CKErrorDomain: NSString! ``` |
| To | ``` let CKErrorDomain: String ``` |

Modified CKErrorRetryAfterKey

|  | Declaration |
| --- | --- |
| From | ``` let CKErrorRetryAfterKey: NSString! ``` |
| To | ``` let CKErrorRetryAfterKey: String ``` |

Modified CKOwnerDefaultName

|  | Declaration |
| --- | --- |
| From | ``` let CKOwnerDefaultName: NSString! ``` |
| To | ``` let CKOwnerDefaultName: String ``` |

Modified CKPartialErrorsByItemIDKey

|  | Declaration |
| --- | --- |
| From | ``` let CKPartialErrorsByItemIDKey: NSString! ``` |
| To | ``` let CKPartialErrorsByItemIDKey: String ``` |

Modified CKRecordChangedErrorAncestorRecordKey

|  | Declaration |
| --- | --- |
| From | ``` let CKRecordChangedErrorAncestorRecordKey: NSString! ``` |
| To | ``` let CKRecordChangedErrorAncestorRecordKey: String ``` |

Modified CKRecordChangedErrorClientRecordKey

|  | Declaration |
| --- | --- |
| From | ``` let CKRecordChangedErrorClientRecordKey: NSString! ``` |
| To | ``` let CKRecordChangedErrorClientRecordKey: String ``` |

Modified CKRecordChangedErrorServerRecordKey

|  | Declaration |
| --- | --- |
| From | ``` let CKRecordChangedErrorServerRecordKey: NSString! ``` |
| To | ``` let CKRecordChangedErrorServerRecordKey: String ``` |

Modified CKRecordTypeUserRecord

|  | Declaration |
| --- | --- |
| From | ``` let CKRecordTypeUserRecord: NSString! ``` |
| To | ``` let CKRecordTypeUserRecord: String ``` |

Modified CKRecordZoneDefaultName

|  | Declaration |
| --- | --- |
| From | ``` let CKRecordZoneDefaultName: NSString! ``` |
| To | ``` let CKRecordZoneDefaultName: String ``` |

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
