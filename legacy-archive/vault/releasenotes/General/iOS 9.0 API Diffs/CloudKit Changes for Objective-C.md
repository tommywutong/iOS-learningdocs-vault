---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CloudKit.html
archived_at: '2026-07-18T02:56:30.943707Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CloudKit Changes for Objective-C

### CloudKit

#### CKContainer.h

Added [CKAccountChangedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged)Modified [-[CKContainer discoverAllContactUserInfosWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399199-discoverallcontactuserinfoswithc)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverAllContactUserInfosWithCompletionHandler:(void (^)(NSArray *userInfos, NSError *error))completionHandler ``` |
| To | ``` - (void)discoverAllContactUserInfosWithCompletionHandler:(void (^ _Nonnull)(NSArray<CKDiscoveredUserInfo *> * _Nullable userInfos, NSError * _Nullable error))completionHandler ``` |

#### CKDatabase.h

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

Modified [-[CKDatabase performQuery:inZoneWithID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449127-performquery)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performQuery:(CKQuery *)query inZoneWithID:(CKRecordZoneID *)zoneID completionHandler:(void (^)(NSArray *results, NSError *error))completionHandler ``` |
| To | ``` - (void)performQuery:(CKQuery * _Nonnull)query inZoneWithID:(CKRecordZoneID * _Nullable)zoneID completionHandler:(void (^ _Nonnull)(NSArray<CKRecord *> * _Nullable results, NSError * _Nullable error))completionHandler ``` |

#### CKDiscoverAllContactsOperation.h

Modified [CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1515099-discoverallcontactscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^discoverAllContactsCompletionBlock)(NSArray *userInfos, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^discoverAllContactsCompletionBlock)(NSArray<CKDiscoveredUserInfo *> * _Nullable userInfos, NSError * _Nullable operationError) ``` |

#### CKDiscoveredUserInfo.h

Added [CKDiscoveredUserInfo.displayContact](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436518-displaycontact)Modified [CKDiscoveredUserInfo.firstName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436520-firstname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [CKDiscoveredUserInfo.lastName](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436514-lastname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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

#### CKFetchRecordChangesOperation.h

Modified [CKFetchRecordChangesOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515230-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

#### CKFetchRecordsOperation.h

Modified [CKFetchRecordsOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476088-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

Modified [CKFetchRecordsOperation.fetchRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476078-fetchrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchRecordsCompletionBlock)(NSDictionary *recordsByRecordID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchRecordsCompletionBlock)(NSDictionary<CKRecordID *,CKRecord *> * _Nullable recordsByRecordID, NSError * _Nullable operationError) ``` |

Modified [-[CKFetchRecordsOperation initWithRecordIDs:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476074-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRecordIDs:(NSArray *)recordIDs ``` |
| To | ``` - (instancetype _Nonnull)initWithRecordIDs:(NSArray<CKRecordID *> * _Nonnull)recordIDs ``` |

Modified [CKFetchRecordsOperation.recordIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476076-recordids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recordIDs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CKRecordID *> *recordIDs ``` |

#### CKFetchRecordZonesOperation.h

Modified [CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515145-fetchrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchRecordZonesCompletionBlock)(NSDictionary *recordZonesByZoneID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchRecordZonesCompletionBlock)(NSDictionary<CKRecordZoneID *,CKRecordZone *> * _Nullable recordZonesByZoneID, NSError * _Nullable operationError) ``` |

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

Modified [CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515261-fetchsubscriptioncompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^fetchSubscriptionCompletionBlock)(NSDictionary *subscriptionsBySubscriptionID, NSError *operationError) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^fetchSubscriptionCompletionBlock)(NSDictionary<NSString *,CKSubscription *> * _Nullable subscriptionsBySubscriptionID, NSError * _Nullable operationError) ``` |

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

#### CKModifyRecordsOperation.h

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

Added [CKNotification.category](https://developer.apple.com/documentation/cloudkit/cknotification/1428107-category)Added [CKNotification.subscriptionID](https://developer.apple.com/documentation/cloudkit/cknotification/1428118-subscriptionid)Modified [CKNotification.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotification/1428105-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *alertLocalizationArgs ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<NSString *> *alertLocalizationArgs ``` |

Modified [+[CKNotification notificationFromRemoteNotificationDictionary:]](https://developer.apple.com/documentation/cloudkit/cknotification/1428130-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)notificationFromRemoteNotificationDictionary:(NSDictionary *)notificationDictionary ``` |
| To | ``` + (instancetype _Nonnull)notificationFromRemoteNotificationDictionary:(NSDictionary<NSString *,NSObject *> * _Nonnull)notificationDictionary ``` |

Modified [CKQueryNotification.recordFields](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428114-recordfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDictionary *recordFields ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDictionary<NSString *,__kindof id<CKRecordValue>> *recordFields ``` |

#### CKOperation.h

Added -[CKOperation activityStart]Modified CKOperation.usesBackgroundSession

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CKQuery.h

Modified [CKQuery.sortDescriptors](https://developer.apple.com/documentation/cloudkit/ckquery/1413121-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *sortDescriptors ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

#### CKQueryOperation.h

Modified [CKQueryOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515268-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

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

#### CKSubscription.h

Added [CKNotificationInfo.category](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo/1515082-category)Modified [CKNotificationInfo.alertLocalizationArgs](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1515182-alertlocalizationargs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *alertLocalizationArgs ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *alertLocalizationArgs ``` |

Modified [CKNotificationInfo.desiredKeys](https://developer.apple.com/documentation/cloudkit/cknotificationinfo/1514931-desiredkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *desiredKeys ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *desiredKeys ``` |

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
