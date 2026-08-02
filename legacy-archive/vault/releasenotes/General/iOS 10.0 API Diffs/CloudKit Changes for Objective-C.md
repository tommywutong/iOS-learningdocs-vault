---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CloudKit.html
archived_at: '2026-07-18T02:54:54.027606Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CloudKit Changes for Objective-C

### CloudKit

#### CKAcceptSharesOperation.h (Added)

Added [CKAcceptSharesOperation](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation)Added [CKAcceptSharesOperation.acceptSharesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640442-acceptsharescompletionblock)Added [-[CKAcceptSharesOperation init]](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640506-init)Added [-[CKAcceptSharesOperation initWithShareMetadatas:]](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1823506-initwithsharemetadatas)Added [CKAcceptSharesOperation.perShareCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640426-persharecompletionblock)Added [CKAcceptSharesOperation.shareMetadatas](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1823508-sharemetadatas)

#### CKContainer.h

Added [-[CKContainer acceptShareMetadata:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/2113667-acceptsharemetadata)Added [-[CKContainer databaseWithDatabaseScope:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640475-databasewithdatabasescope)Added [-[CKContainer discoverAllIdentitiesWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640421-discoverallidentitieswithcomplet)Added [-[CKContainer discoverUserIdentityWithEmailAddress:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640430-discoveruseridentity)Added [-[CKContainer discoverUserIdentityWithPhoneNumber:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640516-discoveruseridentity)Added [-[CKContainer discoverUserIdentityWithUserRecordID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640517-discoveruseridentity)Added [-[CKContainer fetchShareMetadataWithURL:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/2113666-fetchsharemetadata)Added [-[CKContainer fetchShareParticipantWithEmailAddress:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640489-fetchshareparticipant)Added [-[CKContainer fetchShareParticipantWithPhoneNumber:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640493-fetchshareparticipantwithphonenu)Added [-[CKContainer fetchShareParticipantWithUserRecordID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640387-fetchshareparticipant)Added [CKContainer.sharedCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640408-sharedclouddatabase)Added CKContainer(Sharing)Added [CKCurrentUserDefaultName](https://developer.apple.com/documentation/cloudkit/ckcurrentuserdefaultname)Modified [-[CKContainer discoverAllContactUserInfosWithCompletionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399199-discoverallcontactuserinfoswithc)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKContainer discoverUserInfoWithEmailAddress:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399201-discoveruserinfowithemailaddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKContainer discoverUserInfoWithUserRecordID:completionHandler:]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399217-discoveruserinfowithuserrecordid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKOwnerDefaultName](https://developer.apple.com/documentation/cloudkit/ckownerdefaultname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKDatabase.h

Added [CKDatabase.databaseScope](https://developer.apple.com/documentation/cloudkit/ckdatabase/1640398-databasescope)Added [CKDatabaseScope](https://developer.apple.com/documentation/cloudkit/ckdatabasescope)Added [CKDatabaseScopePrivate](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/private)Added [CKDatabaseScopePublic](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/public)Added [CKDatabaseScopeShared](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/shared)

#### CKDefines.h

Added #def CK_HIDDEN

#### CKDiscoverAllContactsOperation.h

Modified [CKDiscoverAllContactsOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1515099-discoverallcontactscompletionblo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKDiscoverAllContactsOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1514998-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKDiscoverAllUserIdentitiesOperation.h (Added)

Added [CKDiscoverAllUserIdentitiesOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation)Added [CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640497-discoveralluseridentitiescomplet)Added [-[CKDiscoverAllUserIdentitiesOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640435-init)Added [CKDiscoverAllUserIdentitiesOperation.userIdentityDiscoveredBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640416-useridentitydiscoveredblock)

#### CKDiscoveredUserInfo.h

Modified [CKDiscoveredUserInfo](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoveredUserInfo.displayContact](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436518-displaycontact)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoveredUserInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436516-userrecordid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKDiscoverUserIdentitiesOperation.h (Added)

Added [CKDiscoverUserIdentitiesOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation)Added [CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640500-discoveruseridentitiescompletion)Added [-[CKDiscoverUserIdentitiesOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640525-init)Added [-[CKDiscoverUserIdentitiesOperation initWithUserIdentityLookupInfos:]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640521-initwithuseridentitylookupinfos)Added [CKDiscoverUserIdentitiesOperation.userIdentityDiscoveredBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640524-useridentitydiscoveredblock)Added [CKDiscoverUserIdentitiesOperation.userIdentityLookupInfos](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640450-useridentitylookupinfos)

#### CKDiscoverUserInfosOperation.h

Modified [CKDiscoverUserInfosOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403386-discoveruserinfoscompletionblock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoverUserInfosOperation.emailAddresses](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403382-emailaddresses)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKDiscoverUserInfosOperation init]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403380-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKDiscoverUserInfosOperation initWithEmailAddresses:userRecordIDs:]](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403391-initwithemailaddresses)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKDiscoverUserInfosOperation.userRecordIDs](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403384-userrecordids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKError.h

Added [CKErrorAlreadyShared](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerroralreadyshared)Added [CKErrorManagedAccountRestricted](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrormanagedaccountrestricted)Added [CKErrorParticipantMayNeedVerification](https://developer.apple.com/documentation/cloudkit/ckerror/code/participantmayneedverification)Added [CKErrorReferenceViolation](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorreferenceviolation)Added [CKErrorTooManyParticipants](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrortoomanyparticipants)Modified [CKErrorResultsTruncated](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorresultstruncated)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKFetchDatabaseChangesOperation.h (Added)

Added [CKFetchDatabaseChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation)Added [CKFetchDatabaseChangesOperation.changeTokenUpdatedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640467-changetokenupdatedblock)Added [CKFetchDatabaseChangesOperation.fetchAllChanges](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640473-fetchallchanges)Added [CKFetchDatabaseChangesOperation.fetchDatabaseChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640434-fetchdatabasechangescompletionbl)Added [-[CKFetchDatabaseChangesOperation initWithPreviousServerChangeToken:]](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640502-initwithpreviousserverchangetoke)Added [CKFetchDatabaseChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640522-previousserverchangetoken)Added [CKFetchDatabaseChangesOperation.recordZoneWithIDChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640391-recordzonewithidchangedblock)Added [CKFetchDatabaseChangesOperation.recordZoneWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640428-recordzonewithidwasdeletedblock)Added [CKFetchDatabaseChangesOperation.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640520-resultslimit)

#### CKFetchRecordChangesOperation.h

Modified [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515230-desiredkeys)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.fetchRecordChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515267-fetchrecordchangescompletionbloc)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKFetchRecordChangesOperation initWithRecordZoneID:previousServerChangeToken:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515224-initwithrecordzoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.moreComing](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515322-morecoming)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515209-previousserverchangetoken)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515155-recordchangedblock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515054-recordwithidwasdeletedblock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515018-recordzoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKFetchRecordChangesOperation.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1514891-resultslimit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKFetchRecordZoneChangesOperation.h (Added)

Added [CKFetchRecordZoneChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation)Added [CKFetchRecordZoneChangesOperation.fetchAllChanges](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640386-fetchallchanges)Added [CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640409-fetchrecordzonechangescompletion)Added [-[CKFetchRecordZoneChangesOperation initWithRecordZoneIDs:optionsByRecordZoneID:]](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640509-init)Added [CKFetchRecordZoneChangesOperation.optionsByRecordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640452-optionsbyrecordzoneid)Added [CKFetchRecordZoneChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640417-recordchangedblock)Added [CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640470-recordwithidwasdeletedblock)Added [CKFetchRecordZoneChangesOperation.recordZoneChangeTokensUpdatedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640422-recordzonechangetokensupdatedblo)Added [CKFetchRecordZoneChangesOperation.recordZoneFetchCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640411-recordzonefetchcompletionblock)Added [CKFetchRecordZoneChangesOperation.recordZoneIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640463-recordzoneids)Added [CKFetchRecordZoneChangesOptions](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions)Added [CKFetchRecordZoneChangesOptions.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/1640472-desiredkeys)Added [CKFetchRecordZoneChangesOptions.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/1640389-previousserverchangetoken)Added [CKFetchRecordZoneChangesOptions.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/1640481-resultslimit)

#### CKFetchShareMetadataOperation.h (Added)

Added [CKFetchShareMetadataOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation)Added [CKFetchShareMetadataOperation.fetchShareMetadataCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640457-fetchsharemetadatacompletionbloc)Added [-[CKFetchShareMetadataOperation initWithShareURLs:]](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640495-init)Added [CKFetchShareMetadataOperation.perShareMetadataBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640447-persharemetadatablock)Added [CKFetchShareMetadataOperation.rootRecordDesiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640375-rootrecorddesiredkeys)Added [CKFetchShareMetadataOperation.shareURLs](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640508-shareurls)Added [CKFetchShareMetadataOperation.shouldFetchRootRecord](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640519-shouldfetchrootrecord)

#### CKFetchShareParticipantsOperation.h (Added)

Added [CKFetchShareParticipantsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation)Added [CKFetchShareParticipantsOperation.fetchShareParticipantsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640529-fetchshareparticipantscompletion)Added [-[CKFetchShareParticipantsOperation init]](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640478-init)Added [-[CKFetchShareParticipantsOperation initWithUserIdentityLookupInfos:]](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640471-initwithuseridentitylookupinfos)Added [CKFetchShareParticipantsOperation.shareParticipantFetchedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640451-shareparticipantfetchedblock)Added [CKFetchShareParticipantsOperation.userIdentityLookupInfos](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640380-useridentitylookupinfos)

#### CKMarkNotificationsReadOperation.h

Added [-[CKMarkNotificationsReadOperation init]](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1640383-init)Modified [-[CKMarkNotificationsReadOperation initWithNotificationIDsToMarkRead:]](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515228-init)

|  | Designated Initializer |
| --- | --- |
| From | yes |
| To | -- |

#### CKNotification.h

Added [CKDatabaseNotification](https://developer.apple.com/documentation/cloudkit/ckdatabasenotification)Added [CKDatabaseNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckdatabasenotification/1640510-databasescope)Added [CKQueryNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1640449-databasescope)Added [CKRecordZoneNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification/1640394-databasescope)Added [CKNotificationTypeDatabase](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype/database)Modified [CKQueryNotification.isPublicDatabase](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428111-ispublicdatabase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKQueryNotification.recordFields](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428114-recordfields)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDictionary<NSString *,__kindof id<CKRecordValue>> *recordFields ``` |
| To | ``` @property(nonatomic, readonly, copy) NSDictionary<NSString *,id> *recordFields ``` |

#### CKOperation.h

Added [CKOperation.timeoutIntervalForRequest](https://developer.apple.com/documentation/cloudkit/ckoperation/1639384-timeoutintervalforrequest)Added [CKOperation.timeoutIntervalForResource](https://developer.apple.com/documentation/cloudkit/ckoperation/1639386-timeoutintervalforresource)

#### CKRecord.h

Added [CKRecord.parent](https://developer.apple.com/documentation/cloudkit/ckrecord/1640527-parent)Added [-[CKRecord setParentReferenceFromRecord:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1690507-setparentreferencefromrecord)Added [-[CKRecord setParentReferenceFromRecordID:]](https://developer.apple.com/documentation/cloudkit/ckrecord/1690508-setparentreferencefromrecordid)Added [CKRecord.share](https://developer.apple.com/documentation/cloudkit/ckrecord/1640378-share)Added [CKRecordParentKey](https://developer.apple.com/documentation/cloudkit/ckrecordparentkey)Added [CKRecordShareKey](https://developer.apple.com/documentation/cloudkit/ckrecordsharekey)

#### CKRecordZone.h

Added [CKRecordZoneCapabilitySharing](https://developer.apple.com/documentation/cloudkit/ckrecordzonecapabilities/ckrecordzonecapabilitysharing)

#### CKShare.h (Added)

Added [CKShare](https://developer.apple.com/documentation/cloudkit/ckshare)Added [-[CKShare addParticipant:]](https://developer.apple.com/documentation/cloudkit/ckshare/1640443-addparticipant)Added [CKShare.currentUserParticipant](https://developer.apple.com/documentation/cloudkit/ckshare/1640441-currentuserparticipant)Added [-[CKShare initWithCoder:]](https://developer.apple.com/documentation/cloudkit/ckshare/1640432-init)Added [-[CKShare initWithRootRecord:]](https://developer.apple.com/documentation/cloudkit/ckshare/1640448-init)Added [-[CKShare initWithRootRecord:shareID:]](https://developer.apple.com/documentation/cloudkit/ckshare/1640381-initwithrootrecord)Added [CKShare.owner](https://developer.apple.com/documentation/cloudkit/ckshare/1640503-owner)Added [CKShare.participants](https://developer.apple.com/documentation/cloudkit/ckshare/1640453-participants)Added [CKShare.publicPermission](https://developer.apple.com/documentation/cloudkit/ckshare/1640494-publicpermission)Added [-[CKShare removeParticipant:]](https://developer.apple.com/documentation/cloudkit/ckshare/1640523-removeparticipant)Added [CKShare.URL](https://developer.apple.com/documentation/cloudkit/ckshare/1640465-url)Added [CKRecordTypeShare](https://developer.apple.com/documentation/cloudkit/ckrecordtypeshare)Added [CKShareThumbnailImageDataKey](https://developer.apple.com/documentation/cloudkit/cksharethumbnailimagedatakey)Added [CKShareTitleKey](https://developer.apple.com/documentation/cloudkit/cksharetitlekey)Added [CKShareTypeKey](https://developer.apple.com/documentation/cloudkit/cksharetypekey)

#### CKShareMetadata.h (Added)

Added [CKShareMetadata](https://developer.apple.com/documentation/cloudkit/cksharemetadata)Added [CKShareMetadata.containerIdentifier](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640400-containeridentifier)Added [CKShareMetadata.ownerIdentity](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640498-owneridentity)Added [CKShareMetadata.participantPermission](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640483-participantpermission)Added [CKShareMetadata.participantStatus](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640420-participantstatus)Added [CKShareMetadata.participantType](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640518-participanttype)Added [CKShareMetadata.rootRecord](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640366-rootrecord)Added [CKShareMetadata.rootRecordID](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640410-rootrecordid)Added [CKShareMetadata.share](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640412-share)

#### CKShareParticipant.h (Added)

Added [CKShareParticipant](https://developer.apple.com/documentation/cloudkit/ckshareparticipant)Added [CKShareParticipant.acceptanceStatus](https://developer.apple.com/documentation/cloudkit/ckshare/participant/1640395-acceptancestatus)Added [CKShareParticipant.permission](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640433-permission)Added [CKShareParticipant.type](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640507-type)Added [CKShareParticipant.userIdentity](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640488-useridentity)Added [CKShareParticipantAcceptanceStatus](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus)Added [CKShareParticipantAcceptanceStatusAccepted](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus/ckshareparticipantacceptancestatusaccepted)Added [CKShareParticipantAcceptanceStatusPending](https://developer.apple.com/documentation/cloudkit/ckshare_participant_acceptancestatus/pending)Added [CKShareParticipantAcceptanceStatusRemoved](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus/ckshareparticipantacceptancestatusremoved)Added [CKShareParticipantAcceptanceStatusUnknown](https://developer.apple.com/documentation/cloudkit/ckshare_participant_acceptancestatus/unknown)Added [CKShareParticipantPermission](https://developer.apple.com/documentation/cloudkit/ckshare_participant_permission)Added [CKShareParticipantPermissionNone](https://developer.apple.com/documentation/cloudkit/ckshare_participant_permission/none)Added [CKShareParticipantPermissionReadOnly](https://developer.apple.com/documentation/cloudkit/ckshareparticipantpermission/ckshareparticipantpermissionreadonly)Added [CKShareParticipantPermissionReadWrite](https://developer.apple.com/documentation/cloudkit/ckshareparticipantpermission/ckshareparticipantpermissionreadwrite)Added [CKShareParticipantPermissionUnknown](https://developer.apple.com/documentation/cloudkit/ckshare_participant_permission/unknown)Added [CKShareParticipantType](https://developer.apple.com/documentation/cloudkit/ckshareparticipanttype)Added [CKShareParticipantTypeOwner](https://developer.apple.com/documentation/cloudkit/ckshareparticipanttype/ckshareparticipanttypeowner)Added [CKShareParticipantTypePrivateUser](https://developer.apple.com/documentation/cloudkit/ckshareparticipanttype/ckshareparticipanttypeprivateuser)Added [CKShareParticipantTypePublicUser](https://developer.apple.com/documentation/cloudkit/ckshareparticipanttype/ckshareparticipanttypepublicuser)Added [CKShareParticipantTypeUnknown](https://developer.apple.com/documentation/cloudkit/ckshare_participant_role/unknown)

#### CKSubscription.h

Added [CKDatabaseSubscription](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription)Added [-[CKDatabaseSubscription init]](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640456-init)Added [-[CKDatabaseSubscription initWithSubscriptionID:]](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640530-initwithsubscriptionid)Added [CKDatabaseSubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640418-recordtype)Added [CKQuerySubscription](https://developer.apple.com/documentation/cloudkit/ckquerysubscription)Added [-[CKQuerySubscription initWithRecordType:predicate:options:]](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640466-initwithrecordtype)Added [-[CKQuerySubscription initWithRecordType:predicate:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640505-initwithrecordtype)Added [CKQuerySubscription.predicate](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640485-predicate)Added [CKQuerySubscription.querySubscriptionOptions](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640414-querysubscriptionoptions)Added [CKQuerySubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640393-recordtype)Added [CKQuerySubscription.zoneID](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640390-zoneid)Added [CKRecordZoneSubscription](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription)Added [-[CKRecordZoneSubscription initWithZoneID:]](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640392-initwithzoneid)Added [-[CKRecordZoneSubscription initWithZoneID:subscriptionID:]](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640415-init)Added [CKRecordZoneSubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640479-recordtype)Added [CKRecordZoneSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640367-zoneid)Added [CKQuerySubscriptionOptions](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions)Added [CKQuerySubscriptionOptionsFiresOnce](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions/ckquerysubscriptionoptionsfiresonce)Added [CKQuerySubscriptionOptionsFiresOnRecordCreation](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions/ckquerysubscriptionoptionsfiresonrecordcreation)Added [CKQuerySubscriptionOptionsFiresOnRecordDeletion](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions/ckquerysubscriptionoptionsfiresonrecorddeletion)Added [CKQuerySubscriptionOptionsFiresOnRecordUpdate](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/1640369-firesonrecordupdate)Added CKSubscription(CKSubscriptionDeprecated)Added [CKSubscriptionTypeDatabase](https://developer.apple.com/documentation/cloudkit/cksubscriptiontype/cksubscriptiontypedatabase)Modified [-[CKSubscription initWithCoder:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515004-initwithcoder)

|  | Deprecation | Designated Initializer |
| --- | --- | --- |
| From | -- | yes |
| To | iOS 10.0 | -- |

Modified [-[CKSubscription initWithRecordType:predicate:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515132-initwithrecordtype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKSubscription initWithRecordType:predicate:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515265-initwithrecordtype)

|  | Deprecation | Designated Initializer |
| --- | --- | --- |
| From | -- | yes |
| To | iOS 10.0 | -- |

Modified [-[CKSubscription initWithZoneID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1514971-initwithzoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[CKSubscription initWithZoneID:subscriptionID:options:]](https://developer.apple.com/documentation/cloudkit/cksubscription/1515215-initwithzoneid)

|  | Deprecation | Designated Initializer |
| --- | --- | --- |
| From | -- | yes |
| To | iOS 10.0 | -- |

Modified [CKSubscription.predicate](https://developer.apple.com/documentation/cloudkit/cksubscription/1515219-predicate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscription.recordType](https://developer.apple.com/documentation/cloudkit/cksubscription/1515080-recordtype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscription.subscriptionOptions](https://developer.apple.com/documentation/cloudkit/cksubscription/1514922-subscriptionoptions)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/cksubscription/1514936-zoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscriptionOptionsFiresOnce](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonce)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscriptionOptionsFiresOnRecordCreation](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecordcreation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscriptionOptionsFiresOnRecordDeletion](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecorddeletion)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CKSubscriptionOptionsFiresOnRecordUpdate](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecordupdate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CKUserIdentity.h (Added)

Added [CKUserIdentity](https://developer.apple.com/documentation/cloudkit/ckuseridentity)Added [CKUserIdentity.hasiCloudAccount](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640513-hasicloudaccount)Added [CKUserIdentity.lookupInfo](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640371-lookupinfo)Added [CKUserIdentity.nameComponents](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640458-namecomponents)Added [CKUserIdentity.userRecordID](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640504-userrecordid)

#### CKUserIdentityLookupInfo.h (Added)

Added [CKUserIdentityLookupInfo](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo)Added [CKUserIdentityLookupInfo.emailAddress](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo/1640462-emailaddress)Added [-[CKUserIdentityLookupInfo initWithEmailAddress:]](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo/1640484-init)Added [-[CKUserIdentityLookupInfo initWithPhoneNumber:]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640402-initwithphonenumber)Added [-[CKUserIdentityLookupInfo initWithUserRecordID:]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640419-initwithuserrecordid)Added [+[CKUserIdentityLookupInfo lookupInfosWithEmails:]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640439-lookupinfoswithemails)Added [+[CKUserIdentityLookupInfo lookupInfosWithPhoneNumbers:]](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo/1640429-lookupinfos)Added [+[CKUserIdentityLookupInfo lookupInfosWithRecordIDs:]](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo/1640407-lookupinfos)Added [CKUserIdentityLookupInfo.phoneNumber](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640482-phonenumber)Added [CKUserIdentityLookupInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640405-userrecordid)

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
