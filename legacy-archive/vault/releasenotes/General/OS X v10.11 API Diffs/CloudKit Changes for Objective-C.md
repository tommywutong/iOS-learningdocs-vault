---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CloudKit.html
archived_at: '2026-07-18T02:52:56.747756Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CloudKit Changes for Objective-C

### CloudKit

#### CKAsset.h

Modified [CKAsset.fileURL](https://developer.apple.com/documentation/cloudkit/ckasset/1515050-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURL *fileURL ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSURL *fileURL ``` |

Modified [-[CKAsset initWithFileURL:]](https://developer.apple.com/documentation/cloudkit/ckasset/1514990-initwithfileurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFileURL:(NSURL *)fileURL ``` |
| To | ``` - (instancetype _Nonnull)initWithFileURL:(NSURL * _Nonnull)fileURL ``` |

#### CKContainer.h

Added [CKAccountChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged)Modified [-[CKContainer accountStatusWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399180-accountstatuswithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` - (void)accountStatusWithCompletionHandler:(void (^)(CKAccountStatus accountStatus, NSError *error))completionHandler ``` |
| To | ``` - (void)accountStatusWithCompletionHandler:(void (^ _Nonnull)(CKAccountStatus accountStatus, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKContainer addOperation:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399215-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOperation:(CKOperation *)operation ``` |
| To | ``` - (void)addOperation:(CKOperation * _Nonnull)operation ``` |

Modified [CKContainer.containerIdentifier](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399182-containeridentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *containerIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *containerIdentifier ``` |

Modified [+[CKContainer containerWithIdentifier:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399193-containerwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (CKContainer *)containerWithIdentifier:(NSString *)containerIdentifier ``` |
| To | ``` + (CKContainer * _Nonnull)containerWithIdentifier:(NSString * _Nonnull)containerIdentifier ``` |

Modified [+[CKContainer defaultContainer]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399189-defaultcontainer)

|  | Declaration |
| --- | --- |
| From | ``` + (CKContainer *)defaultContainer ``` |
| To | ``` + (CKContainer * _Nonnull)defaultContainer ``` |

Modified [-[CKContainer discoverAllContactUserInfosWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399199-discoverallcontactuserinfoswithc)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverAllContactUserInfosWithCompletionHandler:(void (^)(NSArray *userInfos, NSError *error))completionHandler ``` |
| To | ``` - (void)discoverAllContactUserInfosWithCompletionHandler:(void (^ _Nonnull)(NSArray<CKDiscoveredUserInfo *> * _Nullable userInfos, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKContainer discoverUserInfoWithEmailAddress:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399201-discoveruserinfowithemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverUserInfoWithEmailAddress:(NSString *)email completionHandler:(void (^)(CKDiscoveredUserInfo *userInfo, NSError *error))completionHandler ``` |
| To | ``` - (void)discoverUserInfoWithEmailAddress:(NSString * _Nonnull)email completionHandler:(void (^ _Nonnull)(CKDiscoveredUserInfo * _Nullable userInfo, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKContainer discoverUserInfoWithUserRecordID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399217-discoveruserinfowithuserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverUserInfoWithUserRecordID:(CKRecordID *)userRecordID completionHandler:(void (^)(CKDiscoveredUserInfo *userInfo, NSError *error))completionHandler ``` |
| To | ``` - (void)discoverUserInfoWithUserRecordID:(CKRecordID * _Nonnull)userRecordID completionHandler:(void (^ _Nonnull)(CKDiscoveredUserInfo * _Nullable userInfo, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKContainer fetchUserRecordIDWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399191-fetchuserrecordidwithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchUserRecordIDWithCompletionHandler:(void (^)(CKRecordID *recordID, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchUserRecordIDWithCompletionHandler:(void (^ _Nonnull)(CKRecordID * _Nullable recordID, NSError * _Nullable error))completionHandler ``` |

Modified [CKContainer.privateCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399205-privateclouddatabase)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CKDatabase *privateCloudDatabase ``` |
| To | ``` @property(nonatomic, readonly, nonnull) CKDatabase *privateCloudDatabase ``` |

Modified [CKContainer.publicCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399166-publicclouddatabase)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CKDatabase *publicCloudDatabase ``` |
| To | ``` @property(nonatomic, readonly, nonnull) CKDatabase *publicCloudDatabase ``` |

Modified [-[CKContainer requestApplicationPermission:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399174-requestapplicationpermission)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestApplicationPermission:(CKApplicationPermissions)applicationPermission completionHandler:(CKApplicationPermissionBlock)completionHandler ``` |
| To | ``` - (void)requestApplicationPermission:(CKApplicationPermissions)applicationPermission completionHandler:(CKApplicationPermissionBlock _Nonnull)completionHandler ``` |

Modified [-[CKContainer statusForApplicationPermission:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399195-status)

|  | Declaration |
| --- | --- |
| From | ``` - (void)statusForApplicationPermission:(CKApplicationPermissions)applicationPermission completionHandler:(CKApplicationPermissionBlock)completionHandler ``` |
| To | ``` - (void)statusForApplicationPermission:(CKApplicationPermissions)applicationPermission completionHandler:(CKApplicationPermissionBlock _Nonnull)completionHandler ``` |

#### CKDatabase.h

Modified [-[CKDatabase addOperation:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449116-addoperation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOperation:(CKDatabaseOperation *)operation ``` |
| To | ``` - (void)addOperation:(CKDatabaseOperation * _Nonnull)operation ``` |

Modified [-[CKDatabase deleteRecordWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449122-deleterecordwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteRecordWithID:(CKRecordID *)recordID completionHandler:(void (^)(CKRecordID *recordID, NSError *error))completionHandler ``` |
| To | ``` - (void)deleteRecordWithID:(CKRecordID * _Nonnull)recordID completionHandler:(void (^ _Nonnull)(CKRecordID * _Nullable recordID, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase deleteRecordZoneWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449118-deleterecordzonewithid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteRecordZoneWithID:(CKRecordZoneID *)zoneID completionHandler:(void (^)(CKRecordZoneID *zoneID, NSError *error))completionHandler ``` |
| To | ``` - (void)deleteRecordZoneWithID:(CKRecordZoneID * _Nonnull)zoneID completionHandler:(void (^ _Nonnull)(CKRecordZoneID * _Nullable zoneID, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase deleteSubscriptionWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449120-deletesubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteSubscriptionWithID:(NSString *)subscriptionID completionHandler:(void (^)(NSString *subscriptionID, NSError *error))completionHandler ``` |
| To | ``` - (void)deleteSubscriptionWithID:(NSString * _Nonnull)subscriptionID completionHandler:(void (^ _Nonnull)(NSString * _Nullable subscriptionID, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase fetchAllRecordZonesWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449112-fetchallrecordzones)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchAllRecordZonesWithCompletionHandler:(void (^)(NSArray *zones, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchAllRecordZonesWithCompletionHandler:(void (^ _Nonnull)(NSArray<CKRecordZone *> * _Nullable zones, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase fetchAllSubscriptionsWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449110-fetchallsubscriptionswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchAllSubscriptionsWithCompletionHandler:(void (^)(NSArray *subscriptions, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchAllSubscriptionsWithCompletionHandler:(void (^ _Nonnull)(NSArray<CKSubscription *> * _Nullable subscriptions, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase fetchRecordWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449126-fetch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchRecordWithID:(CKRecordID *)recordID completionHandler:(void (^)(CKRecord *record, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchRecordWithID:(CKRecordID * _Nonnull)recordID completionHandler:(void (^ _Nonnull)(CKRecord * _Nullable record, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase fetchRecordZoneWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449104-fetch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchRecordZoneWithID:(CKRecordZoneID *)zoneID completionHandler:(void (^)(CKRecordZone *zone, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchRecordZoneWithID:(CKRecordZoneID * _Nonnull)zoneID completionHandler:(void (^ _Nonnull)(CKRecordZone * _Nullable zone, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase fetchSubscriptionWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449106-fetchsubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchSubscriptionWithID:(NSString *)subscriptionID completionHandler:(void (^)(CKSubscription *subscription, NSError *error))completionHandler ``` |
| To | ``` - (void)fetchSubscriptionWithID:(NSString * _Nonnull)subscriptionID completionHandler:(void (^ _Nonnull)(CKSubscription * _Nullable subscription, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase performQuery:inZoneWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449127-performquery)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performQuery:(CKQuery *)query inZoneWithID:(CKRecordZoneID *)zoneID completionHandler:(void (^)(NSArray *results, NSError *error))completionHandler ``` |
| To | ``` - (void)performQuery:(CKQuery * _Nonnull)query inZoneWithID:(CKRecordZoneID * _Nullable)zoneID completionHandler:(void (^ _Nonnull)(NSArray<CKRecord *> * _Nullable results, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase saveRecord:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449114-save)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveRecord:(CKRecord *)record completionHandler:(void (^)(CKRecord *record, NSError *error))completionHandler ``` |
| To | ``` - (void)saveRecord:(CKRecord * _Nonnull)record completionHandler:(void (^ _Nonnull)(CKRecord * _Nullable record, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase saveRecordZone:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449108-saverecordzone)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveRecordZone:(CKRecordZone *)zone completionHandler:(void (^)(CKRecordZone *zone, NSError *error))completionHandler ``` |
| To | ``` - (void)saveRecordZone:(CKRecordZone * _Nonnull)zone completionHandler:(void (^ _Nonnull)(CKRecordZone * _Nullable zone, NSError * _Nullable error))completionHandler ``` |

Modified [-[CKDatabase saveSubscription:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449102-savesubscription)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveSubscription:(CKSubscription *)subscription completionHandler:(void (^)(CKSubscription *subscription, NSError *error))completionHandler ``` |
| To | ``` - (void)saveSubscription:(CKSubscription * _Nonnull)subscription completionHandler:(void (^ _Nonnull)(CKSubscription * _Nullable subscription, NSError * _Nullable error))completionHandler ``` |

#### CKDatabaseOperation.h

Modified [CKDatabaseOperation.database](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation/1515274-database)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) CKDatabase *database ``` |
| To | ``` @property(nonatomic, strong, nullable) CKDatabase *database ``` |

#### CKDiscoverAllContactsOperation.h

Modified [CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1515099-discoverallcontactscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^discoverAllContactsCompletionBlock)(NSArray *userInfos, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^discoverAllContactsCompletionBlock)(NSArray<CKDiscoveredUserInfo *> * _Nullable userInfos, NSError * _Nullable operationError) ``` |

Modified [-[CKDiscoverAllContactsOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1514998-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

#### CKDiscoveredUserInfo.h

Added [CKDiscoveredUserInfo.displayContact](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436518-displaycontact)Modified [CKDiscoveredUserInfo.firstName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436520-firstname)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *firstName ``` | -- |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *firstName ``` | OS X 10.11 |

Modified [CKDiscoveredUserInfo.lastName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436514-lastname)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *lastName ``` | -- |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *lastName ``` | OS X 10.11 |

Modified [CKDiscoveredUserInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436516-userrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *userRecordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKRecordID *userRecordID ``` |

#### CKDiscoverUserInfosOperation.h

Modified [CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403386-discoveruserinfoscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^discoverUserInfosCompletionBlock)(NSDictionary *emailsToUserInfos, NSDictionary *userRecordIDsToUserInfos, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^discoverUserInfosCompletionBlock)(NSDictionary<NSString *,CKDiscoveredUserInfo *> * _Nullable emailsToUserInfos, NSDictionary<CKRecordID *,CKDiscoveredUserInfo *> * _Nullable userRecordIDsToUserInfos, NSError * _Nullable operationError) ``` |

Modified [CKDiscoverUserInfosOperation.emailAddresses](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403382-emailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *emailAddresses ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *emailAddresses ``` |

Modified [-[CKDiscoverUserInfosOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403380-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKDiscoverUserInfosOperation initWithEmailAddresses:userRecordIDs:]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403391-initwithemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEmailAddresses:(NSArray *)emailAddresses userRecordIDs:(NSArray *)userRecordIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithEmailAddresses:(NSArray<NSString *> * _Nullable)emailAddresses userRecordIDs:(NSArray<CKRecordID *> * _Nullable)userRecordIDs ``` |

Modified [CKDiscoverUserInfosOperation.userRecordIDs](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403384-userrecordids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *userRecordIDs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordID *> *userRecordIDs ``` |

#### CKFetchNotificationChangesOperation.h

Modified [CKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515125-fetchnotificationchangescompleti)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchNotificationChangesCompletionBlock)(CKServerChangeToken *serverChangeToken, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchNotificationChangesCompletionBlock)(CKServerChangeToken * _Nullable serverChangeToken, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchNotificationChangesOperation initWithPreviousServerChangeToken:]](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515141-initwithpreviousserverchangetoke)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPreviousServerChangeToken:(CKServerChangeToken *)previousServerChangeToken ``` |
| To | ``` - (instancetype _Nonnull)initWithPreviousServerChangeToken:(CKServerChangeToken * _Nullable)previousServerChangeToken ``` |

Modified [CKFetchNotificationChangesOperation.notificationChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515253-notificationchangedblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^notificationChangedBlock)(CKNotification *notification) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^notificationChangedBlock)(CKNotification * _Nonnull notification) ``` |

Modified [CKFetchNotificationChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515139-previousserverchangetoken)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKServerChangeToken *previousServerChangeToken ``` |
| To | ``` @property(nonatomic, copy, nullable) CKServerChangeToken *previousServerChangeToken ``` |

#### CKFetchRecordChangesOperation.h

Modified [CKFetchRecordChangesOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515230-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

Modified [CKFetchRecordChangesOperation.fetchRecordChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515267-fetchrecordchangescompletionbloc)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchRecordChangesCompletionBlock)(CKServerChangeToken *serverChangeToken, NSData *clientChangeTokenData, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchRecordChangesCompletionBlock)(CKServerChangeToken * _Nullable serverChangeToken, NSData * _Nullable clientChangeTokenData, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchRecordChangesOperation initWithRecordZoneID:previousServerChangeToken:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515224-initwithrecordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordZoneID:(CKRecordZoneID *)recordZoneID previousServerChangeToken:(CKServerChangeToken *)previousServerChangeToken ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordZoneID:(CKRecordZoneID * _Nonnull)recordZoneID previousServerChangeToken:(CKServerChangeToken * _Nullable)previousServerChangeToken ``` |

Modified [CKFetchRecordChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515209-previousserverchangetoken)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKServerChangeToken *previousServerChangeToken ``` |
| To | ``` @property(nonatomic, copy, nullable) CKServerChangeToken *previousServerChangeToken ``` |

Modified [CKFetchRecordChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515155-recordchangedblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^recordChangedBlock)(CKRecord *record) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^recordChangedBlock)(CKRecord * _Nonnull record) ``` |

Modified [CKFetchRecordChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515054-recordwithidwasdeletedblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^recordWithIDWasDeletedBlock)(CKRecordID *recordID) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^recordWithIDWasDeletedBlock)(CKRecordID * _Nonnull recordID) ``` |

Modified [CKFetchRecordChangesOperation.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515018-recordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKRecordZoneID *recordZoneID ``` |
| To | ``` @property(nonatomic, copy, nonnull) CKRecordZoneID *recordZoneID ``` |

#### CKFetchRecordsOperation.h

Modified [CKFetchRecordsOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476088-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

Modified [+[CKFetchRecordsOperation fetchCurrentUserRecordOperation]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476070-fetchcurrentuserrecordoperation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)fetchCurrentUserRecordOperation ``` |
| To | ``` + (instancetype _Nonnull)fetchCurrentUserRecordOperation ``` |

Modified [CKFetchRecordsOperation.fetchRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476078-fetchrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchRecordsCompletionBlock)(NSDictionary *recordsByRecordID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchRecordsCompletionBlock)(NSDictionary<CKRecordID *,CKRecord *> * _Nullable recordsByRecordID, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchRecordsOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476072-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKFetchRecordsOperation initWithRecordIDs:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476074-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordIDs:(NSArray *)recordIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordIDs:(NSArray<CKRecordID *> * _Nonnull)recordIDs ``` |

Modified [CKFetchRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476082-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^perRecordCompletionBlock)(CKRecord *record, CKRecordID *recordID, NSError *error) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^perRecordCompletionBlock)(CKRecord * _Nullable record, CKRecordID * _Nullable recordID, NSError * _Nullable error) ``` |

Modified [CKFetchRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476080-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^perRecordProgressBlock)(CKRecordID *recordID, double progress) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^perRecordProgressBlock)(CKRecordID * _Nonnull recordID, double progress) ``` |

Modified [CKFetchRecordsOperation.recordIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476076-recordids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordIDs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordID *> *recordIDs ``` |

#### CKFetchRecordZonesOperation.h

Modified [+[CKFetchRecordZonesOperation fetchAllRecordZonesOperation]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1514890-fetchallrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)fetchAllRecordZonesOperation ``` |
| To | ``` + (instancetype _Nonnull)fetchAllRecordZonesOperation ``` |

Modified [CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515145-fetchrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchRecordZonesCompletionBlock)(NSDictionary *recordZonesByZoneID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchRecordZonesCompletionBlock)(NSDictionary<CKRecordZoneID *,CKRecordZone *> * _Nullable recordZonesByZoneID, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchRecordZonesOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515256-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKFetchRecordZonesOperation initWithRecordZoneIDs:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515299-initwithrecordzoneids)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordZoneIDs:(NSArray *)zoneIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordZoneIDs:(NSArray<CKRecordZoneID *> * _Nonnull)zoneIDs ``` |

Modified [CKFetchRecordZonesOperation.recordZoneIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515084-recordzoneids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordZoneIDs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordZoneID *> *recordZoneIDs ``` |

#### CKFetchSubscriptionsOperation.h

Modified [+[CKFetchSubscriptionsOperation fetchAllSubscriptionsOperation]](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515282-fetchallsubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)fetchAllSubscriptionsOperation ``` |
| To | ``` + (instancetype _Nonnull)fetchAllSubscriptionsOperation ``` |

Modified [CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515261-fetchsubscriptioncompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchSubscriptionCompletionBlock)(NSDictionary *subscriptionsBySubscriptionID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchSubscriptionCompletionBlock)(NSDictionary<NSString *,CKSubscription *> * _Nullable subscriptionsBySubscriptionID, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchSubscriptionsOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515123-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKFetchSubscriptionsOperation initWithSubscriptionIDs:]](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515157-initwithsubscriptionids)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSubscriptionIDs:(NSArray *)subscriptionIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithSubscriptionIDs:(NSArray<NSString *> * _Nonnull)subscriptionIDs ``` |

Modified [CKFetchSubscriptionsOperation.subscriptionIDs](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515011-subscriptionids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *subscriptionIDs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *subscriptionIDs ``` |

#### CKLocationSortDescriptor.h

Modified [-[CKLocationSortDescriptor initWithCoder:]](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515257-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nonnull)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[CKLocationSortDescriptor initWithKey:relativeLocation:]](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1515071-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKey:(NSString *)key relativeLocation:(CLLocation *)relativeLocation ``` |
| To | ``` - (instancetype _Nonnull)initWithKey:(NSString * _Nonnull)key relativeLocation:(CLLocation * _Nonnull)relativeLocation ``` |

Modified [CKLocationSortDescriptor.relativeLocation](https://developer.apple.com/documentation/cloudkit/cklocationsortdescriptor/1514915-relativelocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CLLocation *relativeLocation ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) CLLocation *relativeLocation ``` |

#### CKMarkNotificationsReadOperation.h

Modified [-[CKMarkNotificationsReadOperation initWithNotificationIDsToMarkRead:]](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515228-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithNotificationIDsToMarkRead:(NSArray *)notificationIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithNotificationIDsToMarkRead:(NSArray<CKNotificationID *> * _Nonnull)notificationIDs ``` |

Modified [CKMarkNotificationsReadOperation.markNotificationsReadCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515317-marknotificationsreadcompletionb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^markNotificationsReadCompletionBlock)(NSArray *notificationIDsMarkedRead, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^markNotificationsReadCompletionBlock)(NSArray<CKNotificationID *> * _Nullable notificationIDsMarkedRead, NSError * _Nullable operationError) ``` |

Modified [CKMarkNotificationsReadOperation.notificationIDs](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515056-notificationids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *notificationIDs ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<CKNotificationID *> *notificationIDs ``` |

#### CKModifyBadgeOperation.h

Modified [-[CKModifyBadgeOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391678-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKModifyBadgeOperation initWithBadgeValue:]](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391676-initwithbadgevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithBadgeValue:(NSUInteger)badgeValue ``` |
| To | ``` - (instancetype _Nonnull)initWithBadgeValue:(NSUInteger)badgeValue ``` |

Modified [CKModifyBadgeOperation.modifyBadgeCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391682-modifybadgecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^modifyBadgeCompletionBlock)(NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^modifyBadgeCompletionBlock)(NSError * _Nullable operationError) ``` |

#### CKModifyRecordsOperation.h

Modified [CKModifyRecordsOperation.clientChangeTokenData](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447472-clientchangetokendata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSData *clientChangeTokenData ``` |
| To | ``` @property(nonatomic, copy, nullable) NSData *clientChangeTokenData ``` |

Modified [-[CKModifyRecordsOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447466-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKModifyRecordsOperation initWithRecordsToSave:recordIDsToDelete:]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447464-initwithrecordstosave)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordsToSave:(NSArray *)records recordIDsToDelete:(NSArray *)recordIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordsToSave:(NSArray<CKRecord *> * _Nullable)records recordIDsToDelete:(NSArray<CKRecordID *> * _Nullable)recordIDs ``` |

Modified [CKModifyRecordsOperation.modifyRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447486-modifyrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^modifyRecordsCompletionBlock)(NSArray *savedRecords, NSArray *deletedRecordIDs, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^modifyRecordsCompletionBlock)(NSArray<CKRecord *> * _Nullable savedRecords, NSArray<CKRecordID *> * _Nullable deletedRecordIDs, NSError * _Nullable operationError) ``` |

Modified [CKModifyRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447470-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^perRecordCompletionBlock)(CKRecord *record, NSError *error) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^perRecordCompletionBlock)(CKRecord * _Nullable record, NSError * _Nullable error) ``` |

Modified [CKModifyRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447477-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^perRecordProgressBlock)(CKRecord *record, double progress) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^perRecordProgressBlock)(CKRecord * _Nonnull record, double progress) ``` |

Modified [CKModifyRecordsOperation.recordIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447479-recordidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordIDsToDelete ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordID *> *recordIDsToDelete ``` |

Modified [CKModifyRecordsOperation.recordsToSave](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447482-recordstosave)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordsToSave ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecord *> *recordsToSave ``` |

#### CKModifyRecordZonesOperation.h

Modified [-[CKModifyRecordZonesOperation init]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415169-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKModifyRecordZonesOperation initWithRecordZonesToSave:recordZoneIDsToDelete:]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415167-initwithrecordzonestosave)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordZonesToSave:(NSArray *)recordZonesToSave recordZoneIDsToDelete:(NSArray *)recordZoneIDsToDelete ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordZonesToSave:(NSArray<CKRecordZone *> * _Nullable)recordZonesToSave recordZoneIDsToDelete:(NSArray<CKRecordZoneID *> * _Nullable)recordZoneIDsToDelete ``` |

Modified [CKModifyRecordZonesOperation.modifyRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415164-modifyrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^modifyRecordZonesCompletionBlock)(NSArray *savedRecordZones, NSArray *deletedRecordZoneIDs, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^modifyRecordZonesCompletionBlock)(NSArray<CKRecordZone *> * _Nullable savedRecordZones, NSArray<CKRecordZoneID *> * _Nullable deletedRecordZoneIDs, NSError * _Nullable operationError) ``` |

Modified [CKModifyRecordZonesOperation.recordZoneIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415173-recordzoneidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordZoneIDsToDelete ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordZoneID *> *recordZoneIDsToDelete ``` |

Modified [CKModifyRecordZonesOperation.recordZonesToSave](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415171-recordzonestosave)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordZonesToSave ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordZone *> *recordZonesToSave ``` |

#### CKModifySubscriptionsOperation.h

Modified [-[CKModifySubscriptionsOperation initWithSubscriptionsToSave:subscriptionIDsToDelete:]](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515015-initwithsubscriptionstosave)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSubscriptionsToSave:(NSArray *)subscriptionsToSave subscriptionIDsToDelete:(NSArray *)subscriptionIDsToDelete ``` |
| To | ``` - (instancetype _Nonnull)initWithSubscriptionsToSave:(NSArray<CKSubscription *> * _Nullable)subscriptionsToSave subscriptionIDsToDelete:(NSArray<NSString *> * _Nullable)subscriptionIDsToDelete ``` |

Modified [CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515288-modifysubscriptionscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^modifySubscriptionsCompletionBlock)(NSArray *savedSubscriptions, NSArray *deletedSubscriptionIDs, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^modifySubscriptionsCompletionBlock)(NSArray<CKSubscription *> * _Nullable savedSubscriptions, NSArray<NSString *> * _Nullable deletedSubscriptionIDs, NSError * _Nullable operationError) ``` |

Modified [CKModifySubscriptionsOperation.subscriptionIDsToDelete](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1514892-subscriptionidstodelete)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *subscriptionIDsToDelete ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *subscriptionIDsToDelete ``` |

Modified [CKModifySubscriptionsOperation.subscriptionsToSave](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515135-subscriptionstosave)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *subscriptionsToSave ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKSubscription *> *subscriptionsToSave ``` |

#### CKNotification.h

Added [CKNotification.category](https://developer.apple.com/documentation/cloudkit/cknotification/1428107-category)Added [CKNotification.subscriptionID](https://developer.apple.com/documentation/cloudkit/cknotification/1428118-subscriptionid)Modified [CKNotification.alertActionLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotification/1428109-alertactionlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *alertActionLocalizationKey ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *alertActionLocalizationKey ``` |

Modified [CKNotification.alertBody](https://developer.apple.com/documentation/cloudkit/cknotification/1428084-alertbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *alertBody ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *alertBody ``` |

Modified [CKNotification.alertLaunchImage](https://developer.apple.com/documentation/cloudkit/cknotification/1428103-alertlaunchimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *alertLaunchImage ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *alertLaunchImage ``` |

Modified [CKNotification.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotification/1428105-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *alertLocalizationArgs ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<NSString *> *alertLocalizationArgs ``` |

Modified [CKNotification.alertLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotification/1428095-alertlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *alertLocalizationKey ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *alertLocalizationKey ``` |

Modified [CKNotification.badge](https://developer.apple.com/documentation/cloudkit/cknotification/1428082-badge)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSNumber *badge ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSNumber *badge ``` |

Modified [CKNotification.containerIdentifier](https://developer.apple.com/documentation/cloudkit/cknotification/1428119-containeridentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *containerIdentifier ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *containerIdentifier ``` |

Modified [+[CKNotification notificationFromRemoteNotificationDictionary:]](https://developer.apple.com/documentation/cloudkit/cknotification/1428130-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)notificationFromRemoteNotificationDictionary:(NSDictionary *)notificationDictionary ``` |
| To | ``` + (instancetype _Nonnull)notificationFromRemoteNotificationDictionary:(NSDictionary<NSString *,NSObject *> * _Nonnull)notificationDictionary ``` |

Modified [CKNotification.notificationID](https://developer.apple.com/documentation/cloudkit/cknotification/1428080-notificationid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKNotificationID *notificationID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKNotificationID *notificationID ``` |

Modified [CKNotification.soundName](https://developer.apple.com/documentation/cloudkit/cknotification/1428077-soundname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *soundName ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *soundName ``` |

Modified [CKQueryNotification.recordFields](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428114-recordfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDictionary *recordFields ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDictionary<NSString *,__kindof id<CKRecordValue>> *recordFields ``` |

Modified [CKQueryNotification.recordID](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428134-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *recordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKRecordID *recordID ``` |

Modified [CKRecordZoneNotification.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification/1428086-recordzoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordZoneID *recordZoneID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKRecordZoneID *recordZoneID ``` |

#### CKOperation.h

Added -[CKOperation activityStart]Modified [CKOperation.container](https://developer.apple.com/documentation/cloudkit/ckoperation/1452364-container)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) CKContainer *container ``` |
| To | ``` @property(nonatomic, strong, nullable) CKContainer *container ``` |

Modified [-[CKOperation init]](https://developer.apple.com/documentation/cloudkit/ckoperation/1452370-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified CKOperation.usesBackgroundSession

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CKQuery.h

Modified [-[CKQuery initWithCoder:]](https://developer.apple.com/documentation/cloudkit/ckquery/1413111-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nonnull)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[CKQuery initWithRecordType:predicate:]](https://developer.apple.com/documentation/cloudkit/ckquery/1413119-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType predicate:(NSPredicate *)predicate ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType predicate:(NSPredicate * _Nonnull)predicate ``` |

Modified [CKQuery.predicate](https://developer.apple.com/documentation/cloudkit/ckquery/1413112-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSPredicate *predicate ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSPredicate *predicate ``` |

Modified [CKQuery.recordType](https://developer.apple.com/documentation/cloudkit/ckquery/1413117-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *recordType ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *recordType ``` |

Modified [CKQuery.sortDescriptors](https://developer.apple.com/documentation/cloudkit/ckquery/1413121-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *sortDescriptors ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

#### CKQueryOperation.h

Modified [CKQueryOperation.cursor](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1514975-cursor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKQueryCursor *cursor ``` |
| To | ``` @property(nonatomic, copy, nullable) CKQueryCursor *cursor ``` |

Modified [CKQueryOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515268-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

Modified [-[CKQueryOperation init]](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515115-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CKQueryOperation initWithCursor:]](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515033-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCursor:(CKQueryCursor *)cursor ``` |
| To | ``` - (instancetype _Nonnull)initWithCursor:(CKQueryCursor * _Nonnull)cursor ``` |

Modified [-[CKQueryOperation initWithQuery:]](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1514958-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithQuery:(CKQuery *)query ``` |
| To | ``` - (instancetype _Nonnull)initWithQuery:(CKQuery * _Nonnull)query ``` |

Modified [CKQueryOperation.query](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515127-query)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKQuery *query ``` |
| To | ``` @property(nonatomic, copy, nullable) CKQuery *query ``` |

Modified [CKQueryOperation.queryCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515067-querycompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^queryCompletionBlock)(CKQueryCursor *cursor, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^queryCompletionBlock)(CKQueryCursor * _Nullable cursor, NSError * _Nullable operationError) ``` |

Modified [CKQueryOperation.recordFetchedBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515283-recordfetchedblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^recordFetchedBlock)(CKRecord *record) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^recordFetchedBlock)(CKRecord * _Nonnull record) ``` |

Modified [CKQueryOperation.zoneID](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515269-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKRecordZoneID *zoneID ``` |
| To | ``` @property(nonatomic, copy, nullable) CKRecordZoneID *zoneID ``` |

#### CKRecord.h

Modified [-[CKRecord allKeys]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462220-allkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allKeys ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)allKeys ``` |

Modified [-[CKRecord allTokens]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462199-alltokens)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allTokens ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)allTokens ``` |

Modified [-[CKRecord changedKeys]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462197-changedkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)changedKeys ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)changedKeys ``` |

Modified [CKRecord.creationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462223-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDate *creationDate ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDate *creationDate ``` |

Modified [CKRecord.creatorUserRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462208-creatoruserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *creatorUserRecordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKRecordID *creatorUserRecordID ``` |

Modified [-[CKRecord encodeSystemFieldsWithCoder:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462200-encodesystemfieldswithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (void)encodeSystemFieldsWithCoder:(NSCoder *)coder ``` |
| To | ``` - (void)encodeSystemFieldsWithCoder:(NSCoder * _Nonnull)coder ``` |

Modified [-[CKRecord initWithRecordType:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462225-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType ``` |

Modified [-[CKRecord initWithRecordType:recordID:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462204-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType recordID:(CKRecordID *)recordID ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType recordID:(CKRecordID * _Nonnull)recordID ``` |

Modified [-[CKRecord initWithRecordType:zoneID:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462202-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType zoneID:(CKRecordZoneID *)zoneID ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType zoneID:(CKRecordZoneID * _Nonnull)zoneID ``` |

Modified [CKRecord.lastModifiedUserRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462212-lastmodifieduserrecordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *lastModifiedUserRecordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CKRecordID *lastModifiedUserRecordID ``` |

Modified [CKRecord.modificationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462227-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDate *modificationDate ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDate *modificationDate ``` |

Modified [-[CKRecord objectForKey:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462216-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKey:(NSString *)key ``` |
| To | ``` - (__kindof id<CKRecordValue> _Nullable)objectForKey:(NSString * _Nonnull)key ``` |

Modified [-[CKRecord objectForKeyedSubscript:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462210-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectForKeyedSubscript:(NSString *)key ``` |
| To | ``` - (__kindof id<CKRecordValue> _Nullable)objectForKeyedSubscript:(NSString * _Nonnull)key ``` |

Modified [CKRecord.recordChangeTag](https://developer.apple.com/documentation/cloudkit/ckrecord/1462195-recordchangetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *recordChangeTag ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *recordChangeTag ``` |

Modified [CKRecord.recordID](https://developer.apple.com/documentation/cloudkit/ckrecord/1462229-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *recordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) CKRecordID *recordID ``` |

Modified [CKRecord.recordType](https://developer.apple.com/documentation/cloudkit/ckrecord/1462206-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *recordType ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *recordType ``` |

Modified [-[CKRecord setObject:forKey:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462231-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id<CKRecordValue>)object forKey:(NSString *)key ``` |
| To | ``` - (void)setObject:(__kindof id<CKRecordValue> _Nullable)object forKey:(NSString * _Nonnull)key ``` |

Modified [-[CKRecord setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1462221-setobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObject:(id<CKRecordValue>)object forKeyedSubscript:(NSString *)key ``` |
| To | ``` - (void)setObject:(__kindof id<CKRecordValue> _Nullable)object forKeyedSubscript:(NSString * _Nonnull)key ``` |

#### CKRecordID.h

Modified [-[CKRecordID initWithRecordName:]](https://developer.apple.com/documentation/cloudkit/ckrecordid/1500975-initwithrecordname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordName:(NSString *)recordName ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordName:(NSString * _Nonnull)recordName ``` |

Modified [-[CKRecordID initWithRecordName:zoneID:]](https://developer.apple.com/documentation/cloudkit/ckrecord/id/1500967-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordName:(NSString *)recordName zoneID:(CKRecordZoneID *)zoneID ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordName:(NSString * _Nonnull)recordName zoneID:(CKRecordZoneID * _Nonnull)zoneID ``` |

Modified [CKRecordID.recordName](https://developer.apple.com/documentation/cloudkit/ckrecord/id/1500973-recordname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSString *recordName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *recordName ``` |

Modified [CKRecordID.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecord/id/1500969-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) CKRecordZoneID *zoneID ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) CKRecordZoneID *zoneID ``` |

#### CKRecordZone.h

Modified [+[CKRecordZone defaultRecordZone]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1514919-defaultrecordzone)

|  | Declaration |
| --- | --- |
| From | ``` + (CKRecordZone *)defaultRecordZone ``` |
| To | ``` + (CKRecordZone * _Nonnull)defaultRecordZone ``` |

Modified [-[CKRecordZone initWithZoneID:]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1515207-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithZoneID:(CKRecordZoneID *)zoneID ``` |
| To | ``` - (instancetype _Nonnull)initWithZoneID:(CKRecordZoneID * _Nonnull)zoneID ``` |

Modified [-[CKRecordZone initWithZoneName:]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1515102-initwithzonename)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithZoneName:(NSString *)zoneName ``` |
| To | ``` - (instancetype _Nonnull)initWithZoneName:(NSString * _Nonnull)zoneName ``` |

Modified [CKRecordZone.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1514917-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) CKRecordZoneID *zoneID ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) CKRecordZoneID *zoneID ``` |

#### CKRecordZoneID.h

Modified [-[CKRecordZoneID initWithZoneName:ownerName:]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508089-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithZoneName:(NSString *)zoneName ownerName:(NSString *)ownerName ``` |
| To | ``` - (instancetype _Nonnull)initWithZoneName:(NSString * _Nonnull)zoneName ownerName:(NSString * _Nonnull)ownerName ``` |

Modified [CKRecordZoneID.ownerName](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508096-ownername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSString *ownerName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *ownerName ``` |

Modified [CKRecordZoneID.zoneName](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id/1508094-zonename)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSString *zoneName ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSString *zoneName ``` |

#### CKReference.h

Modified [-[CKReference initWithRecord:action:]](https://developer.apple.com/documentation/cloudkit/ckreference/1515312-initwithrecord)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecord:(CKRecord *)record action:(CKReferenceAction)action ``` |
| To | ``` - (instancetype _Nonnull)initWithRecord:(CKRecord * _Nonnull)record action:(CKReferenceAction)action ``` |

Modified [-[CKReference initWithRecordID:action:]](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1515280-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordID:(CKRecordID *)recordID action:(CKReferenceAction)action ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordID:(CKRecordID * _Nonnull)recordID action:(CKReferenceAction)action ``` |

Modified [CKReference.recordID](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/1514956-recordid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CKRecordID *recordID ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) CKRecordID *recordID ``` |

#### CKSubscription.h

Added [CKNotificationInfo.category](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo/1515082-category)Modified [CKNotificationInfo.alertActionLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514945-alertactionlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *alertActionLocalizationKey ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *alertActionLocalizationKey ``` |

Modified [CKNotificationInfo.alertBody](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515270-alertbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *alertBody ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *alertBody ``` |

Modified [CKNotificationInfo.alertLaunchImage](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515075-alertlaunchimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *alertLaunchImage ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *alertLaunchImage ``` |

Modified [CKNotificationInfo.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515182-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *alertLocalizationArgs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *alertLocalizationArgs ``` |

Modified [CKNotificationInfo.alertLocalizationKey](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514968-alertlocalizationkey)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *alertLocalizationKey ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *alertLocalizationKey ``` |

Modified [CKNotificationInfo.desiredKeys](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514931-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

Modified [CKNotificationInfo.soundName](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo/1514987-soundname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *soundName ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *soundName ``` |

Modified [-[CKSubscription initWithCoder:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515004-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nonnull)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[CKSubscription initWithRecordType:predicate:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515132-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType predicate:(NSPredicate *)predicate options:(CKSubscriptionOptions)subscriptionOptions ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType predicate:(NSPredicate * _Nonnull)predicate options:(CKSubscriptionOptions)subscriptionOptions ``` |

Modified [-[CKSubscription initWithRecordType:predicate:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515265-initwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordType:(NSString *)recordType predicate:(NSPredicate *)predicate subscriptionID:(NSString *)subscriptionID options:(CKSubscriptionOptions)subscriptionOptions ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordType:(NSString * _Nonnull)recordType predicate:(NSPredicate * _Nonnull)predicate subscriptionID:(NSString * _Nonnull)subscriptionID options:(CKSubscriptionOptions)subscriptionOptions ``` |

Modified [-[CKSubscription initWithZoneID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1514971-initwithzoneid)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithZoneID:(CKRecordZoneID *)zoneID options:(CKSubscriptionOptions)subscriptionOptions ``` |
| To | ``` - (instancetype _Nonnull)initWithZoneID:(CKRecordZoneID * _Nonnull)zoneID options:(CKSubscriptionOptions)subscriptionOptions ``` |

Modified [-[CKSubscription initWithZoneID:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515215-initwithzoneid)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithZoneID:(CKRecordZoneID *)zoneID subscriptionID:(NSString *)subscriptionID options:(CKSubscriptionOptions)subscriptionOptions ``` |
| To | ``` - (instancetype _Nonnull)initWithZoneID:(CKRecordZoneID * _Nonnull)zoneID subscriptionID:(NSString * _Nonnull)subscriptionID options:(CKSubscriptionOptions)subscriptionOptions ``` |

Modified [CKSubscription.notificationInfo](https://developer.apple.com/documentation/cloudkit/cksubscription/1514948-notificationinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKNotificationInfo *notificationInfo ``` |
| To | ``` @property(nonatomic, copy, nullable) CKNotificationInfo *notificationInfo ``` |

Modified [CKSubscription.predicate](https://developer.apple.com/documentation/cloudkit/cksubscription/1515219-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSPredicate *predicate ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSPredicate *predicate ``` |

Modified [CKSubscription.recordType](https://developer.apple.com/documentation/cloudkit/cksubscription/1515080-recordtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *recordType ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *recordType ``` |

Modified [CKSubscription.subscriptionID](https://developer.apple.com/documentation/cloudkit/cksubscription/1515199-subscriptionid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *subscriptionID ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *subscriptionID ``` |

Modified [CKSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/cksubscription/1514936-zoneid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) CKRecordZoneID *zoneID ``` |
| To | ``` @property(nonatomic, copy, nullable) CKRecordZoneID *zoneID ``` |

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
