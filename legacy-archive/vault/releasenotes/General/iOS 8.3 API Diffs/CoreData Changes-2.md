---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreData.html
archived_at: '2026-07-18T02:56:22.278893Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreData Changes

## CoreData

Modified NSAtomicStore.addCacheNodes(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addCacheNodes(_ cacheNodes: NSSet) ``` | iOS 8.0 |
| To | ``` func addCacheNodes(_ cacheNodes: Set<NSObject>) ``` | iOS 8.3 |

Modified NSAtomicStore.cacheNodes() -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cacheNodes() -> NSSet ``` | iOS 8.0 |
| To | ``` func cacheNodes() -> Set<NSObject> ``` | iOS 8.3 |

Modified NSAtomicStore.willRemoveCacheNodes(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willRemoveCacheNodes(_ cacheNodes: NSSet) ``` | iOS 8.0 |
| To | ``` func willRemoveCacheNodes(_ cacheNodes: Set<NSObject>) ``` | iOS 8.3 |

Modified NSAttributeType.ObjectIDAttributeType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAttributeType.TransformableAttributeType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityDescription.subentities

|  | Declaration |
| --- | --- |
| From | ``` var subentities: [AnyObject] ``` |
| To | ``` var subentities: [AnyObject]? ``` |

Modified NSEntityDescription.subentitiesByName

|  | Declaration |
| --- | --- |
| From | ``` var subentitiesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var subentitiesByName: [NSObject : AnyObject]? { get } ``` |

Modified NSFetchRequestResultType.CountResultType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequestResultType.DictionaryResultType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.didChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: NSSet) ``` | iOS 8.0 |
| To | ``` func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` | iOS 8.3 |

Modified NSManagedObject.willChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: NSSet) ``` | iOS 8.0 |
| To | ``` func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` | iOS 8.3 |

Modified NSManagedObjectContext.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet { get } ``` |
| To | ``` var deletedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.insertedObjects

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: NSSet { get } ``` |
| To | ``` var insertedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.registeredObjects

|  | Declaration |
| --- | --- |
| From | ``` var registeredObjects: NSSet { get } ``` |
| To | ``` var registeredObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.updatedObjects

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: NSSet { get } ``` |
| To | ``` var updatedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectModel.init(byMergingModels: [AnyObject], forStoreMetadata:[NSObject: AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectModel.versionIdentifiers

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var versionIdentifiers: NSSet ``` |
| To | ``` var versionIdentifiers: Set<NSObject> ``` |

Modified NSSaveChangesRequest.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet? { get } ``` |
| To | ``` var deletedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.insertedObjects

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: NSSet? { get } ``` |
| To | ``` var insertedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.init(insertedObjects: Set<NSObject>?, updatedObjects: Set<NSObject>?, deletedObjects: Set<NSObject>?, lockedObjects: Set<NSObject>?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(insertedObjects insertedObjects: NSSet?, updatedObjects updatedObjects: NSSet?, deletedObjects deletedObjects: NSSet?, lockedObjects lockedObjects: NSSet?) ``` | iOS 8.0 |
| To | ``` init(insertedObjects insertedObjects: Set<NSObject>?, updatedObjects updatedObjects: Set<NSObject>?, deletedObjects deletedObjects: Set<NSObject>?, lockedObjects lockedObjects: Set<NSObject>?) ``` | iOS 8.3 |

Modified NSSaveChangesRequest.lockedObjects

|  | Declaration |
| --- | --- |
| From | ``` var lockedObjects: NSSet? { get } ``` |
| To | ``` var lockedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.updatedObjects

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: NSSet? { get } ``` |
| To | ``` var updatedObjects: Set<NSObject>? { get } ``` |

Modified NSAddedPersistentStoresKey

|  | Declaration |
| --- | --- |
| From | ``` let NSAddedPersistentStoresKey: NSString! ``` |
| To | ``` let NSAddedPersistentStoresKey: String ``` |

Modified NSAffectedObjectsErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSAffectedObjectsErrorKey: NSString! ``` |
| To | ``` let NSAffectedObjectsErrorKey: String ``` |

Modified NSAffectedStoresErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSAffectedStoresErrorKey: NSString! ``` |
| To | ``` let NSAffectedStoresErrorKey: String ``` |

Modified NSBinaryStoreType

|  | Declaration |
| --- | --- |
| From | ``` let NSBinaryStoreType: NSString! ``` |
| To | ``` let NSBinaryStoreType: String ``` |

Modified NSDeletedObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSDeletedObjectsKey: NSString! ``` |
| To | ``` let NSDeletedObjectsKey: String ``` |

Modified NSDetailedErrorsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSDetailedErrorsKey: NSString! ``` |
| To | ``` let NSDetailedErrorsKey: String ``` |

Modified NSIgnorePersistentStoreVersioningOption

|  | Declaration |
| --- | --- |
| From | ``` let NSIgnorePersistentStoreVersioningOption: NSString! ``` |
| To | ``` let NSIgnorePersistentStoreVersioningOption: String ``` |

Modified NSInMemoryStoreType

|  | Declaration |
| --- | --- |
| From | ``` let NSInMemoryStoreType: NSString! ``` |
| To | ``` let NSInMemoryStoreType: String ``` |

Modified NSInferMappingModelAutomaticallyOption

|  | Declaration |
| --- | --- |
| From | ``` let NSInferMappingModelAutomaticallyOption: NSString! ``` |
| To | ``` let NSInferMappingModelAutomaticallyOption: String ``` |

Modified NSInsertedObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSInsertedObjectsKey: NSString! ``` |
| To | ``` let NSInsertedObjectsKey: String ``` |

Modified NSInvalidatedAllObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidatedAllObjectsKey: NSString! ``` |
| To | ``` let NSInvalidatedAllObjectsKey: String ``` |

Modified NSInvalidatedObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSInvalidatedObjectsKey: NSString! ``` |
| To | ``` let NSInvalidatedObjectsKey: String ``` |

Modified NSManagedObjectContextDidSaveNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSManagedObjectContextDidSaveNotification: NSString! ``` |
| To | ``` let NSManagedObjectContextDidSaveNotification: String ``` |

Modified NSManagedObjectContextObjectsDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSManagedObjectContextObjectsDidChangeNotification: NSString! ``` |
| To | ``` let NSManagedObjectContextObjectsDidChangeNotification: String ``` |

Modified NSManagedObjectContextWillSaveNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSManagedObjectContextWillSaveNotification: NSString! ``` |
| To | ``` let NSManagedObjectContextWillSaveNotification: String ``` |

Modified NSMigratePersistentStoresAutomaticallyOption

|  | Declaration |
| --- | --- |
| From | ``` let NSMigratePersistentStoresAutomaticallyOption: NSString! ``` |
| To | ``` let NSMigratePersistentStoresAutomaticallyOption: String ``` |

Modified NSMigrationDestinationObjectKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationDestinationObjectKey: NSString! ``` |
| To | ``` let NSMigrationDestinationObjectKey: String ``` |

Modified NSMigrationEntityMappingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationEntityMappingKey: NSString! ``` |
| To | ``` let NSMigrationEntityMappingKey: String ``` |

Modified NSMigrationEntityPolicyKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationEntityPolicyKey: NSString! ``` |
| To | ``` let NSMigrationEntityPolicyKey: String ``` |

Modified NSMigrationManagerKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationManagerKey: NSString! ``` |
| To | ``` let NSMigrationManagerKey: String ``` |

Modified NSMigrationPropertyMappingKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationPropertyMappingKey: NSString! ``` |
| To | ``` let NSMigrationPropertyMappingKey: String ``` |

Modified NSMigrationSourceObjectKey

|  | Declaration |
| --- | --- |
| From | ``` let NSMigrationSourceObjectKey: NSString! ``` |
| To | ``` let NSMigrationSourceObjectKey: String ``` |

Modified NSPersistentStoreCoordinatorStoresDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreCoordinatorStoresDidChangeNotification: NSString! ``` |
| To | ``` let NSPersistentStoreCoordinatorStoresDidChangeNotification: String ``` |

Modified NSPersistentStoreCoordinatorStoresWillChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreCoordinatorStoresWillChangeNotification: NSString! ``` |
| To | ``` let NSPersistentStoreCoordinatorStoresWillChangeNotification: String ``` |

Modified NSPersistentStoreCoordinatorWillRemoveStoreNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreCoordinatorWillRemoveStoreNotification: NSString! ``` |
| To | ``` let NSPersistentStoreCoordinatorWillRemoveStoreNotification: String ``` |

Modified NSPersistentStoreDidImportUbiquitousContentChangesNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreDidImportUbiquitousContentChangesNotification: NSString! ``` |
| To | ``` let NSPersistentStoreDidImportUbiquitousContentChangesNotification: String ``` |

Modified NSPersistentStoreFileProtectionKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreFileProtectionKey: NSString! ``` |
| To | ``` let NSPersistentStoreFileProtectionKey: String ``` |

Modified NSPersistentStoreOSCompatibility

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreOSCompatibility: NSString! ``` |
| To | ``` let NSPersistentStoreOSCompatibility: String ``` |

Modified NSPersistentStoreRebuildFromUbiquitousContentOption

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreRebuildFromUbiquitousContentOption: NSString! ``` |
| To | ``` let NSPersistentStoreRebuildFromUbiquitousContentOption: String ``` |

Modified NSPersistentStoreRemoveUbiquitousMetadataOption

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreRemoveUbiquitousMetadataOption: NSString! ``` |
| To | ``` let NSPersistentStoreRemoveUbiquitousMetadataOption: String ``` |

Modified NSPersistentStoreSaveConflictsErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreSaveConflictsErrorKey: NSString! ``` |
| To | ``` let NSPersistentStoreSaveConflictsErrorKey: String ``` |

Modified NSPersistentStoreTimeoutOption

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreTimeoutOption: NSString! ``` |
| To | ``` let NSPersistentStoreTimeoutOption: String ``` |

Modified NSPersistentStoreUbiquitousContainerIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContainerIdentifierKey: NSString! ``` |
| To | ``` let NSPersistentStoreUbiquitousContainerIdentifierKey: String ``` |

Modified NSPersistentStoreUbiquitousContentNameKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContentNameKey: NSString! ``` |
| To | ``` let NSPersistentStoreUbiquitousContentNameKey: String ``` |

Modified NSPersistentStoreUbiquitousContentURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContentURLKey: NSString! ``` |
| To | ``` let NSPersistentStoreUbiquitousContentURLKey: String ``` |

Modified NSPersistentStoreUbiquitousPeerTokenOption

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreUbiquitousPeerTokenOption: NSString! ``` |
| To | ``` let NSPersistentStoreUbiquitousPeerTokenOption: String ``` |

Modified NSPersistentStoreUbiquitousTransitionTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSPersistentStoreUbiquitousTransitionTypeKey: NSString! ``` |
| To | ``` let NSPersistentStoreUbiquitousTransitionTypeKey: String ``` |

Modified NSReadOnlyPersistentStoreOption

|  | Declaration |
| --- | --- |
| From | ``` let NSReadOnlyPersistentStoreOption: NSString! ``` |
| To | ``` let NSReadOnlyPersistentStoreOption: String ``` |

Modified NSRefreshedObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSRefreshedObjectsKey: NSString! ``` |
| To | ``` let NSRefreshedObjectsKey: String ``` |

Modified NSRemovedPersistentStoresKey

|  | Declaration |
| --- | --- |
| From | ``` let NSRemovedPersistentStoresKey: NSString! ``` |
| To | ``` let NSRemovedPersistentStoresKey: String ``` |

Modified NSSQLiteAnalyzeOption

|  | Declaration |
| --- | --- |
| From | ``` let NSSQLiteAnalyzeOption: NSString! ``` |
| To | ``` let NSSQLiteAnalyzeOption: String ``` |

Modified NSSQLiteErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NSSQLiteErrorDomain: NSString! ``` |
| To | ``` let NSSQLiteErrorDomain: String ``` |

Modified NSSQLiteManualVacuumOption

|  | Declaration |
| --- | --- |
| From | ``` let NSSQLiteManualVacuumOption: NSString! ``` |
| To | ``` let NSSQLiteManualVacuumOption: String ``` |

Modified NSSQLitePragmasOption

|  | Declaration |
| --- | --- |
| From | ``` let NSSQLitePragmasOption: NSString! ``` |
| To | ``` let NSSQLitePragmasOption: String ``` |

Modified NSSQLiteStoreType

|  | Declaration |
| --- | --- |
| From | ``` let NSSQLiteStoreType: NSString! ``` |
| To | ``` let NSSQLiteStoreType: String ``` |

Modified NSStoreModelVersionHashesKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStoreModelVersionHashesKey: NSString! ``` |
| To | ``` let NSStoreModelVersionHashesKey: String ``` |

Modified NSStoreModelVersionIdentifiersKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStoreModelVersionIdentifiersKey: NSString! ``` |
| To | ``` let NSStoreModelVersionIdentifiersKey: String ``` |

Modified NSStoreTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStoreTypeKey: NSString! ``` |
| To | ``` let NSStoreTypeKey: String ``` |

Modified NSStoreUUIDKey

|  | Declaration |
| --- | --- |
| From | ``` let NSStoreUUIDKey: NSString! ``` |
| To | ``` let NSStoreUUIDKey: String ``` |

Modified NSUUIDChangedPersistentStoresKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUUIDChangedPersistentStoresKey: NSString! ``` |
| To | ``` let NSUUIDChangedPersistentStoresKey: String ``` |

Modified NSUpdatedObjectsKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUpdatedObjectsKey: NSString! ``` |
| To | ``` let NSUpdatedObjectsKey: String ``` |

Modified NSValidationKeyErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSValidationKeyErrorKey: NSString! ``` |
| To | ``` let NSValidationKeyErrorKey: String ``` |

Modified NSValidationObjectErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSValidationObjectErrorKey: NSString! ``` |
| To | ``` let NSValidationObjectErrorKey: String ``` |

Modified NSValidationPredicateErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSValidationPredicateErrorKey: NSString! ``` |
| To | ``` let NSValidationPredicateErrorKey: String ``` |

Modified NSValidationValueErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let NSValidationValueErrorKey: NSString! ``` |
| To | ``` let NSValidationValueErrorKey: String ``` |

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
