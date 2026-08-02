---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreData.html
archived_at: '2026-07-18T02:52:10.172985Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreData Changes

## CoreData

Removed NSBatchUpdateRequest.init(entityName: String!)Removed NSFetchRequestResultType.valueRemoved NSSnapshotEventType.valueAdded NSBatchUpdateRequest.init(entityName: String)Added NSFetchRequestResultType.init(rawValue: UInt)Added NSSnapshotEventType.init(rawValue: UInt)Modified NSAsynchronousFetchRequest.completionBlock

|  | Declaration |
| --- | --- |
| From | ``` var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock! { get } ``` |
| To | ``` var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get } ``` |

Modified NSAsynchronousFetchRequest.fetchRequest

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest! { get } ``` |
| To | ``` var fetchRequest: NSFetchRequest { get } ``` |

Modified NSAsynchronousFetchRequest.init(fetchRequest: NSFetchRequest, completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?)

|  | Declaration |
| --- | --- |
| From | ``` init(fetchRequest request: NSFetchRequest!, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock!) ``` |
| To | ``` init(fetchRequest request: NSFetchRequest, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock?) ``` |

Modified NSAsynchronousFetchResult.fetchRequest

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSAsynchronousFetchRequest! { get } ``` |
| To | ``` var fetchRequest: NSAsynchronousFetchRequest { get } ``` |

Modified NSAsynchronousFetchResult.finalResult

|  | Declaration |
| --- | --- |
| From | ``` var finalResult: [AnyObject]! { get } ``` |
| To | ``` var finalResult: [AnyObject]? { get } ``` |

Modified NSAtomicStore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSAtomicStore.addCacheNodes(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addCacheNodes(_ cacheNodes: NSSet!) ``` | OS X 10.10 |
| To | ``` func addCacheNodes(_ cacheNodes: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSAtomicStore.cacheNodeForObjectID(NSManagedObjectID) -> NSAtomicStoreCacheNode?

|  | Declaration |
| --- | --- |
| From | ``` func cacheNodeForObjectID(_ objectID: NSManagedObjectID!) -> NSAtomicStoreCacheNode! ``` |
| To | ``` func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode? ``` |

Modified NSAtomicStore.cacheNodes() -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cacheNodes() -> NSSet! ``` | OS X 10.10 |
| To | ``` func cacheNodes() -> Set<NSObject> ``` | OS X 10.10.3 |

Modified NSAtomicStore.newCacheNodeForManagedObject(NSManagedObject) -> NSAtomicStoreCacheNode

|  | Declaration |
| --- | --- |
| From | ``` func newCacheNodeForManagedObject(_ managedObject: NSManagedObject!) -> NSAtomicStoreCacheNode! ``` |
| To | ``` func newCacheNodeForManagedObject(_ managedObject: NSManagedObject) -> NSAtomicStoreCacheNode ``` |

Modified NSAtomicStore.newReferenceObjectForManagedObject(NSManagedObject) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject!) -> AnyObject! ``` |
| To | ``` func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject) -> AnyObject ``` |

Modified NSAtomicStore.objectIDForEntity(NSEntityDescription, referenceObject: AnyObject) -> NSManagedObjectID

|  | Declaration |
| --- | --- |
| From | ``` func objectIDForEntity(_ entity: NSEntityDescription!, referenceObject data: AnyObject!) -> NSManagedObjectID! ``` |
| To | ``` func objectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID ``` |

Modified NSAtomicStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, URL: NSURL, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator!, configurationName configurationName: String!, URL url: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |

Modified NSAtomicStore.referenceObjectForObjectID(NSManagedObjectID) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID!) -> AnyObject! ``` |
| To | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject ``` |

Modified NSAtomicStore.updateCacheNode(NSAtomicStoreCacheNode, fromManagedObject: NSManagedObject)

|  | Declaration |
| --- | --- |
| From | ``` func updateCacheNode(_ node: NSAtomicStoreCacheNode!, fromManagedObject managedObject: NSManagedObject!) ``` |
| To | ``` func updateCacheNode(_ node: NSAtomicStoreCacheNode, fromManagedObject managedObject: NSManagedObject) ``` |

Modified NSAtomicStore.willRemoveCacheNodes(Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willRemoveCacheNodes(_ cacheNodes: NSSet!) ``` | OS X 10.10 |
| To | ``` func willRemoveCacheNodes(_ cacheNodes: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSAtomicStoreCacheNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSAtomicStoreCacheNode.objectID

|  | Declaration |
| --- | --- |
| From | ``` var objectID: NSManagedObjectID! { get } ``` |
| To | ``` var objectID: NSManagedObjectID { get } ``` |

Modified NSAtomicStoreCacheNode.init(objectID: NSManagedObjectID)

|  | Declaration |
| --- | --- |
| From | ``` init(objectID moid: NSManagedObjectID!) ``` |
| To | ``` init(objectID moid: NSManagedObjectID) ``` |

Modified NSAtomicStoreCacheNode.propertyCache

|  | Declaration |
| --- | --- |
| From | ``` var propertyCache: NSMutableDictionary! ``` |
| To | ``` var propertyCache: NSMutableDictionary? ``` |

Modified NSAtomicStoreCacheNode.setValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSAtomicStoreCacheNode.valueForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject? ``` |

Modified NSAttributeDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSAttributeDescription.allowsExternalBinaryDataStorage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var valueTransformerName: String! ``` | OS X 10.10 |
| To | ``` var valueTransformerName: String? ``` | OS X 10.5 |

Modified NSAttributeDescription.versionHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHash: NSData! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | OS X 10.5 |

Modified NSAttributeType.ObjectIDAttributeType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSAttributeType.TransformableAttributeType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSBatchUpdateRequest.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! { get } ``` |
| To | ``` var entity: NSEntityDescription { get } ``` |

Modified NSBatchUpdateRequest.init(entity: NSEntityDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(entity entity: NSEntityDescription!) ``` |
| To | ``` init(entity entity: NSEntityDescription) ``` |

Modified NSBatchUpdateRequest.entityName

|  | Declaration |
| --- | --- |
| From | ``` var entityName: String! { get } ``` |
| To | ``` var entityName: String { get } ``` |

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
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSEntityDescription.attributesByName

|  | Declaration |
| --- | --- |
| From | ``` var attributesByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var attributesByName: [NSObject : AnyObject] { get } ``` |

Modified NSEntityDescription.compoundIndexes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var compoundIndexes: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var compoundIndexes: [AnyObject]? ``` | OS X 10.7 |

Modified NSEntityDescription.entityForName(String, inManagedObjectContext: NSManagedObjectContext) -> NSEntityDescription? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func entityForName(_ entityName: String!, inManagedObjectContext context: NSManagedObjectContext!) -> NSEntityDescription! ``` |
| To | ``` class func entityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSEntityDescription? ``` |

Modified NSEntityDescription.insertNewObjectForEntityForName(String, inManagedObjectContext: NSManagedObjectContext) -> AnyObject [class]

|  | Declaration |
| --- | --- |
| From | ``` class func insertNewObjectForEntityForName(_ entityName: String!, inManagedObjectContext context: NSManagedObjectContext!) -> AnyObject! ``` |
| To | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> AnyObject ``` |

Modified NSEntityDescription.isKindOfEntity(NSEntityDescription) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isKindOfEntity(_ entity: NSEntityDescription!) -> Bool ``` | OS X 10.10 |
| To | ``` func isKindOfEntity(_ entity: NSEntityDescription) -> Bool ``` | OS X 10.5 |

Modified NSEntityDescription.managedObjectClassName

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectClassName: String! ``` |
| To | ``` var managedObjectClassName: String ``` |

Modified NSEntityDescription.managedObjectModel

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectModel: NSManagedObjectModel! { get } ``` |
| To | ``` unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get } ``` |

Modified NSEntityDescription.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSEntityDescription.properties

|  | Declaration |
| --- | --- |
| From | ``` var properties: [AnyObject]! ``` |
| To | ``` var properties: [AnyObject] ``` |

Modified NSEntityDescription.propertiesByName

|  | Declaration |
| --- | --- |
| From | ``` var propertiesByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var propertiesByName: [NSObject : AnyObject] { get } ``` |

Modified NSEntityDescription.relationshipsByName

|  | Declaration |
| --- | --- |
| From | ``` var relationshipsByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var relationshipsByName: [NSObject : AnyObject] { get } ``` |

Modified NSEntityDescription.relationshipsWithDestinationEntity(NSEntityDescription) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func relationshipsWithDestinationEntity(_ entity: NSEntityDescription!) -> [AnyObject]! ``` |
| To | ``` func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [AnyObject] ``` |

Modified NSEntityDescription.renamingIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var renamingIdentifier: String! ``` | OS X 10.10 |
| To | ``` var renamingIdentifier: String ``` | OS X 10.6 |

Modified NSEntityDescription.subentities

|  | Declaration |
| --- | --- |
| From | ``` var subentities: [AnyObject]! ``` |
| To | ``` var subentities: [AnyObject]? ``` |

Modified NSEntityDescription.subentitiesByName

|  | Declaration |
| --- | --- |
| From | ``` var subentitiesByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var subentitiesByName: [NSObject : AnyObject]? { get } ``` |

Modified NSEntityDescription.superentity

|  | Declaration |
| --- | --- |
| From | ``` var superentity: NSEntityDescription! { get } ``` |
| To | ``` unowned(unsafe) var superentity: NSEntityDescription? { get } ``` |

Modified NSEntityDescription.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSEntityDescription.versionHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHash: NSData! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | OS X 10.5 |

Modified NSEntityDescription.versionHashModifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHashModifier: String! ``` | OS X 10.10 |
| To | ``` var versionHashModifier: String? ``` | OS X 10.5 |

Modified NSEntityMapping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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
| From | ``` var destinationEntityVersionHash: NSData! ``` |
| To | ``` @NSCopying var destinationEntityVersionHash: NSData? ``` |

Modified NSEntityMapping.entityMigrationPolicyClassName

|  | Declaration |
| --- | --- |
| From | ``` var entityMigrationPolicyClassName: String! ``` |
| To | ``` var entityMigrationPolicyClassName: String ``` |

Modified NSEntityMapping.relationshipMappings

|  | Declaration |
| --- | --- |
| From | ``` var relationshipMappings: [AnyObject]! ``` |
| To | ``` var relationshipMappings: [AnyObject] ``` |

Modified NSEntityMapping.sourceEntityName

|  | Declaration |
| --- | --- |
| From | ``` var sourceEntityName: String! ``` |
| To | ``` var sourceEntityName: String ``` |

Modified NSEntityMapping.sourceEntityVersionHash

|  | Declaration |
| --- | --- |
| From | ``` var sourceEntityVersionHash: NSData! ``` |
| To | ``` @NSCopying var sourceEntityVersionHash: NSData ``` |

Modified NSEntityMapping.sourceExpression

|  | Declaration |
| --- | --- |
| From | ``` var sourceExpression: NSExpression! ``` |
| To | ``` var sourceExpression: NSExpression? ``` |

Modified NSEntityMapping.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSEntityMigrationPolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSEntityMigrationPolicy.beginEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func beginEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance(NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject!, entityMapping mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.createRelationshipsForDestinationInstance(NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject!, entityMapping mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.endEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func endEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.endInstanceCreationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSEntityMigrationPolicy.performCustomValidationForEntityMapping(NSEntityMapping, manager: NSMigrationManager, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping!, manager manager: NSMigrationManager!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |

Modified NSExpressionDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSExpressionDescription.expression

|  | Declaration |
| --- | --- |
| From | ``` var expression: NSExpression! ``` |
| To | ``` var expression: NSExpression? ``` |

Modified NSFetchRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSFetchRequest.affectedStores

|  | Declaration |
| --- | --- |
| From | ``` var affectedStores: [AnyObject]! ``` |
| To | ``` var affectedStores: [AnyObject]? ``` |

Modified NSFetchRequest.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! ``` |
| To | ``` var entity: NSEntityDescription? ``` |

Modified NSFetchRequest.entityName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var entityName: String! { get } ``` | OS X 10.10 |
| To | ``` var entityName: String? { get } ``` | OS X 10.7 |

Modified NSFetchRequest.init(entityName: String)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(entityName entityName: String!) ``` | OS X 10.10 |
| To | ``` convenience init(entityName entityName: String) ``` | OS X 10.7 |

Modified NSFetchRequest.fetchBatchSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequest.fetchOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequest.havingPredicate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var havingPredicate: NSPredicate! ``` | OS X 10.10 |
| To | ``` var havingPredicate: NSPredicate? ``` | OS X 10.7 |

Modified NSFetchRequest.includesPendingChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequest.includesPropertyValues

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFetchRequest.includesSubentities

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFetchRequest.predicate

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! ``` |
| To | ``` var predicate: NSPredicate? ``` |

Modified NSFetchRequest.propertiesToFetch

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var propertiesToFetch: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var propertiesToFetch: [AnyObject]? ``` | OS X 10.6 |

Modified NSFetchRequest.propertiesToGroupBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var propertiesToGroupBy: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var propertiesToGroupBy: [AnyObject]? ``` | OS X 10.7 |

Modified NSFetchRequest.relationshipKeyPathsForPrefetching

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var relationshipKeyPathsForPrefetching: [AnyObject]! ``` | OS X 10.10 |
| To | ``` var relationshipKeyPathsForPrefetching: [AnyObject]? ``` | OS X 10.5 |

Modified NSFetchRequest.resultType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFetchRequest.returnsDistinctResults

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequest.returnsObjectsAsFaults

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFetchRequest.shouldRefreshRefetchedObjects

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSFetchRequest.sortDescriptors

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! ``` |
| To | ``` var sortDescriptors: [AnyObject]? ``` |

Modified NSFetchRequestExpression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSFetchRequestExpression.contextExpression

|  | Declaration |
| --- | --- |
| From | ``` var contextExpression: NSExpression! { get } ``` |
| To | ``` var contextExpression: NSExpression { get } ``` |

Modified NSFetchRequestExpression.expressionForFetch(NSExpression, context: NSExpression, countOnly: Bool) -> NSExpression [class]

|  | Declaration |
| --- | --- |
| From | ``` class func expressionForFetch(_ fetch: NSExpression!, context context: NSExpression!, countOnly countFlag: Bool) -> NSExpression! ``` |
| To | ``` class func expressionForFetch(_ fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression ``` |

Modified NSFetchRequestExpression.requestExpression

|  | Declaration |
| --- | --- |
| From | ``` var requestExpression: NSExpression! { get } ``` |
| To | ``` var requestExpression: NSExpression { get } ``` |

Modified NSFetchRequestResultType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFetchRequestResultType : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` | RawOptionSet |
| To | ``` struct NSFetchRequestResultType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` | RawOptionSetType |

Modified NSFetchRequestResultType.CountResultType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequestResultType.DictionaryResultType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSFetchRequestResultType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSFetchedPropertyDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSFetchedPropertyDescription.fetchRequest

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest! ``` |
| To | ``` var fetchRequest: NSFetchRequest? ``` |

Modified NSIncrementalStore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSIncrementalStore.executeRequest(NSPersistentStoreRequest, withContext: NSManagedObjectContext, error: NSErrorPointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest!, withContext context: NSManagedObjectContext!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSIncrementalStore.identifierForNewStoreAtURL(NSURL) -> AnyObject [class]

|  | Declaration |
| --- | --- |
| From | ``` class func identifierForNewStoreAtURL(_ storeURL: NSURL!) -> AnyObject! ``` |
| To | ``` class func identifierForNewStoreAtURL(_ storeURL: NSURL) -> AnyObject ``` |

Modified NSIncrementalStore.managedObjectContextDidRegisterObjectsWithIDs([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [AnyObject]!) ``` |
| To | ``` func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [AnyObject]) ``` |

Modified NSIncrementalStore.managedObjectContextDidUnregisterObjectsWithIDs([AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [AnyObject]!) ``` |
| To | ``` func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [AnyObject]) ``` |

Modified NSIncrementalStore.newObjectIDForEntity(NSEntityDescription, referenceObject: AnyObject) -> NSManagedObjectID

|  | Declaration |
| --- | --- |
| From | ``` func newObjectIDForEntity(_ entity: NSEntityDescription!, referenceObject data: AnyObject!) -> NSManagedObjectID! ``` |
| To | ``` func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID ``` |

Modified NSIncrementalStore.newValueForRelationship(NSRelationshipDescription, forObjectWithID: NSManagedObjectID, withContext: NSManagedObjectContext?, error: NSErrorPointer) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription!, forObjectWithID objectID: NSManagedObjectID!, withContext context: NSManagedObjectContext!, error error: NSErrorPointer) -> AnyObject! ``` |
| To | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?, error error: NSErrorPointer) -> AnyObject? ``` |

Modified NSIncrementalStore.newValuesForObjectWithID(NSManagedObjectID, withContext: NSManagedObjectContext, error: NSErrorPointer) -> NSIncrementalStoreNode?

|  | Declaration |
| --- | --- |
| From | ``` func newValuesForObjectWithID(_ objectID: NSManagedObjectID!, withContext context: NSManagedObjectContext!, error error: NSErrorPointer) -> NSIncrementalStoreNode! ``` |
| To | ``` func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> NSIncrementalStoreNode? ``` |

Modified NSIncrementalStore.obtainPermanentIDsForObjects([AnyObject], error: NSErrorPointer) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ array: [AnyObject]!, error error: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func obtainPermanentIDsForObjects(_ array: [AnyObject], error error: NSErrorPointer) -> [AnyObject]? ``` |

Modified NSIncrementalStore.referenceObjectForObjectID(NSManagedObjectID) -> AnyObject

|  | Declaration |
| --- | --- |
| From | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID!) -> AnyObject! ``` |
| To | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject ``` |

Modified NSIncrementalStoreNode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSIncrementalStoreNode.objectID

|  | Declaration |
| --- | --- |
| From | ``` var objectID: NSManagedObjectID! { get } ``` |
| To | ``` var objectID: NSManagedObjectID { get } ``` |

Modified NSIncrementalStoreNode.init(objectID: NSManagedObjectID, withValues:[NSObject: AnyObject], version: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(objectID objectID: NSManagedObjectID!, withValues values: [NSObject : AnyObject]!, version version: UInt64) ``` |
| To | ``` init(objectID objectID: NSManagedObjectID, withValues values: [NSObject : AnyObject], version version: UInt64) ``` |

Modified NSIncrementalStoreNode.updateWithValues([NSObject: AnyObject], version: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func updateWithValues(_ values: [NSObject : AnyObject]!, version version: UInt64) ``` |
| To | ``` func updateWithValues(_ values: [NSObject : AnyObject], version version: UInt64) ``` |

Modified NSIncrementalStoreNode.valueForPropertyDescription(NSPropertyDescription) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForPropertyDescription(_ prop: NSPropertyDescription!) -> AnyObject! ``` |
| To | ``` func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? ``` |

Modified NSManagedObject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSManagedObject.awakeFromSnapshotEvents(NSSnapshotEventType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSManagedObject.changedValues() -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func changedValues() -> [NSObject : AnyObject]! ``` |
| To | ``` func changedValues() -> [NSObject : AnyObject] ``` |

Modified NSManagedObject.changedValuesForCurrentEvent() -> [NSObject: AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func changedValuesForCurrentEvent() -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` func changedValuesForCurrentEvent() -> [NSObject : AnyObject] ``` | OS X 10.7 |

Modified NSManagedObject.committedValuesForKeys([AnyObject]?) -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func committedValuesForKeys(_ keys: [AnyObject]!) -> [NSObject : AnyObject]! ``` |
| To | ``` func committedValuesForKeys(_ keys: [AnyObject]?) -> [NSObject : AnyObject] ``` |

Modified NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSManagedObject.didAccessValueForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func didAccessValueForKey(_ key: String!) ``` |
| To | ``` func didAccessValueForKey(_ key: String) ``` |

Modified NSManagedObject.didChangeValueForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func didChangeValueForKey(_ key: String!) ``` |
| To | ``` func didChangeValueForKey(_ key: String) ``` |

Modified NSManagedObject.didChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func didChangeValueForKey(_ inKey: String!, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: NSSet!) ``` | OS X 10.10 |
| To | ``` func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSManagedObject.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! { get } ``` |
| To | ``` var entity: NSEntityDescription { get } ``` |

Modified NSManagedObject.init(entity: NSEntityDescription, insertIntoManagedObjectContext: NSManagedObjectContext?)

|  | Declaration |
| --- | --- |
| From | ``` init(entity entity: NSEntityDescription!, insertIntoManagedObjectContext context: NSManagedObjectContext!) ``` |
| To | ``` init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?) ``` |

Modified NSManagedObject.faultingState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSManagedObject.hasChanges

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSManagedObject.hasFaultForRelationshipNamed(String) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func hasFaultForRelationshipNamed(_ key: String!) -> Bool ``` | OS X 10.10 |
| To | ``` func hasFaultForRelationshipNamed(_ key: String) -> Bool ``` | OS X 10.5 |

Modified NSManagedObject.managedObjectContext

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectContext: NSManagedObjectContext! { get } ``` |
| To | ``` unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get } ``` |

Modified NSManagedObject.objectID

|  | Declaration |
| --- | --- |
| From | ``` var objectID: NSManagedObjectID! { get } ``` |
| To | ``` var objectID: NSManagedObjectID { get } ``` |

Modified NSManagedObject.observationInfo() -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func observationInfo() -> AnyObject! ``` |
| To | ``` func observationInfo() -> AnyObject? ``` |

Modified NSManagedObject.prepareForDeletion()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSManagedObject.primitiveValueForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func primitiveValueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func primitiveValueForKey(_ key: String) -> AnyObject? ``` |

Modified NSManagedObject.setObservationInfo(AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` func setObservationInfo(_ inObservationInfo: AnyObject!) ``` |
| To | ``` func setObservationInfo(_ inObservationInfo: AnyObject?) ``` |

Modified NSManagedObject.setPrimitiveValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setPrimitiveValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setPrimitiveValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSManagedObject.setValue(AnyObject?, forKey: String)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forKey key: String!) ``` |
| To | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |

Modified NSManagedObject.validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func validateValue(_ value: AutoreleasingUnsafePointer<AnyObject?>, forKey key: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` |

Modified NSManagedObject.valueForKey(String) -> AnyObject?

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func valueForKey(_ key: String) -> AnyObject? ``` |

Modified NSManagedObject.willAccessValueForKey(String?)

|  | Declaration |
| --- | --- |
| From | ``` func willAccessValueForKey(_ key: String!) ``` |
| To | ``` func willAccessValueForKey(_ key: String?) ``` |

Modified NSManagedObject.willChangeValueForKey(String)

|  | Declaration |
| --- | --- |
| From | ``` func willChangeValueForKey(_ key: String!) ``` |
| To | ``` func willChangeValueForKey(_ key: String) ``` |

Modified NSManagedObject.willChangeValueForKey(String, withSetMutation: NSKeyValueSetMutationKind, usingObjects: Set<NSObject>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func willChangeValueForKey(_ inKey: String!, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: NSSet!) ``` | OS X 10.10 |
| To | ``` func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` | OS X 10.10.3 |

Modified NSManagedObject.willTurnIntoFault()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSManagedObjectContext

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSManagedObjectContext.assignObject(AnyObject, toPersistentStore: NSPersistentStore)

|  | Declaration |
| --- | --- |
| From | ``` func assignObject(_ object: AnyObject!, toPersistentStore store: NSPersistentStore!) ``` |
| To | ``` func assignObject(_ object: AnyObject, toPersistentStore store: NSPersistentStore) ``` |

Modified NSManagedObjectContext.concurrencyType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSManagedObjectContext.init(concurrencyType: NSManagedObjectContextConcurrencyType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSManagedObjectContext.countForFetchRequest(NSFetchRequest, error: NSErrorPointer) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func countForFetchRequest(_ request: NSFetchRequest!, error error: NSErrorPointer) -> Int ``` | OS X 10.10 |
| To | ``` func countForFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> Int ``` | OS X 10.5 |

Modified NSManagedObjectContext.deleteObject(NSManagedObject)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObject(_ object: NSManagedObject!) ``` |
| To | ``` func deleteObject(_ object: NSManagedObject) ``` |

Modified NSManagedObjectContext.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet! { get } ``` |
| To | ``` var deletedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.detectConflictsForObject(NSManagedObject)

|  | Declaration |
| --- | --- |
| From | ``` func detectConflictsForObject(_ object: NSManagedObject!) ``` |
| To | ``` func detectConflictsForObject(_ object: NSManagedObject) ``` |

Modified NSManagedObjectContext.executeFetchRequest(NSFetchRequest, error: NSErrorPointer) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func executeFetchRequest(_ request: NSFetchRequest!, error error: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` func executeFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> [AnyObject]? ``` |

Modified NSManagedObjectContext.executeRequest(NSPersistentStoreRequest, error: NSErrorPointer) -> NSPersistentStoreResult?

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest!, error error: NSErrorPointer) -> NSPersistentStoreResult! ``` |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest, error error: NSErrorPointer) -> NSPersistentStoreResult? ``` |

Modified NSManagedObjectContext.existingObjectWithID(NSManagedObjectID, error: NSErrorPointer) -> NSManagedObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func existingObjectWithID(_ objectID: NSManagedObjectID!, error error: NSErrorPointer) -> NSManagedObject! ``` | OS X 10.10 |
| To | ``` func existingObjectWithID(_ objectID: NSManagedObjectID, error error: NSErrorPointer) -> NSManagedObject? ``` | OS X 10.6 |

Modified NSManagedObjectContext.insertObject(NSManagedObject)

|  | Declaration |
| --- | --- |
| From | ``` func insertObject(_ object: NSManagedObject!) ``` |
| To | ``` func insertObject(_ object: NSManagedObject) ``` |

Modified NSManagedObjectContext.insertedObjects

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: NSSet! { get } ``` |
| To | ``` var insertedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.lock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSManagedObjectContext.mergeChangesFromContextDidSaveNotification(NSNotification)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification!) ``` | OS X 10.10 |
| To | ``` func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification) ``` | OS X 10.5 |

Modified NSManagedObjectContext.mergePolicy

|  | Declaration |
| --- | --- |
| From | ``` var mergePolicy: AnyObject! ``` |
| To | ``` var mergePolicy: AnyObject ``` |

Modified NSManagedObjectContext.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSManagedObjectContext.objectRegisteredForID(NSManagedObjectID) -> NSManagedObject?

|  | Declaration |
| --- | --- |
| From | ``` func objectRegisteredForID(_ objectID: NSManagedObjectID!) -> NSManagedObject! ``` |
| To | ``` func objectRegisteredForID(_ objectID: NSManagedObjectID) -> NSManagedObject? ``` |

Modified NSManagedObjectContext.objectWithID(NSManagedObjectID) -> NSManagedObject

|  | Declaration |
| --- | --- |
| From | ``` func objectWithID(_ objectID: NSManagedObjectID!) -> NSManagedObject! ``` |
| To | ``` func objectWithID(_ objectID: NSManagedObjectID) -> NSManagedObject ``` |

Modified NSManagedObjectContext.observeValueForKeyPath(String?, ofObject: AnyObject?, change:[NSObject: AnyObject]?, context: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func observeValueForKeyPath(_ keyPath: String!, ofObject object: AnyObject!, change change: [NSObject : AnyObject]!, context context: UnsafePointer<()>) ``` |
| To | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [NSObject : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` |

Modified NSManagedObjectContext.obtainPermanentIDsForObjects([AnyObject], error: NSErrorPointer) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ objects: [AnyObject]!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` func obtainPermanentIDsForObjects(_ objects: [AnyObject], error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSManagedObjectContext.parentContext

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var parentContext: NSManagedObjectContext! ``` | OS X 10.10 |
| To | ``` var parentContext: NSManagedObjectContext? ``` | OS X 10.7 |

Modified NSManagedObjectContext.performBlock(() -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performBlock(_ block: (() -> Void)!) ``` | OS X 10.10 |
| To | ``` func performBlock(_ block: () -> Void) ``` | OS X 10.7 |

Modified NSManagedObjectContext.performBlockAndWait(() -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performBlockAndWait(_ block: (() -> Void)!) ``` | OS X 10.10 |
| To | ``` func performBlockAndWait(_ block: () -> Void) ``` | OS X 10.7 |

Modified NSManagedObjectContext.persistentStoreCoordinator

|  | Declaration |
| --- | --- |
| From | ``` var persistentStoreCoordinator: NSPersistentStoreCoordinator! ``` |
| To | ``` var persistentStoreCoordinator: NSPersistentStoreCoordinator? ``` |

Modified NSManagedObjectContext.refreshObject(NSManagedObject, mergeChanges: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func refreshObject(_ object: NSManagedObject!, mergeChanges flag: Bool) ``` |
| To | ``` func refreshObject(_ object: NSManagedObject, mergeChanges flag: Bool) ``` |

Modified NSManagedObjectContext.registeredObjects

|  | Declaration |
| --- | --- |
| From | ``` var registeredObjects: NSSet! { get } ``` |
| To | ``` var registeredObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.tryLock() -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSManagedObjectContext.undoManager

|  | Declaration |
| --- | --- |
| From | ``` var undoManager: NSUndoManager! ``` |
| To | ``` var undoManager: NSUndoManager? ``` |

Modified NSManagedObjectContext.unlock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSManagedObjectContext.updatedObjects

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: NSSet! { get } ``` |
| To | ``` var updatedObjects: Set<NSObject> { get } ``` |

Modified NSManagedObjectContext.userInfo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var userInfo: NSMutableDictionary! { get } ``` | OS X 10.10 |
| To | ``` var userInfo: NSMutableDictionary? { get } ``` | OS X 10.7 |

Modified NSManagedObjectContextConcurrencyType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSManagedObjectID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSManagedObjectID.URIRepresentation() -> NSURL

|  | Declaration |
| --- | --- |
| From | ``` func URIRepresentation() -> NSURL! ``` |
| To | ``` func URIRepresentation() -> NSURL ``` |

Modified NSManagedObjectID.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! { get } ``` |
| To | ``` var entity: NSEntityDescription { get } ``` |

Modified NSManagedObjectID.persistentStore

|  | Declaration |
| --- | --- |
| From | ``` var persistentStore: NSPersistentStore! { get } ``` |
| To | ``` weak var persistentStore: NSPersistentStore? { get } ``` |

Modified NSManagedObjectModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSManagedObjectModel.init(byMergingModels: [AnyObject], forStoreMetadata:[NSObject: AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(byMergingModels models: [AnyObject]!, forStoreMetadata metadata: [NSObject : AnyObject]!) -> NSManagedObjectModel ``` | OS X 10.10 |
| To | ``` init?(byMergingModels models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel ``` | OS X 10.5 |

Modified NSManagedObjectModel.init(byMergingModels: [AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(byMergingModels models: [AnyObject]!) -> NSManagedObjectModel ``` |
| To | ``` init?(byMergingModels models: [AnyObject]?) -> NSManagedObjectModel ``` |

Modified NSManagedObjectModel.configurations

|  | Declaration |
| --- | --- |
| From | ``` var configurations: [AnyObject]! { get } ``` |
| To | ``` var configurations: [AnyObject] { get } ``` |

Modified NSManagedObjectModel.init(contentsOfURL: NSURL)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL url: NSURL!) ``` |
| To | ``` convenience init?(contentsOfURL url: NSURL) ``` |

Modified NSManagedObjectModel.entities

|  | Declaration |
| --- | --- |
| From | ``` var entities: [AnyObject]! ``` |
| To | ``` var entities: [AnyObject] ``` |

Modified NSManagedObjectModel.entitiesByName

|  | Declaration |
| --- | --- |
| From | ``` var entitiesByName: [NSObject : AnyObject]! { get } ``` |
| To | ``` var entitiesByName: [NSObject : AnyObject] { get } ``` |

Modified NSManagedObjectModel.entitiesForConfiguration(String?) -> [AnyObject]?

|  | Declaration |
| --- | --- |
| From | ``` func entitiesForConfiguration(_ configuration: String!) -> [AnyObject]! ``` |
| To | ``` func entitiesForConfiguration(_ configuration: String?) -> [AnyObject]? ``` |

Modified NSManagedObjectModel.entityVersionHashesByName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var entityVersionHashesByName: [NSObject : AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var entityVersionHashesByName: [NSObject : AnyObject] { get } ``` | OS X 10.5 |

Modified NSManagedObjectModel.fetchRequestFromTemplateWithName(String, substitutionVariables:[NSObject: AnyObject]) -> NSFetchRequest?

|  | Declaration |
| --- | --- |
| From | ``` func fetchRequestFromTemplateWithName(_ name: String!, substitutionVariables variables: [NSObject : AnyObject]!) -> NSFetchRequest! ``` |
| To | ``` func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [NSObject : AnyObject]) -> NSFetchRequest? ``` |

Modified NSManagedObjectModel.fetchRequestTemplateForName(String) -> NSFetchRequest?

|  | Declaration |
| --- | --- |
| From | ``` func fetchRequestTemplateForName(_ name: String!) -> NSFetchRequest! ``` |
| To | ``` func fetchRequestTemplateForName(_ name: String) -> NSFetchRequest? ``` |

Modified NSManagedObjectModel.fetchRequestTemplatesByName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var fetchRequestTemplatesByName: [NSObject : AnyObject]! { get } ``` | OS X 10.10 |
| To | ``` var fetchRequestTemplatesByName: [NSObject : AnyObject] { get } ``` | OS X 10.5 |

Modified NSManagedObjectModel.isConfiguration(String?, compatibleWithStoreMetadata:[NSObject: AnyObject]?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func isConfiguration(_ configuration: String!, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]!) -> Bool ``` | OS X 10.10 |
| To | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]?) -> Bool ``` | OS X 10.5 |

Modified NSManagedObjectModel.localizationDictionary

|  | Declaration |
| --- | --- |
| From | ``` var localizationDictionary: [NSObject : AnyObject]! ``` |
| To | ``` var localizationDictionary: [NSObject : AnyObject]? ``` |

Modified NSManagedObjectModel.mergedModelFromBundles([AnyObject]?) -> NSManagedObjectModel? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]!) -> NSManagedObjectModel! ``` |
| To | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?) -> NSManagedObjectModel? ``` |

Modified NSManagedObjectModel.mergedModelFromBundles([AnyObject]?, forStoreMetadata:[NSObject: AnyObject]) -> NSManagedObjectModel? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]!, forStoreMetadata metadata: [NSObject : AnyObject]!) -> NSManagedObjectModel! ``` | OS X 10.10 |
| To | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?, forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel? ``` | OS X 10.5 |

Modified NSManagedObjectModel.setEntities([AnyObject], forConfiguration: String)

|  | Declaration |
| --- | --- |
| From | ``` func setEntities(_ entities: [AnyObject]!, forConfiguration configuration: String!) ``` |
| To | ``` func setEntities(_ entities: [AnyObject], forConfiguration configuration: String) ``` |

Modified NSManagedObjectModel.setFetchRequestTemplate(NSFetchRequest?, forName: String)

|  | Declaration |
| --- | --- |
| From | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest!, forName name: String!) ``` |
| To | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String) ``` |

Modified NSManagedObjectModel.versionIdentifiers

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionIdentifiers: NSSet! ``` | OS X 10.10 |
| To | ``` var versionIdentifiers: Set<NSObject> ``` | OS X 10.5 |

Modified NSMappingModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMappingModel.init(contentsOfURL: NSURL?)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!) ``` |
| To | ``` init?(contentsOfURL url: NSURL?) ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` init(fromBundles bundles: [AnyObject]!, forSourceModel sourceModel: NSManagedObjectModel!, destinationModel destinationModel: NSManagedObjectModel!) -> NSMappingModel ``` |
| To | ``` init?(fromBundles bundles: [AnyObject]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel ``` |

Modified NSMappingModel.inferredMappingModelForSourceModel(NSManagedObjectModel, destinationModel: NSManagedObjectModel, error: NSErrorPointer) -> NSMappingModel? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel!, destinationModel destinationModel: NSManagedObjectModel!, error error: NSErrorPointer) -> NSMappingModel! ``` | OS X 10.10 |
| To | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel, error error: NSErrorPointer) -> NSMappingModel? ``` | OS X 10.6 |

Modified NSMergeConflict

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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

|  | Declaration |
| --- | --- |
| From | ``` init(source srcObject: NSManagedObject!, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject]!, persistedSnapshot persnap: [NSObject : AnyObject]!) ``` |
| To | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject], persistedSnapshot persnap: [NSObject : AnyObject]?) ``` |

Modified NSMergeConflict.sourceObject

|  | Declaration |
| --- | --- |
| From | ``` var sourceObject: NSManagedObject! { get } ``` |
| To | ``` var sourceObject: NSManagedObject { get } ``` |

Modified NSMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSMergePolicy.resolveConflicts([AnyObject], error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func resolveConflicts(_ list: [AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func resolveConflicts(_ list: [AnyObject], error error: NSErrorPointer) -> Bool ``` |

Modified NSMigrationManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSMigrationManager.associateSourceInstance(NSManagedObject, withDestinationInstance: NSManagedObject, forEntityMapping: NSEntityMapping)

|  | Declaration |
| --- | --- |
| From | ``` func associateSourceInstance(_ sourceInstance: NSManagedObject!, withDestinationInstance destinationInstance: NSManagedObject!, forEntityMapping entityMapping: NSEntityMapping!) ``` |
| To | ``` func associateSourceInstance(_ sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, forEntityMapping entityMapping: NSEntityMapping) ``` |

Modified NSMigrationManager.cancelMigrationWithError(NSError)

|  | Declaration |
| --- | --- |
| From | ``` func cancelMigrationWithError(_ error: NSError!) ``` |
| To | ``` func cancelMigrationWithError(_ error: NSError) ``` |

Modified NSMigrationManager.currentEntityMapping

|  | Declaration |
| --- | --- |
| From | ``` var currentEntityMapping: NSEntityMapping! { get } ``` |
| To | ``` var currentEntityMapping: NSEntityMapping { get } ``` |

Modified NSMigrationManager.destinationContext

|  | Declaration |
| --- | --- |
| From | ``` var destinationContext: NSManagedObjectContext! { get } ``` |
| To | ``` var destinationContext: NSManagedObjectContext { get } ``` |

Modified NSMigrationManager.destinationEntityForEntityMapping(NSEntityMapping) -> NSEntityDescription?

|  | Declaration |
| --- | --- |
| From | ``` func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping!) -> NSEntityDescription! ``` |
| To | ``` func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` |

Modified NSMigrationManager.destinationInstancesForEntityMappingNamed(String, sourceInstances:[AnyObject]?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String!, sourceInstances sourceInstances: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [AnyObject]?) -> [AnyObject] ``` |

Modified NSMigrationManager.destinationModel

|  | Declaration |
| --- | --- |
| From | ``` var destinationModel: NSManagedObjectModel! { get } ``` |
| To | ``` var destinationModel: NSManagedObjectModel { get } ``` |

Modified NSMigrationManager.mappingModel

|  | Declaration |
| --- | --- |
| From | ``` var mappingModel: NSMappingModel! { get } ``` |
| To | ``` var mappingModel: NSMappingModel { get } ``` |

Modified NSMigrationManager.migrateStoreFromURL(NSURL, type: String, options:[NSObject: AnyObject]?, withMappingModel: NSMappingModel?, toDestinationURL: NSURL, destinationType: String, destinationOptions:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func migrateStoreFromURL(_ sourceURL: NSURL!, type sStoreType: String!, options sOptions: [NSObject : AnyObject]!, withMappingModel mappings: NSMappingModel!, toDestinationURL dURL: NSURL!, destinationType dStoreType: String!, destinationOptions dOptions: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |

Modified NSMigrationManager.sourceContext

|  | Declaration |
| --- | --- |
| From | ``` var sourceContext: NSManagedObjectContext! { get } ``` |
| To | ``` var sourceContext: NSManagedObjectContext { get } ``` |

Modified NSMigrationManager.sourceEntityForEntityMapping(NSEntityMapping) -> NSEntityDescription?

|  | Declaration |
| --- | --- |
| From | ``` func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping!) -> NSEntityDescription! ``` |
| To | ``` func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` |

Modified NSMigrationManager.sourceInstancesForEntityMappingNamed(String, destinationInstances:[AnyObject]?) -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String!, destinationInstances destinationInstances: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [AnyObject]?) -> [AnyObject] ``` |

Modified NSMigrationManager.sourceModel

|  | Declaration |
| --- | --- |
| From | ``` var sourceModel: NSManagedObjectModel! { get } ``` |
| To | ``` var sourceModel: NSManagedObjectModel { get } ``` |

Modified NSMigrationManager.init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)

|  | Declaration |
| --- | --- |
| From | ``` init(sourceModel sourceModel: NSManagedObjectModel!, destinationModel destinationModel: NSManagedObjectModel!) ``` |
| To | ``` init(sourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) ``` |

Modified NSMigrationManager.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSMigrationManager.usesStoreSpecificMigrationManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSPersistentStore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPersistentStore.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! ``` |
| To | ``` var URL: NSURL? ``` |

Modified NSPersistentStore.configurationName

|  | Declaration |
| --- | --- |
| From | ``` var configurationName: String! { get } ``` |
| To | ``` var configurationName: String { get } ``` |

Modified NSPersistentStore.didAddToPersistentStoreCoordinator(NSPersistentStoreCoordinator)

|  | Declaration |
| --- | --- |
| From | ``` func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator!) ``` |
| To | ``` func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator) ``` |

Modified NSPersistentStore.metadataForPersistentStoreWithURL(NSURL, error: NSErrorPointer) -> [NSObject: AnyObject]? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func metadataForPersistentStoreWithURL(_ url: NSURL!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` |
| To | ``` class func metadataForPersistentStoreWithURL(_ url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |

Modified NSPersistentStore.migrationManagerClass() -> AnyClass [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func migrationManagerClass() -> AnyClass! ``` | OS X 10.10 |
| To | ``` class func migrationManagerClass() -> AnyClass ``` | OS X 10.6 |

Modified NSPersistentStore.options

|  | Declaration |
| --- | --- |
| From | ``` var options: [NSObject : AnyObject]! { get } ``` |
| To | ``` var options: [NSObject : AnyObject]? { get } ``` |

Modified NSPersistentStore.persistentStoreCoordinator

|  | Declaration |
| --- | --- |
| From | ``` var persistentStoreCoordinator: NSPersistentStoreCoordinator! { get } ``` |
| To | ``` weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get } ``` |

Modified NSPersistentStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator, configurationName: String?, URL: NSURL, options:[NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator!, configurationName name: String!, URL url: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |

Modified NSPersistentStore.setMetadata([NSObject: AnyObject]?, forPersistentStoreWithURL: NSURL, error: NSErrorPointer) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]!, forPersistentStoreWithURL url: NSURL!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreWithURL url: NSURL, error error: NSErrorPointer) -> Bool ``` |

Modified NSPersistentStore.type

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: String { get } ``` |

Modified NSPersistentStore.willRemoveFromPersistentStoreCoordinator(NSPersistentStoreCoordinator)

|  | Declaration |
| --- | --- |
| From | ``` func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator!) ``` |
| To | ``` func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator) ``` |

Modified NSPersistentStoreAsynchronousResult.managedObjectContext

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectContext: NSManagedObjectContext! { get } ``` |
| To | ``` var managedObjectContext: NSManagedObjectContext { get } ``` |

Modified NSPersistentStoreAsynchronousResult.operationError

|  | Declaration |
| --- | --- |
| From | ``` var operationError: NSError! { get } ``` |
| To | ``` var operationError: NSError? { get } ``` |

Modified NSPersistentStoreAsynchronousResult.progress

|  | Declaration |
| --- | --- |
| From | ``` var progress: NSProgress! { get } ``` |
| To | ``` var progress: NSProgress? { get } ``` |

Modified NSPersistentStoreCoordinator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSPersistentStoreCoordinator.URLForPersistentStore(NSPersistentStore) -> NSURL

|  | Declaration |
| --- | --- |
| From | ``` func URLForPersistentStore(_ store: NSPersistentStore!) -> NSURL! ``` |
| To | ``` func URLForPersistentStore(_ store: NSPersistentStore) -> NSURL ``` |

Modified NSPersistentStoreCoordinator.addPersistentStoreWithType(String, configuration: String?, URL: NSURL?, options:[NSObject: AnyObject]?, error: NSErrorPointer) -> NSPersistentStore?

|  | Declaration |
| --- | --- |
| From | ``` func addPersistentStoreWithType(_ storeType: String!, configuration configuration: String!, URL storeURL: NSURL!, options options: [NSObject : AnyObject]!, error error: NSErrorPointer) -> NSPersistentStore! ``` |
| To | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> NSPersistentStore? ``` |

Modified NSPersistentStoreCoordinator.elementsDerivedFromExternalRecordURL(NSURL) -> [NSObject: AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func elementsDerivedFromExternalRecordURL(_ fileURL: NSURL!) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` class func elementsDerivedFromExternalRecordURL(_ fileURL: NSURL) -> [NSObject : AnyObject] ``` | OS X 10.6 |

Modified NSPersistentStoreCoordinator.executeRequest(NSPersistentStoreRequest, withContext: NSManagedObjectContext, error: NSErrorPointer) -> AnyObject?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest!, withContext context: NSManagedObjectContext!, error error: NSErrorPointer) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject? ``` | OS X 10.7 |

Modified NSPersistentStoreCoordinator.importStoreWithIdentifier(String?, fromExternalRecordsDirectory: NSURL, toURL: NSURL, options:[NSObject: AnyObject]?, withType: String, error: NSErrorPointer) -> NSPersistentStore?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func importStoreWithIdentifier(_ storeIdentifier: String!, fromExternalRecordsDirectory externalRecordsURL: NSURL!, toURL destinationURL: NSURL!, options options: [NSObject : AnyObject]!, withType storeType: String!, error error: NSErrorPointer) -> NSPersistentStore! ``` | OS X 10.10 |
| To | ``` func importStoreWithIdentifier(_ storeIdentifier: String?, fromExternalRecordsDirectory externalRecordsURL: NSURL, toURL destinationURL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore? ``` | OS X 10.6 |

Modified NSPersistentStoreCoordinator.lock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSPersistentStoreCoordinator.managedObjectIDForURIRepresentation(NSURL) -> NSManagedObjectID?

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectIDForURIRepresentation(_ url: NSURL!) -> NSManagedObjectID! ``` |
| To | ``` func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID? ``` |

Modified NSPersistentStoreCoordinator.managedObjectModel

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectModel: NSManagedObjectModel! { get } ``` |
| To | ``` var managedObjectModel: NSManagedObjectModel { get } ``` |

Modified NSPersistentStoreCoordinator.init(managedObjectModel: NSManagedObjectModel)

|  | Declaration |
| --- | --- |
| From | ``` init(managedObjectModel model: NSManagedObjectModel!) ``` |
| To | ``` init(managedObjectModel model: NSManagedObjectModel) ``` |

Modified NSPersistentStoreCoordinator.metadataForPersistentStore(NSPersistentStore) -> [NSObject: AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func metadataForPersistentStore(_ store: NSPersistentStore!) -> [NSObject : AnyObject]! ``` |
| To | ``` func metadataForPersistentStore(_ store: NSPersistentStore) -> [NSObject : AnyObject] ``` |

Modified NSPersistentStoreCoordinator.metadataForPersistentStoreOfType(String?, URL: NSURL, error: NSErrorPointer) -> [NSObject: AnyObject]? [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func metadataForPersistentStoreOfType(_ storeType: String!, URL url: NSURL!, error error: NSErrorPointer) -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` | OS X 10.5 |

Modified NSPersistentStoreCoordinator.migratePersistentStore(NSPersistentStore, toURL: NSURL, options:[NSObject: AnyObject]?, withType: String, error: NSErrorPointer) -> NSPersistentStore?

|  | Declaration |
| --- | --- |
| From | ``` func migratePersistentStore(_ store: NSPersistentStore!, toURL URL: NSURL!, options options: [NSObject : AnyObject]!, withType storeType: String!, error error: NSErrorPointer) -> NSPersistentStore! ``` |
| To | ``` func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore? ``` |

Modified NSPersistentStoreCoordinator.performBlock(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func performBlock(_ block: (() -> Void)!) ``` |
| To | ``` func performBlock(_ block: () -> Void) ``` |

Modified NSPersistentStoreCoordinator.performBlockAndWait(() -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func performBlockAndWait(_ block: (() -> Void)!) ``` |
| To | ``` func performBlockAndWait(_ block: () -> Void) ``` |

Modified NSPersistentStoreCoordinator.persistentStoreForURL(NSURL) -> NSPersistentStore?

|  | Declaration |
| --- | --- |
| From | ``` func persistentStoreForURL(_ URL: NSURL!) -> NSPersistentStore! ``` |
| To | ``` func persistentStoreForURL(_ URL: NSURL) -> NSPersistentStore? ``` |

Modified NSPersistentStoreCoordinator.persistentStores

|  | Declaration |
| --- | --- |
| From | ``` var persistentStores: [AnyObject]! { get } ``` |
| To | ``` var persistentStores: [AnyObject] { get } ``` |

Modified NSPersistentStoreCoordinator.registerStoreClass(AnyClass?, forStoreType: String) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func registerStoreClass(_ storeClass: AnyClass!, forStoreType storeType: String!) ``` | OS X 10.10 |
| To | ``` class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String) ``` | OS X 10.5 |

Modified NSPersistentStoreCoordinator.registeredStoreTypes() -> [NSObject: AnyObject] [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func registeredStoreTypes() -> [NSObject : AnyObject]! ``` | OS X 10.10 |
| To | ``` class func registeredStoreTypes() -> [NSObject : AnyObject] ``` | OS X 10.5 |

Modified NSPersistentStoreCoordinator.removePersistentStore(NSPersistentStore, error: NSErrorPointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func removePersistentStore(_ store: NSPersistentStore!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removePersistentStore(_ store: NSPersistentStore, error error: NSErrorPointer) -> Bool ``` |

Modified NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStoreAtURL(NSURL, options:[NSObject: AnyObject]?, error: NSErrorPointer) -> Bool [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL!, options options: [NSObject : AnyObject]!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` | OS X 10.9 |

Modified NSPersistentStoreCoordinator.setMetadata([NSObject: AnyObject]?, forPersistentStore: NSPersistentStore)

|  | Declaration |
| --- | --- |
| From | ``` func setMetadata(_ metadata: [NSObject : AnyObject]!, forPersistentStore store: NSPersistentStore!) ``` |
| To | ``` func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStore store: NSPersistentStore) ``` |

Modified NSPersistentStoreCoordinator.setMetadata([NSObject: AnyObject]?, forPersistentStoreOfType: String?, URL: NSURL, error: NSErrorPointer) -> Bool [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]!, forPersistentStoreOfType storeType: String!, URL url: NSURL!, error error: NSErrorPointer) -> Bool ``` | OS X 10.10 |
| To | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> Bool ``` | OS X 10.5 |

Modified NSPersistentStoreCoordinator.setURL(NSURL, forPersistentStore: NSPersistentStore) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setURL(_ url: NSURL!, forPersistentStore store: NSPersistentStore!) -> Bool ``` | OS X 10.10 |
| To | ``` func setURL(_ url: NSURL, forPersistentStore store: NSPersistentStore) -> Bool ``` | OS X 10.5 |

Modified NSPersistentStoreCoordinator.tryLock() -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSPersistentStoreCoordinator.unlock()

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified NSPersistentStoreRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSPersistentStoreRequest.affectedStores

|  | Declaration |
| --- | --- |
| From | ``` var affectedStores: [AnyObject]! ``` |
| To | ``` var affectedStores: [AnyObject]? ``` |

Modified NSPersistentStoreUbiquitousTransitionType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified NSPropertyDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSPropertyDescription.entity

|  | Declaration |
| --- | --- |
| From | ``` var entity: NSEntityDescription! { get } ``` |
| To | ``` unowned(unsafe) var entity: NSEntityDescription { get } ``` |

Modified NSPropertyDescription.indexed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPropertyDescription.indexedBySpotlight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyDescription.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String ``` |

Modified NSPropertyDescription.renamingIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var renamingIdentifier: String! ``` | OS X 10.10 |
| To | ``` var renamingIdentifier: String? ``` | OS X 10.6 |

Modified NSPropertyDescription.setValidationPredicates([AnyObject]?, withValidationWarnings:[AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func setValidationPredicates(_ validationPredicates: [AnyObject]!, withValidationWarnings validationWarnings: [AnyObject]!) ``` |
| To | ``` func setValidationPredicates(_ validationPredicates: [AnyObject]?, withValidationWarnings validationWarnings: [AnyObject]?) ``` |

Modified NSPropertyDescription.storedInExternalRecord

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified NSPropertyDescription.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

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

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHash: NSData! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | OS X 10.5 |

Modified NSPropertyDescription.versionHashModifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHashModifier: String! ``` | OS X 10.10 |
| To | ``` var versionHashModifier: String? ``` | OS X 10.5 |

Modified NSPropertyMapping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified NSPropertyMapping.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified NSPropertyMapping.userInfo

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? ``` |

Modified NSPropertyMapping.valueExpression

|  | Declaration |
| --- | --- |
| From | ``` var valueExpression: NSExpression! ``` |
| To | ``` var valueExpression: NSExpression? ``` |

Modified NSRelationshipDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSRelationshipDescription.destinationEntity

|  | Declaration |
| --- | --- |
| From | ``` var destinationEntity: NSEntityDescription! ``` |
| To | ``` unowned(unsafe) var destinationEntity: NSEntityDescription? ``` |

Modified NSRelationshipDescription.inverseRelationship

|  | Declaration |
| --- | --- |
| From | ``` var inverseRelationship: NSRelationshipDescription! ``` |
| To | ``` unowned(unsafe) var inverseRelationship: NSRelationshipDescription? ``` |

Modified NSRelationshipDescription.ordered

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSRelationshipDescription.versionHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var versionHash: NSData! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var versionHash: NSData { get } ``` | OS X 10.5 |

Modified NSSaveChangesRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified NSSaveChangesRequest.deletedObjects

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: NSSet! { get } ``` |
| To | ``` var deletedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.insertedObjects

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: NSSet! { get } ``` |
| To | ``` var insertedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.init(insertedObjects: Set<NSObject>?, updatedObjects: Set<NSObject>?, deletedObjects: Set<NSObject>?, lockedObjects: Set<NSObject>?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(insertedObjects insertedObjects: NSSet!, updatedObjects updatedObjects: NSSet!, deletedObjects deletedObjects: NSSet!, lockedObjects lockedObjects: NSSet!) ``` | OS X 10.10 |
| To | ``` init(insertedObjects insertedObjects: Set<NSObject>?, updatedObjects updatedObjects: Set<NSObject>?, deletedObjects deletedObjects: Set<NSObject>?, lockedObjects lockedObjects: Set<NSObject>?) ``` | OS X 10.10.3 |

Modified NSSaveChangesRequest.lockedObjects

|  | Declaration |
| --- | --- |
| From | ``` var lockedObjects: NSSet! { get } ``` |
| To | ``` var lockedObjects: Set<NSObject>? { get } ``` |

Modified NSSaveChangesRequest.updatedObjects

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: NSSet! { get } ``` |
| To | ``` var updatedObjects: Set<NSObject>? { get } ``` |

Modified NSSnapshotEventType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSnapshotEventType : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` | RawOptionSet |
| To | ``` struct NSSnapshotEventType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` | RawOptionSetType |

Modified NSSnapshotEventType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSAddedPersistentStoresKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAddedPersistentStoresKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSAddedPersistentStoresKey: String ``` | OS X 10.4 |

Modified NSAffectedObjectsErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAffectedObjectsErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSAffectedObjectsErrorKey: String ``` | OS X 10.4 |

Modified NSAffectedStoresErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSAffectedStoresErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSAffectedStoresErrorKey: String ``` | OS X 10.4 |

Modified NSBinaryExternalRecordType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSBinaryExternalRecordType: NSString! ``` | OS X 10.10 |
| To | ``` let NSBinaryExternalRecordType: String ``` | OS X 10.6 |

Modified NSBinaryStoreType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSBinaryStoreType: NSString! ``` | OS X 10.10 |
| To | ``` let NSBinaryStoreType: String ``` | OS X 10.4 |

Modified NSDeletedObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSDeletedObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSDeletedObjectsKey: String ``` | OS X 10.4 |

Modified NSDetailedErrorsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSDetailedErrorsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSDetailedErrorsKey: String ``` | OS X 10.4 |

Modified NSEntityNameInPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSEntityNameInPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSEntityNameInPathKey: String ``` | OS X 10.6 |

Modified NSErrorMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSExternalRecordExtensionOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSExternalRecordExtensionOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSExternalRecordExtensionOption: String ``` | OS X 10.6 |

Modified NSExternalRecordsDirectoryOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSExternalRecordsDirectoryOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSExternalRecordsDirectoryOption: String ``` | OS X 10.6 |

Modified NSExternalRecordsFileFormatOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSExternalRecordsFileFormatOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSExternalRecordsFileFormatOption: String ``` | OS X 10.6 |

Modified NSIgnorePersistentStoreVersioningOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSIgnorePersistentStoreVersioningOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSIgnorePersistentStoreVersioningOption: String ``` | OS X 10.5 |

Modified NSInMemoryStoreType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInMemoryStoreType: NSString! ``` | OS X 10.10 |
| To | ``` let NSInMemoryStoreType: String ``` | OS X 10.4 |

Modified NSInferMappingModelAutomaticallyOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInferMappingModelAutomaticallyOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSInferMappingModelAutomaticallyOption: String ``` | OS X 10.6 |

Modified NSInsertedObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInsertedObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSInsertedObjectsKey: String ``` | OS X 10.4 |

Modified NSInvalidatedAllObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInvalidatedAllObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSInvalidatedAllObjectsKey: String ``` | OS X 10.5 |

Modified NSInvalidatedObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSInvalidatedObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSInvalidatedObjectsKey: String ``` | OS X 10.5 |

Modified NSManagedObjectContextDidSaveNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSManagedObjectContextDidSaveNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSManagedObjectContextDidSaveNotification: String ``` | OS X 10.4 |

Modified NSManagedObjectContextObjectsDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSManagedObjectContextObjectsDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSManagedObjectContextObjectsDidChangeNotification: String ``` | OS X 10.4 |

Modified NSManagedObjectContextWillSaveNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSManagedObjectContextWillSaveNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSManagedObjectContextWillSaveNotification: String ``` | OS X 10.5 |

Modified NSMergeByPropertyObjectTrumpMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMergeByPropertyStoreTrumpMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSMigratePersistentStoresAutomaticallyOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigratePersistentStoresAutomaticallyOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigratePersistentStoresAutomaticallyOption: String ``` | OS X 10.5 |

Modified NSMigrationDestinationObjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationDestinationObjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationDestinationObjectKey: String ``` | OS X 10.5 |

Modified NSMigrationEntityMappingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationEntityMappingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationEntityMappingKey: String ``` | OS X 10.5 |

Modified NSMigrationEntityPolicyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationEntityPolicyKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationEntityPolicyKey: String ``` | OS X 10.5 |

Modified NSMigrationManagerKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationManagerKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationManagerKey: String ``` | OS X 10.5 |

Modified NSMigrationPropertyMappingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationPropertyMappingKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationPropertyMappingKey: String ``` | OS X 10.5 |

Modified NSMigrationSourceObjectKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSMigrationSourceObjectKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSMigrationSourceObjectKey: String ``` | OS X 10.5 |

Modified NSModelPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSModelPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSModelPathKey: String ``` | OS X 10.6 |

Modified NSObjectURIKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSObjectURIKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSObjectURIKey: String ``` | OS X 10.6 |

Modified NSOverwriteMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSPersistentStoreCoordinatorStoresDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreCoordinatorStoresDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreCoordinatorStoresDidChangeNotification: String ``` | OS X 10.4 |

Modified NSPersistentStoreCoordinatorStoresWillChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreCoordinatorStoresWillChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreCoordinatorStoresWillChangeNotification: String ``` | OS X 10.9 |

Modified NSPersistentStoreCoordinatorWillRemoveStoreNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreCoordinatorWillRemoveStoreNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreCoordinatorWillRemoveStoreNotification: String ``` | OS X 10.5 |

Modified NSPersistentStoreDidImportUbiquitousContentChangesNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreDidImportUbiquitousContentChangesNotification: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreDidImportUbiquitousContentChangesNotification: String ``` | OS X 10.7 |

Modified NSPersistentStoreOSCompatibility

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreOSCompatibility: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreOSCompatibility: String ``` | OS X 10.5 |

Modified NSPersistentStoreRebuildFromUbiquitousContentOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreRebuildFromUbiquitousContentOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreRebuildFromUbiquitousContentOption: String ``` | OS X 10.9 |

Modified NSPersistentStoreRemoveUbiquitousMetadataOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreRemoveUbiquitousMetadataOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreRemoveUbiquitousMetadataOption: String ``` | OS X 10.9 |

Modified NSPersistentStoreSaveConflictsErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreSaveConflictsErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreSaveConflictsErrorKey: String ``` | OS X 10.7 |

Modified NSPersistentStoreTimeoutOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreTimeoutOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreTimeoutOption: String ``` | OS X 10.5 |

Modified NSPersistentStoreUbiquitousContainerIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContainerIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreUbiquitousContainerIdentifierKey: String ``` | OS X 10.9 |

Modified NSPersistentStoreUbiquitousContentNameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContentNameKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreUbiquitousContentNameKey: String ``` | OS X 10.7 |

Modified NSPersistentStoreUbiquitousContentURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreUbiquitousContentURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreUbiquitousContentURLKey: String ``` | OS X 10.7 |

Modified NSPersistentStoreUbiquitousPeerTokenOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreUbiquitousPeerTokenOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreUbiquitousPeerTokenOption: String ``` | OS X 10.9 |

Modified NSPersistentStoreUbiquitousTransitionTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSPersistentStoreUbiquitousTransitionTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSPersistentStoreUbiquitousTransitionTypeKey: String ``` | OS X 10.9 |

Modified NSReadOnlyPersistentStoreOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSReadOnlyPersistentStoreOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSReadOnlyPersistentStoreOption: String ``` | OS X 10.4 |

Modified NSRefreshedObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSRefreshedObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSRefreshedObjectsKey: String ``` | OS X 10.5 |

Modified NSRemovedPersistentStoresKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSRemovedPersistentStoresKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSRemovedPersistentStoresKey: String ``` | OS X 10.4 |

Modified NSRollbackMergePolicy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified NSSQLiteAnalyzeOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSQLiteAnalyzeOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSSQLiteAnalyzeOption: String ``` | OS X 10.5 |

Modified NSSQLiteErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSQLiteErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let NSSQLiteErrorDomain: String ``` | OS X 10.5 |

Modified NSSQLiteManualVacuumOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSQLiteManualVacuumOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSSQLiteManualVacuumOption: String ``` | OS X 10.6 |

Modified NSSQLitePragmasOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSQLitePragmasOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSSQLitePragmasOption: String ``` | OS X 10.5 |

Modified NSSQLiteStoreType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSSQLiteStoreType: NSString! ``` | OS X 10.10 |
| To | ``` let NSSQLiteStoreType: String ``` | OS X 10.4 |

Modified NSStoreModelVersionHashesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStoreModelVersionHashesKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStoreModelVersionHashesKey: String ``` | OS X 10.5 |

Modified NSStoreModelVersionIdentifiersKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStoreModelVersionIdentifiersKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStoreModelVersionIdentifiersKey: String ``` | OS X 10.5 |

Modified NSStorePathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStorePathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStorePathKey: String ``` | OS X 10.6 |

Modified NSStoreTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStoreTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStoreTypeKey: String ``` | OS X 10.4 |

Modified NSStoreUUIDInPathKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStoreUUIDInPathKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStoreUUIDInPathKey: String ``` | OS X 10.6 |

Modified NSStoreUUIDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSStoreUUIDKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSStoreUUIDKey: String ``` | OS X 10.4 |

Modified NSUUIDChangedPersistentStoresKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUUIDChangedPersistentStoresKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSUUIDChangedPersistentStoresKey: String ``` | OS X 10.4 |

Modified NSUpdatedObjectsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSUpdatedObjectsKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSUpdatedObjectsKey: String ``` | OS X 10.4 |

Modified NSValidateXMLStoreOption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSValidateXMLStoreOption: NSString! ``` | OS X 10.10 |
| To | ``` let NSValidateXMLStoreOption: String ``` | OS X 10.4 |

Modified NSValidationKeyErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSValidationKeyErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSValidationKeyErrorKey: String ``` | OS X 10.4 |

Modified NSValidationObjectErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSValidationObjectErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSValidationObjectErrorKey: String ``` | OS X 10.4 |

Modified NSValidationPredicateErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSValidationPredicateErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSValidationPredicateErrorKey: String ``` | OS X 10.4 |

Modified NSValidationValueErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSValidationValueErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let NSValidationValueErrorKey: String ``` | OS X 10.4 |

Modified NSXMLExternalRecordType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSXMLExternalRecordType: NSString! ``` | OS X 10.10 |
| To | ``` let NSXMLExternalRecordType: String ``` | OS X 10.6 |

Modified NSXMLStoreType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let NSXMLStoreType: NSString! ``` | OS X 10.10 |
| To | ``` let NSXMLStoreType: String ``` | OS X 10.4 |

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
