---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreData.html
archived_at: '2026-07-18T02:54:26.536410Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreData Changes

## CoreData

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CoreDataDefines.hAdded [#def NSCoreDataVersionNumber10_6](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_6)Added [#def NSCoreDataVersionNumber10_6_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_6_2)Added [#def NSCoreDataVersionNumber10_6_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_6_3)Added [#def NSCoreDataVersionNumber_iPhoneOS_3_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_3_0)Added [#def NSCoreDataVersionNumber_iPhoneOS_3_1](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_3_1)Added [#def NSCoreDataVersionNumber_iPhoneOS_3_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_3_2)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_0)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_1](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_1)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_2)Added [#def NSCoreDataVersionNumber_iPhoneOS_4_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_4_3)CoreDataErrors.hAdded [NSPersistentStoreSaveConflictsError](https://developer.apple.com/documentation/coredata/nspersistentstoresaveconflictserror)Added [NSPersistentStoreSaveConflictsErrorKey](https://developer.apple.com/documentation/coredata/nspersistentstoresaveconflictserrorkey)Added [NSPersistentStoreUnsupportedRequestTypeError](https://developer.apple.com/documentation/coredata/nspersistentstoreunsupportedrequesttypeerror)NSAttributeDescription.hAdded [-[NSAttributeDescription allowsExternalBinaryDataStorage]](https://developer.apple.com/documentation/coredata/nsattributedescription/1498295-allowsexternalbinarydatastorage)Added [-[NSAttributeDescription setAllowsExternalBinaryDataStorage:]](https://developer.apple.com/documentation/coredata/nsattributedescription/1498295-allowsexternalbinarydatastorage)NSFetchRequest.hAdded [-[NSFetchRequest entityName]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506233-entityname)Added [+[NSFetchRequest fetchRequestWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1563437-fetchrequestwithentityname)Added [-[NSFetchRequest havingPredicate]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)Added [-[NSFetchRequest init]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506679-init)Added [-[NSFetchRequest initWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506802-init)Added [-[NSFetchRequest propertiesToGroupBy]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)Added [-[NSFetchRequest setHavingPredicate:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)Added [-[NSFetchRequest setPropertiesToGroupBy:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)Added [-[NSFetchRequest setShouldRefreshRefetchedObjects:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506440-shouldrefreshrefetchedobjects)Added [-[NSFetchRequest shouldRefreshRefetchedObjects]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506440-shouldrefreshrefetchedobjects)Added [NSCountResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/nscountresulttype)Modified [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest)

|  | Superclass | Protocols |
| --- | --- | --- |
| From | NSObject | NSCoding, NSCopying |
| To | NSPersistentStoreRequest | NSCoding |

NSIncrementalStore.hAdded [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore)Added [-[NSIncrementalStore executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506653-execute)Added [+[NSIncrementalStore identifierForNewStoreAtURL:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506781-identifierfornewstore)Added [-[NSIncrementalStore loadMetadata:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506708-loadmetadata)Added [-[NSIncrementalStore managedObjectContextDidRegisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506199-managedobjectcontextdidregistero)Added [-[NSIncrementalStore managedObjectContextDidUnregisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506878-managedobjectcontextdidunregiste)Added [-[NSIncrementalStore newObjectIDForEntity:referenceObject:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506666-newobjectidforentity)Added [-[NSIncrementalStore newValueForRelationship:forObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506438-newvalueforrelationship)Added [-[NSIncrementalStore newValuesForObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobjectwithid)Added [-[NSIncrementalStore obtainPermanentIDsForObjects:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentids)Added [-[NSIncrementalStore referenceObjectForObjectID:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506828-referenceobjectforobjectid)NSIncrementalStoreNode.hAdded [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)Added [-[NSIncrementalStoreNode initWithObjectID:withValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-init)Added [-[NSIncrementalStoreNode objectID]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506827-objectid)Added [-[NSIncrementalStoreNode updateWithValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-updatewithvalues)Added [-[NSIncrementalStoreNode valueForPropertyDescription:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506442-value)Added [-[NSIncrementalStoreNode version]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506769-version)NSManagedObject.hAdded [-[NSManagedObject changedValuesForCurrentEvent]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506472-changedvaluesforcurrentevent)Added [-[NSManagedObject hasChanges]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506654-haschanges)NSManagedObjectContext.hAdded [-[NSManagedObjectContext concurrencyType]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506792-concurrencytype)Added [-[NSManagedObjectContext initWithConcurrencyType:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506709-init)Added [-[NSManagedObjectContext parentContext]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506529-parent)Added [-[NSManagedObjectContext performBlock:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock)Added [-[NSManagedObjectContext performBlockAndWait:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait)Added -[NSManagedObjectContext setParentContext:]Added [-[NSManagedObjectContext userInfo]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506740-userinfo)Added [NSConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)Added [NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype)Added [NSManagedObjectContextConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)Added [NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype)NSMergePolicy.hAdded [NSMergeConflict](https://developer.apple.com/documentation/coredata/nsmergeconflict)Added [NSMergeConflict.cachedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506685-cachedsnapshot)Added [-[NSMergeConflict initWithSource:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:]](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506216-init)Added [NSMergeConflict.newVersionNumber](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506190-newversionnumber)Added [NSMergeConflict.objectSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506454-objectsnapshot)Added [NSMergeConflict.oldVersionNumber](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506271-oldversionnumber)Added [NSMergeConflict.persistedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506412-persistedsnapshot)Added [NSMergeConflict.sourceObject](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506809-sourceobject)Added [NSMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy)Added [-[NSMergePolicy initWithMergeType:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506763-init)Added [NSMergePolicy.mergeType](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506675-mergetype)Added [-[NSMergePolicy resolveConflicts:error:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506253-resolveconflicts)Added [NSErrorMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nserrormergepolicytype)Added [NSMergeByPropertyObjectTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype)Added [NSMergeByPropertyStoreTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype)Added [NSMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype)Added [NSOverwriteMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsoverwritemergepolicytype)Added [NSRollbackMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsrollbackmergepolicytype)NSMigrationManager.hAdded [-[NSMigrationManager setUsesStoreSpecificMigrationManager:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417606-usesstorespecificmigrationmanage)Added [-[NSMigrationManager usesStoreSpecificMigrationManager]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417606-usesstorespecificmigrationmanage)NSPersistentStoreCoordinator.hAdded [-[NSPersistentStoreCoordinator executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468872-execute)Added [NSPersistentStoreDidImportUbiquitousContentChangesNotification](https://developer.apple.com/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification)Added [NSPersistentStoreUbiquitousContentNameKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey)Added [NSPersistentStoreUbiquitousContentURLKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontenturlkey)NSPersistentStoreRequest.hAdded [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)Added [-[NSPersistentStoreRequest affectedStores]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)Added [-[NSPersistentStoreRequest requestType]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506892-requesttype)Added [-[NSPersistentStoreRequest setAffectedStores:]](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)Added [NSFetchRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/fetchrequesttype)Added [NSPersistentStoreRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)Added [NSSaveRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/saverequesttype)NSRelationshipDescription.hAdded [-[NSRelationshipDescription isOrdered]](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506382-isordered)Added [-[NSRelationshipDescription setOrdered:]](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506382-isordered)NSSaveChangesRequest.hAdded [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest)Added [-[NSSaveChangesRequest deletedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500420-deletedobjects)Added [-[NSSaveChangesRequest initWithInsertedObjects:updatedObjects:deletedObjects:lockedObjects:]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500418-init)Added [-[NSSaveChangesRequest insertedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500416-insertedobjects)Added [-[NSSaveChangesRequest lockedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500426-lockedobjects)Added [-[NSSaveChangesRequest updatedObjects]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500424-updatedobjects)

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
