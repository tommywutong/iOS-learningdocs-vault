---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreData.html
archived_at: '2026-07-18T02:56:08.229189Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreData Changes

## CoreData

Removed NSFetchRequestResultType.valueRemoved NSSnapshotEventType.valueAdded NSFetchRequestResultType.init(rawValue: UInt)Added NSSnapshotEventType.init(rawValue: UInt)Modified NSAsynchronousFetchRequest.init(fetchRequest: NSFetchRequest, completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fetchRequest request: NSFetchRequest, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock!) ``` | iOS 8.0 |
| To | ``` init(fetchRequest request: NSFetchRequest, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock?) ``` | iOS 8.1 |

Modified NSAsynchronousFetchResult.finalResult

|  | Declaration |
| --- | --- |
| From | ``` var finalResult: [AnyObject]! { get } ``` |
| To | ``` var finalResult: [AnyObject]? { get } ``` |

Modified NSAtomicStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAtomicStore.cacheNodeForObjectID(NSManagedObjectID) -> NSAtomicStoreCacheNode?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode! ``` | iOS 8.0 |
| To | ``` func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode? ``` | iOS 8.1 |

Modified NSAtomicStoreCacheNode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAttributeDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAttributeDescription.allowsExternalBinaryDataStorage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSAttributeDescription.attributeValueClassName

|  | Declaration |
| --- | --- |
| From | ``` var attributeValueClassName: String! ``` |
| To | ``` var attributeValueClassName: String? ``` |

Modified NSAttributeDescription.defaultValue

|  | Declaration |
| --- | --- |
| From | ``` var defaultValue: AnyObject! ``` |
| To | ``` var defaultValue: AnyObject? ``` |

Modified NSAttributeDescription.valueTransformerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAttributeDescription.versionHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var versionHash: NSData! { get } ``` | iOS 8.0 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | iOS 3.0 |

Modified NSBatchUpdateRequest.init(entity: NSEntityDescription)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(entity entity: NSEntityDescription!) ``` | iOS 8.0 |
| To | ``` init(entity entity: NSEntityDescription) ``` | iOS 8.1 |

Modified NSBatchUpdateRequest.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! ``` |
| To | ``` var predicate: NSPredicate? ``` |

Modified NSBatchUpdateRequest.propertiesToUpdate

|  | Declaration |
| --- | --- |
| From | ``` var propertiesToUpdate: [NSObject : AnyObject]! ``` |
| To | ``` var propertiesToUpdate: [NSObject : AnyObject]? ``` |

Modified NSBatchUpdateResult.result

|  | Declaration |
| --- | --- |
| From | ``` var result: AnyObject! { get } ``` |
| To | ``` var result: AnyObject? { get } ``` |

Modified NSEntityDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityDescription.compoundIndexes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSEntityDescription.insertNewObjectForEntityForName(String, inManagedObjectContext: NSManagedObjectContext) -> AnyObject [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> AnyObject! ``` | iOS 8.0 |
| To | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> AnyObject ``` | iOS 8.1 |

Modified NSEntityDescription.isKindOfEntity(NSEntityDescription) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isKindOfEntity(_ entity: NSEntityDescription!) -> Bool ``` | iOS 8.0 |
| To | ``` func isKindOfEntity(_ entity: NSEntityDescription) -> Bool ``` | iOS 3.0 |

Modified NSEntityDescription.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSEntityDescription.renamingIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityDescription.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSEntityDescription.versionHash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityDescription.versionHashModifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHashModifier: String! ``` | iOS 8.0 |
| To | ``` var versionHashModifier: String? ``` | iOS 3.0 |

Modified NSEntityMapping

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityMapping.attributeMappings

|  | Declaration |
| --- | --- |
| From | ``` var attributeMappings: [AnyObject]! ``` |
| To | ``` var attributeMappings: [AnyObject]? ``` |

Modified NSEntityMapping.destinationEntityName

|  | Declaration |
| --- | --- |
| From | ``` var destinationEntityName: String! ``` |
| To | ``` var destinationEntityName: String? ``` |

Modified NSEntityMapping.destinationEntityVersionHash

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var destinationEntityVersionHash: NSData! ``` |
| To | ``` @NSCopying var destinationEntityVersionHash: NSData? ``` |

Modified NSEntityMapping.sourceExpression

|  | Declaration |
| --- | --- |
| From | ``` var sourceExpression: NSExpression! ``` |
| To | ``` var sourceExpression: NSExpression? ``` |

Modified NSEntityMigrationPolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSEntityMigrationPolicy.beginEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func beginEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance(NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject!, entityMapping mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.createRelationshipsForDestinationInstance(NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject!, entityMapping mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.endEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func endEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.endInstanceCreationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSEntityMigrationPolicy.performCustomValidationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSExpressionDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSExpressionDescription.expression

|  | Declaration |
| --- | --- |
| From | ``` var expression: NSExpression! ``` |
| To | ``` var expression: NSExpression? ``` |

Modified NSFetchRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! ``` |
| To | ``` var entity: NSEntityDescription? ``` |

Modified NSFetchRequest.entityName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var entityName: String! { get } ``` | iOS 8.0 |
| To | ``` var entityName: String? { get } ``` | iOS 4.0 |

Modified NSFetchRequest.init(entityName: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified NSFetchRequest.fetchBatchSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.fetchOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.havingPredicate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var havingPredicate: NSPredicate! ``` | iOS 8.0 |
| To | ``` var havingPredicate: NSPredicate? ``` | iOS 5.0 |

Modified NSFetchRequest.includesPendingChanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.includesPropertyValues

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.includesSubentities

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! ``` |
| To | ``` var predicate: NSPredicate? ``` |

Modified NSFetchRequest.propertiesToFetch

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var propertiesToFetch: [AnyObject]! ``` | iOS 8.0 |
| To | ``` var propertiesToFetch: [AnyObject]? ``` | iOS 3.0 |

Modified NSFetchRequest.propertiesToGroupBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var propertiesToGroupBy: [AnyObject]! ``` | iOS 8.0 |
| To | ``` var propertiesToGroupBy: [AnyObject]? ``` | iOS 5.0 |

Modified NSFetchRequest.relationshipKeyPathsForPrefetching

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var relationshipKeyPathsForPrefetching: [AnyObject]! ``` | iOS 8.0 |
| To | ``` var relationshipKeyPathsForPrefetching: [AnyObject]? ``` | iOS 3.0 |

Modified NSFetchRequest.resultType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.returnsDistinctResults

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.returnsObjectsAsFaults

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequest.shouldRefreshRefetchedObjects

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSFetchRequest.sortDescriptors

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! ``` |
| To | ``` var sortDescriptors: [AnyObject]? ``` |

Modified NSFetchRequestExpression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchRequestExpression.contextExpression

|  | Declaration |
| --- | --- |
| From | ``` var contextExpression: NSExpression! { get } ``` |
| To | ``` var contextExpression: NSExpression { get } ``` |

Modified NSFetchRequestExpression.expressionForFetch(NSExpression, context: NSExpression, countOnly: Bool) -> NSExpression [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func expressionForFetch(_ fetch: NSExpression!, context context: NSExpression!, countOnly countFlag: Bool) -> NSExpression! ``` | iOS 8.0 |
| To | ``` class func expressionForFetch(_ fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression ``` | iOS 8.1 |

Modified NSFetchRequestExpression.requestExpression

|  | Declaration |
| --- | --- |
| From | ``` var requestExpression: NSExpression! { get } ``` |
| To | ``` var requestExpression: NSExpression { get } ``` |

Modified NSFetchRequestResultType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSFetchRequestResultType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` |
| To | ``` struct NSFetchRequestResultType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` |

Modified NSFetchRequestResultType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFetchedPropertyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchedPropertyDescription.fetchRequest

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest! ``` |
| To | ``` var fetchRequest: NSFetchRequest? ``` |

Modified NSFetchedResultsChangeType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchedResultsController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSFetchedResultsController.fetchRequest

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest! { get } ``` |
| To | ``` var fetchRequest: NSFetchRequest { get } ``` |

Modified NSFetchedResultsController.objectAtIndexPath(NSIndexPath) -> AnyObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func objectAtIndexPath(_ indexPath: NSIndexPath) -> AnyObject! ``` | iOS 8.0 |
| To | ``` func objectAtIndexPath(_ indexPath: NSIndexPath) -> AnyObject ``` | iOS 8.1 |

Modified NSFetchedResultsController.sectionIndexTitleForSectionName(String?) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sectionIndexTitleForSectionName(_ sectionName: String) -> String! ``` | iOS 8.0 |
| To | ``` func sectionIndexTitleForSectionName(_ sectionName: String?) -> String? ``` | iOS 8.1 |

Modified NSFetchedResultsController.sectionIndexTitles

|  | Declaration |
| --- | --- |
| From | ``` var sectionIndexTitles: [AnyObject]! { get } ``` |
| To | ``` var sectionIndexTitles: [AnyObject] { get } ``` |

Modified NSFetchedResultsControllerDelegate.controller(NSFetchedResultsController, sectionIndexTitleForSectionName: String?) -> String?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func controller(_ controller: NSFetchedResultsController, sectionIndexTitleForSectionName sectionName: String!) -> String! ``` | iOS 8.0 |
| To | ``` optional func controller(_ controller: NSFetchedResultsController, sectionIndexTitleForSectionName sectionName: String?) -> String? ``` | iOS 4.0 |

Modified NSFetchedResultsSectionInfo.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified NSIncrementalStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSIncrementalStore.newObjectIDForEntity(NSEntityDescription, referenceObject: AnyObject) -> NSManagedObjectID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject!) -> NSManagedObjectID! ``` | iOS 8.0 |
| To | ``` func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID ``` | iOS 8.1 |

Modified NSIncrementalStore.newValueForRelationship(NSRelationshipDescription, forObjectWithID: NSManagedObjectID, withContext: NSManagedObjectContext?, error: NSErrorPointer) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription!, forObjectWithID objectID: NSManagedObjectID!, withContext context: NSManagedObjectContext!, error error: NSErrorPointer) -> AnyObject? ``` | iOS 8.0 |
| To | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?, error error: NSErrorPointer) -> AnyObject? ``` | iOS 8.1 |

Modified NSIncrementalStore.referenceObjectForObjectID(NSManagedObjectID) -> AnyObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID!) -> AnyObject! ``` | iOS 8.0 |
| To | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject ``` | iOS 8.1 |

Modified NSIncrementalStoreNode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSIncrementalStoreNode.init(objectID: NSManagedObjectID, withValues:[NSObject: AnyObject], version: UInt64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(objectID objectID: NSManagedObjectID!, withValues values: [NSObject : AnyObject]!, version version: UInt64) ``` | iOS 8.0 |
| To | ``` init(objectID objectID: NSManagedObjectID, withValues values: [NSObject : AnyObject], version version: UInt64) ``` | iOS 8.1 |

Modified NSIncrementalStoreNode.valueForPropertyDescription(NSPropertyDescription) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject! ``` | iOS 8.0 |
| To | ``` func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? ``` | iOS 8.1 |

Modified NSManagedObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.awakeFromSnapshotEvents(NSSnapshotEventType)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.changedValuesForCurrentEvent() -> [NSObject: AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.init(entity: NSEntityDescription, insertIntoManagedObjectContext: NSManagedObjectContext?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext!) ``` | iOS 8.0 |
| To | ``` init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?) ``` | iOS 8.1 |

Modified NSManagedObject.faultingState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.hasChanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObject.hasFaultForRelationshipNamed(String) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.managedObjectContext

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var managedObjectContext: NSManagedObjectContext! { get } ``` |
| To | ``` unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get } ``` |

Modified NSManagedObject.prepareForDeletion()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObject.willAccessValueForKey(String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willAccessValueForKey(_ key: String!) ``` | iOS 8.0 |
| To | ``` func willAccessValueForKey(_ key: String?) ``` | iOS 8.1 |

Modified NSManagedObject.willTurnIntoFault()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext.concurrencyType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectContext.init(concurrencyType: NSManagedObjectContextConcurrencyType)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectContext.countForFetchRequest(NSFetchRequest, error: NSErrorPointer) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet! { get } ``` |
| To | ``` var deletedObjects: NSSet { get } ``` |

Modified NSManagedObjectContext.existingObjectWithID(NSManagedObjectID, error: NSErrorPointer) -> NSManagedObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext.lock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSManagedObjectContext.mergeChangesFromContextDidSaveNotification(NSNotification)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext.mergePolicy

|  | Declaration |
| --- | --- |
| From | ``` var mergePolicy: AnyObject! ``` |
| To | ``` var mergePolicy: AnyObject ``` |

Modified NSManagedObjectContext.observeValueForKeyPath(String?, ofObject: AnyObject?, change:[NSObject: AnyObject]?, context: UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func observeValueForKeyPath(_ keyPath: String!, ofObject object: AnyObject!, change change: [NSObject : AnyObject]!, context context: UnsafeMutablePointer<Void>) ``` | iOS 8.0 |
| To | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [NSObject : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` | iOS 8.1 |

Modified NSManagedObjectContext.obtainPermanentIDsForObjects([AnyObject], error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContext.parentContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectContext.performBlock(() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectContext.performBlockAndWait(() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectContext.persistentStoreCoordinator

|  | Declaration |
| --- | --- |
| From | ``` var persistentStoreCoordinator: NSPersistentStoreCoordinator! ``` |
| To | ``` var persistentStoreCoordinator: NSPersistentStoreCoordinator? ``` |

Modified NSManagedObjectContext.tryLock() -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSManagedObjectContext.unlock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSManagedObjectContext.updatedObjects

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: NSSet! { get } ``` |
| To | ``` var updatedObjects: NSSet { get } ``` |

Modified NSManagedObjectContext.userInfo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var userInfo: NSMutableDictionary! { get } ``` | iOS 8.0 |
| To | ``` var userInfo: NSMutableDictionary? { get } ``` | iOS 5.0 |

Modified NSManagedObjectContextConcurrencyType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSManagedObjectID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectID.URIRepresentation() -> NSURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func URIRepresentation() -> NSURL! ``` | iOS 8.0 |
| To | ``` func URIRepresentation() -> NSURL ``` | iOS 8.1 |

Modified NSManagedObjectModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectModel.init(byMergingModels: [AnyObject], forStoreMetadata:[NSObject: AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(byMergingModels models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel ``` |
| To | ``` init?(byMergingModels models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel ``` |

Modified NSManagedObjectModel.init(byMergingModels: [AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(byMergingModels models: [AnyObject]!) -> NSManagedObjectModel ``` | iOS 8.0 |
| To | ``` init?(byMergingModels models: [AnyObject]?) -> NSManagedObjectModel ``` | iOS 8.1 |

Modified NSManagedObjectModel.configurations

|  | Declaration |
| --- | --- |
| From | ``` var configurations: [AnyObject]! { get } ``` |
| To | ``` var configurations: [AnyObject] { get } ``` |

Modified NSManagedObjectModel.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSManagedObjectModel.entityVersionHashesByName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var entityVersionHashesByName: [NSObject : AnyObject]! { get } ``` | iOS 8.0 |
| To | ``` var entityVersionHashesByName: [NSObject : AnyObject] { get } ``` | iOS 3.0 |

Modified NSManagedObjectModel.fetchRequestTemplatesByName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var fetchRequestTemplatesByName: [NSObject : AnyObject]! { get } ``` | iOS 8.0 |
| To | ``` var fetchRequestTemplatesByName: [NSObject : AnyObject] { get } ``` | iOS 3.0 |

Modified NSManagedObjectModel.isConfiguration(String?, compatibleWithStoreMetadata:[NSObject: AnyObject]?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]!) -> Bool ``` | iOS 8.0 |
| To | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]?) -> Bool ``` | iOS 3.0 |

Modified NSManagedObjectModel.mergedModelFromBundles([AnyObject]?) -> NSManagedObjectModel? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?) -> NSManagedObjectModel! ``` | iOS 8.0 |
| To | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?) -> NSManagedObjectModel? ``` | iOS 8.1 |

Modified NSManagedObjectModel.mergedModelFromBundles([AnyObject]?, forStoreMetadata:[NSObject: AnyObject]) -> NSManagedObjectModel? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel? ``` | iOS 8.0 |
| To | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?, forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel? ``` | iOS 3.0 |

Modified NSManagedObjectModel.setFetchRequestTemplate(NSFetchRequest?, forName: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String!) ``` | iOS 8.0 |
| To | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String) ``` | iOS 8.1 |

Modified NSManagedObjectModel.versionIdentifiers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMappingModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMappingModel.init(contentsOfURL: NSURL?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!) ``` | iOS 8.0 |
| To | ``` init?(contentsOfURL url: NSURL?) ``` | iOS 8.1 |

Modified NSMappingModel.entityMappings

|  | Declaration |
| --- | --- |
| From | ``` var entityMappings: [AnyObject]! ``` |
| To | ``` var entityMappings: [AnyObject]? ``` |

Modified NSMappingModel.entityMappingsByName

|  | Declaration |
| --- | --- |
| From | ``` var entityMappingsByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var entityMappingsByName: [NSObject : AnyObject] { get } ``` |

Modified NSMappingModel.init(fromBundles: [AnyObject]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(fromBundles bundles: [AnyObject]!, forSourceModel sourceModel: NSManagedObjectModel!, destinationModel destinationModel: NSManagedObjectModel!) -> NSMappingModel ``` | iOS 8.0 |
| To | ``` init?(fromBundles bundles: [AnyObject]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel ``` | iOS 8.1 |

Modified NSMappingModel.inferredMappingModelForSourceModel(NSManagedObjectModel, destinationModel: NSManagedObjectModel, error: NSErrorPointer) -> NSMappingModel? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel!, destinationModel destinationModel: NSManagedObjectModel!, error error: NSErrorPointer) -> NSMappingModel? ``` | iOS 8.0 |
| To | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel, error error: NSErrorPointer) -> NSMappingModel? ``` | iOS 3.0 |

Modified NSMergeConflict

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMergeConflict.cachedSnapshot

|  | Declaration |
| --- | --- |
| From | ``` var cachedSnapshot: [NSObject : AnyObject]! { get } ``` |
| To | ``` var cachedSnapshot: [NSObject : AnyObject] { get } ``` |

Modified NSMergeConflict.objectSnapshot

|  | Declaration |
| --- | --- |
| From | ``` var objectSnapshot: [NSObject : AnyObject]! { get } ``` |
| To | ``` var objectSnapshot: [NSObject : AnyObject]? { get } ``` |

Modified NSMergeConflict.persistedSnapshot

|  | Declaration |
| --- | --- |
| From | ``` var persistedSnapshot: [NSObject : AnyObject]! { get } ``` |
| To | ``` var persistedSnapshot: [NSObject : AnyObject]? { get } ``` |

Modified NSMergeConflict.init(source: NSManagedObject, newVersion: Int, oldVersion: Int, cachedSnapshot:[NSObject: AnyObject], persistedSnapshot:[NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(source srcObject: NSManagedObject!, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject]!, persistedSnapshot persnap: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject], persistedSnapshot persnap: [NSObject : AnyObject]?) ``` | iOS 8.1 |

Modified NSMergeConflict.sourceObject

|  | Declaration |
| --- | --- |
| From | ``` var sourceObject: NSManagedObject! { get } ``` |
| To | ``` var sourceObject: NSManagedObject { get } ``` |

Modified NSMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSMergePolicy.resolveConflicts([AnyObject], error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func resolveConflicts(_ list: [AnyObject]!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func resolveConflicts(_ list: [AnyObject], error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSMigrationManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationManager.cancelMigrationWithError(NSError)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cancelMigrationWithError(_ error: NSError!) ``` | iOS 8.0 |
| To | ``` func cancelMigrationWithError(_ error: NSError) ``` | iOS 8.1 |

Modified NSMigrationManager.destinationEntityForEntityMapping(NSEntityMapping) -> NSEntityDescription?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription! ``` | iOS 8.0 |
| To | ``` func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` | iOS 8.1 |

Modified NSMigrationManager.destinationInstancesForEntityMappingNamed(String, sourceInstances:[AnyObject]?) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [AnyObject]?) -> [AnyObject]! ``` | iOS 8.0 |
| To | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [AnyObject]?) -> [AnyObject] ``` | iOS 8.1 |

Modified NSMigrationManager.migrateStoreFromURL(NSURL, type: String, options:[NSObject: AnyObject]?, withMappingModel: NSMappingModel?, toDestinationURL: NSURL, destinationType: String, destinationOptions:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String!, options sOptions: [NSObject : AnyObject]!, withMappingModel mappings: NSMappingModel!, toDestinationURL dURL: NSURL!, destinationType dStoreType: String!, destinationOptions dOptions: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` | iOS 8.0 |
| To | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` | iOS 8.1 |

Modified NSMigrationManager.sourceEntityForEntityMapping(NSEntityMapping) -> NSEntityDescription?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription! ``` | iOS 8.0 |
| To | ``` func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` | iOS 8.1 |

Modified NSMigrationManager.sourceInstancesForEntityMappingNamed(String, destinationInstances:[AnyObject]?) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [AnyObject]?) -> [AnyObject]! ``` | iOS 8.0 |
| To | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [AnyObject]?) -> [AnyObject] ``` | iOS 8.1 |

Modified NSMigrationManager.usesStoreSpecificMigrationManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStore.configurationName

|  | Declaration |
| --- | --- |
| From | ``` var configurationName: String! { get } ``` |
| To | ``` var configurationName: String { get } ``` |

Modified NSPersistentStore.migrationManagerClass() -> AnyClass [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator, configurationName: String?, URL: NSURL, options:[NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator, configurationName name: String?, URL url: NSURL!, options options: [NSObject : AnyObject]?) ``` | iOS 8.0 |
| To | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` | iOS 8.1 |

Modified NSPersistentStoreAsynchronousResult.managedObjectContext

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectContext: NSManagedObjectContext! { get } ``` |
| To | ``` var managedObjectContext: NSManagedObjectContext { get } ``` |

Modified NSPersistentStoreAsynchronousResult.progress

|  | Declaration |
| --- | --- |
| From | ``` var progress: NSProgress! { get } ``` |
| To | ``` var progress: NSProgress? { get } ``` |

Modified NSPersistentStoreCoordinator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinator.addPersistentStoreWithType(String, configuration: String?, URL: NSURL?, options:[NSObject: AnyObject]?, error: NSErrorPointer) -> NSPersistentStore?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL!, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> NSPersistentStore? ``` | iOS 8.0 |
| To | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> NSPersistentStore? ``` | iOS 8.1 |

Modified NSPersistentStoreCoordinator.executeRequest(NSPersistentStoreRequest, withContext: NSManagedObjectContext, error: NSErrorPointer) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreCoordinator.lock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSPersistentStoreCoordinator.managedObjectIDForURIRepresentation(NSURL) -> NSManagedObjectID?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID! ``` | iOS 8.0 |
| To | ``` func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID? ``` | iOS 8.1 |

Modified NSPersistentStoreCoordinator.metadataForPersistentStoreOfType(String?, URL: NSURL, error: NSErrorPointer) -> [NSObject: AnyObject]? [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinator.performBlockAndWait(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func performBlockAndWait(_ block: (() -> Void)!) ``` |
| To | ``` func performBlockAndWait(_ block: () -> Void) ``` |

Modified NSPersistentStoreCoordinator.registerStoreClass(AnyClass?, forStoreType: String) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func registerStoreClass(_ storeClass: AnyClass!, forStoreType storeType: String) ``` | iOS 8.0 |
| To | ``` class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String) ``` | iOS 3.0 |

Modified NSPersistentStoreCoordinator.registeredStoreTypes() -> [NSObject: AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func registeredStoreTypes() -> [NSObject : AnyObject]! ``` | iOS 8.0 |
| To | ``` class func registeredStoreTypes() -> [NSObject : AnyObject] ``` | iOS 3.0 |

Modified NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStoreAtURL(NSURL, options:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreCoordinator.setMetadata([NSObject: AnyObject]?, forPersistentStore: NSPersistentStore)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setMetadata(_ metadata: [NSObject : AnyObject]!, forPersistentStore store: NSPersistentStore) ``` | iOS 8.0 |
| To | ``` func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStore store: NSPersistentStore) ``` | iOS 8.1 |

Modified NSPersistentStoreCoordinator.setMetadata([NSObject: AnyObject]?, forPersistentStoreOfType: String?, URL: NSURL, error: NSErrorPointer) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinator.setURL(NSURL, forPersistentStore: NSPersistentStore) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinator.tryLock() -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSPersistentStoreCoordinator.unlock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified NSPersistentStoreRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreRequest.affectedStores

|  | Declaration |
| --- | --- |
| From | ``` var affectedStores: [AnyObject]! ``` |
| To | ``` var affectedStores: [AnyObject]? ``` |

Modified NSPersistentStoreUbiquitousTransitionType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPropertyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.indexed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.indexedBySpotlight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.renamingIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.setValidationPredicates([AnyObject]?, withValidationWarnings:[AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setValidationPredicates(_ validationPredicates: [AnyObject]!, withValidationWarnings validationWarnings: [AnyObject]!) ``` | iOS 8.0 |
| To | ``` func setValidationPredicates(_ validationPredicates: [AnyObject]?, withValidationWarnings validationWarnings: [AnyObject]?) ``` | iOS 8.1 |

Modified NSPropertyDescription.storedInExternalRecord

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.validationPredicates

|  | Declaration |
| --- | --- |
| From | ``` var validationPredicates: [AnyObject]! { get } ``` |
| To | ``` var validationPredicates: [AnyObject] { get } ``` |

Modified NSPropertyDescription.validationWarnings

|  | Declaration |
| --- | --- |
| From | ``` var validationWarnings: [AnyObject]! { get } ``` |
| To | ``` var validationWarnings: [AnyObject] { get } ``` |

Modified NSPropertyDescription.versionHash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyDescription.versionHashModifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHashModifier: String! ``` | iOS 8.0 |
| To | ``` var versionHashModifier: String? ``` | iOS 3.0 |

Modified NSPropertyMapping

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPropertyMapping.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSRelationshipDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSRelationshipDescription.destinationEntity

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var destinationEntity: NSEntityDescription! ``` |
| To | ``` unowned(unsafe) var destinationEntity: NSEntityDescription? ``` |

Modified NSRelationshipDescription.inverseRelationship

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var inverseRelationship: NSRelationshipDescription! ``` |
| To | ``` unowned(unsafe) var inverseRelationship: NSRelationshipDescription? ``` |

Modified NSRelationshipDescription.ordered

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSRelationshipDescription.versionHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var versionHash: NSData! { get } ``` | iOS 8.0 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | iOS 3.0 |

Modified NSSaveChangesRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSSaveChangesRequest.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet! { get } ``` |
| To | ``` var deletedObjects: NSSet? { get } ``` |

Modified NSSnapshotEventType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSSnapshotEventType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` |
| To | ``` struct NSSnapshotEventType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` |

Modified NSSnapshotEventType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSAddedPersistentStoresKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAffectedObjectsErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSAffectedStoresErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSBinaryStoreType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSDeletedObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSDetailedErrorsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSErrorMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSIgnorePersistentStoreVersioningOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSInMemoryStoreType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSInferMappingModelAutomaticallyOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSInsertedObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSInvalidatedAllObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSInvalidatedObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContextDidSaveNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContextObjectsDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSManagedObjectContextWillSaveNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMergeByPropertyObjectTrumpMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMergeByPropertyStoreTrumpMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigratePersistentStoresAutomaticallyOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationDestinationObjectKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationEntityMappingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationEntityPolicyKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationManagerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationPropertyMappingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSMigrationSourceObjectKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSOverwriteMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinatorStoresDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreCoordinatorStoresWillChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreCoordinatorWillRemoveStoreNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreDidImportUbiquitousContentChangesNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreFileProtectionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreOSCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreRebuildFromUbiquitousContentOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreRemoveUbiquitousMetadataOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreSaveConflictsErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreTimeoutOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSPersistentStoreUbiquitousContainerIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreUbiquitousContentNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreUbiquitousContentURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NSPersistentStoreUbiquitousPeerTokenOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPersistentStoreUbiquitousTransitionTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSReadOnlyPersistentStoreOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSRefreshedObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSRemovedPersistentStoresKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSRollbackMergePolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSQLiteAnalyzeOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSQLiteErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSQLiteManualVacuumOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSQLitePragmasOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSSQLiteStoreType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSStoreModelVersionHashesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSStoreModelVersionIdentifiersKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSStoreTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSStoreUUIDKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUUIDChangedPersistentStoresKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSUpdatedObjectsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSValidationKeyErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSValidationObjectErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSValidationPredicateErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified NSValidationValueErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

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
