---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CloudKit.html
archived_at: '2026-07-18T02:56:42.253430Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CloudKit Changes for Swift

### CloudKit

Removed CKApplicationPermissions.init(_: UInt)Removed CKRecord.setObject(_: CKRecordValue!, forKeyedSubscript: String!)Removed CKRecordZoneCapabilities.init(_: UInt)Removed CKSubscriptionOptions.init(_: UInt)Added [CKDiscoveredUserInfo.displayContact](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436518-displaycontact)Added [CKNotification.category](https://developer.apple.com/documentation/cloudkit/cknotification/1428107-category)Added [CKNotification.subscriptionID](https://developer.apple.com/documentation/cloudkit/cknotification/1428118-subscriptionid)Added [CKNotificationInfo.category](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515082-category)Added CKOperation.activityStart() -> os_activity_tAdded [CKAccountChangedNotification](https://developer.apple.com/documentation/cloudkit/ckaccountchangednotification)Modified [CKAccountStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckaccountstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKApplicationPermissions [struct]](https://developer.apple.com/documentation/cloudkit/ckcontainer_application_permissions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKApplicationPermissions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PermissionUserDiscoverability: CKApplicationPermissions { get } } ``` | RawOptionSetType |
| To | ``` struct CKApplicationPermissions : OptionSetType {     init(rawValue rawValue: UInt)     static var UserDiscoverability: CKApplicationPermissions { get } } ``` | OptionSetType |

Modified [CKApplicationPermissions.UserDiscoverability](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissions/ckapplicationpermissionuserdiscoverability)

|  | Declaration |
| --- | --- |
| From | ``` static var PermissionUserDiscoverability: CKApplicationPermissions { get } ``` |
| To | ``` static var UserDiscoverability: CKApplicationPermissions { get } ``` |

Modified [CKApplicationPermissionStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset)

|  | Declaration |
| --- | --- |
| From | ``` class CKAsset : NSObject {     init!()     init!(fileURL fileURL: NSURL!)     @NSCopying var fileURL: NSURL! { get } } extension CKAsset : CKRecordValue, NSObjectProtocol { } ``` |
| To | ``` class CKAsset : NSObject {     init()     init(fileURL fileURL: NSURL)     @NSCopying var fileURL: NSURL { get } } extension CKAsset : CKRecordValue { } ``` |

Modified [CKAsset.fileURL](https://developer.apple.com/documentation/cloudkit/ckasset/1515050-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fileURL: NSURL! { get } ``` |
| To | ``` @NSCopying var fileURL: NSURL { get } ``` |

Modified [CKAsset.init(fileURL: NSURL)](https://developer.apple.com/documentation/cloudkit/ckasset/1514990-initwithfileurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(fileURL fileURL: NSURL!) ``` |
| To | ``` init(fileURL fileURL: NSURL) ``` |

Modified [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer)

|  | Declaration |
| --- | --- |
| From | ``` class CKContainer : NSObject {     init!()     class func defaultContainer() -> CKContainer!     init!(identifier containerIdentifier: String!) -> CKContainer     class func containerWithIdentifier(_ containerIdentifier: String!) -> CKContainer!     var containerIdentifier: String! { get }     func addOperation(_ operation: CKOperation!) } extension CKContainer {     var privateCloudDatabase: CKDatabase! { get }     var publicCloudDatabase: CKDatabase! { get } } extension CKContainer {     func accountStatusWithCompletionHandler(_ completionHandler: ((CKAccountStatus, NSError!) -> Void)!) } extension CKContainer {     func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock!)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock!) } extension CKContainer {     func fetchUserRecordIDWithCompletionHandler(_ completionHandler: ((CKRecordID!, NSError!) -> Void)!)     func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func discoverUserInfoWithEmailAddress(_ email: String!, completionHandler completionHandler: ((CKDiscoveredUserInfo!, NSError!) -> Void)!)     func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID!, completionHandler completionHandler: ((CKDiscoveredUserInfo!, NSError!) -> Void)!) } ``` |
| To | ``` class CKContainer : NSObject {     init()     class func defaultContainer() -> CKContainer      init(identifier containerIdentifier: String)     class func containerWithIdentifier(_ containerIdentifier: String) -> CKContainer     var containerIdentifier: String? { get }     func addOperation(_ operation: CKOperation) } extension CKContainer {     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get } } extension CKContainer {     func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) } extension CKContainer {     func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) } extension CKContainer {     func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void)     func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void)     func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)     func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) } ``` |

Modified [CKContainer.accountStatusWithCompletionHandler(_: (CKAccountStatus, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399180-accountstatuswithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func accountStatusWithCompletionHandler(_ completionHandler: ((CKAccountStatus, NSError!) -> Void)!) ``` |
| To | ``` func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) ``` |

Modified [CKContainer.addOperation(_: CKOperation)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399215-addoperation)

|  | Declaration |
| --- | --- |
| From | ``` func addOperation(_ operation: CKOperation!) ``` |
| To | ``` func addOperation(_ operation: CKOperation) ``` |

Modified [CKContainer.containerIdentifier](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399182-containeridentifier)

|  | Declaration |
| --- | --- |
| From | ``` var containerIdentifier: String! { get } ``` |
| To | ``` var containerIdentifier: String? { get } ``` |

Modified [CKContainer.defaultContainer() -> CKContainer [class]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399189-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultContainer() -> CKContainer! ``` |
| To | ``` class func defaultContainer() -> CKContainer ``` |

Modified [CKContainer.discoverAllContactUserInfosWithCompletionHandler(_: ([CKDiscoveredUserInfo]?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399199-discoverallcontactuserinfoswithc)

|  | Declaration |
| --- | --- |
| From | ``` func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void) ``` |

Modified [CKContainer.discoverUserInfoWithEmailAddress(_: String, completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399201-discoveruserinfowithemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` func discoverUserInfoWithEmailAddress(_ email: String!, completionHandler completionHandler: ((CKDiscoveredUserInfo!, NSError!) -> Void)!) ``` |
| To | ``` func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) ``` |

Modified [CKContainer.discoverUserInfoWithUserRecordID(_: CKRecordID, completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399217-discoveruserinfowithuserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID!, completionHandler completionHandler: ((CKDiscoveredUserInfo!, NSError!) -> Void)!) ``` |
| To | ``` func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) ``` |

Modified [CKContainer.fetchUserRecordIDWithCompletionHandler(_: (CKRecordID?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399191-fetchuserrecordidwithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func fetchUserRecordIDWithCompletionHandler(_ completionHandler: ((CKRecordID!, NSError!) -> Void)!) ``` |
| To | ``` func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void) ``` |

Modified [CKContainer.init(identifier: String)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399193-containerwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier containerIdentifier: String!) -> CKContainer ``` |
| To | ``` init(identifier containerIdentifier: String) ``` |

Modified [CKContainer.privateCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399205-privateclouddatabase)

|  | Declaration |
| --- | --- |
| From | ``` var privateCloudDatabase: CKDatabase! { get } ``` |
| To | ``` var privateCloudDatabase: CKDatabase { get } ``` |

Modified [CKContainer.publicCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399166-publicclouddatabase)

|  | Declaration |
| --- | --- |
| From | ``` var publicCloudDatabase: CKDatabase! { get } ``` |
| To | ``` var publicCloudDatabase: CKDatabase { get } ``` |

Modified [CKContainer.requestApplicationPermission(_: CKApplicationPermissions, completionHandler: CKApplicationPermissionBlock)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399174-requestapplicationpermission)

|  | Declaration |
| --- | --- |
| From | ``` func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock!) ``` |
| To | ``` func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) ``` |

Modified [CKContainer.statusForApplicationPermission(_: CKApplicationPermissions, completionHandler: CKApplicationPermissionBlock)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399195-status)

|  | Declaration |
| --- | --- |
| From | ``` func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock!) ``` |
| To | ``` func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) ``` |

Modified [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase)

|  | Declaration |
| --- | --- |
| From | ``` class CKDatabase : NSObject {     init!()     func addOperation(_ operation: CKDatabaseOperation!) } extension CKDatabase {     func fetchRecordWithID(_ recordID: CKRecordID!, completionHandler completionHandler: ((CKRecord!, NSError!) -> Void)!)     func saveRecord(_ record: CKRecord!, completionHandler completionHandler: ((CKRecord!, NSError!) -> Void)!)     func deleteRecordWithID(_ recordID: CKRecordID!, completionHandler completionHandler: ((CKRecordID!, NSError!) -> Void)!)     func performQuery(_ query: CKQuery!, inZoneWithID zoneID: CKRecordZoneID!, completionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID!, completionHandler completionHandler: ((CKRecordZone!, NSError!) -> Void)!)     func saveRecordZone(_ zone: CKRecordZone!, completionHandler completionHandler: ((CKRecordZone!, NSError!) -> Void)!)     func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID!, completionHandler completionHandler: ((CKRecordZoneID!, NSError!) -> Void)!)     func fetchSubscriptionWithID(_ subscriptionID: String!, completionHandler completionHandler: ((CKSubscription!, NSError!) -> Void)!)     func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func saveSubscription(_ subscription: CKSubscription!, completionHandler completionHandler: ((CKSubscription!, NSError!) -> Void)!)     func deleteSubscriptionWithID(_ subscriptionID: String!, completionHandler completionHandler: ((String!, NSError!) -> Void)!) } ``` |
| To | ``` class CKDatabase : NSObject {     init()     func addOperation(_ operation: CKDatabaseOperation) } extension CKDatabase {     func fetchRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecord?, NSError?) -> Void)     func saveRecord(_ record: CKRecord, completionHandler completionHandler: (CKRecord?, NSError?) -> Void)     func deleteRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecordID?, NSError?) -> Void)     func performQuery(_ query: CKQuery, inZoneWithID zoneID: CKRecordZoneID?, completionHandler completionHandler: ([CKRecord]?, NSError?) -> Void)     func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: ([CKRecordZone]?, NSError?) -> Void)     func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void)     func saveRecordZone(_ zone: CKRecordZone, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void)     func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZoneID?, NSError?) -> Void)     func fetchSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void)     func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: ([CKSubscription]?, NSError?) -> Void)     func saveSubscription(_ subscription: CKSubscription, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void)     func deleteSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (String?, NSError?) -> Void) } ``` |

Modified [CKDatabase.addOperation(_: CKDatabaseOperation)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449116-addoperation)

|  | Declaration |
| --- | --- |
| From | ``` func addOperation(_ operation: CKDatabaseOperation!) ``` |
| To | ``` func addOperation(_ operation: CKDatabaseOperation) ``` |

Modified [CKDatabase.deleteRecordWithID(_: CKRecordID, completionHandler: (CKRecordID?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449122-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecordWithID(_ recordID: CKRecordID!, completionHandler completionHandler: ((CKRecordID!, NSError!) -> Void)!) ``` |
| To | ``` func deleteRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecordID?, NSError?) -> Void) ``` |

Modified [CKDatabase.deleteRecordZoneWithID(_: CKRecordZoneID, completionHandler: (CKRecordZoneID?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449118-deleterecordzonewithid)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID!, completionHandler completionHandler: ((CKRecordZoneID!, NSError!) -> Void)!) ``` |
| To | ``` func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZoneID?, NSError?) -> Void) ``` |

Modified [CKDatabase.deleteSubscriptionWithID(_: String, completionHandler: (String?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449120-deletesubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSubscriptionWithID(_ subscriptionID: String!, completionHandler completionHandler: ((String!, NSError!) -> Void)!) ``` |
| To | ``` func deleteSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (String?, NSError?) -> Void) ``` |

Modified [CKDatabase.fetchAllRecordZonesWithCompletionHandler(_: ([CKRecordZone]?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449112-fetchallrecordzones)

|  | Declaration |
| --- | --- |
| From | ``` func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: ([CKRecordZone]?, NSError?) -> Void) ``` |

Modified [CKDatabase.fetchAllSubscriptionsWithCompletionHandler(_: ([CKSubscription]?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449110-fetchallsubscriptionswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: ([CKSubscription]?, NSError?) -> Void) ``` |

Modified [CKDatabase.fetchRecordWithID(_: CKRecordID, completionHandler: (CKRecord?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449126-fetchrecordwithid)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRecordWithID(_ recordID: CKRecordID!, completionHandler completionHandler: ((CKRecord!, NSError!) -> Void)!) ``` |
| To | ``` func fetchRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecord?, NSError?) -> Void) ``` |

Modified [CKDatabase.fetchRecordZoneWithID(_: CKRecordZoneID, completionHandler: (CKRecordZone?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449104-fetch)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID!, completionHandler completionHandler: ((CKRecordZone!, NSError!) -> Void)!) ``` |
| To | ``` func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void) ``` |

Modified [CKDatabase.fetchSubscriptionWithID(_: String, completionHandler: (CKSubscription?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449106-fetchsubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` func fetchSubscriptionWithID(_ subscriptionID: String!, completionHandler completionHandler: ((CKSubscription!, NSError!) -> Void)!) ``` |
| To | ``` func fetchSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void) ``` |

Modified [CKDatabase.performQuery(_: CKQuery, inZoneWithID: CKRecordZoneID?, completionHandler: ([CKRecord]?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449127-performquery)

|  | Declaration |
| --- | --- |
| From | ``` func performQuery(_ query: CKQuery!, inZoneWithID zoneID: CKRecordZoneID!, completionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func performQuery(_ query: CKQuery, inZoneWithID zoneID: CKRecordZoneID?, completionHandler completionHandler: ([CKRecord]?, NSError?) -> Void) ``` |

Modified [CKDatabase.saveRecord(_: CKRecord, completionHandler: (CKRecord?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449114-saverecord)

|  | Declaration |
| --- | --- |
| From | ``` func saveRecord(_ record: CKRecord!, completionHandler completionHandler: ((CKRecord!, NSError!) -> Void)!) ``` |
| To | ``` func saveRecord(_ record: CKRecord, completionHandler completionHandler: (CKRecord?, NSError?) -> Void) ``` |

Modified [CKDatabase.saveRecordZone(_: CKRecordZone, completionHandler: (CKRecordZone?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449108-saverecordzone)

|  | Declaration |
| --- | --- |
| From | ``` func saveRecordZone(_ zone: CKRecordZone!, completionHandler completionHandler: ((CKRecordZone!, NSError!) -> Void)!) ``` |
| To | ``` func saveRecordZone(_ zone: CKRecordZone, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void) ``` |

Modified [CKDatabase.saveSubscription(_: CKSubscription, completionHandler: (CKSubscription?, NSError?) -> Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449102-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveSubscription(_ subscription: CKSubscription!, completionHandler completionHandler: ((CKSubscription!, NSError!) -> Void)!) ``` |
| To | ``` func saveSubscription(_ subscription: CKSubscription, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void) ``` |

Modified [CKDatabaseOperation](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKDatabaseOperation : CKOperation {     var database: CKDatabase! } ``` |
| To | ``` class CKDatabaseOperation : CKOperation {     var database: CKDatabase? } ``` |

Modified [CKDatabaseOperation.database](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation/1515274-database)

|  | Declaration |
| --- | --- |
| From | ``` var database: CKDatabase! ``` |
| To | ``` var database: CKDatabase? ``` |

Modified [CKDiscoverAllContactsOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKDiscoverAllContactsOperation : CKOperation {     init!()     var discoverAllContactsCompletionBlock: (([AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKDiscoverAllContactsOperation : CKOperation {     init()     var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, NSError?) -> Void)? } ``` |

Modified [CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1515099-discoverallcontactscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` var discoverAllContactsCompletionBlock: (([AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, NSError?) -> Void)? ``` |

Modified [CKDiscoverAllContactsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1514998-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKDiscoveredUserInfo](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo)

|  | Declaration |
| --- | --- |
| From | ``` class CKDiscoveredUserInfo : NSObject {     init!()     @NSCopying var userRecordID: CKRecordID! { get }     var firstName: String! { get }     var lastName: String! { get } } ``` |
| To | ``` class CKDiscoveredUserInfo : NSObject {     init()     @NSCopying var userRecordID: CKRecordID? { get }     var firstName: String? { get }     var lastName: String? { get }     @NSCopying var displayContact: CNContact? { get } } ``` |

Modified [CKDiscoveredUserInfo.firstName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436520-firstname)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var firstName: String! { get } ``` | -- |
| To | ``` var firstName: String? { get } ``` | iOS 9.0 |

Modified [CKDiscoveredUserInfo.lastName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436514-lastname)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var lastName: String! { get } ``` | -- |
| To | ``` var lastName: String? { get } ``` | iOS 9.0 |

Modified [CKDiscoveredUserInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436516-userrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var userRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var userRecordID: CKRecordID? { get } ``` |

Modified [CKDiscoverUserInfosOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKDiscoverUserInfosOperation : CKOperation {     init!()     convenience init!(emailAddresses emailAddresses: [AnyObject]!, userRecordIDs userRecordIDs: [AnyObject]!)     var emailAddresses: [AnyObject]!     var userRecordIDs: [AnyObject]!     var discoverUserInfosCompletionBlock: (([NSObject : AnyObject]!, [NSObject : AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKDiscoverUserInfosOperation : CKOperation {     init()     convenience init(emailAddresses emailAddresses: [String]?, userRecordIDs userRecordIDs: [CKRecordID]?)     var emailAddresses: [String]?     var userRecordIDs: [CKRecordID]?     var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, NSError?) -> Void)? } ``` |

Modified [CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403386-discoveruserinfoscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var discoverUserInfosCompletionBlock: (([NSObject : AnyObject]!, [NSObject : AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, NSError?) -> Void)? ``` |

Modified [CKDiscoverUserInfosOperation.emailAddresses](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403382-emailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` var emailAddresses: [AnyObject]! ``` |
| To | ``` var emailAddresses: [String]? ``` |

Modified [CKDiscoverUserInfosOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403380-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKDiscoverUserInfosOperation.init(emailAddresses: [String]?, userRecordIDs: [CKRecordID]?)](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403391-initwithemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(emailAddresses emailAddresses: [AnyObject]!, userRecordIDs userRecordIDs: [AnyObject]!) ``` |
| To | ``` convenience init(emailAddresses emailAddresses: [String]?, userRecordIDs userRecordIDs: [CKRecordID]?) ``` |

Modified [CKDiscoverUserInfosOperation.userRecordIDs](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403384-userrecordids)

|  | Declaration |
| --- | --- |
| From | ``` var userRecordIDs: [AnyObject]! ``` |
| To | ``` var userRecordIDs: [CKRecordID]? ``` |

Modified [CKErrorCode [enum]](https://developer.apple.com/documentation/cloudkit/ckerrorcode)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum CKErrorCode : Int {     case InternalError     case PartialFailure     case NetworkUnavailable     case NetworkFailure     case BadContainer     case ServiceUnavailable     case RequestRateLimited     case MissingEntitlement     case NotAuthenticated     case PermissionFailure     case UnknownItem     case InvalidArguments     case ResultsTruncated     case ServerRecordChanged     case ServerRejectedRequest     case AssetFileNotFound     case AssetFileModified     case IncompatibleVersion     case ConstraintViolation     case OperationCancelled     case ChangeTokenExpired     case BatchRequestFailed     case ZoneBusy     case BadDatabase     case QuotaExceeded     case ZoneNotFound     case LimitExceeded     case UserDeletedZone } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum CKErrorCode : Int {     case InternalError     case PartialFailure     case NetworkUnavailable     case NetworkFailure     case BadContainer     case ServiceUnavailable     case RequestRateLimited     case MissingEntitlement     case NotAuthenticated     case PermissionFailure     case UnknownItem     case InvalidArguments     case ResultsTruncated     case ServerRecordChanged     case ServerRejectedRequest     case AssetFileNotFound     case AssetFileModified     case IncompatibleVersion     case ConstraintViolation     case OperationCancelled     case ChangeTokenExpired     case BatchRequestFailed     case ZoneBusy     case BadDatabase     case QuotaExceeded     case ZoneNotFound     case LimitExceeded     case UserDeletedZone } extension CKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [CKFetchNotificationChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchNotificationChangesOperation : CKOperation {     init!(previousServerChangeToken previousServerChangeToken: CKServerChangeToken!)     @NSCopying var previousServerChangeToken: CKServerChangeToken!     var resultsLimit: Int     var moreComing: Bool { get }     var notificationChangedBlock: ((CKNotification!) -> Void)!     var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken!, NSError!) -> Void)! } ``` |
| To | ``` class CKFetchNotificationChangesOperation : CKOperation {     init(previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var moreComing: Bool { get }     var notificationChangedBlock: ((CKNotification) -> Void)?     var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, NSError?) -> Void)? } ``` |

Modified [CKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515125-fetchnotificationchangescompleti)

|  | Declaration |
| --- | --- |
| From | ``` var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken!, NSError!) -> Void)! ``` |
| To | ``` var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, NSError?) -> Void)? ``` |

Modified [CKFetchNotificationChangesOperation.init(previousServerChangeToken: CKServerChangeToken?)](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515141-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |
| To | ``` init(previousServerChangeToken previousServerChangeToken: CKServerChangeToken?) ``` |

Modified [CKFetchNotificationChangesOperation.notificationChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515253-notificationchangedblock)

|  | Declaration |
| --- | --- |
| From | ``` var notificationChangedBlock: ((CKNotification!) -> Void)! ``` |
| To | ``` var notificationChangedBlock: ((CKNotification) -> Void)? ``` |

Modified [CKFetchNotificationChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515139-previousserverchangetoken)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken! ``` |
| To | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken? ``` |

Modified [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchRecordChangesOperation : CKDatabaseOperation {     init!(recordZoneID recordZoneID: CKRecordZoneID!, previousServerChangeToken previousServerChangeToken: CKServerChangeToken!)     @NSCopying var recordZoneID: CKRecordZoneID!     @NSCopying var previousServerChangeToken: CKServerChangeToken!     var resultsLimit: Int     var desiredKeys: [AnyObject]!     var recordChangedBlock: ((CKRecord!) -> Void)!     var recordWithIDWasDeletedBlock: ((CKRecordID!) -> Void)!     var moreComing: Bool { get }     var fetchRecordChangesCompletionBlock: ((CKServerChangeToken!, NSData!, NSError!) -> Void)! } ``` |
| To | ``` class CKFetchRecordChangesOperation : CKDatabaseOperation {     init(recordZoneID recordZoneID: CKRecordZoneID, previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var recordZoneID: CKRecordZoneID     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var desiredKeys: [String]?     var recordChangedBlock: ((CKRecord) -> Void)?     var recordWithIDWasDeletedBlock: ((CKRecordID) -> Void)?     var moreComing: Bool { get }     var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, NSData?, NSError?) -> Void)? } ``` |

Modified [CKFetchRecordChangesOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515230-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` var desiredKeys: [AnyObject]! ``` |
| To | ``` var desiredKeys: [String]? ``` |

Modified [CKFetchRecordChangesOperation.fetchRecordChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515267-fetchrecordchangescompletionbloc)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRecordChangesCompletionBlock: ((CKServerChangeToken!, NSData!, NSError!) -> Void)! ``` |
| To | ``` var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, NSData?, NSError?) -> Void)? ``` |

Modified [CKFetchRecordChangesOperation.init(recordZoneID: CKRecordZoneID, previousServerChangeToken: CKServerChangeToken?)](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515224-initwithrecordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordZoneID recordZoneID: CKRecordZoneID!, previousServerChangeToken previousServerChangeToken: CKServerChangeToken!) ``` |
| To | ``` init(recordZoneID recordZoneID: CKRecordZoneID, previousServerChangeToken previousServerChangeToken: CKServerChangeToken?) ``` |

Modified [CKFetchRecordChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515209-previousserverchangetoken)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken! ``` |
| To | ``` @NSCopying var previousServerChangeToken: CKServerChangeToken? ``` |

Modified [CKFetchRecordChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515155-recordchangedblock)

|  | Declaration |
| --- | --- |
| From | ``` var recordChangedBlock: ((CKRecord!) -> Void)! ``` |
| To | ``` var recordChangedBlock: ((CKRecord) -> Void)? ``` |

Modified [CKFetchRecordChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515054-recordwithidwasdeletedblock)

|  | Declaration |
| --- | --- |
| From | ``` var recordWithIDWasDeletedBlock: ((CKRecordID!) -> Void)! ``` |
| To | ``` var recordWithIDWasDeletedBlock: ((CKRecordID) -> Void)? ``` |

Modified [CKFetchRecordChangesOperation.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515018-recordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recordZoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var recordZoneID: CKRecordZoneID ``` |

Modified [CKFetchRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchRecordsOperation : CKDatabaseOperation {     init!()     convenience init!(recordIDs recordIDs: [AnyObject]!)     class func fetchCurrentUserRecordOperation() -> Self!     var recordIDs: [AnyObject]!     var desiredKeys: [AnyObject]!     var perRecordProgressBlock: ((CKRecordID!, Double) -> Void)!     var perRecordCompletionBlock: ((CKRecord!, CKRecordID!, NSError!) -> Void)!     var fetchRecordsCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKFetchRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordIDs recordIDs: [CKRecordID])     class func fetchCurrentUserRecordOperation() -> Self     var recordIDs: [CKRecordID]?     var desiredKeys: [String]?     var perRecordProgressBlock: ((CKRecordID, Double) -> Void)?     var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, NSError?) -> Void)?     var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, NSError?) -> Void)? } ``` |

Modified [CKFetchRecordsOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476088-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` var desiredKeys: [AnyObject]! ``` |
| To | ``` var desiredKeys: [String]? ``` |

Modified [CKFetchRecordsOperation.fetchCurrentUserRecordOperation() -> Self [class]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476070-fetchcurrentuserrecordoperation)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCurrentUserRecordOperation() -> Self! ``` |
| To | ``` class func fetchCurrentUserRecordOperation() -> Self ``` |

Modified [CKFetchRecordsOperation.fetchRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476078-fetchrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRecordsCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, NSError?) -> Void)? ``` |

Modified [CKFetchRecordsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476072-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKFetchRecordsOperation.init(recordIDs: [CKRecordID])](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476074-initwithrecordids)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordIDs recordIDs: [AnyObject]!) ``` |
| To | ``` convenience init(recordIDs recordIDs: [CKRecordID]) ``` |

Modified [CKFetchRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476082-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordCompletionBlock: ((CKRecord!, CKRecordID!, NSError!) -> Void)! ``` |
| To | ``` var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, NSError?) -> Void)? ``` |

Modified [CKFetchRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476080-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordProgressBlock: ((CKRecordID!, Double) -> Void)! ``` |
| To | ``` var perRecordProgressBlock: ((CKRecordID, Double) -> Void)? ``` |

Modified [CKFetchRecordsOperation.recordIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476076-recordids)

|  | Declaration |
| --- | --- |
| From | ``` var recordIDs: [AnyObject]! ``` |
| To | ``` var recordIDs: [CKRecordID]? ``` |

Modified [CKFetchRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchRecordZonesOperation : CKDatabaseOperation {     class func fetchAllRecordZonesOperation() -> Self!     init!()     convenience init!(recordZoneIDs zoneIDs: [AnyObject]!)     var recordZoneIDs: [AnyObject]!     var fetchRecordZonesCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKFetchRecordZonesOperation : CKDatabaseOperation {     class func fetchAllRecordZonesOperation() -> Self     init()     convenience init(recordZoneIDs zoneIDs: [CKRecordZoneID])     var recordZoneIDs: [CKRecordZoneID]?     var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, NSError?) -> Void)? } ``` |

Modified [CKFetchRecordZonesOperation.fetchAllRecordZonesOperation() -> Self [class]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1514890-fetchallrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAllRecordZonesOperation() -> Self! ``` |
| To | ``` class func fetchAllRecordZonesOperation() -> Self ``` |

Modified [CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515145-fetchrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRecordZonesCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, NSError?) -> Void)? ``` |

Modified [CKFetchRecordZonesOperation.init()](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515256-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKFetchRecordZonesOperation.init(recordZoneIDs: [CKRecordZoneID])](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515299-initwithrecordzoneids)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordZoneIDs zoneIDs: [AnyObject]!) ``` |
| To | ``` convenience init(recordZoneIDs zoneIDs: [CKRecordZoneID]) ``` |

Modified [CKFetchRecordZonesOperation.recordZoneIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515084-recordzoneids)

|  | Declaration |
| --- | --- |
| From | ``` var recordZoneIDs: [AnyObject]! ``` |
| To | ``` var recordZoneIDs: [CKRecordZoneID]? ``` |

Modified [CKFetchSubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchSubscriptionsOperation : CKDatabaseOperation {     init!()     class func fetchAllSubscriptionsOperation() -> Self!     convenience init!(subscriptionIDs subscriptionIDs: [AnyObject]!)     var subscriptionIDs: [AnyObject]!     var fetchSubscriptionCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKFetchSubscriptionsOperation : CKDatabaseOperation {     init()     class func fetchAllSubscriptionsOperation() -> Self     convenience init(subscriptionIDs subscriptionIDs: [String])     var subscriptionIDs: [String]?     var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, NSError?) -> Void)? } ``` |

Modified [CKFetchSubscriptionsOperation.fetchAllSubscriptionsOperation() -> Self [class]](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515282-fetchallsubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAllSubscriptionsOperation() -> Self! ``` |
| To | ``` class func fetchAllSubscriptionsOperation() -> Self ``` |

Modified [CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515261-fetchsubscriptioncompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchSubscriptionCompletionBlock: (([NSObject : AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, NSError?) -> Void)? ``` |

Modified [CKFetchSubscriptionsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515123-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKFetchSubscriptionsOperation.init(subscriptionIDs: [String])](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515157-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(subscriptionIDs subscriptionIDs: [AnyObject]!) ``` |
| To | ``` convenience init(subscriptionIDs subscriptionIDs: [String]) ``` |

Modified [CKFetchSubscriptionsOperation.subscriptionIDs](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515011-subscriptionids)

|  | Declaration |
| --- | --- |
| From | ``` var subscriptionIDs: [AnyObject]! ``` |
| To | ``` var subscriptionIDs: [String]? ``` |

Modified [CKLocationSortDescriptor](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class CKLocationSortDescriptor : NSSortDescriptor, NSSecureCoding, NSCoding {     convenience init!()     init!(key key: String!, relativeLocation relativeLocation: CLLocation!)     init!(coder aDecoder: NSCoder!)     @NSCopying var relativeLocation: CLLocation! { get } } ``` |
| To | ``` class CKLocationSortDescriptor : NSSortDescriptor {     convenience init()     init(key key: String, relativeLocation relativeLocation: CLLocation)     init(coder aDecoder: NSCoder)     @NSCopying var relativeLocation: CLLocation { get } } ``` |

Modified [CKLocationSortDescriptor.init(coder: NSCoder)](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515257-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` init!(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified [CKLocationSortDescriptor.init(key: String, relativeLocation: CLLocation)](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515071-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(key key: String!, relativeLocation relativeLocation: CLLocation!) ``` |
| To | ``` init(key key: String, relativeLocation relativeLocation: CLLocation) ``` |

Modified [CKLocationSortDescriptor.relativeLocation](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1514915-relativelocation)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var relativeLocation: CLLocation! { get } ``` |
| To | ``` @NSCopying var relativeLocation: CLLocation { get } ``` |

Modified [CKMarkNotificationsReadOperation](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKMarkNotificationsReadOperation : CKOperation {     convenience init!()     init!(notificationIDsToMarkRead notificationIDs: [AnyObject]!)     var notificationIDs: [AnyObject]!     var markNotificationsReadCompletionBlock: (([AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKMarkNotificationsReadOperation : CKOperation {     convenience init()     init(notificationIDsToMarkRead notificationIDs: [CKNotificationID])     var notificationIDs: [CKNotificationID]     var markNotificationsReadCompletionBlock: (([CKNotificationID]?, NSError?) -> Void)? } ``` |

Modified [CKMarkNotificationsReadOperation.init(notificationIDsToMarkRead: [CKNotificationID])](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515228-initwithnotificationidstomarkrea)

|  | Declaration |
| --- | --- |
| From | ``` init!(notificationIDsToMarkRead notificationIDs: [AnyObject]!) ``` |
| To | ``` init(notificationIDsToMarkRead notificationIDs: [CKNotificationID]) ``` |

Modified [CKMarkNotificationsReadOperation.markNotificationsReadCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515317-marknotificationsreadcompletionb)

|  | Declaration |
| --- | --- |
| From | ``` var markNotificationsReadCompletionBlock: (([AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var markNotificationsReadCompletionBlock: (([CKNotificationID]?, NSError?) -> Void)? ``` |

Modified [CKMarkNotificationsReadOperation.notificationIDs](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515056-notificationids)

|  | Declaration |
| --- | --- |
| From | ``` var notificationIDs: [AnyObject]! ``` |
| To | ``` var notificationIDs: [CKNotificationID] ``` |

Modified [CKModifyBadgeOperation](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyBadgeOperation : CKOperation {     init!()     convenience init!(badgeValue badgeValue: Int)     var badgeValue: Int     var modifyBadgeCompletionBlock: ((NSError!) -> Void)! } ``` |
| To | ``` class CKModifyBadgeOperation : CKOperation {     init()     convenience init(badgeValue badgeValue: Int)     var badgeValue: Int     var modifyBadgeCompletionBlock: ((NSError?) -> Void)? } ``` |

Modified [CKModifyBadgeOperation.init()](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391678-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKModifyBadgeOperation.init(badgeValue: Int)](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391676-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(badgeValue badgeValue: Int) ``` |
| To | ``` convenience init(badgeValue badgeValue: Int) ``` |

Modified [CKModifyBadgeOperation.modifyBadgeCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391682-modifybadgecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyBadgeCompletionBlock: ((NSError!) -> Void)! ``` |
| To | ``` var modifyBadgeCompletionBlock: ((NSError?) -> Void)? ``` |

Modified [CKModifyRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyRecordsOperation : CKDatabaseOperation {     init!()     convenience init!(recordsToSave records: [AnyObject]!, recordIDsToDelete recordIDs: [AnyObject]!)     var recordsToSave: [AnyObject]!     var recordIDsToDelete: [AnyObject]!     var savePolicy: CKRecordSavePolicy     @NSCopying var clientChangeTokenData: NSData!     var atomic: Bool     var perRecordProgressBlock: ((CKRecord!, Double) -> Void)!     var perRecordCompletionBlock: ((CKRecord!, NSError!) -> Void)!     var modifyRecordsCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKModifyRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordsToSave records: [CKRecord]?, recordIDsToDelete recordIDs: [CKRecordID]?)     var recordsToSave: [CKRecord]?     var recordIDsToDelete: [CKRecordID]?     var savePolicy: CKRecordSavePolicy     @NSCopying var clientChangeTokenData: NSData?     var atomic: Bool     var perRecordProgressBlock: ((CKRecord, Double) -> Void)?     var perRecordCompletionBlock: ((CKRecord?, NSError?) -> Void)?     var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, NSError?) -> Void)? } ``` |

Modified [CKModifyRecordsOperation.clientChangeTokenData](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447472-clientchangetokendata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var clientChangeTokenData: NSData! ``` |
| To | ``` @NSCopying var clientChangeTokenData: NSData? ``` |

Modified [CKModifyRecordsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447466-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKModifyRecordsOperation.init(recordsToSave: [CKRecord]?, recordIDsToDelete: [CKRecordID]?)](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447464-initwithrecordstosave)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordsToSave records: [AnyObject]!, recordIDsToDelete recordIDs: [AnyObject]!) ``` |
| To | ``` convenience init(recordsToSave records: [CKRecord]?, recordIDsToDelete recordIDs: [CKRecordID]?) ``` |

Modified [CKModifyRecordsOperation.modifyRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447486-modifyrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyRecordsCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, NSError?) -> Void)? ``` |

Modified [CKModifyRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447470-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordCompletionBlock: ((CKRecord!, NSError!) -> Void)! ``` |
| To | ``` var perRecordCompletionBlock: ((CKRecord?, NSError?) -> Void)? ``` |

Modified [CKModifyRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447477-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordProgressBlock: ((CKRecord!, Double) -> Void)! ``` |
| To | ``` var perRecordProgressBlock: ((CKRecord, Double) -> Void)? ``` |

Modified [CKModifyRecordsOperation.recordIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447479-recordidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` var recordIDsToDelete: [AnyObject]! ``` |
| To | ``` var recordIDsToDelete: [CKRecordID]? ``` |

Modified [CKModifyRecordsOperation.recordsToSave](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447482-recordstosave)

|  | Declaration |
| --- | --- |
| From | ``` var recordsToSave: [AnyObject]! ``` |
| To | ``` var recordsToSave: [CKRecord]? ``` |

Modified [CKModifyRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyRecordZonesOperation : CKDatabaseOperation {     init!()     convenience init!(recordZonesToSave recordZonesToSave: [AnyObject]!, recordZoneIDsToDelete recordZoneIDsToDelete: [AnyObject]!)     var recordZonesToSave: [AnyObject]!     var recordZoneIDsToDelete: [AnyObject]!     var modifyRecordZonesCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKModifyRecordZonesOperation : CKDatabaseOperation {     init()     convenience init(recordZonesToSave recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete recordZoneIDsToDelete: [CKRecordZoneID]?)     var recordZonesToSave: [CKRecordZone]?     var recordZoneIDsToDelete: [CKRecordZoneID]?     var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, NSError?) -> Void)? } ``` |

Modified [CKModifyRecordZonesOperation.init()](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415169-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKModifyRecordZonesOperation.init(recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete: [CKRecordZoneID]?)](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415167-initwithrecordzonestosave)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordZonesToSave recordZonesToSave: [AnyObject]!, recordZoneIDsToDelete recordZoneIDsToDelete: [AnyObject]!) ``` |
| To | ``` convenience init(recordZonesToSave recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete recordZoneIDsToDelete: [CKRecordZoneID]?) ``` |

Modified [CKModifyRecordZonesOperation.modifyRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415164-modifyrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyRecordZonesCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, NSError?) -> Void)? ``` |

Modified [CKModifyRecordZonesOperation.recordZoneIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415173-recordzoneidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` var recordZoneIDsToDelete: [AnyObject]! ``` |
| To | ``` var recordZoneIDsToDelete: [CKRecordZoneID]? ``` |

Modified [CKModifyRecordZonesOperation.recordZonesToSave](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415171-recordzonestosave)

|  | Declaration |
| --- | --- |
| From | ``` var recordZonesToSave: [AnyObject]! ``` |
| To | ``` var recordZonesToSave: [CKRecordZone]? ``` |

Modified [CKModifySubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifySubscriptionsOperation : CKDatabaseOperation {     init!(subscriptionsToSave subscriptionsToSave: [AnyObject]!, subscriptionIDsToDelete subscriptionIDsToDelete: [AnyObject]!)     var subscriptionsToSave: [AnyObject]!     var subscriptionIDsToDelete: [AnyObject]!     var modifySubscriptionsCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! } ``` |
| To | ``` class CKModifySubscriptionsOperation : CKDatabaseOperation {     init(subscriptionsToSave subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete subscriptionIDsToDelete: [String]?)     var subscriptionsToSave: [CKSubscription]?     var subscriptionIDsToDelete: [String]?     var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, NSError?) -> Void)? } ``` |

Modified [CKModifySubscriptionsOperation.init(subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete: [String]?)](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515015-initwithsubscriptionstosave)

|  | Declaration |
| --- | --- |
| From | ``` init!(subscriptionsToSave subscriptionsToSave: [AnyObject]!, subscriptionIDsToDelete subscriptionIDsToDelete: [AnyObject]!) ``` |
| To | ``` init(subscriptionsToSave subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete subscriptionIDsToDelete: [String]?) ``` |

Modified [CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515288-modifysubscriptionscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` var modifySubscriptionsCompletionBlock: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)! ``` |
| To | ``` var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, NSError?) -> Void)? ``` |

Modified [CKModifySubscriptionsOperation.subscriptionIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1514892-subscriptionidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` var subscriptionIDsToDelete: [AnyObject]! ``` |
| To | ``` var subscriptionIDsToDelete: [String]? ``` |

Modified [CKModifySubscriptionsOperation.subscriptionsToSave](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515135-subscriptionstosave)

|  | Declaration |
| --- | --- |
| From | ``` var subscriptionsToSave: [AnyObject]! ``` |
| To | ``` var subscriptionsToSave: [CKSubscription]? ``` |

Modified [CKNotification](https://developer.apple.com/documentation/cloudkit/cknotification)

|  | Declaration |
| --- | --- |
| From | ``` class CKNotification : NSObject {     init!()     convenience init!(fromRemoteNotificationDictionary notificationDictionary: [NSObject : AnyObject]!)     class func notificationFromRemoteNotificationDictionary(_ notificationDictionary: [NSObject : AnyObject]!) -> Self!     var notificationType: CKNotificationType { get }     @NSCopying var notificationID: CKNotificationID! { get }     var containerIdentifier: String! { get }     var isPruned: Bool { get }     var alertBody: String! { get }     var alertLocalizationKey: String! { get }     var alertLocalizationArgs: [AnyObject]! { get }     var alertActionLocalizationKey: String! { get }     var alertLaunchImage: String! { get }     @NSCopying var badge: NSNumber! { get }     var soundName: String! { get } } ``` |
| To | ``` class CKNotification : NSObject {     init()     convenience init(fromRemoteNotificationDictionary notificationDictionary: [String : NSObject])     class func notificationFromRemoteNotificationDictionary(_ notificationDictionary: [String : NSObject]) -> Self     var notificationType: CKNotificationType { get }     @NSCopying var notificationID: CKNotificationID? { get }     var containerIdentifier: String? { get }     var isPruned: Bool { get }     var alertBody: String? { get }     var alertLocalizationKey: String? { get }     var alertLocalizationArgs: [String]? { get }     var alertActionLocalizationKey: String? { get }     var alertLaunchImage: String? { get }     @NSCopying var badge: NSNumber? { get }     var soundName: String? { get }     var subscriptionID: String? { get }     var category: String? { get } } ``` |

Modified [CKNotification.alertActionLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotification/1428109-alertactionlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` var alertActionLocalizationKey: String! { get } ``` |
| To | ``` var alertActionLocalizationKey: String? { get } ``` |

Modified [CKNotification.alertBody](https://developer.apple.com/documentation/cloudkit/cknotification/1428084-alertbody)

|  | Declaration |
| --- | --- |
| From | ``` var alertBody: String! { get } ``` |
| To | ``` var alertBody: String? { get } ``` |

Modified [CKNotification.alertLaunchImage](https://developer.apple.com/documentation/cloudkit/cknotification/1428103-alertlaunchimage)

|  | Declaration |
| --- | --- |
| From | ``` var alertLaunchImage: String! { get } ``` |
| To | ``` var alertLaunchImage: String? { get } ``` |

Modified [CKNotification.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotification/1428105-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` var alertLocalizationArgs: [AnyObject]! { get } ``` |
| To | ``` var alertLocalizationArgs: [String]? { get } ``` |

Modified [CKNotification.alertLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotification/1428095-alertlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` var alertLocalizationKey: String! { get } ``` |
| To | ``` var alertLocalizationKey: String? { get } ``` |

Modified [CKNotification.badge](https://developer.apple.com/documentation/cloudkit/cknotification/1428082-badge)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var badge: NSNumber! { get } ``` |
| To | ``` @NSCopying var badge: NSNumber? { get } ``` |

Modified [CKNotification.containerIdentifier](https://developer.apple.com/documentation/cloudkit/cknotification/1428119-containeridentifier)

|  | Declaration |
| --- | --- |
| From | ``` var containerIdentifier: String! { get } ``` |
| To | ``` var containerIdentifier: String? { get } ``` |

Modified [CKNotification.init(fromRemoteNotificationDictionary: [String : NSObject])](https://developer.apple.com/documentation/cloudkit/cknotification/1428130-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromRemoteNotificationDictionary notificationDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(fromRemoteNotificationDictionary notificationDictionary: [String : NSObject]) ``` |

Modified [CKNotification.notificationID](https://developer.apple.com/documentation/cloudkit/cknotification/1428080-notificationid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var notificationID: CKNotificationID! { get } ``` |
| To | ``` @NSCopying var notificationID: CKNotificationID? { get } ``` |

Modified [CKNotification.soundName](https://developer.apple.com/documentation/cloudkit/cknotification/1428077-soundname)

|  | Declaration |
| --- | --- |
| From | ``` var soundName: String! { get } ``` |
| To | ``` var soundName: String? { get } ``` |

Modified [CKNotificationInfo](https://developer.apple.com/documentation/cloudkit/cknotificationinfo)

|  | Declaration |
| --- | --- |
| From | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCoding, NSCopying {     var alertBody: String!     var alertLocalizationKey: String!     var alertLocalizationArgs: [AnyObject]!     var alertActionLocalizationKey: String!     var alertLaunchImage: String!     var soundName: String!     var desiredKeys: [AnyObject]!     var shouldBadge: Bool     var shouldSendContentAvailable: Bool } ``` |
| To | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCoding, NSCopying {     var alertBody: String?     var alertLocalizationKey: String?     var alertLocalizationArgs: [String]?     var alertActionLocalizationKey: String?     var alertLaunchImage: String?     var soundName: String?     var desiredKeys: [String]?     var shouldBadge: Bool     var shouldSendContentAvailable: Bool     var category: String? } ``` |

Modified [CKNotificationInfo.alertActionLocalizationKey](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo/1514945-alertactionlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` var alertActionLocalizationKey: String! ``` |
| To | ``` var alertActionLocalizationKey: String? ``` |

Modified [CKNotificationInfo.alertBody](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo/1515270-alertbody)

|  | Declaration |
| --- | --- |
| From | ``` var alertBody: String! ``` |
| To | ``` var alertBody: String? ``` |

Modified [CKNotificationInfo.alertLaunchImage](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515075-alertlaunchimage)

|  | Declaration |
| --- | --- |
| From | ``` var alertLaunchImage: String! ``` |
| To | ``` var alertLaunchImage: String? ``` |

Modified [CKNotificationInfo.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515182-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` var alertLocalizationArgs: [AnyObject]! ``` |
| To | ``` var alertLocalizationArgs: [String]? ``` |

Modified [CKNotificationInfo.alertLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514968-alertlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` var alertLocalizationKey: String! ``` |
| To | ``` var alertLocalizationKey: String? ``` |

Modified [CKNotificationInfo.desiredKeys](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514931-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` var desiredKeys: [AnyObject]! ``` |
| To | ``` var desiredKeys: [String]? ``` |

Modified [CKNotificationInfo.soundName](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514987-soundname)

|  | Declaration |
| --- | --- |
| From | ``` var soundName: String! ``` |
| To | ``` var soundName: String? ``` |

Modified [CKNotificationType [enum]](https://developer.apple.com/documentation/cloudkit/cknotificationtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKOperation](https://developer.apple.com/documentation/cloudkit/ckoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKOperation : NSOperation {     init!()     var container: CKContainer!     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool } ``` |
| To | ``` class CKOperation : NSOperation {     init()     func activityStart() -> os_activity_t     var container: CKContainer?     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool } ``` |

Modified [CKOperation.container](https://developer.apple.com/documentation/cloudkit/ckoperation/1452364-container)

|  | Declaration |
| --- | --- |
| From | ``` var container: CKContainer! ``` |
| To | ``` var container: CKContainer? ``` |

Modified [CKOperation.init()](https://developer.apple.com/documentation/cloudkit/ckoperation/1452370-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified CKOperation.usesBackgroundSession

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [CKQuery](https://developer.apple.com/documentation/cloudkit/ckquery)

|  | Declaration |
| --- | --- |
| From | ``` class CKQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init!()     init!(coder aDecoder: NSCoder!)     init!(recordType recordType: String!, predicate predicate: NSPredicate!)     var recordType: String! { get }     @NSCopying var predicate: NSPredicate! { get }     var sortDescriptors: [AnyObject]! } ``` |
| To | ``` class CKQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     init(recordType recordType: String, predicate predicate: NSPredicate)     var recordType: String { get }     @NSCopying var predicate: NSPredicate { get }     var sortDescriptors: [NSSortDescriptor]? } ``` |

Modified [CKQuery.init(coder: NSCoder)](https://developer.apple.com/documentation/cloudkit/ckquery/1413111-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified [CKQuery.init(recordType: String, predicate: NSPredicate)](https://developer.apple.com/documentation/cloudkit/ckquery/1413119-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordType recordType: String!, predicate predicate: NSPredicate!) ``` |
| To | ``` init(recordType recordType: String, predicate predicate: NSPredicate) ``` |

Modified [CKQuery.predicate](https://developer.apple.com/documentation/cloudkit/ckquery/1413112-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var predicate: NSPredicate! { get } ``` |
| To | ``` @NSCopying var predicate: NSPredicate { get } ``` |

Modified [CKQuery.recordType](https://developer.apple.com/documentation/cloudkit/ckquery/1413117-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` var recordType: String! { get } ``` |
| To | ``` var recordType: String { get } ``` |

Modified [CKQuery.sortDescriptors](https://developer.apple.com/documentation/cloudkit/ckquery/1413121-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! ``` |
| To | ``` var sortDescriptors: [NSSortDescriptor]? ``` |

Modified [CKQueryCursor](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor)

|  | Declaration |
| --- | --- |
| From | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!() } ``` |
| To | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding, NSCoding {     init() } ``` |

Modified [CKQueryNotification](https://developer.apple.com/documentation/cloudkit/ckquerynotification)

|  | Declaration |
| --- | --- |
| From | ``` class CKQueryNotification : CKNotification {     var queryNotificationReason: CKQueryNotificationReason { get }     var recordFields: [NSObject : AnyObject]! { get }     @NSCopying var recordID: CKRecordID! { get }     var isPublicDatabase: Bool { get } } ``` |
| To | ``` class CKQueryNotification : CKNotification {     var queryNotificationReason: CKQueryNotificationReason { get }     var recordFields: [String : CKRecordValue]? { get }     @NSCopying var recordID: CKRecordID? { get }     var isPublicDatabase: Bool { get } } ``` |

Modified [CKQueryNotification.recordFields](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428114-recordfields)

|  | Declaration |
| --- | --- |
| From | ``` var recordFields: [NSObject : AnyObject]! { get } ``` |
| To | ``` var recordFields: [String : CKRecordValue]? { get } ``` |

Modified [CKQueryNotification.recordID](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428134-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID? { get } ``` |

Modified [CKQueryNotificationReason [enum]](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKQueryOperation : CKDatabaseOperation {     init!()     convenience init!(query query: CKQuery!)     convenience init!(cursor cursor: CKQueryCursor!)     @NSCopying var query: CKQuery!     @NSCopying var cursor: CKQueryCursor!     @NSCopying var zoneID: CKRecordZoneID!     var resultsLimit: Int     var desiredKeys: [AnyObject]!     var recordFetchedBlock: ((CKRecord!) -> Void)!     var queryCompletionBlock: ((CKQueryCursor!, NSError!) -> Void)! } ``` |
| To | ``` class CKQueryOperation : CKDatabaseOperation {     init()     convenience init(query query: CKQuery)     convenience init(cursor cursor: CKQueryCursor)     @NSCopying var query: CKQuery?     @NSCopying var cursor: CKQueryCursor?     @NSCopying var zoneID: CKRecordZoneID?     var resultsLimit: Int     var desiredKeys: [String]?     var recordFetchedBlock: ((CKRecord) -> Void)?     var queryCompletionBlock: ((CKQueryCursor?, NSError?) -> Void)? } ``` |

Modified [CKQueryOperation.cursor](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1514975-cursor)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var cursor: CKQueryCursor! ``` |
| To | ``` @NSCopying var cursor: CKQueryCursor? ``` |

Modified [CKQueryOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515268-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` var desiredKeys: [AnyObject]! ``` |
| To | ``` var desiredKeys: [String]? ``` |

Modified [CKQueryOperation.init()](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515115-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CKQueryOperation.init(cursor: CKQueryCursor)](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515033-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(cursor cursor: CKQueryCursor!) ``` |
| To | ``` convenience init(cursor cursor: CKQueryCursor) ``` |

Modified [CKQueryOperation.init(query: CKQuery)](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1514958-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(query query: CKQuery!) ``` |
| To | ``` convenience init(query query: CKQuery) ``` |

Modified [CKQueryOperation.query](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515127-query)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var query: CKQuery! ``` |
| To | ``` @NSCopying var query: CKQuery? ``` |

Modified [CKQueryOperation.queryCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515067-querycompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var queryCompletionBlock: ((CKQueryCursor!, NSError!) -> Void)! ``` |
| To | ``` var queryCompletionBlock: ((CKQueryCursor?, NSError?) -> Void)? ``` |

Modified [CKQueryOperation.recordFetchedBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515283-recordfetchedblock)

|  | Declaration |
| --- | --- |
| From | ``` var recordFetchedBlock: ((CKRecord!) -> Void)! ``` |
| To | ``` var recordFetchedBlock: ((CKRecord) -> Void)? ``` |

Modified [CKQueryOperation.zoneID](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515269-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var zoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var zoneID: CKRecordZoneID? ``` |

Modified [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecord : NSObject, NSSecureCoding, NSCoding, NSCopying {     init!()     init!(recordType recordType: String!)     init!(recordType recordType: String!, recordID recordID: CKRecordID!)     init!(recordType recordType: String!, zoneID zoneID: CKRecordZoneID!)     var recordType: String! { get }     @NSCopying var recordID: CKRecordID! { get }     var recordChangeTag: String! { get }     @NSCopying var creatorUserRecordID: CKRecordID! { get }     @NSCopying var creationDate: NSDate! { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID! { get }     @NSCopying var modificationDate: NSDate! { get }     func objectForKey(_ key: String!) -> AnyObject!     func setObject(_ object: CKRecordValue!, forKey key: String!)     func allKeys() -> [AnyObject]!     func allTokens() -> [AnyObject]!     func objectForKeyedSubscript(_ key: String!) -> AnyObject!     func setObject(_ object: CKRecordValue!, forKeyedSubscript key: String!)     func changedKeys() -> [AnyObject]!     func encodeSystemFieldsWithCoder(_ coder: NSCoder!) } ``` |
| To | ``` class CKRecord : NSObject, NSSecureCoding, NSCoding, NSCopying {     init()     init(recordType recordType: String)     init(recordType recordType: String, recordID recordID: CKRecordID)     init(recordType recordType: String, zoneID zoneID: CKRecordZoneID)     var recordType: String { get }     @NSCopying var recordID: CKRecordID { get }     var recordChangeTag: String? { get }     @NSCopying var creatorUserRecordID: CKRecordID? { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID? { get }     @NSCopying var modificationDate: NSDate? { get }     func objectForKey(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKey key: String)     func allKeys() -> [String]     func allTokens() -> [String]     subscript (_ key: String) -> CKRecordValue?     func objectForKeyedSubscript(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKeyedSubscript key: String)     func changedKeys() -> [String]     func encodeSystemFieldsWithCoder(_ coder: NSCoder) } ``` |

Modified [CKRecord.allKeys() -> [String]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462220-allkeys)

|  | Declaration |
| --- | --- |
| From | ``` func allKeys() -> [AnyObject]! ``` |
| To | ``` func allKeys() -> [String] ``` |

Modified [CKRecord.allTokens() -> [String]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462199-alltokens)

|  | Declaration |
| --- | --- |
| From | ``` func allTokens() -> [AnyObject]! ``` |
| To | ``` func allTokens() -> [String] ``` |

Modified [CKRecord.changedKeys() -> [String]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462197-changedkeys)

|  | Declaration |
| --- | --- |
| From | ``` func changedKeys() -> [AnyObject]! ``` |
| To | ``` func changedKeys() -> [String] ``` |

Modified [CKRecord.creationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462223-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var creationDate: NSDate? { get } ``` |

Modified [CKRecord.creatorUserRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462208-creatoruserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creatorUserRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var creatorUserRecordID: CKRecordID? { get } ``` |

Modified [CKRecord.encodeSystemFieldsWithCoder(_: NSCoder)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462200-encodesystemfields)

|  | Declaration |
| --- | --- |
| From | ``` func encodeSystemFieldsWithCoder(_ coder: NSCoder!) ``` |
| To | ``` func encodeSystemFieldsWithCoder(_ coder: NSCoder) ``` |

Modified [CKRecord.init(recordType: String)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462225-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordType recordType: String!) ``` |
| To | ``` init(recordType recordType: String) ``` |

Modified [CKRecord.init(recordType: String, recordID: CKRecordID)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462204-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordType recordType: String!, recordID recordID: CKRecordID!) ``` |
| To | ``` init(recordType recordType: String, recordID recordID: CKRecordID) ``` |

Modified [CKRecord.init(recordType: String, zoneID: CKRecordZoneID)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462202-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordType recordType: String!, zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init(recordType recordType: String, zoneID zoneID: CKRecordZoneID) ``` |

Modified [CKRecord.lastModifiedUserRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462212-lastmodifieduserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastModifiedUserRecordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var lastModifiedUserRecordID: CKRecordID? { get } ``` |

Modified [CKRecord.modificationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462227-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate? { get } ``` |

Modified [CKRecord.objectForKey(_: String) -> CKRecordValue?](https://developer.apple.com/documentation/cloudkit/ckrecord/1462216-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func objectForKey(_ key: String) -> CKRecordValue? ``` |

Modified [CKRecord.recordChangeTag](https://developer.apple.com/documentation/cloudkit/ckrecord/1462195-recordchangetag)

|  | Declaration |
| --- | --- |
| From | ``` var recordChangeTag: String! { get } ``` |
| To | ``` var recordChangeTag: String? { get } ``` |

Modified [CKRecord.recordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462229-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID { get } ``` |

Modified [CKRecord.recordType](https://developer.apple.com/documentation/cloudkit/ckrecord/1462206-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` var recordType: String! { get } ``` |
| To | ``` var recordType: String { get } ``` |

Modified [CKRecord.setObject(_: CKRecordValue?, forKey: String)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462231-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: CKRecordValue!, forKey key: String!) ``` |
| To | ``` func setObject(_ object: CKRecordValue?, forKey key: String) ``` |

Modified [CKRecord.subscript(_: String) -> CKRecordValue?](https://developer.apple.com/documentation/cloudkit/ckrecord/1462210-objectforkeyedsubscript)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | objectForKeyedSubscript(_:) | ``` func objectForKeyedSubscript(_ key: String!) -> AnyObject! ``` | iOS 8.0 |
| To | subscript(_:) | ``` subscript (_ key: String) -> CKRecordValue? ``` | iOS 9.0 |

Modified [CKRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/id)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecordID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init!()     convenience init!(recordName recordName: String!)     init!(recordName recordName: String!, zoneID zoneID: CKRecordZoneID!)     var recordName: String! { get }     var zoneID: CKRecordZoneID! { get } } ``` |
| To | ``` class CKRecordID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     convenience init(recordName recordName: String)     init(recordName recordName: String, zoneID zoneID: CKRecordZoneID)     var recordName: String { get }     var zoneID: CKRecordZoneID { get } } ``` |

Modified [CKRecordID.init(recordName: String)](https://developer.apple.com/documentation/cloudkit/ckrecordid/1500975-initwithrecordname)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordName recordName: String!) ``` |
| To | ``` convenience init(recordName recordName: String) ``` |

Modified [CKRecordID.init(recordName: String, zoneID: CKRecordZoneID)](https://developer.apple.com/documentation/cloudkit/ckrecordid/1500967-initwithrecordname)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordName recordName: String!, zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init(recordName recordName: String, zoneID zoneID: CKRecordZoneID) ``` |

Modified [CKRecordID.recordName](https://developer.apple.com/documentation/cloudkit/ckrecordid/1500973-recordname)

|  | Declaration |
| --- | --- |
| From | ``` var recordName: String! { get } ``` |
| To | ``` var recordName: String { get } ``` |

Modified [CKRecordID.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecordid/1500969-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` var zoneID: CKRecordZoneID! { get } ``` |
| To | ``` var zoneID: CKRecordZoneID { get } ``` |

Modified [CKRecordSavePolicy [enum]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKRecordZone](https://developer.apple.com/documentation/cloudkit/ckrecordzone)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCoding, NSCopying {     class func defaultRecordZone() -> CKRecordZone!     init!()     init!(zoneName zoneName: String!)     init!(zoneID zoneID: CKRecordZoneID!)     var zoneID: CKRecordZoneID! { get }     var capabilities: CKRecordZoneCapabilities { get } } ``` |
| To | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCoding, NSCopying {     class func defaultRecordZone() -> CKRecordZone     init()     init(zoneName zoneName: String)     init(zoneID zoneID: CKRecordZoneID)     var zoneID: CKRecordZoneID { get }     var capabilities: CKRecordZoneCapabilities { get } } ``` |

Modified [CKRecordZone.defaultRecordZone() -> CKRecordZone [class]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1514919-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultRecordZone() -> CKRecordZone! ``` |
| To | ``` class func defaultRecordZone() -> CKRecordZone ``` |

Modified [CKRecordZone.init(zoneID: CKRecordZoneID)](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1515207-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(zoneID zoneID: CKRecordZoneID!) ``` |
| To | ``` init(zoneID zoneID: CKRecordZoneID) ``` |

Modified [CKRecordZone.init(zoneName: String)](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1515102-initwithzonename)

|  | Declaration |
| --- | --- |
| From | ``` init!(zoneName zoneName: String!) ``` |
| To | ``` init(zoneName zoneName: String) ``` |

Modified [CKRecordZone.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1514917-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` var zoneID: CKRecordZoneID! { get } ``` |
| To | ``` var zoneID: CKRecordZoneID { get } ``` |

Modified [CKRecordZoneCapabilities [struct]](https://developer.apple.com/documentation/cloudkit/ckrecordzonecapabilities)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKRecordZoneCapabilities : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FetchChanges: CKRecordZoneCapabilities { get }     static var Atomic: CKRecordZoneCapabilities { get } } ``` | RawOptionSetType |
| To | ``` struct CKRecordZoneCapabilities : OptionSetType {     init(rawValue rawValue: UInt)     static var FetchChanges: CKRecordZoneCapabilities { get }     static var Atomic: CKRecordZoneCapabilities { get } } ``` | OptionSetType |

Modified [CKRecordZoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init!()     init!(zoneName zoneName: String!, ownerName ownerName: String!)     var zoneName: String! { get }     var ownerName: String! { get } } ``` |
| To | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(zoneName zoneName: String, ownerName ownerName: String)     var zoneName: String { get }     var ownerName: String { get } } ``` |

Modified [CKRecordZoneID.init(zoneName: String, ownerName: String)](https://developer.apple.com/documentation/cloudkit/ckrecordzoneid/1508089-initwithzonename)

|  | Declaration |
| --- | --- |
| From | ``` init!(zoneName zoneName: String!, ownerName ownerName: String!) ``` |
| To | ``` init(zoneName zoneName: String, ownerName ownerName: String) ``` |

Modified [CKRecordZoneID.ownerName](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508096-ownername)

|  | Declaration |
| --- | --- |
| From | ``` var ownerName: String! { get } ``` |
| To | ``` var ownerName: String { get } ``` |

Modified [CKRecordZoneID.zoneName](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508094-zonename)

|  | Declaration |
| --- | --- |
| From | ``` var zoneName: String! { get } ``` |
| To | ``` var zoneName: String { get } ``` |

Modified [CKRecordZoneNotification](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecordZoneNotification : CKNotification {     @NSCopying var recordZoneID: CKRecordZoneID! { get } } ``` |
| To | ``` class CKRecordZoneNotification : CKNotification {     @NSCopying var recordZoneID: CKRecordZoneID? { get } } ``` |

Modified [CKRecordZoneNotification.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification/1428086-recordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recordZoneID: CKRecordZoneID! { get } ``` |
| To | ``` @NSCopying var recordZoneID: CKRecordZoneID? { get } ``` |

Modified [CKReference](https://developer.apple.com/documentation/cloudkit/ckreference)

|  | Declaration |
| --- | --- |
| From | ``` class CKReference : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init!()     init!(recordID recordID: CKRecordID!, action action: CKReferenceAction)     convenience init!(record record: CKRecord!, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID! { get } } extension CKReference : CKRecordValue, NSObjectProtocol { } ``` |
| To | ``` class CKReference : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(recordID recordID: CKRecordID, action action: CKReferenceAction)     convenience init(record record: CKRecord, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID { get } } extension CKReference : CKRecordValue { } ``` |

Modified [CKReference.init(record: CKRecord, action: CKReferenceAction)](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1515312-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(record record: CKRecord!, action action: CKReferenceAction) ``` |
| To | ``` convenience init(record record: CKRecord, action action: CKReferenceAction) ``` |

Modified [CKReference.init(recordID: CKRecordID, action: CKReferenceAction)](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1515280-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordID recordID: CKRecordID!, action action: CKReferenceAction) ``` |
| To | ``` init(recordID recordID: CKRecordID, action action: CKReferenceAction) ``` |

Modified [CKReference.recordID](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1514956-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recordID: CKRecordID! { get } ``` |
| To | ``` @NSCopying var recordID: CKRecordID { get } ``` |

Modified [CKReferenceAction [enum]](https://developer.apple.com/documentation/cloudkit/ckrecord_reference_action)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [CKServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckserverchangetoken)

|  | Declaration |
| --- | --- |
| From | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!() } ``` |
| To | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding, NSCoding {     init() } ``` |

Modified [CKSubscription](https://developer.apple.com/documentation/cloudkit/cksubscription)

|  | Declaration |
| --- | --- |
| From | ``` class CKSubscription : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init!()     init!(coder aDecoder: NSCoder!)     convenience init!(recordType recordType: String!, predicate predicate: NSPredicate!, options subscriptionOptions: CKSubscriptionOptions)     init!(recordType recordType: String!, predicate predicate: NSPredicate!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions)     convenience init!(zoneID zoneID: CKRecordZoneID!, options subscriptionOptions: CKSubscriptionOptions)     init!(zoneID zoneID: CKRecordZoneID!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions)     var subscriptionID: String! { get }     var subscriptionType: CKSubscriptionType { get }     var recordType: String! { get }     @NSCopying var predicate: NSPredicate! { get }     var subscriptionOptions: CKSubscriptionOptions { get }     @NSCopying var notificationInfo: CKNotificationInfo!     @NSCopying var zoneID: CKRecordZoneID! } ``` |
| To | ``` class CKSubscription : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions)     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions)     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     var subscriptionID: String { get }     var subscriptionType: CKSubscriptionType { get }     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     @NSCopying var notificationInfo: CKNotificationInfo?     @NSCopying var zoneID: CKRecordZoneID? } ``` |

Modified [CKSubscription.init(coder: NSCoder)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515004-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` init!(coder aDecoder: NSCoder!) ``` |
| To | ``` init(coder aDecoder: NSCoder) ``` |

Modified [CKSubscription.init(recordType: String, predicate: NSPredicate, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515132-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(recordType recordType: String!, predicate predicate: NSPredicate!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified [CKSubscription.init(recordType: String, predicate: NSPredicate, subscriptionID: String, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515265-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(recordType recordType: String!, predicate predicate: NSPredicate!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified [CKSubscription.init(zoneID: CKRecordZoneID, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1514971-initwithzoneid)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(zoneID zoneID: CKRecordZoneID!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified [CKSubscription.init(zoneID: CKRecordZoneID, subscriptionID: String, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515215-initwithzoneid)

|  | Declaration |
| --- | --- |
| From | ``` init!(zoneID zoneID: CKRecordZoneID!, subscriptionID subscriptionID: String!, options subscriptionOptions: CKSubscriptionOptions) ``` |
| To | ``` init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions) ``` |

Modified [CKSubscription.notificationInfo](https://developer.apple.com/documentation/cloudkit/cksubscription/1514948-notificationinfo)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var notificationInfo: CKNotificationInfo! ``` |
| To | ``` @NSCopying var notificationInfo: CKNotificationInfo? ``` |

Modified [CKSubscription.predicate](https://developer.apple.com/documentation/cloudkit/cksubscription/1515219-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var predicate: NSPredicate! { get } ``` |
| To | ``` @NSCopying var predicate: NSPredicate? { get } ``` |

Modified [CKSubscription.recordType](https://developer.apple.com/documentation/cloudkit/cksubscription/1515080-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` var recordType: String! { get } ``` |
| To | ``` var recordType: String? { get } ``` |

Modified [CKSubscription.subscriptionID](https://developer.apple.com/documentation/cloudkit/cksubscription/1515199-subscriptionid)

|  | Declaration |
| --- | --- |
| From | ``` var subscriptionID: String! { get } ``` |
| To | ``` var subscriptionID: String { get } ``` |

Modified [CKSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/cksubscription/1514936-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var zoneID: CKRecordZoneID! ``` |
| To | ``` @NSCopying var zoneID: CKRecordZoneID? ``` |

Modified [CKSubscriptionOptions [struct]](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKSubscriptionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var FiresOnRecordCreation: CKSubscriptionOptions { get }     static var FiresOnRecordUpdate: CKSubscriptionOptions { get }     static var FiresOnRecordDeletion: CKSubscriptionOptions { get }     static var FiresOnce: CKSubscriptionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CKSubscriptionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var FiresOnRecordCreation: CKSubscriptionOptions { get }     static var FiresOnRecordUpdate: CKSubscriptionOptions { get }     static var FiresOnRecordDeletion: CKSubscriptionOptions { get }     static var FiresOnce: CKSubscriptionOptions { get } } ``` | OptionSetType |

Modified [CKSubscriptionType [enum]](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CKApplicationPermissionBlock](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias CKApplicationPermissionBlock = (CKApplicationPermissionStatus, NSError!) -> Void ``` |
| To | ``` typealias CKApplicationPermissionBlock = (CKApplicationPermissionStatus, NSError?) -> Void ``` |

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
