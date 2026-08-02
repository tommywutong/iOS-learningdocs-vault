---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CloudKit.html
archived_at: '2026-07-18T02:51:04.268781Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CloudKit Changes for Swift

### CloudKit

Removed [CKSubscription.init(coder: NSCoder)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515004-initwithcoder)Added [CKAcceptSharesOperation](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation)Added [CKAcceptSharesOperation.acceptSharesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640442-acceptsharescompletionblock)Added [CKAcceptSharesOperation.init()](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640506-init)Added [CKAcceptSharesOperation.init(shareMetadatas: [CKShareMetadata])](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1823506-initwithsharemetadatas)Added [CKAcceptSharesOperation.perShareCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1640426-persharecompletionblock)Added [CKAcceptSharesOperation.shareMetadatas](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/1823508-sharemetadatas)Added [CKContainer.accept(_: CKShareMetadata, completionHandler: (CKShare, Error) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/2113667-acceptsharemetadata)Added [CKContainer.database(with: CKDatabaseScope) -> CKDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640475-database)Added [CKContainer.discoverAllIdentities(completionHandler: ([CKUserIdentity]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640421-discoverallidentitieswithcomplet)Added [CKContainer.discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640430-discoveruseridentity)Added [CKContainer.discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640516-discoveruseridentitywithphonenum)Added [CKContainer.discoverUserIdentity(withUserRecordID: CKRecordID, completionHandler: (CKUserIdentity?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640517-discoveruseridentitywithuserreco)Added [CKContainer.fetchShareMetadata(with: URL, completionHandler: (CKShareMetadata, Error) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/2113666-fetchsharemetadata)Added [CKContainer.fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShareParticipant, Error) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640489-fetchshareparticipant)Added [CKContainer.fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShareParticipant, Error) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640493-fetchshareparticipant)Added [CKContainer.fetchShareParticipant(withUserRecordID: CKRecordID, completionHandler: (CKShareParticipant, Error) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640387-fetchshareparticipant)Added [CKContainer.sharedCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/1640408-sharedclouddatabase)Added [CKDatabase.databaseScope](https://developer.apple.com/documentation/cloudkit/ckdatabase/1640398-databasescope)Added [CKDatabaseNotification](https://developer.apple.com/documentation/cloudkit/ckdatabasenotification)Added [CKDatabaseNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckdatabasenotification/1640510-databasescope)Added [CKDatabaseScope [enum]](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope)Added [CKDatabaseScope.private](https://developer.apple.com/documentation/cloudkit/ckdatabasescope/ckdatabasescopeprivate)Added [CKDatabaseScope.public](https://developer.apple.com/documentation/cloudkit/ckdatabasescope/ckdatabasescopepublic)Added [CKDatabaseScope.shared](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/shared)Added [CKDatabaseSubscription](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription)Added [CKDatabaseSubscription.init()](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640456-init)Added [CKDatabaseSubscription.init(subscriptionID: String)](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640530-init)Added [CKDatabaseSubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/1640418-recordtype)Added [CKDiscoverAllUserIdentitiesOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation)Added [CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640497-discoveralluseridentitiescomplet)Added [CKDiscoverAllUserIdentitiesOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640435-init)Added [CKDiscoverAllUserIdentitiesOperation.userIdentityDiscoveredBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/1640416-useridentitydiscoveredblock)Added [CKDiscoverUserIdentitiesOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation)Added [CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640500-discoveruseridentitiescompletion)Added [CKDiscoverUserIdentitiesOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640525-init)Added [CKDiscoverUserIdentitiesOperation.init(userIdentityLookupInfos: [CKUserIdentityLookupInfo])](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640521-init)Added [CKDiscoverUserIdentitiesOperation.userIdentityDiscoveredBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640524-useridentitydiscoveredblock)Added [CKDiscoverUserIdentitiesOperation.userIdentityLookupInfos](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/1640450-useridentitylookupinfos)Added [CKError [struct]](https://developer.apple.com/documentation/cloudkit/ckerror)Added [CKError.alreadyShared](https://developer.apple.com/documentation/cloudkit/ckerror/2325196-alreadyshared)Added [CKError.ancestorRecord](https://developer.apple.com/documentation/cloudkit/ckerror/2299832-ancestorrecord)Added [CKError.assetFileModified](https://developer.apple.com/documentation/cloudkit/ckerror/2325217-assetfilemodified)Added [CKError.assetFileNotFound](https://developer.apple.com/documentation/cloudkit/ckerror/2325214-assetfilenotfound)Added [CKError.badContainer](https://developer.apple.com/documentation/cloudkit/ckerror/2325218-badcontainer)Added [CKError.badDatabase](https://developer.apple.com/documentation/cloudkit/ckerror/2325199-baddatabase)Added [CKError.batchRequestFailed](https://developer.apple.com/documentation/cloudkit/ckerror/2325195-batchrequestfailed)Added [CKError.changeTokenExpired](https://developer.apple.com/documentation/cloudkit/ckerror/2325216-changetokenexpired)Added [CKError.clientRecord](https://developer.apple.com/documentation/cloudkit/ckerror/2299848-clientrecord)Added [CKError.constraintViolation](https://developer.apple.com/documentation/cloudkit/ckerror/2325200-constraintviolation)Added [CKError.incompatibleVersion](https://developer.apple.com/documentation/cloudkit/ckerror/2325215-incompatibleversion)Added CKError.init(_nsError: NSError)Added [CKError.internalError](https://developer.apple.com/documentation/cloudkit/ckerror/2325203-internalerror)Added [CKError.invalidArguments](https://developer.apple.com/documentation/cloudkit/ckerror/2325210-invalidarguments)Added [CKError.limitExceeded](https://developer.apple.com/documentation/cloudkit/ckerror/2325211-limitexceeded)Added [CKError.managedAccountRestricted](https://developer.apple.com/documentation/cloudkit/ckerror/2325198-managedaccountrestricted)Added [CKError.missingEntitlement](https://developer.apple.com/documentation/cloudkit/ckerror/2325206-missingentitlement)Added [CKError.networkFailure](https://developer.apple.com/documentation/cloudkit/ckerror/2325207-networkfailure)Added [CKError.networkUnavailable](https://developer.apple.com/documentation/cloudkit/ckerror/2325209-networkunavailable)Added [CKError.notAuthenticated](https://developer.apple.com/documentation/cloudkit/ckerror/2325221-notauthenticated)Added [CKError.operationCancelled](https://developer.apple.com/documentation/cloudkit/ckerror/2325213-operationcancelled)Added CKError.partialErrorsByItemIDAdded [CKError.partialFailure](https://developer.apple.com/documentation/cloudkit/ckerror/2325226-partialfailure)Added [CKError.participantMayNeedVerification](https://developer.apple.com/documentation/cloudkit/ckerror/2325205-participantmayneedverification)Added [CKError.permissionFailure](https://developer.apple.com/documentation/cloudkit/ckerror/2325225-permissionfailure)Added [CKError.quotaExceeded](https://developer.apple.com/documentation/cloudkit/ckerror/2325197-quotaexceeded)Added [CKError.referenceViolation](https://developer.apple.com/documentation/cloudkit/ckerror/2325204-referenceviolation)Added [CKError.requestRateLimited](https://developer.apple.com/documentation/cloudkit/ckerror/2325202-requestratelimited)Added [CKError.resultsTruncated](https://developer.apple.com/documentation/cloudkit/ckerror/2325224-resultstruncated)Added [CKError.retryAfterSeconds](https://developer.apple.com/documentation/cloudkit/ckerror/2299866-retryafterseconds)Added [CKError.serverRecord](https://developer.apple.com/documentation/cloudkit/ckerror/2299836-serverrecord)Added [CKError.serverRecordChanged](https://developer.apple.com/documentation/cloudkit/ckerror/2325208-serverrecordchanged)Added [CKError.serverRejectedRequest](https://developer.apple.com/documentation/cloudkit/ckerror/2325219-serverrejectedrequest)Added [CKError.serviceUnavailable](https://developer.apple.com/documentation/cloudkit/ckerror/2325227-serviceunavailable)Added [CKError.tooManyParticipants](https://developer.apple.com/documentation/cloudkit/ckerror/2325201-toomanyparticipants)Added [CKError.unknownItem](https://developer.apple.com/documentation/cloudkit/ckerror/2325223-unknownitem)Added [CKError.userDeletedZone](https://developer.apple.com/documentation/cloudkit/ckerror/2325212-userdeletedzone)Added [CKError.zoneBusy](https://developer.apple.com/documentation/cloudkit/ckerror/2325220-zonebusy)Added [CKError.zoneNotFound](https://developer.apple.com/documentation/cloudkit/ckerror/2325222-zonenotfound)Added [CKError.Code.alreadyShared](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerroralreadyshared)Added [CKError.Code.managedAccountRestricted](https://developer.apple.com/documentation/cloudkit/ckerror/code/managedaccountrestricted)Added [CKError.Code.participantMayNeedVerification](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorparticipantmayneedverification)Added [CKError.Code.referenceViolation](https://developer.apple.com/documentation/cloudkit/ckerror/code/referenceviolation)Added [CKError.Code.tooManyParticipants](https://developer.apple.com/documentation/cloudkit/ckerror/code/toomanyparticipants)Added [CKFetchDatabaseChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation)Added [CKFetchDatabaseChangesOperation.changeTokenUpdatedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640467-changetokenupdatedblock)Added [CKFetchDatabaseChangesOperation.fetchAllChanges](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640473-fetchallchanges)Added [CKFetchDatabaseChangesOperation.fetchDatabaseChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640434-fetchdatabasechangescompletionbl)Added [CKFetchDatabaseChangesOperation.init(previousServerChangeToken: CKServerChangeToken?)](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640502-initwithpreviousserverchangetoke)Added [CKFetchDatabaseChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640522-previousserverchangetoken)Added [CKFetchDatabaseChangesOperation.recordZoneWithIDChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640391-recordzonewithidchangedblock)Added [CKFetchDatabaseChangesOperation.recordZoneWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640428-recordzonewithidwasdeletedblock)Added [CKFetchDatabaseChangesOperation.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/1640520-resultslimit)Added [CKFetchRecordZoneChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation)Added [CKFetchRecordZoneChangesOperation.fetchAllChanges](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640386-fetchallchanges)Added [CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640409-fetchrecordzonechangescompletion)Added [CKFetchRecordZoneChangesOperation.init(recordZoneIDs: [CKRecordZoneID], optionsByRecordZoneID: [CKRecordZoneID : CKFetchRecordZoneChangesOptions]?)](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640509-initwithrecordzoneids)Added [CKFetchRecordZoneChangesOperation.optionsByRecordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640452-optionsbyrecordzoneid)Added [CKFetchRecordZoneChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640417-recordchangedblock)Added [CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640470-recordwithidwasdeletedblock)Added [CKFetchRecordZoneChangesOperation.recordZoneChangeTokensUpdatedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640422-recordzonechangetokensupdatedblo)Added [CKFetchRecordZoneChangesOperation.recordZoneFetchCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640411-recordzonefetchcompletionblock)Added [CKFetchRecordZoneChangesOperation.recordZoneIDs](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/1640463-recordzoneids)Added [CKFetchRecordZoneChangesOptions](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoptions)Added [CKFetchRecordZoneChangesOptions.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoptions/1640472-desiredkeys)Added [CKFetchRecordZoneChangesOptions.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoptions/1640389-previousserverchangetoken)Added [CKFetchRecordZoneChangesOptions.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoptions/1640481-resultslimit)Added [CKFetchShareMetadataOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation)Added [CKFetchShareMetadataOperation.fetchShareMetadataCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640457-fetchsharemetadatacompletionbloc)Added [CKFetchShareMetadataOperation.init(share: [URL])](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640495-init)Added [CKFetchShareMetadataOperation.perShareMetadataBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640447-persharemetadatablock)Added [CKFetchShareMetadataOperation.rootRecordDesiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640375-rootrecorddesiredkeys)Added [CKFetchShareMetadataOperation.shareURLs](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640508-shareurls)Added [CKFetchShareMetadataOperation.shouldFetchRootRecord](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/1640519-shouldfetchrootrecord)Added [CKFetchShareParticipantsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation)Added [CKFetchShareParticipantsOperation.fetchShareParticipantsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640529-fetchshareparticipantscompletion)Added [CKFetchShareParticipantsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640478-init)Added [CKFetchShareParticipantsOperation.init(userIdentityLookupInfos: [CKUserIdentityLookupInfo])](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640471-init)Added [CKFetchShareParticipantsOperation.shareParticipantFetchedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640451-shareparticipantfetchedblock)Added [CKFetchShareParticipantsOperation.userIdentityLookupInfos](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/1640380-useridentitylookupinfos)Added [CKMarkNotificationsReadOperation.init()](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1640383-init)Added [CKNotificationType.database](https://developer.apple.com/documentation/cloudkit/cknotificationtype/cknotificationtypedatabase)Added [CKOperation.timeoutIntervalForRequest](https://developer.apple.com/documentation/cloudkit/ckoperation/1639384-timeoutintervalforrequest)Added [CKOperation.timeoutIntervalForResource](https://developer.apple.com/documentation/cloudkit/ckoperation/1639386-timeoutintervalforresource)Added [CKQueryNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1640449-databasescope)Added [CKQuerySubscription](https://developer.apple.com/documentation/cloudkit/ckquerysubscription)Added [CKQuerySubscription.init(recordType: String, predicate: NSPredicate, options: CKQuerySubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640466-initwithrecordtype)Added [CKQuerySubscription.init(recordType: String, predicate: NSPredicate, subscriptionID: String, options: CKQuerySubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640505-initwithrecordtype)Added [CKQuerySubscription.predicate](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640485-predicate)Added [CKQuerySubscription.querySubscriptionOptions](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640414-querysubscriptionoptions)Added [CKQuerySubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640393-recordtype)Added [CKQuerySubscription.zoneID](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/1640390-zoneid)Added [CKQuerySubscriptionOptions [struct]](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions)Added [CKQuerySubscriptionOptions.firesOnce](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions/ckquerysubscriptionoptionsfiresonce)Added [CKQuerySubscriptionOptions.firesOnRecordCreation](https://developer.apple.com/documentation/cloudkit/ckquerysubscriptionoptions/ckquerysubscriptionoptionsfiresonrecordcreation)Added [CKQuerySubscriptionOptions.firesOnRecordDeletion](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/1640425-firesonrecorddeletion)Added [CKQuerySubscriptionOptions.firesOnRecordUpdate](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/1640369-firesonrecordupdate)Added [CKQuerySubscriptionOptions.init(rawValue: UInt)](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/1640404-init)Added [CKRecord.parent](https://developer.apple.com/documentation/cloudkit/ckrecord/1640527-parent)Added [CKRecord.setParent(_: CKRecordID?)](https://developer.apple.com/documentation/cloudkit/ckrecord/1690508-setparentreferencefromrecordid)Added [CKRecord.setParent(_: CKRecord?)](https://developer.apple.com/documentation/cloudkit/ckrecord/1690507-setparentreferencefromrecord)Added [CKRecord.share](https://developer.apple.com/documentation/cloudkit/ckrecord/1640378-share)Added [CKRecordZoneCapabilities.sharing](https://developer.apple.com/documentation/cloudkit/ckrecordzonecapabilities/ckrecordzonecapabilitysharing)Added [CKRecordZoneNotification.databaseScope](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification/1640394-databasescope)Added [CKRecordZoneSubscription](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription)Added [CKRecordZoneSubscription.init(zoneID: CKRecordZoneID)](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640392-initwithzoneid)Added [CKRecordZoneSubscription.init(zoneID: CKRecordZoneID, subscriptionID: String)](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640415-initwithzoneid)Added [CKRecordZoneSubscription.recordType](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640479-recordtype)Added [CKRecordZoneSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/1640367-zoneid)Added [CKShare](https://developer.apple.com/documentation/cloudkit/ckshare)Added [CKShare.addParticipant(_: CKShareParticipant)](https://developer.apple.com/documentation/cloudkit/ckshare/1640443-addparticipant)Added [CKShare.currentUserParticipant](https://developer.apple.com/documentation/cloudkit/ckshare/1640441-currentuserparticipant)Added [CKShare.init(coder: NSCoder)](https://developer.apple.com/documentation/cloudkit/ckshare/1640432-initwithcoder)Added [CKShare.init(rootRecord: CKRecord)](https://developer.apple.com/documentation/cloudkit/ckshare/1640448-initwithrootrecord)Added [CKShare.init(rootRecord: CKRecord, share: CKRecordID)](https://developer.apple.com/documentation/cloudkit/ckshare/1640381-initwithrootrecord)Added [CKShare.owner](https://developer.apple.com/documentation/cloudkit/ckshare/1640503-owner)Added [CKShare.participants](https://developer.apple.com/documentation/cloudkit/ckshare/1640453-participants)Added [CKShare.publicPermission](https://developer.apple.com/documentation/cloudkit/ckshare/1640494-publicpermission)Added [CKShare.removeParticipant(_: CKShareParticipant)](https://developer.apple.com/documentation/cloudkit/ckshare/1640523-removeparticipant)Added [CKShare.url](https://developer.apple.com/documentation/cloudkit/ckshare/1640465-url)Added [CKShareMetadata](https://developer.apple.com/documentation/cloudkit/ckshare/metadata)Added [CKShareMetadata.containerIdentifier](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640400-containeridentifier)Added [CKShareMetadata.ownerIdentity](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640498-owneridentity)Added [CKShareMetadata.participantPermission](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640483-participantpermission)Added [CKShareMetadata.participantStatus](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640420-participantstatus)Added [CKShareMetadata.participantType](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640518-participanttype)Added [CKShareMetadata.rootRecord](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640366-rootrecord)Added [CKShareMetadata.rootRecordID](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/1640410-rootrecordid)Added [CKShareMetadata.share](https://developer.apple.com/documentation/cloudkit/cksharemetadata/1640412-share)Added [CKShareParticipant](https://developer.apple.com/documentation/cloudkit/ckshare/participant)Added [CKShareParticipant.acceptanceStatus](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640395-acceptancestatus)Added [CKShareParticipant.permission](https://developer.apple.com/documentation/cloudkit/ckshare/participant/1640433-permission)Added [CKShareParticipant.type](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640507-type)Added [CKShareParticipant.userIdentity](https://developer.apple.com/documentation/cloudkit/ckshareparticipant/1640488-useridentity)Added [CKShareParticipantAcceptanceStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus)Added [CKShareParticipantAcceptanceStatus.accepted](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus/ckshareparticipantacceptancestatusaccepted)Added [CKShareParticipantAcceptanceStatus.pending](https://developer.apple.com/documentation/cloudkit/ckshareparticipantacceptancestatus/ckshareparticipantacceptancestatuspending)Added [CKShareParticipantAcceptanceStatus.removed](https://developer.apple.com/documentation/cloudkit/ckshare_participant_acceptancestatus/removed)Added [CKShareParticipantAcceptanceStatus.unknown](https://developer.apple.com/documentation/cloudkit/ckshare_participant_acceptancestatus/unknown)Added [CKShareParticipantPermission [enum]](https://developer.apple.com/documentation/cloudkit/ckshareparticipantpermission)Added [CKShareParticipantPermission.none](https://developer.apple.com/documentation/cloudkit/ckshare_participant_permission/none)Added [CKShareParticipantPermission.readOnly](https://developer.apple.com/documentation/cloudkit/ckshareparticipantpermission/ckshareparticipantpermissionreadonly)Added [CKShareParticipantPermission.readWrite](https://developer.apple.com/documentation/cloudkit/ckshare_participant_permission/readwrite)Added [CKShareParticipantPermission.unknown](https://developer.apple.com/documentation/cloudkit/ckshareparticipantpermission/ckshareparticipantpermissionunknown)Added [CKShareParticipantType [enum]](https://developer.apple.com/documentation/cloudkit/ckshare_participant_role)Added [CKShareParticipantType.owner](https://developer.apple.com/documentation/cloudkit/ckshare_participant_role/owner)Added [CKShareParticipantType.privateUser](https://developer.apple.com/documentation/cloudkit/ckshare_participant_role/privateuser)Added [CKShareParticipantType.publicUser](https://developer.apple.com/documentation/cloudkit/ckshare_participant_role/publicuser)Added [CKShareParticipantType.unknown](https://developer.apple.com/documentation/cloudkit/ckshareparticipanttype/ckshareparticipanttypeunknown)Added [CKSubscriptionType.database](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype/database)Added [CKUserIdentity](https://developer.apple.com/documentation/cloudkit/ckuseridentity)Added [CKUserIdentity.hasiCloudAccount](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640513-hasicloudaccount)Added [CKUserIdentity.lookupInfo](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640371-lookupinfo)Added [CKUserIdentity.nameComponents](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640458-namecomponents)Added [CKUserIdentity.userRecordID](https://developer.apple.com/documentation/cloudkit/ckuseridentity/1640504-userrecordid)Added [CKUserIdentityLookupInfo](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo)Added [CKUserIdentityLookupInfo.emailAddress](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640462-emailaddress)Added [CKUserIdentityLookupInfo.init(emailAddress: String)](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo/1640484-init)Added [CKUserIdentityLookupInfo.init(phoneNumber: String)](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640402-initwithphonenumber)Added [CKUserIdentityLookupInfo.init(userRecordID: CKRecordID)](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640419-initwithuserrecordid)Added [CKUserIdentityLookupInfo.lookupInfos(with: [CKRecordID]) -> [CKUserIdentityLookupInfo] [class]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640407-lookupinfoswithrecordids)Added [CKUserIdentityLookupInfo.lookupInfos(withEmails: [String]) -> [CKUserIdentityLookupInfo] [class]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640439-lookupinfoswithemails)Added [CKUserIdentityLookupInfo.lookupInfos(withPhoneNumbers: [String]) -> [CKUserIdentityLookupInfo] [class]](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640429-lookupinfoswithphonenumbers)Added [CKUserIdentityLookupInfo.phoneNumber](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640482-phonenumber)Added [CKUserIdentityLookupInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckuseridentitylookupinfo/1640405-userrecordid)Added [CKCurrentUserDefaultName](https://developer.apple.com/documentation/cloudkit/ckcurrentuserdefaultname)Added [CKRecordParentKey](https://developer.apple.com/documentation/cloudkit/ckrecordparentkey)Added [CKRecordShareKey](https://developer.apple.com/documentation/cloudkit/ckrecordsharekey)Added [CKRecordTypeShare](https://developer.apple.com/documentation/cloudkit/ckrecordtypeshare)Added [CKShareThumbnailImageDataKey](https://developer.apple.com/documentation/cloudkit/cksharethumbnailimagedatakey)Added [CKShareTitleKey](https://developer.apple.com/documentation/cloudkit/cksharetitlekey)Added [CKShareTypeKey](https://developer.apple.com/documentation/cloudkit/cksharetypekey)Modified [CKAccountStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckaccountstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CKAccountStatus : Int {     case CouldNotDetermine     case Available     case Restricted     case NoAccount } ``` |
| To | ``` enum CKAccountStatus : Int {     case couldNotDetermine     case available     case restricted     case noAccount } ``` |

Modified [CKAccountStatus.available](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/ckaccountstatusavailable)

|  | Declaration |
| --- | --- |
| From | ``` case Available ``` |
| To | ``` case available ``` |

Modified [CKAccountStatus.couldNotDetermine](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/ckaccountstatuscouldnotdetermine)

|  | Declaration |
| --- | --- |
| From | ``` case CouldNotDetermine ``` |
| To | ``` case couldNotDetermine ``` |

Modified [CKAccountStatus.noAccount](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/noaccount)

|  | Declaration |
| --- | --- |
| From | ``` case NoAccount ``` |
| To | ``` case noAccount ``` |

Modified [CKAccountStatus.restricted](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/ckaccountstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [CKApplicationPermissions [struct]](https://developer.apple.com/documentation/cloudkit/ckcontainer_application_permissions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKApplicationPermissions : OptionSetType {     init(rawValue rawValue: UInt)     static var UserDiscoverability: CKApplicationPermissions { get } } ``` | OptionSetType |
| To | ``` struct CKApplicationPermissions : OptionSet {     init(rawValue rawValue: UInt)     static var userDiscoverability: CKApplicationPermissions { get }     func intersect(_ other: CKApplicationPermissions) -> CKApplicationPermissions     func exclusiveOr(_ other: CKApplicationPermissions) -> CKApplicationPermissions     mutating func unionInPlace(_ other: CKApplicationPermissions)     mutating func intersectInPlace(_ other: CKApplicationPermissions)     mutating func exclusiveOrInPlace(_ other: CKApplicationPermissions)     func isSubsetOf(_ other: CKApplicationPermissions) -> Bool     func isDisjointWith(_ other: CKApplicationPermissions) -> Bool     func isSupersetOf(_ other: CKApplicationPermissions) -> Bool     mutating func subtractInPlace(_ other: CKApplicationPermissions)     func isStrictSupersetOf(_ other: CKApplicationPermissions) -> Bool     func isStrictSubsetOf(_ other: CKApplicationPermissions) -> Bool } extension CKApplicationPermissions {     func union(_ other: CKApplicationPermissions) -> CKApplicationPermissions     func intersection(_ other: CKApplicationPermissions) -> CKApplicationPermissions     func symmetricDifference(_ other: CKApplicationPermissions) -> CKApplicationPermissions } extension CKApplicationPermissions {     func contains(_ member: CKApplicationPermissions) -> Bool     mutating func insert(_ newMember: CKApplicationPermissions) -> (inserted: Bool, memberAfterInsert: CKApplicationPermissions)     mutating func remove(_ member: CKApplicationPermissions) -> CKApplicationPermissions?     mutating func update(with newMember: CKApplicationPermissions) -> CKApplicationPermissions? } extension CKApplicationPermissions {     convenience init()     mutating func formUnion(_ other: CKApplicationPermissions)     mutating func formIntersection(_ other: CKApplicationPermissions)     mutating func formSymmetricDifference(_ other: CKApplicationPermissions) } extension CKApplicationPermissions {     convenience init<S : Sequence where S.Iterator.Element == CKApplicationPermissions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CKApplicationPermissions...)     mutating func subtract(_ other: CKApplicationPermissions)     func isSubset(of other: CKApplicationPermissions) -> Bool     func isSuperset(of other: CKApplicationPermissions) -> Bool     func isDisjoint(with other: CKApplicationPermissions) -> Bool     func subtracting(_ other: CKApplicationPermissions) -> CKApplicationPermissions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CKApplicationPermissions) -> Bool     func isStrictSubset(of other: CKApplicationPermissions) -> Bool } ``` | OptionSet |

Modified [CKApplicationPermissions.userDiscoverability](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissions/ckapplicationpermissionuserdiscoverability)

|  | Declaration |
| --- | --- |
| From | ``` static var UserDiscoverability: CKApplicationPermissions { get } ``` |
| To | ``` static var userDiscoverability: CKApplicationPermissions { get } ``` |

Modified [CKApplicationPermissionStatus [enum]](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CKApplicationPermissionStatus : Int {     case InitialState     case CouldNotComplete     case Denied     case Granted } ``` |
| To | ``` enum CKApplicationPermissionStatus : Int {     case initialState     case couldNotComplete     case denied     case granted } ``` |

Modified [CKApplicationPermissionStatus.couldNotComplete](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionstatus/ckapplicationpermissionstatuscouldnotcomplete)

|  | Declaration |
| --- | --- |
| From | ``` case CouldNotComplete ``` |
| To | ``` case couldNotComplete ``` |

Modified [CKApplicationPermissionStatus.denied](https://developer.apple.com/documentation/cloudkit/ckcontainer_application_permissionstatus/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [CKApplicationPermissionStatus.granted](https://developer.apple.com/documentation/cloudkit/ckcontainer_application_permissionstatus/granted)

|  | Declaration |
| --- | --- |
| From | ``` case Granted ``` |
| To | ``` case granted ``` |

Modified [CKApplicationPermissionStatus.initialState](https://developer.apple.com/documentation/cloudkit/ckcontainer_application_permissionstatus/initialstate)

|  | Declaration |
| --- | --- |
| From | ``` case InitialState ``` |
| To | ``` case initialState ``` |

Modified [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKAsset : NSObject {     init()     init(fileURL fileURL: NSURL)     @NSCopying var fileURL: NSURL { get } } extension CKAsset : CKRecordValue { } ``` | CKRecordValue |
| To | ``` class CKAsset : NSObject {     init()     init(fileURL fileURL: URL)     var fileURL: URL { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKAsset : CVarArg { } extension CKAsset : Equatable, Hashable {     var hashValue: Int { get } } extension CKAsset : CKRecordValue { } ``` | CKRecordValue, CVarArg, Equatable, Hashable |

Modified [CKAsset.fileURL](https://developer.apple.com/documentation/cloudkit/ckasset/1515050-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fileURL: NSURL { get } ``` |
| To | ``` var fileURL: URL { get } ``` |

Modified [CKAsset.init(fileURL: URL)](https://developer.apple.com/documentation/cloudkit/ckasset/1514990-initwithfileurl)

|  | Declaration |
| --- | --- |
| From | ``` init(fileURL fileURL: NSURL) ``` |
| To | ``` init(fileURL fileURL: URL) ``` |

Modified [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKContainer : NSObject {     init()     class func defaultContainer() -> CKContainer      init(identifier containerIdentifier: String)     class func containerWithIdentifier(_ containerIdentifier: String) -> CKContainer     var containerIdentifier: String? { get }     func addOperation(_ operation: CKOperation) } extension CKContainer {     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get } } extension CKContainer {     func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) } extension CKContainer {     func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) } extension CKContainer {     func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void)     func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void)     func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void)     func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) } extension CKContainer {     func fetchAllLongLivedOperationIDsWithCompletionHandler(_ completionHandler: ([String]?, NSError?) -> Void)     func fetchLongLivedOperationWithID(_ operationID: String, completionHandler completionHandler: (CKOperation?, NSError?) -> Void) } ``` | -- |
| To | ``` class CKContainer : NSObject {     init()     class func `default`() -> CKContainer      init(identifier containerIdentifier: String)     class func withIdentifier(_ containerIdentifier: String) -> CKContainer     var containerIdentifier: String? { get }     func add(_ operation: CKOperation)     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get }     var sharedCloudDatabase: CKDatabase { get }     func database(with databaseScope: CKDatabaseScope) -> CKDatabase     func accountStatus(completionHandler completionHandler: @escaping (CKAccountStatus, Error?) -> Swift.Void)     func status(forApplicationPermission applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock)     func fetchUserRecordID(completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void)     func discoverAllIdentities(completionHandler completionHandler: @escaping ([CKUserIdentity]?, Error?) -> Swift.Void)     func discoverUserIdentity(withEmailAddress email: String, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverUserIdentity(withPhoneNumber phoneNumber: String, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverUserIdentity(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverAllContactUserInfos(completionHandler completionHandler: @escaping ([CKDiscoveredUserInfo]?, Error?) -> Swift.Void)     func discoverUserInfo(withEmailAddress email: String, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void)     func discoverUserInfo(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void)     func fetchShareParticipant(withEmailAddress emailAddress: String, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareParticipant(withPhoneNumber phoneNumber: String, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareParticipant(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareMetadata(with url: URL, completionHandler completionHandler: @escaping (CKShareMetadata, Error) -> Swift.Void)     func accept(_ metadata: CKShareMetadata, completionHandler completionHandler: @escaping (CKShare, Error) -> Swift.Void)     func fetchAllLongLivedOperationIDs(completionHandler completionHandler: @escaping ([String]?, Error?) -> Swift.Void)     func fetchLongLivedOperation(withID operationID: String, completionHandler completionHandler: @escaping (CKOperation?, Error?) -> Swift.Void)     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension CKContainer : CVarArg { } extension CKContainer : Equatable, Hashable {     var hashValue: Int { get } } extension CKContainer {     var privateCloudDatabase: CKDatabase { get }     var publicCloudDatabase: CKDatabase { get }     var sharedCloudDatabase: CKDatabase { get }     func database(with databaseScope: CKDatabaseScope) -> CKDatabase } extension CKContainer {     func accountStatus(completionHandler completionHandler: @escaping (CKAccountStatus, Error?) -> Swift.Void) } extension CKContainer {     func status(forApplicationPermission applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock)     func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock) } extension CKContainer {     func fetchUserRecordID(completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void)     func discoverAllIdentities(completionHandler completionHandler: @escaping ([CKUserIdentity]?, Error?) -> Swift.Void)     func discoverUserIdentity(withEmailAddress email: String, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverUserIdentity(withPhoneNumber phoneNumber: String, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverUserIdentity(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKUserIdentity?, Error?) -> Swift.Void)     func discoverAllContactUserInfos(completionHandler completionHandler: @escaping ([CKDiscoveredUserInfo]?, Error?) -> Swift.Void)     func discoverUserInfo(withEmailAddress email: String, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void)     func discoverUserInfo(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void) } extension CKContainer {     func fetchShareParticipant(withEmailAddress emailAddress: String, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareParticipant(withPhoneNumber phoneNumber: String, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareParticipant(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKShareParticipant, Error) -> Swift.Void)     func fetchShareMetadata(with url: URL, completionHandler completionHandler: @escaping (CKShareMetadata, Error) -> Swift.Void)     func accept(_ metadata: CKShareMetadata, completionHandler completionHandler: @escaping (CKShare, Error) -> Swift.Void) } extension CKContainer {     func fetchAllLongLivedOperationIDs(completionHandler completionHandler: @escaping ([String]?, Error?) -> Swift.Void)     func fetchLongLivedOperation(withID operationID: String, completionHandler completionHandler: @escaping (CKOperation?, Error?) -> Swift.Void) } ``` | CVarArg, Equatable, Hashable |

Modified [CKContainer.accountStatus(completionHandler: (CKAccountStatus, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399180-accountstatuswithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func accountStatusWithCompletionHandler(_ completionHandler: (CKAccountStatus, NSError?) -> Void) ``` |
| To | ``` func accountStatus(completionHandler completionHandler: @escaping (CKAccountStatus, Error?) -> Swift.Void) ``` |

Modified [CKContainer.add(_: CKOperation)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399215-addoperation)

|  | Declaration |
| --- | --- |
| From | ``` func addOperation(_ operation: CKOperation) ``` |
| To | ``` func add(_ operation: CKOperation) ``` |

Modified [CKContainer.default() [class]](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399189-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultContainer() -> CKContainer ``` |
| To | ``` class func `default`() -> CKContainer ``` |

Modified [CKContainer.discoverAllContactUserInfos(completionHandler: ([CKDiscoveredUserInfo]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399199-discoverallcontactuserinfoswithc)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func discoverAllContactUserInfosWithCompletionHandler(_ completionHandler: ([CKDiscoveredUserInfo]?, NSError?) -> Void) ``` | -- |
| To | ``` func discoverAllContactUserInfos(completionHandler completionHandler: @escaping ([CKDiscoveredUserInfo]?, Error?) -> Swift.Void) ``` | OS X 10.12 |

Modified [CKContainer.discoverUserInfo(withEmailAddress: String, completionHandler: (CKDiscoveredUserInfo?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399201-discoveruserinfowithemailaddress)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func discoverUserInfoWithEmailAddress(_ email: String, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) ``` | -- |
| To | ``` func discoverUserInfo(withEmailAddress email: String, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void) ``` | OS X 10.12 |

Modified [CKContainer.discoverUserInfo(withUserRecordID: CKRecordID, completionHandler: (CKDiscoveredUserInfo?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399217-discoveruserinfowithuserrecordid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func discoverUserInfoWithUserRecordID(_ userRecordID: CKRecordID, completionHandler completionHandler: (CKDiscoveredUserInfo?, NSError?) -> Void) ``` | -- |
| To | ``` func discoverUserInfo(withUserRecordID userRecordID: CKRecordID, completionHandler completionHandler: @escaping (CKDiscoveredUserInfo?, Error?) -> Swift.Void) ``` | OS X 10.12 |

Modified [CKContainer.fetchAllLongLivedOperationIDs(completionHandler: ([String]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399160-fetchalllonglivedoperationidswit)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fetchAllLongLivedOperationIDsWithCompletionHandler(_ completionHandler: ([String]?, NSError?) -> Void) ``` | OS X 10.11.4 |
| To | ``` func fetchAllLongLivedOperationIDs(completionHandler completionHandler: @escaping ([String]?, Error?) -> Swift.Void) ``` | OS X 10.12 |

Modified [CKContainer.fetchLongLivedOperation(withID: String, completionHandler: (CKOperation?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399164-fetchlonglivedoperationwithid)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fetchLongLivedOperationWithID(_ operationID: String, completionHandler completionHandler: (CKOperation?, NSError?) -> Void) ``` | OS X 10.11.4 |
| To | ``` func fetchLongLivedOperation(withID operationID: String, completionHandler completionHandler: @escaping (CKOperation?, Error?) -> Swift.Void) ``` | OS X 10.12 |

Modified [CKContainer.fetchUserRecordID(completionHandler: (CKRecordID?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399191-fetchuserrecordidwithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func fetchUserRecordIDWithCompletionHandler(_ completionHandler: (CKRecordID?, NSError?) -> Void) ``` |
| To | ``` func fetchUserRecordID(completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void) ``` |

Modified [CKContainer.requestApplicationPermission(_: CKApplicationPermissions, completionHandler: CloudKit.CKApplicationPermissionBlock)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399174-requestapplicationpermission)

|  | Declaration |
| --- | --- |
| From | ``` func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) ``` |
| To | ``` func requestApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock) ``` |

Modified [CKContainer.status(forApplicationPermission: CKApplicationPermissions, completionHandler: CloudKit.CKApplicationPermissionBlock)](https://developer.apple.com/documentation/cloudkit/ckcontainer/1399195-status)

|  | Declaration |
| --- | --- |
| From | ``` func statusForApplicationPermission(_ applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CKApplicationPermissionBlock) ``` |
| To | ``` func status(forApplicationPermission applicationPermission: CKApplicationPermissions, completionHandler completionHandler: CloudKit.CKApplicationPermissionBlock) ``` |

Modified [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKDatabase : NSObject {     init()     func addOperation(_ operation: CKDatabaseOperation) } extension CKDatabase {     func fetchRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecord?, NSError?) -> Void)     func saveRecord(_ record: CKRecord, completionHandler completionHandler: (CKRecord?, NSError?) -> Void)     func deleteRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecordID?, NSError?) -> Void)     func performQuery(_ query: CKQuery, inZoneWithID zoneID: CKRecordZoneID?, completionHandler completionHandler: ([CKRecord]?, NSError?) -> Void)     func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: ([CKRecordZone]?, NSError?) -> Void)     func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void)     func saveRecordZone(_ zone: CKRecordZone, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void)     func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZoneID?, NSError?) -> Void)     func fetchSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void)     func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: ([CKSubscription]?, NSError?) -> Void)     func saveSubscription(_ subscription: CKSubscription, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void)     func deleteSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (String?, NSError?) -> Void) } ``` | -- |
| To | ``` class CKDatabase : NSObject {     init()     func add(_ operation: CKDatabaseOperation)     var databaseScope: CKDatabaseScope { get }     func fetch(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void)     func save(_ record: CKRecord, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void)     func delete(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void)     func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZoneID?, completionHandler completionHandler: @escaping ([CKRecord]?, Error?) -> Swift.Void)     func fetchAllRecordZones(completionHandler completionHandler: @escaping ([CKRecordZone]?, Error?) -> Swift.Void)     func fetch(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void)     func save(_ zone: CKRecordZone, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void)     func delete(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZoneID?, Error?) -> Swift.Void)     func fetch(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void)     func fetchAllSubscriptions(completionHandler completionHandler: @escaping ([CKSubscription]?, Error?) -> Swift.Void)     func save(_ subscription: CKSubscription, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void)     func delete(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (String?, Error?) -> Swift.Void)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKDatabase : CVarArg { } extension CKDatabase : Equatable, Hashable {     var hashValue: Int { get } } extension CKDatabase {     func fetch(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void)     func save(_ record: CKRecord, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void)     func delete(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void)     func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZoneID?, completionHandler completionHandler: @escaping ([CKRecord]?, Error?) -> Swift.Void)     func fetchAllRecordZones(completionHandler completionHandler: @escaping ([CKRecordZone]?, Error?) -> Swift.Void)     func fetch(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void)     func save(_ zone: CKRecordZone, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void)     func delete(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZoneID?, Error?) -> Swift.Void)     func fetch(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void)     func fetchAllSubscriptions(completionHandler completionHandler: @escaping ([CKSubscription]?, Error?) -> Swift.Void)     func save(_ subscription: CKSubscription, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void)     func delete(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (String?, Error?) -> Swift.Void) } ``` | CVarArg, Equatable, Hashable |

Modified [CKDatabase.add(_: CKDatabaseOperation)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449116-addoperation)

|  | Declaration |
| --- | --- |
| From | ``` func addOperation(_ operation: CKDatabaseOperation) ``` |
| To | ``` func add(_ operation: CKDatabaseOperation) ``` |

Modified [CKDatabase.delete(withRecordID: CKRecordID, completionHandler: (CKRecordID?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449122-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecordID?, NSError?) -> Void) ``` |
| To | ``` func delete(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecordID?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.delete(withRecordZoneID: CKRecordZoneID, completionHandler: (CKRecordZoneID?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449118-deleterecordzonewithid)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZoneID?, NSError?) -> Void) ``` |
| To | ``` func delete(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZoneID?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.delete(withSubscriptionID: String, completionHandler: (String?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449120-deletesubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (String?, NSError?) -> Void) ``` |
| To | ``` func delete(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (String?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.fetch(withRecordID: CKRecordID, completionHandler: (CKRecord?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449126-fetchrecordwithid)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRecordWithID(_ recordID: CKRecordID, completionHandler completionHandler: (CKRecord?, NSError?) -> Void) ``` |
| To | ``` func fetch(withRecordID recordID: CKRecordID, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.fetch(withRecordZoneID: CKRecordZoneID, completionHandler: (CKRecordZone?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449104-fetch)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRecordZoneWithID(_ zoneID: CKRecordZoneID, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void) ``` |
| To | ``` func fetch(withRecordZoneID zoneID: CKRecordZoneID, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.fetch(withSubscriptionID: String, completionHandler: (CKSubscription?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449106-fetchsubscriptionwithid)

|  | Declaration |
| --- | --- |
| From | ``` func fetchSubscriptionWithID(_ subscriptionID: String, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void) ``` |
| To | ``` func fetch(withSubscriptionID subscriptionID: String, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.fetchAllRecordZones(completionHandler: ([CKRecordZone]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449112-fetchallrecordzones)

|  | Declaration |
| --- | --- |
| From | ``` func fetchAllRecordZonesWithCompletionHandler(_ completionHandler: ([CKRecordZone]?, NSError?) -> Void) ``` |
| To | ``` func fetchAllRecordZones(completionHandler completionHandler: @escaping ([CKRecordZone]?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.fetchAllSubscriptions(completionHandler: ([CKSubscription]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449110-fetchallsubscriptionswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func fetchAllSubscriptionsWithCompletionHandler(_ completionHandler: ([CKSubscription]?, NSError?) -> Void) ``` |
| To | ``` func fetchAllSubscriptions(completionHandler completionHandler: @escaping ([CKSubscription]?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.perform(_: CKQuery, inZoneWith: CKRecordZoneID?, completionHandler: ([CKRecord]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449127-performquery)

|  | Declaration |
| --- | --- |
| From | ``` func performQuery(_ query: CKQuery, inZoneWithID zoneID: CKRecordZoneID?, completionHandler completionHandler: ([CKRecord]?, NSError?) -> Void) ``` |
| To | ``` func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZoneID?, completionHandler completionHandler: @escaping ([CKRecord]?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.save(_: CKSubscription, completionHandler: (CKSubscription?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449102-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveSubscription(_ subscription: CKSubscription, completionHandler completionHandler: (CKSubscription?, NSError?) -> Void) ``` |
| To | ``` func save(_ subscription: CKSubscription, completionHandler completionHandler: @escaping (CKSubscription?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.save(_: CKRecord, completionHandler: (CKRecord?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449114-saverecord)

|  | Declaration |
| --- | --- |
| From | ``` func saveRecord(_ record: CKRecord, completionHandler completionHandler: (CKRecord?, NSError?) -> Void) ``` |
| To | ``` func save(_ record: CKRecord, completionHandler completionHandler: @escaping (CKRecord?, Error?) -> Swift.Void) ``` |

Modified [CKDatabase.save(_: CKRecordZone, completionHandler: (CKRecordZone?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cloudkit/ckdatabase/1449108-saverecordzone)

|  | Declaration |
| --- | --- |
| From | ``` func saveRecordZone(_ zone: CKRecordZone, completionHandler completionHandler: (CKRecordZone?, NSError?) -> Void) ``` |
| To | ``` func save(_ zone: CKRecordZone, completionHandler completionHandler: @escaping (CKRecordZone?, Error?) -> Swift.Void) ``` |

Modified [CKDiscoverAllContactsOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class CKDiscoverAllContactsOperation : CKOperation {     init()     var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, NSError?) -> Void)? } ``` | -- |
| To | ``` class CKDiscoverAllContactsOperation : CKOperation {     init()     var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, Error?) -> Swift.Void)? } ``` | OS X 10.12 |

Modified [CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1515099-discoverallcontactscompletionblo)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, NSError?) -> Void)? ``` | -- |
| To | ``` var discoverAllContactsCompletionBlock: (([CKDiscoveredUserInfo]?, Error?) -> Swift.Void)? ``` | OS X 10.12 |

Modified [CKDiscoverAllContactsOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoverallcontactsoperation/1514998-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoveredUserInfo](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo)

|  | Declaration | Protocols | Deprecation |
| --- | --- | --- | --- |
| From | ``` class CKDiscoveredUserInfo : NSObject {     init()     @NSCopying var userRecordID: CKRecordID? { get }     var firstName: String? { get }     var lastName: String? { get }     @NSCopying var displayContact: CNContact? { get } } ``` | -- | -- |
| To | ``` class CKDiscoveredUserInfo : NSObject {     init()     @NSCopying var userRecordID: CKRecordID? { get }     var firstName: String? { get }     var lastName: String? { get }     @NSCopying var displayContact: CNContact? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKDiscoveredUserInfo : CVarArg { } extension CKDiscoveredUserInfo : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | OS X 10.12 |

Modified [CKDiscoveredUserInfo.displayContact](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436518-displaycontact)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoveredUserInfo.userRecordID](https://developer.apple.com/documentation/cloudkit/ckdiscovereduserinfo/1436516-userrecordid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class CKDiscoverUserInfosOperation : CKOperation {     init()     convenience init(emailAddresses emailAddresses: [String]?, userRecordIDs userRecordIDs: [CKRecordID]?)     var emailAddresses: [String]?     var userRecordIDs: [CKRecordID]?     var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, NSError?) -> Void)? } ``` | -- |
| To | ``` class CKDiscoverUserInfosOperation : CKOperation {     init()     convenience init(emailAddresses emailAddresses: [String]?, userRecordIDs userRecordIDs: [CKRecordID]?)     var emailAddresses: [String]?     var userRecordIDs: [CKRecordID]?     var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, Error?) -> Swift.Void)? } ``` | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403386-discoveruserinfoscompletionblock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, NSError?) -> Void)? ``` | -- |
| To | ``` var discoverUserInfosCompletionBlock: (([String : CKDiscoveredUserInfo]?, [CKRecordID : CKDiscoveredUserInfo]?, Error?) -> Swift.Void)? ``` | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation.emailAddresses](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403382-emailaddresses)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation.init()](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403380-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation.init(emailAddresses: [String]?, userRecordIDs: [CKRecordID]?)](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403391-initwithemailaddresses)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKDiscoverUserInfosOperation.userRecordIDs](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation/1403384-userrecordids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKError.Code [enum]](https://developer.apple.com/documentation/cloudkit/ckerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum CKErrorCode : Int {     case InternalError     case PartialFailure     case NetworkUnavailable     case NetworkFailure     case BadContainer     case ServiceUnavailable     case RequestRateLimited     case MissingEntitlement     case NotAuthenticated     case PermissionFailure     case UnknownItem     case InvalidArguments     case ResultsTruncated     case ServerRecordChanged     case ServerRejectedRequest     case AssetFileNotFound     case AssetFileModified     case IncompatibleVersion     case ConstraintViolation     case OperationCancelled     case ChangeTokenExpired     case BatchRequestFailed     case ZoneBusy     case BadDatabase     case QuotaExceeded     case ZoneNotFound     case LimitExceeded     case UserDeletedZone } extension CKErrorCode : _BridgedNSError { } extension CKErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = CKError         case internalError         case partialFailure         case networkUnavailable         case networkFailure         case badContainer         case serviceUnavailable         case requestRateLimited         case missingEntitlement         case notAuthenticated         case permissionFailure         case unknownItem         case invalidArguments         case resultsTruncated         case serverRecordChanged         case serverRejectedRequest         case assetFileNotFound         case assetFileModified         case incompatibleVersion         case constraintViolation         case operationCancelled         case changeTokenExpired         case batchRequestFailed         case zoneBusy         case badDatabase         case quotaExceeded         case zoneNotFound         case limitExceeded         case userDeletedZone         case tooManyParticipants         case alreadyShared         case referenceViolation         case managedAccountRestricted         case participantMayNeedVerification     } ``` |

Modified [CKError.Code.assetFileModified](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorassetfilemodified)

|  | Declaration |
| --- | --- |
| From | ``` case AssetFileModified ``` |
| To | ``` case assetFileModified ``` |

Modified [CKError.Code.assetFileNotFound](https://developer.apple.com/documentation/cloudkit/ckerror/code/assetfilenotfound)

|  | Declaration |
| --- | --- |
| From | ``` case AssetFileNotFound ``` |
| To | ``` case assetFileNotFound ``` |

Modified [CKError.Code.badContainer](https://developer.apple.com/documentation/cloudkit/ckerror/code/badcontainer)

|  | Declaration |
| --- | --- |
| From | ``` case BadContainer ``` |
| To | ``` case badContainer ``` |

Modified [CKError.Code.badDatabase](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorbaddatabase)

|  | Declaration |
| --- | --- |
| From | ``` case BadDatabase ``` |
| To | ``` case badDatabase ``` |

Modified [CKError.Code.batchRequestFailed](https://developer.apple.com/documentation/cloudkit/ckerror/code/batchrequestfailed)

|  | Declaration |
| --- | --- |
| From | ``` case BatchRequestFailed ``` |
| To | ``` case batchRequestFailed ``` |

Modified [CKError.Code.changeTokenExpired](https://developer.apple.com/documentation/cloudkit/ckerror/code/changetokenexpired)

|  | Declaration |
| --- | --- |
| From | ``` case ChangeTokenExpired ``` |
| To | ``` case changeTokenExpired ``` |

Modified [CKError.Code.constraintViolation](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorconstraintviolation)

|  | Declaration |
| --- | --- |
| From | ``` case ConstraintViolation ``` |
| To | ``` case constraintViolation ``` |

Modified [CKError.Code.incompatibleVersion](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorincompatibleversion)

|  | Declaration |
| --- | --- |
| From | ``` case IncompatibleVersion ``` |
| To | ``` case incompatibleVersion ``` |

Modified [CKError.Code.internalError](https://developer.apple.com/documentation/cloudkit/ckerror/code/internalerror)

|  | Declaration |
| --- | --- |
| From | ``` case InternalError ``` |
| To | ``` case internalError ``` |

Modified [CKError.Code.invalidArguments](https://developer.apple.com/documentation/cloudkit/ckerror/code/invalidarguments)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidArguments ``` |
| To | ``` case invalidArguments ``` |

Modified [CKError.Code.limitExceeded](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorlimitexceeded)

|  | Declaration |
| --- | --- |
| From | ``` case LimitExceeded ``` |
| To | ``` case limitExceeded ``` |

Modified [CKError.Code.missingEntitlement](https://developer.apple.com/documentation/cloudkit/ckerror/code/missingentitlement)

|  | Declaration |
| --- | --- |
| From | ``` case MissingEntitlement ``` |
| To | ``` case missingEntitlement ``` |

Modified [CKError.Code.networkFailure](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrornetworkfailure)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkFailure ``` |
| To | ``` case networkFailure ``` |

Modified [CKError.Code.networkUnavailable](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrornetworkunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkUnavailable ``` |
| To | ``` case networkUnavailable ``` |

Modified [CKError.Code.notAuthenticated](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrornotauthenticated)

|  | Declaration |
| --- | --- |
| From | ``` case NotAuthenticated ``` |
| To | ``` case notAuthenticated ``` |

Modified [CKError.Code.operationCancelled](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerroroperationcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case OperationCancelled ``` |
| To | ``` case operationCancelled ``` |

Modified [CKError.Code.partialFailure](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorpartialfailure)

|  | Declaration |
| --- | --- |
| From | ``` case PartialFailure ``` |
| To | ``` case partialFailure ``` |

Modified [CKError.Code.permissionFailure](https://developer.apple.com/documentation/cloudkit/ckerror/code/permissionfailure)

|  | Declaration |
| --- | --- |
| From | ``` case PermissionFailure ``` |
| To | ``` case permissionFailure ``` |

Modified [CKError.Code.quotaExceeded](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorquotaexceeded)

|  | Declaration |
| --- | --- |
| From | ``` case QuotaExceeded ``` |
| To | ``` case quotaExceeded ``` |

Modified [CKError.Code.requestRateLimited](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorrequestratelimited)

|  | Declaration |
| --- | --- |
| From | ``` case RequestRateLimited ``` |
| To | ``` case requestRateLimited ``` |

Modified [CKError.Code.resultsTruncated](https://developer.apple.com/documentation/cloudkit/ckerror/code/resultstruncated)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` case ResultsTruncated ``` | -- |
| To | ``` case resultsTruncated ``` | OS X 10.12 |

Modified [CKError.Code.serverRecordChanged](https://developer.apple.com/documentation/cloudkit/ckerror/code/serverrecordchanged)

|  | Declaration |
| --- | --- |
| From | ``` case ServerRecordChanged ``` |
| To | ``` case serverRecordChanged ``` |

Modified [CKError.Code.serverRejectedRequest](https://developer.apple.com/documentation/cloudkit/ckerror/code/serverrejectedrequest)

|  | Declaration |
| --- | --- |
| From | ``` case ServerRejectedRequest ``` |
| To | ``` case serverRejectedRequest ``` |

Modified [CKError.Code.serviceUnavailable](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorserviceunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case ServiceUnavailable ``` |
| To | ``` case serviceUnavailable ``` |

Modified [CKError.Code.unknownItem](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorunknownitem)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownItem ``` |
| To | ``` case unknownItem ``` |

Modified [CKError.Code.userDeletedZone](https://developer.apple.com/documentation/cloudkit/ckerror/code/userdeletedzone)

|  | Declaration |
| --- | --- |
| From | ``` case UserDeletedZone ``` |
| To | ``` case userDeletedZone ``` |

Modified [CKError.Code.zoneBusy](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorzonebusy)

|  | Declaration |
| --- | --- |
| From | ``` case ZoneBusy ``` |
| To | ``` case zoneBusy ``` |

Modified [CKError.Code.zoneNotFound](https://developer.apple.com/documentation/cloudkit/ckerrorcode/ckerrorzonenotfound)

|  | Declaration |
| --- | --- |
| From | ``` case ZoneNotFound ``` |
| To | ``` case zoneNotFound ``` |

Modified [CKFetchNotificationChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchNotificationChangesOperation : CKOperation {     init(previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var moreComing: Bool { get }     var notificationChangedBlock: ((CKNotification) -> Void)?     var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, NSError?) -> Void)? } ``` |
| To | ``` class CKFetchNotificationChangesOperation : CKOperation {     init(previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var moreComing: Bool { get }     var notificationChangedBlock: ((CKNotification) -> Swift.Void)?     var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, Error?) -> Swift.Void)? } ``` |

Modified [CKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515125-fetchnotificationchangescompleti)

|  | Declaration |
| --- | --- |
| From | ``` var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, NSError?) -> Void)? ``` |
| To | ``` var fetchNotificationChangesCompletionBlock: ((CKServerChangeToken?, Error?) -> Swift.Void)? ``` |

Modified [CKFetchNotificationChangesOperation.notificationChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchnotificationchangesoperation/1515253-notificationchangedblock)

|  | Declaration |
| --- | --- |
| From | ``` var notificationChangedBlock: ((CKNotification) -> Void)? ``` |
| To | ``` var notificationChangedBlock: ((CKNotification) -> Swift.Void)? ``` |

Modified [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class CKFetchRecordChangesOperation : CKDatabaseOperation {     init(recordZoneID recordZoneID: CKRecordZoneID, previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var recordZoneID: CKRecordZoneID     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var desiredKeys: [String]?     var recordChangedBlock: ((CKRecord) -> Void)?     var recordWithIDWasDeletedBlock: ((CKRecordID) -> Void)?     var moreComing: Bool { get }     var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, NSData?, NSError?) -> Void)? } ``` | -- |
| To | ``` class CKFetchRecordChangesOperation : CKDatabaseOperation {     init(recordZoneID recordZoneID: CKRecordZoneID, previousServerChangeToken previousServerChangeToken: CKServerChangeToken?)     @NSCopying var recordZoneID: CKRecordZoneID     @NSCopying var previousServerChangeToken: CKServerChangeToken?     var resultsLimit: Int     var desiredKeys: [String]?     var recordChangedBlock: ((CKRecord) -> Swift.Void)?     var recordWithIDWasDeletedBlock: ((CKRecordID) -> Swift.Void)?     var moreComing: Bool { get }     var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, Error?) -> Swift.Void)? } ``` | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.desiredKeys](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515230-desiredkeys)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.fetchRecordChangesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515267-fetchrecordchangescompletionbloc)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, NSData?, NSError?) -> Void)? ``` | -- |
| To | ``` var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, Error?) -> Swift.Void)? ``` | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.init(recordZoneID: CKRecordZoneID, previousServerChangeToken: CKServerChangeToken?)](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515224-initwithrecordzoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.moreComing](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515322-morecoming)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.previousServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515209-previousserverchangetoken)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.recordChangedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515155-recordchangedblock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var recordChangedBlock: ((CKRecord) -> Void)? ``` | -- |
| To | ``` var recordChangedBlock: ((CKRecord) -> Swift.Void)? ``` | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.recordWithIDWasDeletedBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515054-recordwithidwasdeletedblock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var recordWithIDWasDeletedBlock: ((CKRecordID) -> Void)? ``` | -- |
| To | ``` var recordWithIDWasDeletedBlock: ((CKRecordID) -> Swift.Void)? ``` | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.recordZoneID](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1515018-recordzoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordChangesOperation.resultsLimit](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/1514891-resultslimit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKFetchRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordIDs recordIDs: [CKRecordID])     class func fetchCurrentUserRecordOperation() -> Self     var recordIDs: [CKRecordID]?     var desiredKeys: [String]?     var perRecordProgressBlock: ((CKRecordID, Double) -> Void)?     var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, NSError?) -> Void)?     var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, NSError?) -> Void)? } ``` |
| To | ``` class CKFetchRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordIDs recordIDs: [CKRecordID])     class func fetchCurrentUserRecordOperation() -> Self     var recordIDs: [CKRecordID]?     var desiredKeys: [String]?     var perRecordProgressBlock: ((CKRecordID, Double) -> Swift.Void)?     var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, Error?) -> Swift.Void)?     var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, Error?) -> Swift.Void)? } ``` |

Modified [CKFetchRecordsOperation.fetchRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476078-fetchrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, NSError?) -> Void)? ``` |
| To | ``` var fetchRecordsCompletionBlock: (([CKRecordID : CKRecord]?, Error?) -> Swift.Void)? ``` |

Modified [CKFetchRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476082-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, NSError?) -> Void)? ``` |
| To | ``` var perRecordCompletionBlock: ((CKRecord?, CKRecordID?, Error?) -> Swift.Void)? ``` |

Modified [CKFetchRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/1476080-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordProgressBlock: ((CKRecordID, Double) -> Void)? ``` |
| To | ``` var perRecordProgressBlock: ((CKRecordID, Double) -> Swift.Void)? ``` |

Modified [CKFetchRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchRecordZonesOperation : CKDatabaseOperation {     class func fetchAllRecordZonesOperation() -> Self     init()     convenience init(recordZoneIDs zoneIDs: [CKRecordZoneID])     var recordZoneIDs: [CKRecordZoneID]?     var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, NSError?) -> Void)? } ``` |
| To | ``` class CKFetchRecordZonesOperation : CKDatabaseOperation {     class func fetchAllRecordZonesOperation() -> Self     init()     convenience init(recordZoneIDs zoneIDs: [CKRecordZoneID])     var recordZoneIDs: [CKRecordZoneID]?     var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, Error?) -> Swift.Void)? } ``` |

Modified [CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/1515145-fetchrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, NSError?) -> Void)? ``` |
| To | ``` var fetchRecordZonesCompletionBlock: (([CKRecordZoneID : CKRecordZone]?, Error?) -> Swift.Void)? ``` |

Modified [CKFetchSubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchSubscriptionsOperation : CKDatabaseOperation {     init()     class func fetchAllSubscriptionsOperation() -> Self     convenience init(subscriptionIDs subscriptionIDs: [String])     var subscriptionIDs: [String]?     var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, NSError?) -> Void)? } ``` |
| To | ``` class CKFetchSubscriptionsOperation : CKDatabaseOperation {     init()     class func fetchAllSubscriptionsOperation() -> Self     convenience init(subscriptionIDs subscriptionIDs: [String])     var subscriptionIDs: [String]?     var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, Error?) -> Swift.Void)? } ``` |

Modified [CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/1515261-fetchsubscriptioncompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, NSError?) -> Void)? ``` |
| To | ``` var fetchSubscriptionCompletionBlock: (([String : CKSubscription]?, Error?) -> Swift.Void)? ``` |

Modified [CKFetchWebAuthTokenOperation](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKFetchWebAuthTokenOperation : CKDatabaseOperation {     init(APIToken APIToken: String)     var APIToken: String     var fetchWebAuthTokenCompletionBlock: ((String, NSError) -> Void)? } ``` |
| To | ``` class CKFetchWebAuthTokenOperation : CKDatabaseOperation {     init(apiToken APIToken: String)     var apiToken: String?     var fetchWebAuthTokenCompletionBlock: ((String, Error) -> Swift.Void)? } ``` |

Modified [CKFetchWebAuthTokenOperation.apiToken](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1515095-apitoken)

|  | Declaration |
| --- | --- |
| From | ``` var APIToken: String ``` |
| To | ``` var apiToken: String? ``` |

Modified [CKFetchWebAuthTokenOperation.fetchWebAuthTokenCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1514980-fetchwebauthtokencompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var fetchWebAuthTokenCompletionBlock: ((String, NSError) -> Void)? ``` |
| To | ``` var fetchWebAuthTokenCompletionBlock: ((String, Error) -> Swift.Void)? ``` |

Modified [CKFetchWebAuthTokenOperation.init(apiToken: String)](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/1515266-initwithapitoken)

|  | Declaration |
| --- | --- |
| From | ``` init(APIToken APIToken: String) ``` |
| To | ``` init(apiToken APIToken: String) ``` |

Modified [CKMarkNotificationsReadOperation](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKMarkNotificationsReadOperation : CKOperation {     convenience init()     init(notificationIDsToMarkRead notificationIDs: [CKNotificationID])     var notificationIDs: [CKNotificationID]     var markNotificationsReadCompletionBlock: (([CKNotificationID]?, NSError?) -> Void)? } ``` |
| To | ``` class CKMarkNotificationsReadOperation : CKOperation {     init()     convenience init(notificationIDsToMarkRead notificationIDs: [CKNotificationID])     var notificationIDs: [CKNotificationID]     var markNotificationsReadCompletionBlock: (([CKNotificationID]?, Error?) -> Swift.Void)? } ``` |

Modified [CKMarkNotificationsReadOperation.init(notificationIDsToMarkRead: [CKNotificationID])](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515228-initwithnotificationidstomarkrea)

|  | Declaration |
| --- | --- |
| From | ``` init(notificationIDsToMarkRead notificationIDs: [CKNotificationID]) ``` |
| To | ``` convenience init(notificationIDsToMarkRead notificationIDs: [CKNotificationID]) ``` |

Modified [CKMarkNotificationsReadOperation.markNotificationsReadCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmarknotificationsreadoperation/1515317-marknotificationsreadcompletionb)

|  | Declaration |
| --- | --- |
| From | ``` var markNotificationsReadCompletionBlock: (([CKNotificationID]?, NSError?) -> Void)? ``` |
| To | ``` var markNotificationsReadCompletionBlock: (([CKNotificationID]?, Error?) -> Swift.Void)? ``` |

Modified [CKModifyBadgeOperation](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyBadgeOperation : CKOperation {     init()     convenience init(badgeValue badgeValue: Int)     var badgeValue: Int     var modifyBadgeCompletionBlock: ((NSError?) -> Void)? } ``` |
| To | ``` class CKModifyBadgeOperation : CKOperation {     init()     convenience init(badgeValue badgeValue: Int)     var badgeValue: Int     var modifyBadgeCompletionBlock: ((Error?) -> Swift.Void)? } ``` |

Modified [CKModifyBadgeOperation.modifyBadgeCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifybadgeoperation/1391682-modifybadgecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyBadgeCompletionBlock: ((NSError?) -> Void)? ``` |
| To | ``` var modifyBadgeCompletionBlock: ((Error?) -> Swift.Void)? ``` |

Modified [CKModifyRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordsToSave records: [CKRecord]?, recordIDsToDelete recordIDs: [CKRecordID]?)     var recordsToSave: [CKRecord]?     var recordIDsToDelete: [CKRecordID]?     var savePolicy: CKRecordSavePolicy     @NSCopying var clientChangeTokenData: NSData?     var atomic: Bool     var perRecordProgressBlock: ((CKRecord, Double) -> Void)?     var perRecordCompletionBlock: ((CKRecord?, NSError?) -> Void)?     var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, NSError?) -> Void)? } ``` |
| To | ``` class CKModifyRecordsOperation : CKDatabaseOperation {     init()     convenience init(recordsToSave records: [CKRecord]?, recordIDsToDelete recordIDs: [CKRecordID]?)     var recordsToSave: [CKRecord]?     var recordIDsToDelete: [CKRecordID]?     var savePolicy: CKRecordSavePolicy     var clientChangeTokenData: Data?     var isAtomic: Bool     var perRecordProgressBlock: ((CKRecord, Double) -> Swift.Void)?     var perRecordCompletionBlock: ((CKRecord?, Error?) -> Swift.Void)?     var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, Error?) -> Swift.Void)? } ``` |

Modified [CKModifyRecordsOperation.clientChangeTokenData](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447472-clientchangetokendata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var clientChangeTokenData: NSData? ``` |
| To | ``` var clientChangeTokenData: Data? ``` |

Modified [CKModifyRecordsOperation.isAtomic](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447484-isatomic)

|  | Declaration |
| --- | --- |
| From | ``` var atomic: Bool ``` |
| To | ``` var isAtomic: Bool ``` |

Modified [CKModifyRecordsOperation.modifyRecordsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447486-modifyrecordscompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, NSError?) -> Void)? ``` |
| To | ``` var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecordID]?, Error?) -> Swift.Void)? ``` |

Modified [CKModifyRecordsOperation.perRecordCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447470-perrecordcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordCompletionBlock: ((CKRecord?, NSError?) -> Void)? ``` |
| To | ``` var perRecordCompletionBlock: ((CKRecord?, Error?) -> Swift.Void)? ``` |

Modified [CKModifyRecordsOperation.perRecordProgressBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447477-perrecordprogressblock)

|  | Declaration |
| --- | --- |
| From | ``` var perRecordProgressBlock: ((CKRecord, Double) -> Void)? ``` |
| To | ``` var perRecordProgressBlock: ((CKRecord, Double) -> Swift.Void)? ``` |

Modified [CKModifyRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifyRecordZonesOperation : CKDatabaseOperation {     init()     convenience init(recordZonesToSave recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete recordZoneIDsToDelete: [CKRecordZoneID]?)     var recordZonesToSave: [CKRecordZone]?     var recordZoneIDsToDelete: [CKRecordZoneID]?     var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, NSError?) -> Void)? } ``` |
| To | ``` class CKModifyRecordZonesOperation : CKDatabaseOperation {     init()     convenience init(recordZonesToSave recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete recordZoneIDsToDelete: [CKRecordZoneID]?)     var recordZonesToSave: [CKRecordZone]?     var recordZoneIDsToDelete: [CKRecordZoneID]?     var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, Error?) -> Swift.Void)? } ``` |

Modified [CKModifyRecordZonesOperation.modifyRecordZonesCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/1415164-modifyrecordzonescompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, NSError?) -> Void)? ``` |
| To | ``` var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZoneID]?, Error?) -> Swift.Void)? ``` |

Modified [CKModifySubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKModifySubscriptionsOperation : CKDatabaseOperation {     init(subscriptionsToSave subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete subscriptionIDsToDelete: [String]?)     var subscriptionsToSave: [CKSubscription]?     var subscriptionIDsToDelete: [String]?     var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, NSError?) -> Void)? } ``` |
| To | ``` class CKModifySubscriptionsOperation : CKDatabaseOperation {     init(subscriptionsToSave subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete subscriptionIDsToDelete: [String]?)     var subscriptionsToSave: [CKSubscription]?     var subscriptionIDsToDelete: [String]?     var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, Error?) -> Swift.Void)? } ``` |

Modified [CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/1515288-modifysubscriptionscompletionblo)

|  | Declaration |
| --- | --- |
| From | ``` var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, NSError?) -> Void)? ``` |
| To | ``` var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [String]?, Error?) -> Swift.Void)? ``` |

Modified [CKNotification](https://developer.apple.com/documentation/cloudkit/cknotification)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKNotification : NSObject {     init()     convenience init(fromRemoteNotificationDictionary notificationDictionary: [String : NSObject])     class func notificationFromRemoteNotificationDictionary(_ notificationDictionary: [String : NSObject]) -> Self     var notificationType: CKNotificationType { get }     @NSCopying var notificationID: CKNotificationID? { get }     var containerIdentifier: String? { get }     var isPruned: Bool { get }     var alertBody: String? { get }     var alertLocalizationKey: String? { get }     var alertLocalizationArgs: [String]? { get }     var alertActionLocalizationKey: String? { get }     var alertLaunchImage: String? { get }     @NSCopying var badge: NSNumber? { get }     var soundName: String? { get }     var subscriptionID: String? { get }     var category: String? { get } } ``` | -- |
| To | ``` class CKNotification : NSObject {     init()     convenience init(fromRemoteNotificationDictionary notificationDictionary: [String : NSObject])     class func fromRemoteNotificationDictionary(_ notificationDictionary: [String : NSObject]) -> Self     var notificationType: CKNotificationType { get }     @NSCopying var notificationID: CKNotificationID? { get }     var containerIdentifier: String? { get }     var isPruned: Bool { get }     var alertBody: String? { get }     var alertLocalizationKey: String? { get }     var alertLocalizationArgs: [String]? { get }     var alertActionLocalizationKey: String? { get }     var alertLaunchImage: String? { get }     @NSCopying var badge: NSNumber? { get }     var soundName: String? { get }     var subscriptionID: String? { get }     var category: String? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKNotification : CVarArg { } extension CKNotification : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CKNotificationID](https://developer.apple.com/documentation/cloudkit/cknotification/id)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKNotificationID : NSObject, NSCopying, NSSecureCoding { } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKNotificationID : NSObject, NSCopying, NSSecureCoding {     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKNotificationID : CVarArg { } extension CKNotificationID : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKNotificationInfo](https://developer.apple.com/documentation/cloudkit/cknotificationinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCopying {     var alertBody: String?     var alertLocalizationKey: String?     var alertLocalizationArgs: [String]?     var alertActionLocalizationKey: String?     var alertLaunchImage: String?     var soundName: String?     var desiredKeys: [String]?     var shouldBadge: Bool     var shouldSendContentAvailable: Bool     var category: String? } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKNotificationInfo : NSObject, NSSecureCoding, NSCopying {     var alertBody: String?     var alertLocalizationKey: String?     var alertLocalizationArgs: [String]?     var alertActionLocalizationKey: String?     var alertLaunchImage: String?     var soundName: String?     var desiredKeys: [String]?     var shouldBadge: Bool     var shouldSendContentAvailable: Bool     var category: String?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKNotificationInfo : CVarArg { } extension CKNotificationInfo : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKNotificationType [enum]](https://developer.apple.com/documentation/cloudkit/cknotificationtype)

|  | Declaration |
| --- | --- |
| From | ``` enum CKNotificationType : Int {     case Query     case RecordZone     case ReadNotification } ``` |
| To | ``` enum CKNotificationType : Int {     case query     case recordZone     case readNotification     case database } ``` |

Modified [CKNotificationType.query](https://developer.apple.com/documentation/cloudkit/cknotificationtype/cknotificationtypequery)

|  | Declaration |
| --- | --- |
| From | ``` case Query ``` |
| To | ``` case query ``` |

Modified [CKNotificationType.readNotification](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype/readnotification)

|  | Declaration |
| --- | --- |
| From | ``` case ReadNotification ``` |
| To | ``` case readNotification ``` |

Modified [CKNotificationType.recordZone](https://developer.apple.com/documentation/cloudkit/cknotification/notificationtype/recordzone)

|  | Declaration |
| --- | --- |
| From | ``` case RecordZone ``` |
| To | ``` case recordZone ``` |

Modified [CKOperation](https://developer.apple.com/documentation/cloudkit/ckoperation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKOperation : NSOperation {     init()     var container: CKContainer?     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool     var operationID: String { get }     var longLived: Bool     var longLivedOperationWasPersistedBlock: () -> Void } ``` | -- |
| To | ``` class CKOperation : Operation {     init()     var container: CKContainer?     var usesBackgroundSession: Bool     var allowsCellularAccess: Bool     var operationID: String { get }     var isLongLived: Bool     var timeoutIntervalForRequest: TimeInterval     var timeoutIntervalForResource: TimeInterval     var longLivedOperationWasPersistedBlock: () -> Swift.Void     enum QueuePriority : Int {         case veryLow         case low         case normal         case high         case veryHigh     }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKOperation : CVarArg { } extension CKOperation : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CKOperation.isLongLived](https://developer.apple.com/documentation/cloudkit/ckoperation/1452374-longlived)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var longLived: Bool ``` | OS X 10.11.4 |
| To | ``` var isLongLived: Bool ``` | OS X 10.12 |

Modified [CKOperation.longLivedOperationWasPersistedBlock](https://developer.apple.com/documentation/cloudkit/ckoperation/1452366-longlivedoperationwaspersistedbl)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var longLivedOperationWasPersistedBlock: () -> Void ``` | OS X 10.11.4 |
| To | ``` var longLivedOperationWasPersistedBlock: () -> Swift.Void ``` | OS X 10.12 |

Modified [CKOperation.operationID](https://developer.apple.com/documentation/cloudkit/ckoperation/1452362-operationid)

|  | Introduction |
| --- | --- |
| From | OS X 10.11.4 |
| To | OS X 10.12 |

Modified [CKQuery](https://developer.apple.com/documentation/cloudkit/ckquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKQuery : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     init(recordType recordType: String, predicate predicate: NSPredicate)     var recordType: String { get }     @NSCopying var predicate: NSPredicate { get }     var sortDescriptors: [NSSortDescriptor]? } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKQuery : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     init(recordType recordType: String, predicate predicate: NSPredicate)     var recordType: String { get }     @NSCopying var predicate: NSPredicate { get }     var sortDescriptors: [NSSortDescriptor]?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKQuery : CVarArg { } extension CKQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKQueryCursor](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding {     init() } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKQueryCursor : NSObject, NSCopying, NSSecureCoding {     init()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKQueryCursor : CVarArg { } extension CKQueryCursor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKQueryNotification](https://developer.apple.com/documentation/cloudkit/ckquerynotification)

|  | Declaration |
| --- | --- |
| From | ``` class CKQueryNotification : CKNotification {     var queryNotificationReason: CKQueryNotificationReason { get }     var recordFields: [String : CKRecordValue]? { get }     @NSCopying var recordID: CKRecordID? { get }     var isPublicDatabase: Bool { get } } ``` |
| To | ``` class CKQueryNotification : CKNotification {     var queryNotificationReason: CKQueryNotificationReason { get }     var recordFields: [String : Any]? { get }     @NSCopying var recordID: CKRecordID? { get }     var isPublicDatabase: Bool { get }     var databaseScope: CKDatabaseScope { get } } ``` |

Modified [CKQueryNotification.isPublicDatabase](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428111-ispublicdatabase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKQueryNotification.recordFields](https://developer.apple.com/documentation/cloudkit/ckquerynotification/1428114-recordfields)

|  | Declaration |
| --- | --- |
| From | ``` var recordFields: [String : CKRecordValue]? { get } ``` |
| To | ``` var recordFields: [String : Any]? { get } ``` |

Modified [CKQueryNotificationReason [enum]](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason)

|  | Declaration |
| --- | --- |
| From | ``` enum CKQueryNotificationReason : Int {     case RecordCreated     case RecordUpdated     case RecordDeleted } ``` |
| To | ``` enum CKQueryNotificationReason : Int {     case recordCreated     case recordUpdated     case recordDeleted } ``` |

Modified [CKQueryNotificationReason.recordCreated](https://developer.apple.com/documentation/cloudkit/ckquerynotificationreason/ckquerynotificationreasonrecordcreated)

|  | Declaration |
| --- | --- |
| From | ``` case RecordCreated ``` |
| To | ``` case recordCreated ``` |

Modified [CKQueryNotificationReason.recordDeleted](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason/recorddeleted)

|  | Declaration |
| --- | --- |
| From | ``` case RecordDeleted ``` |
| To | ``` case recordDeleted ``` |

Modified [CKQueryNotificationReason.recordUpdated](https://developer.apple.com/documentation/cloudkit/ckquerynotificationreason/ckquerynotificationreasonrecordupdated)

|  | Declaration |
| --- | --- |
| From | ``` case RecordUpdated ``` |
| To | ``` case recordUpdated ``` |

Modified [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation)

|  | Declaration |
| --- | --- |
| From | ``` class CKQueryOperation : CKDatabaseOperation {     init()     convenience init(query query: CKQuery)     convenience init(cursor cursor: CKQueryCursor)     @NSCopying var query: CKQuery?     @NSCopying var cursor: CKQueryCursor?     @NSCopying var zoneID: CKRecordZoneID?     var resultsLimit: Int     var desiredKeys: [String]?     var recordFetchedBlock: ((CKRecord) -> Void)?     var queryCompletionBlock: ((CKQueryCursor?, NSError?) -> Void)? } ``` |
| To | ``` class CKQueryOperation : CKDatabaseOperation {     init()     convenience init(query query: CKQuery)     convenience init(cursor cursor: CKQueryCursor)     @NSCopying var query: CKQuery?     @NSCopying var cursor: CKQueryCursor?     @NSCopying var zoneID: CKRecordZoneID?     var resultsLimit: Int     var desiredKeys: [String]?     var recordFetchedBlock: ((CKRecord) -> Swift.Void)?     var queryCompletionBlock: ((CKQueryCursor?, Error?) -> Swift.Void)? } ``` |

Modified [CKQueryOperation.queryCompletionBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515067-querycompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` var queryCompletionBlock: ((CKQueryCursor?, NSError?) -> Void)? ``` |
| To | ``` var queryCompletionBlock: ((CKQueryCursor?, Error?) -> Swift.Void)? ``` |

Modified [CKQueryOperation.recordFetchedBlock](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/1515283-recordfetchedblock)

|  | Declaration |
| --- | --- |
| From | ``` var recordFetchedBlock: ((CKRecord) -> Void)? ``` |
| To | ``` var recordFetchedBlock: ((CKRecord) -> Swift.Void)? ``` |

Modified [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecord : NSObject, NSSecureCoding, NSCopying {     init()     init(recordType recordType: String)     init(recordType recordType: String, recordID recordID: CKRecordID)     init(recordType recordType: String, zoneID zoneID: CKRecordZoneID)     var recordType: String { get }     @NSCopying var recordID: CKRecordID { get }     var recordChangeTag: String? { get }     @NSCopying var creatorUserRecordID: CKRecordID? { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID? { get }     @NSCopying var modificationDate: NSDate? { get }     func objectForKey(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKey key: String)     func allKeys() -> [String]     func allTokens() -> [String]     subscript (_ key: String) -> CKRecordValue?     func objectForKeyedSubscript(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKeyedSubscript key: String)     func changedKeys() -> [String]     func encodeSystemFieldsWithCoder(_ coder: NSCoder) } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKRecord : NSObject, NSSecureCoding, NSCopying {     init()     init(recordType recordType: String)     init(recordType recordType: String, recordID recordID: CKRecordID)     init(recordType recordType: String, zoneID zoneID: CKRecordZoneID)     var recordType: String { get }     @NSCopying var recordID: CKRecordID { get }     var recordChangeTag: String? { get }     @NSCopying var creatorUserRecordID: CKRecordID? { get }     var creationDate: Date? { get }     @NSCopying var lastModifiedUserRecordID: CKRecordID? { get }     var modificationDate: Date? { get }     func object(forKey key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKey key: String)     func allKeys() -> [String]     func allTokens() -> [String]     subscript(_ key: String) -> CKRecordValue?     func objectForKeyedSubscript(_ key: String) -> CKRecordValue?     func setObject(_ object: CKRecordValue?, forKeyedSubscript key: String)     func changedKeys() -> [String]     func encodeSystemFields(with coder: NSCoder)     @NSCopying var share: CKReference? { get }     @NSCopying var parent: CKReference?     func setParent(_ parentRecord: CKRecord?)     func setParent(_ parentRecordID: CKRecordID?)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKRecord : CVarArg { } extension CKRecord : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKRecord.creationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462223-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creationDate: NSDate? { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified [CKRecord.encodeSystemFields(with: NSCoder)](https://developer.apple.com/documentation/cloudkit/ckrecord/1462200-encodesystemfields)

|  | Declaration |
| --- | --- |
| From | ``` func encodeSystemFieldsWithCoder(_ coder: NSCoder) ``` |
| To | ``` func encodeSystemFields(with coder: NSCoder) ``` |

Modified [CKRecord.modificationDate](https://developer.apple.com/documentation/cloudkit/ckrecord/1462227-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate? { get } ``` |
| To | ``` var modificationDate: Date? { get } ``` |

Modified [CKRecord.object(forKey: String) -> CKRecordValue?](https://developer.apple.com/documentation/cloudkit/ckrecord/1462216-objectforkey)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ key: String) -> CKRecordValue? ``` |
| To | ``` func object(forKey key: String) -> CKRecordValue? ``` |

Modified [CKRecord.subscript(_: String) -> CKRecordValue?](https://developer.apple.com/documentation/cloudkit/ckrecord/1462210-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ key: String) -> CKRecordValue? ``` |
| To | ``` subscript(_ key: String) -> CKRecordValue? ``` |

Modified [CKRecordID](https://developer.apple.com/documentation/cloudkit/ckrecord/id)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordID : NSObject, NSSecureCoding, NSCopying {     convenience init()     convenience init(recordName recordName: String)     init(recordName recordName: String, zoneID zoneID: CKRecordZoneID)     var recordName: String { get }     var zoneID: CKRecordZoneID { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKRecordID : NSObject, NSSecureCoding, NSCopying {     convenience init()     convenience init(recordName recordName: String)     init(recordName recordName: String, zoneID zoneID: CKRecordZoneID)     var recordName: String { get }     var zoneID: CKRecordZoneID { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKRecordID : CVarArg { } extension CKRecordID : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKRecordSavePolicy [enum]](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy)

|  | Declaration |
| --- | --- |
| From | ``` enum CKRecordSavePolicy : Int {     case IfServerRecordUnchanged     case ChangedKeys     case AllKeys } ``` |
| To | ``` enum CKRecordSavePolicy : Int {     case ifServerRecordUnchanged     case changedKeys     case allKeys } ``` |

Modified [CKRecordSavePolicy.allKeys](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/allkeys)

|  | Declaration |
| --- | --- |
| From | ``` case AllKeys ``` |
| To | ``` case allKeys ``` |

Modified [CKRecordSavePolicy.changedKeys](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/changedkeys)

|  | Declaration |
| --- | --- |
| From | ``` case ChangedKeys ``` |
| To | ``` case changedKeys ``` |

Modified [CKRecordSavePolicy.ifServerRecordUnchanged](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged)

|  | Declaration |
| --- | --- |
| From | ``` case IfServerRecordUnchanged ``` |
| To | ``` case ifServerRecordUnchanged ``` |

Modified [CKRecordZone](https://developer.apple.com/documentation/cloudkit/ckrecordzone)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCopying {     class func defaultRecordZone() -> CKRecordZone     init()     init(zoneName zoneName: String)     init(zoneID zoneID: CKRecordZoneID)     var zoneID: CKRecordZoneID { get }     var capabilities: CKRecordZoneCapabilities { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKRecordZone : NSObject, NSSecureCoding, NSCopying {     class func `default`() -> CKRecordZone     init()     init(zoneName zoneName: String)     init(zoneID zoneID: CKRecordZoneID)     var zoneID: CKRecordZoneID { get }     var capabilities: CKRecordZoneCapabilities { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKRecordZone : CVarArg { } extension CKRecordZone : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKRecordZone.default() [class]](https://developer.apple.com/documentation/cloudkit/ckrecordzone/1514919-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultRecordZone() -> CKRecordZone ``` |
| To | ``` class func `default`() -> CKRecordZone ``` |

Modified [CKRecordZoneCapabilities [struct]](https://developer.apple.com/documentation/cloudkit/ckrecordzonecapabilities)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CKRecordZoneCapabilities : OptionSetType {     init(rawValue rawValue: UInt)     static var FetchChanges: CKRecordZoneCapabilities { get }     static var Atomic: CKRecordZoneCapabilities { get } } ``` | OptionSetType |
| To | ``` struct CKRecordZoneCapabilities : OptionSet {     init(rawValue rawValue: UInt)     static var fetchChanges: CKRecordZoneCapabilities { get }     static var atomic: CKRecordZoneCapabilities { get }     static var sharing: CKRecordZoneCapabilities { get }     func intersect(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities     func exclusiveOr(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities     mutating func unionInPlace(_ other: CKRecordZoneCapabilities)     mutating func intersectInPlace(_ other: CKRecordZoneCapabilities)     mutating func exclusiveOrInPlace(_ other: CKRecordZoneCapabilities)     func isSubsetOf(_ other: CKRecordZoneCapabilities) -> Bool     func isDisjointWith(_ other: CKRecordZoneCapabilities) -> Bool     func isSupersetOf(_ other: CKRecordZoneCapabilities) -> Bool     mutating func subtractInPlace(_ other: CKRecordZoneCapabilities)     func isStrictSupersetOf(_ other: CKRecordZoneCapabilities) -> Bool     func isStrictSubsetOf(_ other: CKRecordZoneCapabilities) -> Bool } extension CKRecordZoneCapabilities {     func union(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities     func intersection(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities     func symmetricDifference(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities } extension CKRecordZoneCapabilities {     func contains(_ member: CKRecordZoneCapabilities) -> Bool     mutating func insert(_ newMember: CKRecordZoneCapabilities) -> (inserted: Bool, memberAfterInsert: CKRecordZoneCapabilities)     mutating func remove(_ member: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities?     mutating func update(with newMember: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities? } extension CKRecordZoneCapabilities {     convenience init()     mutating func formUnion(_ other: CKRecordZoneCapabilities)     mutating func formIntersection(_ other: CKRecordZoneCapabilities)     mutating func formSymmetricDifference(_ other: CKRecordZoneCapabilities) } extension CKRecordZoneCapabilities {     convenience init<S : Sequence where S.Iterator.Element == CKRecordZoneCapabilities>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CKRecordZoneCapabilities...)     mutating func subtract(_ other: CKRecordZoneCapabilities)     func isSubset(of other: CKRecordZoneCapabilities) -> Bool     func isSuperset(of other: CKRecordZoneCapabilities) -> Bool     func isDisjoint(with other: CKRecordZoneCapabilities) -> Bool     func subtracting(_ other: CKRecordZoneCapabilities) -> CKRecordZoneCapabilities     var isEmpty: Bool { get }     func isStrictSuperset(of other: CKRecordZoneCapabilities) -> Bool     func isStrictSubset(of other: CKRecordZoneCapabilities) -> Bool } ``` | OptionSet |

Modified [CKRecordZoneCapabilities.atomic](https://developer.apple.com/documentation/cloudkit/ckrecordzonecapabilities/ckrecordzonecapabilityatomic)

|  | Declaration |
| --- | --- |
| From | ``` static var Atomic: CKRecordZoneCapabilities { get } ``` |
| To | ``` static var atomic: CKRecordZoneCapabilities { get } ``` |

Modified [CKRecordZoneCapabilities.fetchChanges](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities/1515273-fetchchanges)

|  | Declaration |
| --- | --- |
| From | ``` static var FetchChanges: CKRecordZoneCapabilities { get } ``` |
| To | ``` static var fetchChanges: CKRecordZoneCapabilities { get } ``` |

Modified [CKRecordZoneID](https://developer.apple.com/documentation/cloudkit/ckrecordzoneid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(zoneName zoneName: String, ownerName ownerName: String)     var zoneName: String { get }     var ownerName: String { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKRecordZoneID : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(zoneName zoneName: String, ownerName ownerName: String)     var zoneName: String { get }     var ownerName: String { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKRecordZoneID : CVarArg { } extension CKRecordZoneID : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKRecordZoneNotification](https://developer.apple.com/documentation/cloudkit/ckrecordzonenotification)

|  | Declaration |
| --- | --- |
| From | ``` class CKRecordZoneNotification : CKNotification {     @NSCopying var recordZoneID: CKRecordZoneID? { get } } ``` |
| To | ``` class CKRecordZoneNotification : CKNotification {     @NSCopying var recordZoneID: CKRecordZoneID? { get }     var databaseScope: CKDatabaseScope { get } } ``` |

Modified [CKReference](https://developer.apple.com/documentation/cloudkit/ckreference)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKReference : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(recordID recordID: CKRecordID, action action: CKReferenceAction)     convenience init(record record: CKRecord, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID { get } } extension CKReference : CKRecordValue { } ``` | CKRecordValue, NSCopying, NSSecureCoding |
| To | ``` class CKReference : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(recordID recordID: CKRecordID, action action: CKReferenceAction)     convenience init(record record: CKRecord, action action: CKReferenceAction)     var referenceAction: CKReferenceAction { get }     @NSCopying var recordID: CKRecordID { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKReference : CKRecordValue { } extension CKReference : CVarArg { } extension CKReference : Equatable, Hashable {     var hashValue: Int { get } } ``` | CKRecordValue, CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKReferenceAction [enum]](https://developer.apple.com/documentation/cloudkit/ckrecord_reference_action)

|  | Declaration |
| --- | --- |
| From | ``` enum CKReferenceAction : UInt {     case None     case DeleteSelf } ``` |
| To | ``` enum CKReferenceAction : UInt {     case none     case deleteSelf } ``` |

Modified [CKReferenceAction.deleteSelf](https://developer.apple.com/documentation/cloudkit/ckreferenceaction/ckreferenceactiondeleteself)

|  | Declaration |
| --- | --- |
| From | ``` case DeleteSelf ``` |
| To | ``` case deleteSelf ``` |

Modified [CKReferenceAction.none](https://developer.apple.com/documentation/cloudkit/ckrecord_reference_action/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CKServerChangeToken](https://developer.apple.com/documentation/cloudkit/ckserverchangetoken)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding {     init() } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKServerChangeToken : NSObject, NSCopying, NSSecureCoding {     init()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKServerChangeToken : CVarArg { } extension CKServerChangeToken : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKSubscription](https://developer.apple.com/documentation/cloudkit/cksubscription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CKSubscription : NSObject, NSSecureCoding, NSCopying {     convenience init()     init(coder aDecoder: NSCoder)     convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions)     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions)     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions)     var subscriptionID: String { get }     var subscriptionType: CKSubscriptionType { get }     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     @NSCopying var notificationInfo: CKNotificationInfo?     @NSCopying var zoneID: CKRecordZoneID? } ``` | NSCopying, NSSecureCoding |
| To | ``` class CKSubscription : NSObject, NSSecureCoding, NSCopying {     init()     var subscriptionID: String { get }     var subscriptionType: CKSubscriptionType { get }     @NSCopying var notificationInfo: CKNotificationInfo?     init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions = [])     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = [])     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions = [])     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = [])     @NSCopying var zoneID: CKRecordZoneID?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CKSubscription : CVarArg { } extension CKSubscription : Equatable, Hashable {     var hashValue: Int { get } } extension CKSubscription {     init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions = [])     init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = [])     var recordType: String? { get }     @NSCopying var predicate: NSPredicate? { get }     var subscriptionOptions: CKSubscriptionOptions { get }     init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions = [])     init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = [])     @NSCopying var zoneID: CKRecordZoneID? } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CKSubscription.init(recordType: String, predicate: NSPredicate, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515132-initwithrecordtype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` convenience init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions) ``` | -- |
| To | ``` init(recordType recordType: String, predicate predicate: NSPredicate, options subscriptionOptions: CKSubscriptionOptions = []) ``` | OS X 10.12 |

Modified [CKSubscription.init(recordType: String, predicate: NSPredicate, subscriptionID: String, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515265-initwithrecordtype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions) ``` | -- |
| To | ``` init(recordType recordType: String, predicate predicate: NSPredicate, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = []) ``` | OS X 10.12 |

Modified [CKSubscription.init(zoneID: CKRecordZoneID, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1514971-initwithzoneid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` convenience init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions) ``` | -- |
| To | ``` init(zoneID zoneID: CKRecordZoneID, options subscriptionOptions: CKSubscriptionOptions = []) ``` | OS X 10.12 |

Modified [CKSubscription.init(zoneID: CKRecordZoneID, subscriptionID: String, options: CKSubscriptionOptions)](https://developer.apple.com/documentation/cloudkit/cksubscription/1515215-initwithzoneid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions) ``` | -- |
| To | ``` init(zoneID zoneID: CKRecordZoneID, subscriptionID subscriptionID: String, options subscriptionOptions: CKSubscriptionOptions = []) ``` | OS X 10.12 |

Modified [CKSubscription.predicate](https://developer.apple.com/documentation/cloudkit/cksubscription/1515219-predicate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKSubscription.recordType](https://developer.apple.com/documentation/cloudkit/cksubscription/1515080-recordtype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKSubscription.subscriptionOptions](https://developer.apple.com/documentation/cloudkit/cksubscription/1514922-subscriptionoptions)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKSubscription.zoneID](https://developer.apple.com/documentation/cloudkit/cksubscription/1514936-zoneid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKSubscriptionOptions [struct]](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions)

|  | Declaration | Protocols | Deprecation |
| --- | --- | --- | --- |
| From | ``` struct CKSubscriptionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var FiresOnRecordCreation: CKSubscriptionOptions { get }     static var FiresOnRecordUpdate: CKSubscriptionOptions { get }     static var FiresOnRecordDeletion: CKSubscriptionOptions { get }     static var FiresOnce: CKSubscriptionOptions { get } } ``` | OptionSetType | -- |
| To | ``` struct CKSubscriptionOptions : OptionSet {     init(rawValue rawValue: UInt)     static var firesOnRecordCreation: CKSubscriptionOptions { get }     static var firesOnRecordUpdate: CKSubscriptionOptions { get }     static var firesOnRecordDeletion: CKSubscriptionOptions { get }     static var firesOnce: CKSubscriptionOptions { get }     func intersect(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions     func exclusiveOr(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions     mutating func unionInPlace(_ other: CKSubscriptionOptions)     mutating func intersectInPlace(_ other: CKSubscriptionOptions)     mutating func exclusiveOrInPlace(_ other: CKSubscriptionOptions)     func isSubsetOf(_ other: CKSubscriptionOptions) -> Bool     func isDisjointWith(_ other: CKSubscriptionOptions) -> Bool     func isSupersetOf(_ other: CKSubscriptionOptions) -> Bool     mutating func subtractInPlace(_ other: CKSubscriptionOptions)     func isStrictSupersetOf(_ other: CKSubscriptionOptions) -> Bool     func isStrictSubsetOf(_ other: CKSubscriptionOptions) -> Bool } extension CKSubscriptionOptions {     func union(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions     func intersection(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions     func symmetricDifference(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions } extension CKSubscriptionOptions {     func contains(_ member: CKSubscriptionOptions) -> Bool     mutating func insert(_ newMember: CKSubscriptionOptions) -> (inserted: Bool, memberAfterInsert: CKSubscriptionOptions)     mutating func remove(_ member: CKSubscriptionOptions) -> CKSubscriptionOptions?     mutating func update(with newMember: CKSubscriptionOptions) -> CKSubscriptionOptions? } extension CKSubscriptionOptions {     convenience init()     mutating func formUnion(_ other: CKSubscriptionOptions)     mutating func formIntersection(_ other: CKSubscriptionOptions)     mutating func formSymmetricDifference(_ other: CKSubscriptionOptions) } extension CKSubscriptionOptions {     convenience init<S : Sequence where S.Iterator.Element == CKSubscriptionOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CKSubscriptionOptions...)     mutating func subtract(_ other: CKSubscriptionOptions)     func isSubset(of other: CKSubscriptionOptions) -> Bool     func isSuperset(of other: CKSubscriptionOptions) -> Bool     func isDisjoint(with other: CKSubscriptionOptions) -> Bool     func subtracting(_ other: CKSubscriptionOptions) -> CKSubscriptionOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CKSubscriptionOptions) -> Bool     func isStrictSubset(of other: CKSubscriptionOptions) -> Bool } ``` | OptionSet | OS X 10.12 |

Modified [CKSubscriptionOptions.firesOnce](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonce)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` static var FiresOnce: CKSubscriptionOptions { get } ``` | -- |
| To | ``` static var firesOnce: CKSubscriptionOptions { get } ``` | OS X 10.12 |

Modified [CKSubscriptionOptions.firesOnRecordCreation](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecordcreation)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` static var FiresOnRecordCreation: CKSubscriptionOptions { get } ``` | -- |
| To | ``` static var firesOnRecordCreation: CKSubscriptionOptions { get } ``` | OS X 10.12 |

Modified [CKSubscriptionOptions.firesOnRecordDeletion](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecorddeletion)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` static var FiresOnRecordDeletion: CKSubscriptionOptions { get } ``` | -- |
| To | ``` static var firesOnRecordDeletion: CKSubscriptionOptions { get } ``` | OS X 10.12 |

Modified [CKSubscriptionOptions.firesOnRecordUpdate](https://developer.apple.com/documentation/cloudkit/cksubscriptionoptions/cksubscriptionoptionsfiresonrecordupdate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` static var FiresOnRecordUpdate: CKSubscriptionOptions { get } ``` | -- |
| To | ``` static var firesOnRecordUpdate: CKSubscriptionOptions { get } ``` | OS X 10.12 |

Modified CKSubscriptionOptions.init(rawValue: UInt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [CKSubscriptionType [enum]](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum CKSubscriptionType : Int {     case Query     case RecordZone } ``` |
| To | ``` enum CKSubscriptionType : Int {     case query     case recordZone     case database } ``` |

Modified [CKSubscriptionType.query](https://developer.apple.com/documentation/cloudkit/cksubscriptiontype/cksubscriptiontypequery)

|  | Declaration |
| --- | --- |
| From | ``` case Query ``` |
| To | ``` case query ``` |

Modified [CKSubscriptionType.recordZone](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype/recordzone)

|  | Declaration |
| --- | --- |
| From | ``` case RecordZone ``` |
| To | ``` case recordZone ``` |

Modified [NSNotification.Name.CKAccountChanged](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged)

|  | Name | Declaration |
| --- | --- | --- |
| From | CKAccountChangedNotification | ``` let CKAccountChangedNotification: String ``` |
| To | CKAccountChanged | ``` static let CKAccountChanged: NSNotification.Name ``` |

Modified [CKApplicationPermissionBlock](https://developer.apple.com/documentation/cloudkit/ckapplicationpermissionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias CKApplicationPermissionBlock = (CKApplicationPermissionStatus, NSError?) -> Void ``` |
| To | ``` typealias CKApplicationPermissionBlock = (CKApplicationPermissionStatus, Error?) -> Swift.Void ``` |

Modified [CKOwnerDefaultName](https://developer.apple.com/documentation/cloudkit/ckownerdefaultname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

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
