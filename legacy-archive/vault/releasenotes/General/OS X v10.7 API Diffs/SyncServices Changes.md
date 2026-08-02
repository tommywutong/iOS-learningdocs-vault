---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/SyncServices.html
archived_at: '2026-07-18T02:54:40.360602Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# SyncServices Changes

## SyncServices

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

ISyncChange.hModified -[ISyncChange type]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertyActionKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangeType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncChange changes]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncChange changeWithType:recordIdentifier:changes:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertyValueKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncChange recordIdentifier]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncChange record]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncChange initWithChangeType:recordIdentifier:changes:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertyClear

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertySet

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertyNameKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncChangePropertyValueIsDefaultKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncClient.hModified ISyncStatus

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient imagePath]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient clientIdentifier]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient lastSyncStatusForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient canPullChangesForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncClientTypeApplication

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient syncAlertToolPath]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setShouldReplaceClientRecords:forEntityNames:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient shouldSynchronizeWithClientsOfType:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient filters]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncClientTypeServer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient objectForKey:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setEnabled:forEntityNames:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient formatsRelationships]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient enabledEntityNames]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient canPushChangesForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient displayName]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient clientType]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setSyncAlertToolPath:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setImagePath:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient shouldReplaceClientRecordsForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient lastSyncDateForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setObject:forKey:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setSyncAlertHandler:selector:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setShouldSynchronize:withClientsOfType:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setFilters:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setFormatsRelationships:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient supportedEntityNames]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncClientTypePeer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncClientTypeDevice

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient setDisplayName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncClient isEnabledForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncCommon.hAdded #def SYNCSERVICESUI_EXPORTAdded #def SYNCSERVICESUI_EXPORT_DEFINITIONAdded #def SYNCSERVICESUI_IMPORTAdded #def SYNCSERVICES_EXPORT_DEFINITIONAdded #def SYNCSERVICES_EXTERNAdded #def SYNCSERVICES_IMPORTISyncConflictPropertyType.hAdded ISyncConflictPropertyTypeAdded -[ISyncConflictPropertyType enumValues]Added -[ISyncConflictPropertyType isRelationship]Added -[ISyncConflictPropertyType isRequired]Added -[ISyncConflictPropertyType isToMany]Added -[ISyncConflictPropertyType name]Added -[ISyncConflictPropertyType subtype]Added -[ISyncConflictPropertyType type]ISyncCoreData.hModified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willDeleteRecordWithIdentifier:inSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didCommitChanges:inSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPushRecord:forManagedObject:inSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willApplyChange:toManagedObject:inSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didPullChangesInSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinatorShouldStartSyncing:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didPushChangesInSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinator setStoresFastSyncDetailsAtURL:forPersistentStore:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didApplyChange:toManagedObject:inSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPushChangesInSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didCancelSyncSession:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:didFinishSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinator syncWithClient:inBackground:handler:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing persistentStoreCoordinator:willPullChangesInSyncSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSPersistentStoreCoordinatorSyncing managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncFilter.hModified +[ISyncFilter filterMatchingAllFilters:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncFiltering isEqual:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncFilter filterMatchingAtLeastOneFilter:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncFiltering shouldApplyRecord:withRecordIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncFiltering supportedEntityNames]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncManager.hModified -[ISyncManager unregisterClient:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager clientWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager syncDisabledReason]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncServerUnavailableException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager requestModes]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager clientWithIdentifier:needsSyncing:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncAvailabilityChangedNotification

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncManager sharedManager]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager isEnabled]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager unregisterSchemaWithName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager registerClientWithIdentifier:descriptionFilePath:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager removeRequestMode:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager snapshotOfRecordsInTruthWithEntityNames:usingIdentifiersForClient:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager registerSchemaWithBundlePath:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncManager addRequestMode:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncRecordSnapshot.hModified -[ISyncRecordSnapshot recordsWithMatchingAttributes:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncRecordSnapshot recordsWithIdentifiers:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncRecordSnapshot sourceIdentifiersForRelationshipName:withTargetIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncRecordSnapshot recordIdentifierForReference:isModified:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncRecordSnapshot recordReferenceForRecordWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncRecordSnapshot targetIdentifiersForRelationshipName:withSourceIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncSession.hModified -[ISyncSession setClientInfo:forRecordWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession prepareToPullChangesInBackgroundForEntityNames:target:selector:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientDidResetEntityNames:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientChangedRecordIdentifiers:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSession beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession shouldPushAllRecordsForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncSessionUnavailableException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidRecordReasonsKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidRecordsKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSession beginSessionWithClient:entityNames:beforeDate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncRecordEntityNameKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncSessionCancelledException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidRecordIdentifiersKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientCommittedAcceptedChangesWithNextAnchors:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession pushChange:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientAcceptedChangesForRecordWithIdentifier:formattedRecord:newRecordIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession finishSyncing]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientLostRecordWithIdentifier:shouldReplaceOnNextSync:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession shouldPushChangesForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientCommittedAcceptedChanges]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSession beginSessionInBackgroundWithClient:entityNames:target:selector:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession changeEnumeratorForEntityNames:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSession beginSessionWithClient:entityNames:beforeDate:lastAnchors:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession cancelSyncing]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession prepareToPullChangesForEntityNames:beforeDate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSession cancelPreviousBeginSessionWithClient:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession deleteRecordWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession shouldPullChangesForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession isCancelled]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientInfoForRecordWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidEntityException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidRecordException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession ping]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientRefusedChangesForRecordWithIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncUnsupportedEntityException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession pushChangesFromRecord:withIdentifier:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientFinishedPushingChangesWithNextAnchors:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession clientWantsToPushAllRecordsForEntityNames:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession shouldReplaceAllRecordsOnClientForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSession snapshotOfRecordsInTruth]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncSessionDriver.hRemoved -[NSObject changedRecordsForEntityName:moreComing:error:]Removed -[NSObject changesForEntityName:moreComing:error:]Removed -[NSObject entityNamesToPull]Removed -[NSObject entityNamesToSync]Removed -[NSObject identifiersForRecordsToDeleteForEntityName:moreComing:error:]Removed -[NSObject lastAnchorForEntityName:]Removed -[NSObject nextAnchorForEntityName:]Removed -[NSObject sessionBeginTimeout]Removed -[NSObject sessionPullChangesTimeout]Removed NSObject(ISyncSessionDriverDataSourceOptionalMethods)Added -[ISyncSessionDriverDataSource changedRecordsForEntityName:moreComing:error:]Added -[ISyncSessionDriverDataSource changesForEntityName:moreComing:error:]Added -[ISyncSessionDriverDataSource entityNamesToPull]Added -[ISyncSessionDriverDataSource entityNamesToSync]Added -[ISyncSessionDriverDataSource identifiersForRecordsToDeleteForEntityName:moreComing:error:]Added -[ISyncSessionDriverDataSource lastAnchorForEntityName:]Added -[ISyncSessionDriverDataSource nextAnchorForEntityName:]Added -[ISyncSessionDriverDataSource sessionBeginTimeout]Added -[ISyncSessionDriverDataSource sessionPullChangesTimeout]Modified -[ISyncSessionDriverDataSource recordsForEntityName:moreComing:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver dataSource]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver delegate]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver session]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:willNegotiateAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver startAsynchronousSync:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource deleteAllRecordsForEntityName:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver finishSyncing]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:didPullAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:didPushAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriverDidCancelSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:didRegisterClientAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource clientIdentifier]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver sync]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver lastError]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource clientDescriptionURL]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver client]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:didNegotiateAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver setDelegate:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver setHandlesSyncAlerts:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource schemaBundleURLs]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource preferredSyncModeForEntityName:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:willPushAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriver handlesSyncAlerts]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriverWillCancelSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:didReceiveSyncAlertAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:willPullAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[ISyncSessionDriverDataSource applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriverDidFinishSession:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject sessionDriver:willFinishSessionAndReturnError:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[ISyncSessionDriver sessionDriverWithDataSource:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ISyncUIHelper.hModified -[NSObject attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[NSObject attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SyncServicesErrors.hModified ISyncInvalidArgumentsException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncErrorDomain

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ISyncInvalidSchemaException

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
