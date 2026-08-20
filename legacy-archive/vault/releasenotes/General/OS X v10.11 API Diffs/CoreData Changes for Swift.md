---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreData.html
archived_at: '2026-07-18T02:53:24.990192Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreData Changes for Swift

### CoreData

Removed NSFetchRequestResultType.init(_: UInt)Removed NSSnapshotEventType.init(_: UInt)Added [NSBatchDeleteRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest)Added [NSBatchDeleteRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506206-fetchrequest)Added [NSBatchDeleteRequest.init(fetchRequest: NSFetchRequest)](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506302-init)Added [NSBatchDeleteRequest.init(objectIDs: [NSManagedObjectID])](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506746-initwithobjectids)Added [NSBatchDeleteRequest.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506389-resulttype)Added [NSBatchDeleteRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)Added [NSBatchDeleteRequestResultType.ResultTypeCount](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypecount)Added [NSBatchDeleteRequestResultType.ResultTypeObjectIDs](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypeobjectids)Added [NSBatchDeleteRequestResultType.ResultTypeStatusOnly](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypestatusonly)Added [NSBatchDeleteResult](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)Added [NSBatchDeleteResult.result](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404922-result)Added [NSBatchDeleteResult.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404941-resulttype)Added NSCocoaError.CoreDataErrorAdded NSCocoaError.EntityMigrationPolicyErrorAdded NSCocoaError.ExternalRecordImportErrorAdded NSCocoaError.InferredMappingModelErrorAdded NSCocoaError.ManagedObjectConstraintMergeErrorAdded NSCocoaError.ManagedObjectContextLockingErrorAdded NSCocoaError.ManagedObjectExternalRelationshipErrorAdded NSCocoaError.ManagedObjectMergeErrorAdded NSCocoaError.ManagedObjectReferentialIntegrityErrorAdded NSCocoaError.ManagedObjectValidationErrorAdded NSCocoaError.MigrationCancelledErrorAdded NSCocoaError.MigrationErrorAdded NSCocoaError.MigrationManagerDestinationStoreErrorAdded NSCocoaError.MigrationManagerSourceStoreErrorAdded NSCocoaError.MigrationMissingMappingModelErrorAdded NSCocoaError.MigrationMissingSourceModelErrorAdded NSCocoaError.PersistentStoreCoordinatorLockingErrorAdded NSCocoaError.PersistentStoreIncompatibleSchemaErrorAdded NSCocoaError.PersistentStoreIncompatibleVersionHashErrorAdded NSCocoaError.PersistentStoreIncompleteSaveErrorAdded NSCocoaError.PersistentStoreInvalidTypeErrorAdded NSCocoaError.PersistentStoreOpenErrorAdded NSCocoaError.PersistentStoreOperationErrorAdded NSCocoaError.PersistentStoreSaveConflictsErrorAdded NSCocoaError.PersistentStoreSaveErrorAdded NSCocoaError.PersistentStoreTimeoutErrorAdded NSCocoaError.PersistentStoreTypeMismatchErrorAdded NSCocoaError.PersistentStoreUnsupportedRequestTypeErrorAdded NSCocoaError.SQLiteErrorAdded NSCocoaError.ValidationDateTooLateErrorAdded NSCocoaError.ValidationDateTooSoonErrorAdded NSCocoaError.ValidationInvalidDateErrorAdded NSCocoaError.ValidationMissingMandatoryPropertyErrorAdded NSCocoaError.ValidationMultipleErrorsErrorAdded NSCocoaError.ValidationNumberTooLargeErrorAdded NSCocoaError.ValidationNumberTooSmallErrorAdded NSCocoaError.ValidationRelationshipDeniedDeleteErrorAdded NSCocoaError.ValidationRelationshipExceedsMaximumCountErrorAdded NSCocoaError.ValidationRelationshipLacksMinimumCountErrorAdded NSCocoaError.ValidationStringPatternMatchingErrorAdded NSCocoaError.ValidationStringTooLongErrorAdded NSCocoaError.ValidationStringTooShortErrorAdded [NSConstraintConflict](https://developer.apple.com/documentation/coredata/nsconstraintconflict)Added [NSConstraintConflict.conflictingObjects](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506707-conflictingobjects)Added [NSConstraintConflict.conflictingSnapshots](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506774-conflictingsnapshots)Added [NSConstraintConflict.constraint](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506902-constraint)Added [NSConstraintConflict.constraintValues](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506399-constraintvalues)Added [NSConstraintConflict.databaseObject](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506665-databaseobject)Added [NSConstraintConflict.databaseSnapshot](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506687-databasesnapshot)Added [NSConstraintConflict.init(constraint: [String], databaseObject: NSManagedObject?, databaseSnapshot: [NSObject : AnyObject]?, conflictingObjects: [NSManagedObject], conflictingSnapshots: [AnyObject])](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506668-init)Added [NSEntityDescription.uniquenessConstraints](https://developer.apple.com/documentation/coredata/nsentitydescription/1425095-uniquenessconstraints)Added [NSManagedObject.hasPersistentChangedValues](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506240-haspersistentchangedvalues)Added [NSManagedObject.objectIDsForRelationshipNamed(_: String) -> [NSManagedObjectID]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506201-objectidsforrelationshipnamed)Added [NSManagedObjectContext.mergeChangesFromRemoteContextSave(_: [NSObject : AnyObject], intoContexts: [NSManagedObjectContext]) [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506546-mergechanges)Added [NSManagedObjectContext.new() -> Self [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506632-new)Added [NSManagedObjectContext.refreshAllObjects()](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506217-refreshallobjects)Added [NSManagedObjectContext.shouldDeleteInaccessibleFaults](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506221-shoulddeleteinaccessiblefaults)Added [NSManagedObjectContext.shouldHandleInaccessibleFault(_: NSManagedObject, forObjectID: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506810-shouldhandleinaccessiblefault)Added [NSMergePolicy.resolveConstraintConflicts(_: [NSConstraintConflict]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506678-resolve)Added [NSMergePolicy.resolveOptimisticLockingVersionConflicts(_: [NSMergeConflict]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506787-resolve)Added [NSPersistentStoreCoordinator.destroyPersistentStoreAtURL(_: NSURL, withType: String, options: [NSObject : AnyObject]?) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468888-destroypersistentstoreaturl)Added [NSPersistentStoreCoordinator.metadataForPersistentStoreOfType(_: String, URL: NSURL, options: [NSObject : AnyObject]?) throws -> [String : AnyObject] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468778-metadataforpersistentstoreoftype)Added [NSPersistentStoreCoordinator.replacePersistentStoreAtURL(_: NSURL, destinationOptions: [NSObject : AnyObject]?, withPersistentStoreFromURL: NSURL, sourceOptions: [NSObject : AnyObject]?, storeType: String) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468917-replacepersistentstoreaturl)Added [NSPersistentStoreCoordinator.setMetadata(_: [String : AnyObject]?, forPersistentStoreOfType: String, URL: NSURL, options: [NSObject : AnyObject]?) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468893-setmetadata)Added [NSPersistentStoreRequestType.BatchDeleteRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/batchdeleterequesttype)Added [NSCoreDataVersionNumber10_10](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10)Added [NSCoreDataVersionNumber10_10_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10_2)Added [NSCoreDataVersionNumber10_10_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10_3)Added [NSCoreDataVersionNumber_iPhoneOS_8_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_8_0)Added [NSCoreDataVersionNumber_iPhoneOS_8_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_8_3)Added [NSManagedObjectConstraintMergeError](https://developer.apple.com/documentation/coredata/nsmanagedobjectconstraintmergeerror)Added [NSManagedObjectConstraintValidationError](https://developer.apple.com/documentation/coredata/nsmanagedobjectconstraintvalidationerror)Added [NSMigrationConstraintViolationError](https://developer.apple.com/documentation/coredata/1535452-validation_error_codes/nsmigrationconstraintviolationerror)Added [NSPersistentStoreForceDestroyOption](https://developer.apple.com/documentation/coredata/nspersistentstoreforcedestroyoption)Modified [NSAtomicStore](https://developer.apple.com/documentation/coredata/nsatomicstore)

|  | Declaration |
| --- | --- |
| From | ``` class NSAtomicStore : NSPersistentStore {     init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     func load(_ error: NSErrorPointer) -> Bool     func save(_ error: NSErrorPointer) -> Bool     func newCacheNodeForManagedObject(_ managedObject: NSManagedObject) -> NSAtomicStoreCacheNode     func updateCacheNode(_ node: NSAtomicStoreCacheNode, fromManagedObject managedObject: NSManagedObject)     func cacheNodes() -> Set<NSObject>     func addCacheNodes(_ cacheNodes: Set<NSObject>)     func willRemoveCacheNodes(_ cacheNodes: Set<NSObject>)     func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?     func objectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject) -> AnyObject     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |
| To | ``` class NSAtomicStore : NSPersistentStore {     init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     func load() throws     func save() throws     func newCacheNodeForManagedObject(_ managedObject: NSManagedObject) -> NSAtomicStoreCacheNode     func updateCacheNode(_ node: NSAtomicStoreCacheNode, fromManagedObject managedObject: NSManagedObject)     func cacheNodes() -> Set<NSAtomicStoreCacheNode>     func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?     func objectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject) -> AnyObject     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |

Modified [NSAtomicStore.addCacheNodes(_: Set<NSAtomicStoreCacheNode>)](https://developer.apple.com/documentation/coredata/nsatomicstore/1388062-addcachenodes)

|  | Declaration |
| --- | --- |
| From | ``` func addCacheNodes(_ cacheNodes: Set<NSObject>) ``` |
| To | ``` func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>) ``` |

Modified [NSAtomicStore.cacheNodes() -> Set<NSAtomicStoreCacheNode>](https://developer.apple.com/documentation/coredata/nsatomicstore/1388042-cachenodes)

|  | Declaration |
| --- | --- |
| From | ``` func cacheNodes() -> Set<NSObject> ``` |
| To | ``` func cacheNodes() -> Set<NSAtomicStoreCacheNode> ``` |

Modified [NSAtomicStore.load() throws](https://developer.apple.com/documentation/coredata/nsatomicstore/1388060-load)

|  | Declaration |
| --- | --- |
| From | ``` func load(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func load() throws ``` |

Modified [NSAtomicStore.save() throws](https://developer.apple.com/documentation/coredata/nsatomicstore/1388056-save)

|  | Declaration |
| --- | --- |
| From | ``` func save(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func save() throws ``` |

Modified [NSAtomicStore.willRemoveCacheNodes(_: Set<NSAtomicStoreCacheNode>)](https://developer.apple.com/documentation/coredata/nsatomicstore/1388064-willremovecachenodes)

|  | Declaration |
| --- | --- |
| From | ``` func willRemoveCacheNodes(_ cacheNodes: Set<NSObject>) ``` |
| To | ``` func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>) ``` |

Modified [NSAttributeType [enum]](https://developer.apple.com/documentation/coredata/nsattributetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSBatchUpdateRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSDeleteRule [enum]](https://developer.apple.com/documentation/coredata/nsdeleterule)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription)

|  | Declaration |
| --- | --- |
| From | ``` class NSEntityDescription : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func entityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSEntityDescription?     class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> AnyObject     unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }     var managedObjectClassName: String     var name: String?     var abstract: Bool     var subentitiesByName: [NSObject : AnyObject]? { get }     var subentities: [AnyObject]?     unowned(unsafe) var superentity: NSEntityDescription? { get }     var propertiesByName: [NSObject : AnyObject] { get }     var properties: [AnyObject]     var userInfo: [NSObject : AnyObject]?     var attributesByName: [NSObject : AnyObject] { get }     var relationshipsByName: [NSObject : AnyObject] { get }     func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [AnyObject]     func isKindOfEntity(_ entity: NSEntityDescription) -> Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var renamingIdentifier: String     var compoundIndexes: [AnyObject]? } ``` |
| To | ``` class NSEntityDescription : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func entityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSEntityDescription?     class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSManagedObject     unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }     var managedObjectClassName: String!     var name: String?     var abstract: Bool     var subentitiesByName: [String : NSEntityDescription] { get }     var subentities: [NSEntityDescription]     unowned(unsafe) var superentity: NSEntityDescription? { get }     var propertiesByName: [String : NSPropertyDescription] { get }     var properties: [NSPropertyDescription]     var userInfo: [NSObject : AnyObject]?     var attributesByName: [String : NSAttributeDescription] { get }     var relationshipsByName: [String : NSRelationshipDescription] { get }     func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [NSRelationshipDescription]     func isKindOfEntity(_ entity: NSEntityDescription) -> Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var renamingIdentifier: String?     var compoundIndexes: [[AnyObject]]     var uniquenessConstraints: [[AnyObject]] } ``` |

Modified [NSEntityDescription.attributesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425099-attributesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var attributesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var attributesByName: [String : NSAttributeDescription] { get } ``` |

Modified [NSEntityDescription.compoundIndexes](https://developer.apple.com/documentation/coredata/nsentitydescription/1425115-compoundindexes)

|  | Declaration |
| --- | --- |
| From | ``` var compoundIndexes: [AnyObject]? ``` |
| To | ``` var compoundIndexes: [[AnyObject]] ``` |

Modified [NSEntityDescription.insertNewObjectForEntityForName(_: String, inManagedObjectContext: NSManagedObjectContext) -> NSManagedObject [class]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425093-insertnewobjectforentityforname)

|  | Declaration |
| --- | --- |
| From | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> AnyObject ``` |
| To | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSManagedObject ``` |

Modified [NSEntityDescription.managedObjectClassName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425131-managedobjectclassname)

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectClassName: String ``` |
| To | ``` var managedObjectClassName: String! ``` |

Modified [NSEntityDescription.properties](https://developer.apple.com/documentation/coredata/nsentitydescription/1425125-properties)

|  | Declaration |
| --- | --- |
| From | ``` var properties: [AnyObject] ``` |
| To | ``` var properties: [NSPropertyDescription] ``` |

Modified [NSEntityDescription.propertiesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425137-propertiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var propertiesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var propertiesByName: [String : NSPropertyDescription] { get } ``` |

Modified [NSEntityDescription.relationshipsByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425106-relationshipsbyname)

|  | Declaration |
| --- | --- |
| From | ``` var relationshipsByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var relationshipsByName: [String : NSRelationshipDescription] { get } ``` |

Modified [NSEntityDescription.relationshipsWithDestinationEntity(_: NSEntityDescription) -> [NSRelationshipDescription]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425127-relationships)

|  | Declaration |
| --- | --- |
| From | ``` func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [AnyObject] ``` |
| To | ``` func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [NSRelationshipDescription] ``` |

Modified [NSEntityDescription.renamingIdentifier](https://developer.apple.com/documentation/coredata/nsentitydescription/1425135-renamingidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var renamingIdentifier: String ``` |
| To | ``` var renamingIdentifier: String? ``` |

Modified [NSEntityDescription.subentities](https://developer.apple.com/documentation/coredata/nsentitydescription/1425104-subentities)

|  | Declaration |
| --- | --- |
| From | ``` var subentities: [AnyObject]? ``` |
| To | ``` var subentities: [NSEntityDescription] ``` |

Modified [NSEntityDescription.subentitiesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425123-subentitiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var subentitiesByName: [NSObject : AnyObject]? { get } ``` |
| To | ``` var subentitiesByName: [String : NSEntityDescription] { get } ``` |

Modified [NSEntityMapping](https://developer.apple.com/documentation/coredata/nsentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` class NSEntityMapping : NSObject {     var name: String!     var mappingType: NSEntityMappingType     var sourceEntityName: String     @NSCopying var sourceEntityVersionHash: NSData     var destinationEntityName: String?     @NSCopying var destinationEntityVersionHash: NSData?     var attributeMappings: [AnyObject]?     var relationshipMappings: [AnyObject]     var sourceExpression: NSExpression?     var userInfo: [NSObject : AnyObject]?     var entityMigrationPolicyClassName: String } ``` |
| To | ``` class NSEntityMapping : NSObject {     var name: String!     var mappingType: NSEntityMappingType     var sourceEntityName: String?     @NSCopying var sourceEntityVersionHash: NSData?     var destinationEntityName: String?     @NSCopying var destinationEntityVersionHash: NSData?     var attributeMappings: [NSPropertyMapping]?     var relationshipMappings: [NSPropertyMapping]?     var sourceExpression: NSExpression?     var userInfo: [NSObject : AnyObject]?     var entityMigrationPolicyClassName: String? } ``` |

Modified [NSEntityMapping.attributeMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443193-attributemappings)

|  | Declaration |
| --- | --- |
| From | ``` var attributeMappings: [AnyObject]? ``` |
| To | ``` var attributeMappings: [NSPropertyMapping]? ``` |

Modified [NSEntityMapping.entityMigrationPolicyClassName](https://developer.apple.com/documentation/coredata/nsentitymapping/1443171-entitymigrationpolicyclassname)

|  | Declaration |
| --- | --- |
| From | ``` var entityMigrationPolicyClassName: String ``` |
| To | ``` var entityMigrationPolicyClassName: String? ``` |

Modified [NSEntityMapping.relationshipMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443163-relationshipmappings)

|  | Declaration |
| --- | --- |
| From | ``` var relationshipMappings: [AnyObject] ``` |
| To | ``` var relationshipMappings: [NSPropertyMapping]? ``` |

Modified [NSEntityMapping.sourceEntityName](https://developer.apple.com/documentation/coredata/nsentitymapping/1443187-sourceentityname)

|  | Declaration |
| --- | --- |
| From | ``` var sourceEntityName: String ``` |
| To | ``` var sourceEntityName: String? ``` |

Modified [NSEntityMapping.sourceEntityVersionHash](https://developer.apple.com/documentation/coredata/nsentitymapping/1443182-sourceentityversionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceEntityVersionHash: NSData ``` |
| To | ``` @NSCopying var sourceEntityVersionHash: NSData? ``` |

Modified [NSEntityMappingType [enum]](https://developer.apple.com/documentation/coredata/nsentitymappingtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy)

|  | Declaration |
| --- | --- |
| From | ``` class NSEntityMigrationPolicy : NSObject {     func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool     func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class NSEntityMigrationPolicy : NSObject {     func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws } ``` |

Modified [NSEntityMigrationPolicy.beginEntityMapping(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423785-beginentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.createDestinationInstancesForSourceInstance(_: NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423801-createdestinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.createRelationshipsForDestinationInstance(_: NSManagedObject, entityMapping: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423783-createrelationshipsfordestinatio)

|  | Declaration |
| --- | --- |
| From | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.endEntityMapping(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423787-endentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.endInstanceCreationForEntityMapping(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423805-endinstancecreation)

|  | Declaration |
| --- | --- |
| From | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.endRelationshipCreationForEntityMapping(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423793-endrelationshipcreation)

|  | Declaration |
| --- | --- |
| From | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.performCustomValidationForEntityMapping(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423791-performcustomvalidationforentity)

|  | Declaration |
| --- | --- |
| From | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSFetchRequest : NSPersistentStoreRequest, NSCoding {     init(entityName entityName: String) -> NSFetchRequest     class func fetchRequestWithEntityName(_ entityName: String) -> NSFetchRequest     init()     convenience init(entityName entityName: String)     var entity: NSEntityDescription?     var entityName: String? { get }     var predicate: NSPredicate?     var sortDescriptors: [AnyObject]?     var fetchLimit: Int     var affectedStores: [AnyObject]?     var resultType: NSFetchRequestResultType     var includesSubentities: Bool     var includesPropertyValues: Bool     var returnsObjectsAsFaults: Bool     var relationshipKeyPathsForPrefetching: [AnyObject]?     var includesPendingChanges: Bool     var returnsDistinctResults: Bool     var propertiesToFetch: [AnyObject]?     var fetchOffset: Int     var fetchBatchSize: Int     var shouldRefreshRefetchedObjects: Bool     var propertiesToGroupBy: [AnyObject]?     var havingPredicate: NSPredicate? } ``` |
| To | ``` class NSFetchRequest : NSPersistentStoreRequest, NSCoding {     convenience init(entityName entityName: String)     class func fetchRequestWithEntityName(_ entityName: String) -> Self     init()     convenience init(entityName entityName: String)     var entity: NSEntityDescription?     var entityName: String? { get }     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var fetchLimit: Int     var affectedStores: [NSPersistentStore]?     var resultType: NSFetchRequestResultType     var includesSubentities: Bool     var includesPropertyValues: Bool     var returnsObjectsAsFaults: Bool     var relationshipKeyPathsForPrefetching: [String]?     var includesPendingChanges: Bool     var returnsDistinctResults: Bool     var propertiesToFetch: [AnyObject]?     var fetchOffset: Int     var fetchBatchSize: Int     var shouldRefreshRefetchedObjects: Bool     var propertiesToGroupBy: [AnyObject]?     var havingPredicate: NSPredicate? } ``` |

Modified [NSFetchRequest.affectedStores](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506518-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` var affectedStores: [AnyObject]? ``` |
| To | ``` var affectedStores: [NSPersistentStore]? ``` |

Modified [NSFetchRequest.relationshipKeyPathsForPrefetching](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506813-relationshipkeypathsforprefetchi)

|  | Declaration |
| --- | --- |
| From | ``` var relationshipKeyPathsForPrefetching: [AnyObject]? ``` |
| To | ``` var relationshipKeyPathsForPrefetching: [String]? ``` |

Modified [NSFetchRequest.sortDescriptors](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506262-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]? ``` |
| To | ``` var sortDescriptors: [NSSortDescriptor]? ``` |

Modified [NSFetchRequestResultType [struct]](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFetchRequestResultType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` | RawOptionSetType |
| To | ``` struct NSFetchRequestResultType : OptionSetType {     init(rawValue rawValue: UInt)     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` | OptionSetType |

Modified [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore)

|  | Declaration |
| --- | --- |
| From | ``` class NSIncrementalStore : NSPersistentStore {     func loadMetadata(_ error: NSErrorPointer) -> Bool     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject?     func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> NSIncrementalStoreNode?     func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?, error error: NSErrorPointer) -> AnyObject?     class func identifierForNewStoreAtURL(_ storeURL: NSURL) -> AnyObject     func obtainPermanentIDsForObjects(_ array: [AnyObject], error error: NSErrorPointer) -> [AnyObject]?     func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [AnyObject])     func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [AnyObject])     func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |
| To | ``` class NSIncrementalStore : NSPersistentStore {     func loadMetadata() throws     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext?) throws -> AnyObject     func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext) throws -> NSIncrementalStoreNode     func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?) throws -> AnyObject     class func identifierForNewStoreAtURL(_ storeURL: NSURL) -> AnyObject     func obtainPermanentIDsForObjects(_ array: [NSManagedObject]) throws -> [NSManagedObjectID]     func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID])     func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID])     func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |

Modified [NSIncrementalStore.executeRequest(_: NSPersistentStoreRequest, withContext: NSManagedObjectContext?) throws -> AnyObject](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506653-executerequest)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext?) throws -> AnyObject ``` |

Modified [NSIncrementalStore.loadMetadata() throws](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506708-loadmetadata)

|  | Declaration |
| --- | --- |
| From | ``` func loadMetadata(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func loadMetadata() throws ``` |

Modified [NSIncrementalStore.managedObjectContextDidRegisterObjectsWithIDs(_: [NSManagedObjectID])](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506199-managedobjectcontextdidregistero)

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [AnyObject]) ``` |
| To | ``` func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID]) ``` |

Modified [NSIncrementalStore.managedObjectContextDidUnregisterObjectsWithIDs(_: [NSManagedObjectID])](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506878-managedobjectcontextdidunregiste)

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [AnyObject]) ``` |
| To | ``` func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID]) ``` |

Modified [NSIncrementalStore.newValueForRelationship(_: NSRelationshipDescription, forObjectWithID: NSManagedObjectID, withContext: NSManagedObjectContext?) throws -> AnyObject](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506438-newvalue)

|  | Declaration |
| --- | --- |
| From | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?) throws -> AnyObject ``` |

Modified [NSIncrementalStore.newValuesForObjectWithID(_: NSManagedObjectID, withContext: NSManagedObjectContext) throws -> NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobject)

|  | Declaration |
| --- | --- |
| From | ``` func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> NSIncrementalStoreNode? ``` |
| To | ``` func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext) throws -> NSIncrementalStoreNode ``` |

Modified [NSIncrementalStore.obtainPermanentIDsForObjects(_: [NSManagedObject]) throws -> [NSManagedObjectID]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentidsforobjects)

|  | Declaration |
| --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ array: [AnyObject], error error: NSErrorPointer) -> [AnyObject]? ``` |
| To | ``` func obtainPermanentIDsForObjects(_ array: [NSManagedObject]) throws -> [NSManagedObjectID] ``` |

Modified [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)

|  | Declaration |
| --- | --- |
| From | ``` class NSIncrementalStoreNode : NSObject {     init(objectID objectID: NSManagedObjectID, withValues values: [NSObject : AnyObject], version version: UInt64)     func updateWithValues(_ values: [NSObject : AnyObject], version version: UInt64)     var objectID: NSManagedObjectID { get }     var version: UInt64 { get }     func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? } ``` |
| To | ``` class NSIncrementalStoreNode : NSObject {     init(objectID objectID: NSManagedObjectID, withValues values: [String : AnyObject], version version: UInt64)     func updateWithValues(_ values: [String : AnyObject], version version: UInt64)     var objectID: NSManagedObjectID { get }     var version: UInt64 { get }     func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? } ``` |

Modified [NSIncrementalStoreNode.init(objectID: NSManagedObjectID, withValues: [String : AnyObject], version: UInt64)](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-initwithobjectid)

|  | Declaration |
| --- | --- |
| From | ``` init(objectID objectID: NSManagedObjectID, withValues values: [NSObject : AnyObject], version version: UInt64) ``` |
| To | ``` init(objectID objectID: NSManagedObjectID, withValues values: [String : AnyObject], version version: UInt64) ``` |

Modified [NSIncrementalStoreNode.updateWithValues(_: [String : AnyObject], version: UInt64)](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-update)

|  | Declaration |
| --- | --- |
| From | ``` func updateWithValues(_ values: [NSObject : AnyObject], version version: UInt64) ``` |
| To | ``` func updateWithValues(_ values: [String : AnyObject], version version: UInt64) ``` |

Modified [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject)

|  | Declaration |
| --- | --- |
| From | ``` class NSManagedObject : NSObject {     class func contextShouldIgnoreUnmodeledPropertyChanges() -> Bool     init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?)     unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }     var entity: NSEntityDescription { get }     var objectID: NSManagedObjectID { get }     var inserted: Bool { get }     var updated: Bool { get }     var deleted: Bool { get }     var hasChanges: Bool { get }     var fault: Bool { get }     func hasFaultForRelationshipNamed(_ key: String) -> Bool     var faultingState: Int { get }     func willAccessValueForKey(_ key: String?)     func didAccessValueForKey(_ key: String)     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func awakeFromFetch()     func awakeFromInsert()     func awakeFromSnapshotEvents(_ flags: NSSnapshotEventType)     func prepareForDeletion()     func willSave()     func didSave()     func willTurnIntoFault()     func didTurnIntoFault()     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func primitiveValueForKey(_ key: String) -> AnyObject?     func setPrimitiveValue(_ value: AnyObject?, forKey key: String)     func committedValuesForKeys(_ keys: [AnyObject]?) -> [NSObject : AnyObject]     func changedValues() -> [NSObject : AnyObject]     func changedValuesForCurrentEvent() -> [NSObject : AnyObject]     func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool     func validateForDelete(_ error: NSErrorPointer) -> Bool     func validateForInsert(_ error: NSErrorPointer) -> Bool     func validateForUpdate(_ error: NSErrorPointer) -> Bool     func setObservationInfo(_ inObservationInfo: AnyObject?)     func observationInfo() -> AnyObject? } ``` |
| To | ``` class NSManagedObject : NSObject {     class func contextShouldIgnoreUnmodeledPropertyChanges() -> Bool     init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?)     unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }     var entity: NSEntityDescription { get }     var objectID: NSManagedObjectID { get }     var inserted: Bool { get }     var updated: Bool { get }     var deleted: Bool { get }     var hasChanges: Bool { get }     var hasPersistentChangedValues: Bool { get }     var fault: Bool { get }     func hasFaultForRelationshipNamed(_ key: String) -> Bool     func objectIDsForRelationshipNamed(_ key: String) -> [NSManagedObjectID]     var faultingState: Int { get }     func willAccessValueForKey(_ key: String?)     func didAccessValueForKey(_ key: String?)     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func awakeFromFetch()     func awakeFromInsert()     func awakeFromSnapshotEvents(_ flags: NSSnapshotEventType)     func prepareForDeletion()     func willSave()     func didSave()     func willTurnIntoFault()     func didTurnIntoFault()     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func primitiveValueForKey(_ key: String) -> AnyObject?     func setPrimitiveValue(_ value: AnyObject?, forKey key: String)     func committedValuesForKeys(_ keys: [String]?) -> [String : AnyObject]     func changedValues() -> [String : AnyObject]     func changedValuesForCurrentEvent() -> [String : AnyObject]     func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func validateForDelete() throws     func validateForInsert() throws     func validateForUpdate() throws     func setObservationInfo(_ inObservationInfo: UnsafeMutablePointer<Void>)     func observationInfo() -> UnsafeMutablePointer<Void> } ``` |

Modified [NSManagedObject.changedValues() -> [String : AnyObject]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506775-changedvalues)

|  | Declaration |
| --- | --- |
| From | ``` func changedValues() -> [NSObject : AnyObject] ``` |
| To | ``` func changedValues() -> [String : AnyObject] ``` |

Modified [NSManagedObject.changedValuesForCurrentEvent() -> [String : AnyObject]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506472-changedvaluesforcurrentevent)

|  | Declaration |
| --- | --- |
| From | ``` func changedValuesForCurrentEvent() -> [NSObject : AnyObject] ``` |
| To | ``` func changedValuesForCurrentEvent() -> [String : AnyObject] ``` |

Modified [NSManagedObject.committedValuesForKeys(_: [String]?) -> [String : AnyObject]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506771-committedvaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func committedValuesForKeys(_ keys: [AnyObject]?) -> [NSObject : AnyObject] ``` |
| To | ``` func committedValuesForKeys(_ keys: [String]?) -> [String : AnyObject] ``` |

Modified [NSManagedObject.didAccessValueForKey(_: String?)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506865-didaccessvalue)

|  | Declaration |
| --- | --- |
| From | ``` func didAccessValueForKey(_ key: String) ``` |
| To | ``` func didAccessValueForKey(_ key: String?) ``` |

Modified [NSManagedObject.observationInfo() -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506210-observationinfo)

|  | Declaration |
| --- | --- |
| From | ``` func observationInfo() -> AnyObject? ``` |
| To | ``` func observationInfo() -> UnsafeMutablePointer<Void> ``` |

Modified [NSManagedObject.setObservationInfo(_: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506535-setobservationinfo)

|  | Declaration |
| --- | --- |
| From | ``` func setObservationInfo(_ inObservationInfo: AnyObject?) ``` |
| To | ``` func setObservationInfo(_ inObservationInfo: UnsafeMutablePointer<Void>) ``` |

Modified [NSManagedObject.validateForDelete() throws](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506195-validatefordelete)

|  | Declaration |
| --- | --- |
| From | ``` func validateForDelete(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateForDelete() throws ``` |

Modified [NSManagedObject.validateForInsert() throws](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506683-validateforinsert)

|  | Declaration |
| --- | --- |
| From | ``` func validateForInsert(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateForInsert() throws ``` |

Modified [NSManagedObject.validateForUpdate() throws](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506998-validateforupdate)

|  | Declaration |
| --- | --- |
| From | ``` func validateForUpdate(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateForUpdate() throws ``` |

Modified [NSManagedObject.validateValue(_: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506776-validatevalue)

|  | Declaration |
| --- | --- |
| From | ``` func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws ``` |

Modified [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)

|  | Declaration |
| --- | --- |
| From | ``` class NSManagedObjectContext : NSObject, NSCoding, NSLocking {     convenience init()     init(concurrencyType ct: NSManagedObjectContextConcurrencyType)     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     var persistentStoreCoordinator: NSPersistentStoreCoordinator?     var parentContext: NSManagedObjectContext?     var name: String?     var undoManager: NSUndoManager?     var hasChanges: Bool { get }     var userInfo: NSMutableDictionary? { get }     var concurrencyType: NSManagedObjectContextConcurrencyType { get }     func objectRegisteredForID(_ objectID: NSManagedObjectID) -> NSManagedObject?     func objectWithID(_ objectID: NSManagedObjectID) -> NSManagedObject     func existingObjectWithID(_ objectID: NSManagedObjectID, error error: NSErrorPointer) -> NSManagedObject?     func executeFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> [AnyObject]?     func countForFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> Int     func executeRequest(_ request: NSPersistentStoreRequest, error error: NSErrorPointer) -> NSPersistentStoreResult?     func insertObject(_ object: NSManagedObject)     func deleteObject(_ object: NSManagedObject)     func refreshObject(_ object: NSManagedObject, mergeChanges flag: Bool)     func detectConflictsForObject(_ object: NSManagedObject)     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [NSObject : AnyObject]?, context context: UnsafeMutablePointer<Void>)     func processPendingChanges()     func assignObject(_ object: AnyObject, toPersistentStore store: NSPersistentStore)     var insertedObjects: Set<NSObject> { get }     var updatedObjects: Set<NSObject> { get }     var deletedObjects: Set<NSObject> { get }     var registeredObjects: Set<NSObject> { get }     func undo()     func redo()     func reset()     func rollback()     func save(_ error: NSErrorPointer) -> Bool     func lock()     func unlock()     func tryLock() -> Bool     var propagatesDeletesAtEndOfEvent: Bool     var retainsRegisteredObjects: Bool     var stalenessInterval: NSTimeInterval     var mergePolicy: AnyObject     func obtainPermanentIDsForObjects(_ objects: [AnyObject], error error: NSErrorPointer) -> Bool     func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification) } ``` |
| To | ``` class NSManagedObjectContext : NSObject, NSCoding, NSLocking {     class func new() -> Self     convenience init()     init(concurrencyType ct: NSManagedObjectContextConcurrencyType)     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     var persistentStoreCoordinator: NSPersistentStoreCoordinator?     var parentContext: NSManagedObjectContext?     var name: String?     var undoManager: NSUndoManager?     var hasChanges: Bool { get }     var userInfo: NSMutableDictionary { get }     var concurrencyType: NSManagedObjectContextConcurrencyType { get }     func objectRegisteredForID(_ objectID: NSManagedObjectID) -> NSManagedObject?     func objectWithID(_ objectID: NSManagedObjectID) -> NSManagedObject     func existingObjectWithID(_ objectID: NSManagedObjectID) throws -> NSManagedObject     func executeFetchRequest(_ request: NSFetchRequest) throws -> [AnyObject]     func countForFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> Int     func executeRequest(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult     func insertObject(_ object: NSManagedObject)     func deleteObject(_ object: NSManagedObject)     func refreshObject(_ object: NSManagedObject, mergeChanges flag: Bool)     func detectConflictsForObject(_ object: NSManagedObject)     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>)     func processPendingChanges()     func assignObject(_ object: AnyObject, toPersistentStore store: NSPersistentStore)     var insertedObjects: Set<NSManagedObject> { get }     var updatedObjects: Set<NSManagedObject> { get }     var deletedObjects: Set<NSManagedObject> { get }     var registeredObjects: Set<NSManagedObject> { get }     func undo()     func redo()     func reset()     func rollback()     func save() throws     func refreshAllObjects()     func lock()     func unlock()     func tryLock() -> Bool     var propagatesDeletesAtEndOfEvent: Bool     var retainsRegisteredObjects: Bool     var shouldDeleteInaccessibleFaults: Bool     func shouldHandleInaccessibleFault(_ fault: NSManagedObject, forObjectID oid: NSManagedObjectID, triggeredByProperty property: NSPropertyDescription?) -> Bool     var stalenessInterval: NSTimeInterval     var mergePolicy: AnyObject     func obtainPermanentIDsForObjects(_ objects: [NSManagedObject]) throws     func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification)     class func mergeChangesFromRemoteContextSave(_ changeNotificationData: [NSObject : AnyObject], intoContexts contexts: [NSManagedObjectContext]) } ``` |

Modified [NSManagedObjectContext.deletedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506699-deletedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: Set<NSObject> { get } ``` |
| To | ``` var deletedObjects: Set<NSManagedObject> { get } ``` |

Modified [NSManagedObjectContext.executeFetchRequest(_: NSFetchRequest) throws -> [AnyObject]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-executefetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func executeFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> [AnyObject]? ``` |
| To | ``` func executeFetchRequest(_ request: NSFetchRequest) throws -> [AnyObject] ``` |

Modified [NSManagedObjectContext.executeRequest(_: NSPersistentStoreRequest) throws -> NSPersistentStoreResult](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506834-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest, error error: NSErrorPointer) -> NSPersistentStoreResult? ``` |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult ``` |

Modified [NSManagedObjectContext.existingObjectWithID(_: NSManagedObjectID) throws -> NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506686-existingobject)

|  | Declaration |
| --- | --- |
| From | ``` func existingObjectWithID(_ objectID: NSManagedObjectID, error error: NSErrorPointer) -> NSManagedObject? ``` |
| To | ``` func existingObjectWithID(_ objectID: NSManagedObjectID) throws -> NSManagedObject ``` |

Modified [NSManagedObjectContext.init()](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506673-init)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.11 |

Modified [NSManagedObjectContext.insertedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506192-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: Set<NSObject> { get } ``` |
| To | ``` var insertedObjects: Set<NSManagedObject> { get } ``` |

Modified [NSManagedObjectContext.observeValueForKeyPath(_: String?, ofObject: AnyObject?, change: [String : AnyObject]?, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506849-observevalue)

|  | Declaration |
| --- | --- |
| From | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [NSObject : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` |

Modified [NSManagedObjectContext.obtainPermanentIDsForObjects(_: [NSManagedObject]) throws](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506793-obtainpermanentids)

|  | Declaration |
| --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ objects: [AnyObject], error error: NSErrorPointer) -> Bool ``` |
| To | ``` func obtainPermanentIDsForObjects(_ objects: [NSManagedObject]) throws ``` |

Modified [NSManagedObjectContext.registeredObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506493-registeredobjects)

|  | Declaration |
| --- | --- |
| From | ``` var registeredObjects: Set<NSObject> { get } ``` |
| To | ``` var registeredObjects: Set<NSManagedObject> { get } ``` |

Modified [NSManagedObjectContext.save() throws](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save)

|  | Declaration |
| --- | --- |
| From | ``` func save(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func save() throws ``` |

Modified [NSManagedObjectContext.updatedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506985-updatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: Set<NSObject> { get } ``` |
| To | ``` var updatedObjects: Set<NSManagedObject> { get } ``` |

Modified [NSManagedObjectContext.userInfo](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506740-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: NSMutableDictionary? { get } ``` |
| To | ``` var userInfo: NSMutableDictionary { get } ``` |

Modified [NSManagedObjectContextConcurrencyType [enum]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSManagedObjectContextConcurrencyType.ConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.11 |

Modified [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel)

|  | Declaration |
| --- | --- |
| From | ``` class NSManagedObjectModel : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func mergedModelFromBundles(_ bundles: [AnyObject]?) -> NSManagedObjectModel?     init?(byMergingModels models: [AnyObject]?) -> NSManagedObjectModel     class func modelByMergingModels(_ models: [AnyObject]?) -> NSManagedObjectModel?     init()     convenience init?(contentsOfURL url: NSURL)     var entitiesByName: [NSObject : AnyObject] { get }     var entities: [AnyObject]     var configurations: [AnyObject] { get }     func entitiesForConfiguration(_ configuration: String?) -> [AnyObject]?     func setEntities(_ entities: [AnyObject], forConfiguration configuration: String)     func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String)     func fetchRequestTemplateForName(_ name: String) -> NSFetchRequest?     func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [NSObject : AnyObject]) -> NSFetchRequest?     var localizationDictionary: [NSObject : AnyObject]?     class func mergedModelFromBundles(_ bundles: [AnyObject]?, forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel?     init?(byMergingModels models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel     class func modelByMergingModels(_ models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel?     var fetchRequestTemplatesByName: [NSObject : AnyObject] { get }     var versionIdentifiers: Set<NSObject>     func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]?) -> Bool     var entityVersionHashesByName: [NSObject : AnyObject] { get } } ``` |
| To | ``` class NSManagedObjectModel : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func mergedModelFromBundles(_ bundles: [NSBundle]?) -> NSManagedObjectModel?      init?(byMergingModels models: [NSManagedObjectModel]?)     class func modelByMergingModels(_ models: [NSManagedObjectModel]?) -> NSManagedObjectModel?     init()     convenience init?(contentsOfURL url: NSURL)     var entitiesByName: [String : NSEntityDescription] { get }     var entities: [NSEntityDescription]     var configurations: [String] { get }     func entitiesForConfiguration(_ configuration: String?) -> [NSEntityDescription]?     func setEntities(_ entities: [NSEntityDescription], forConfiguration configuration: String)     func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String)     func fetchRequestTemplateForName(_ name: String) -> NSFetchRequest?     func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [String : AnyObject]) -> NSFetchRequest?     var localizationDictionary: [String : String]?     class func mergedModelFromBundles(_ bundles: [NSBundle]?, forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel?      init?(byMergingModels models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject])     class func modelByMergingModels(_ models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel?     var fetchRequestTemplatesByName: [String : NSFetchRequest] { get }     var versionIdentifiers: Set<NSObject>     func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [String : AnyObject]) -> Bool     var entityVersionHashesByName: [String : NSData] { get } } ``` |

Modified [NSManagedObjectModel.configurations](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506804-configurations)

|  | Declaration |
| --- | --- |
| From | ``` var configurations: [AnyObject] { get } ``` |
| To | ``` var configurations: [String] { get } ``` |

Modified [NSManagedObjectModel.entities](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506318-entities)

|  | Declaration |
| --- | --- |
| From | ``` var entities: [AnyObject] ``` |
| To | ``` var entities: [NSEntityDescription] ``` |

Modified [NSManagedObjectModel.entitiesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506203-entitiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var entitiesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var entitiesByName: [String : NSEntityDescription] { get } ``` |

Modified [NSManagedObjectModel.entitiesForConfiguration(_: String?) -> [NSEntityDescription]?](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506693-entities)

|  | Declaration |
| --- | --- |
| From | ``` func entitiesForConfiguration(_ configuration: String?) -> [AnyObject]? ``` |
| To | ``` func entitiesForConfiguration(_ configuration: String?) -> [NSEntityDescription]? ``` |

Modified [NSManagedObjectModel.entityVersionHashesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506992-entityversionhashesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var entityVersionHashesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var entityVersionHashesByName: [String : NSData] { get } ``` |

Modified [NSManagedObjectModel.fetchRequestFromTemplateWithName(_: String, substitutionVariables: [String : AnyObject]) -> NSFetchRequest?](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506422-fetchrequestfromtemplate)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [NSObject : AnyObject]) -> NSFetchRequest? ``` |
| To | ``` func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [String : AnyObject]) -> NSFetchRequest? ``` |

Modified [NSManagedObjectModel.fetchRequestTemplatesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506580-fetchrequesttemplatesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequestTemplatesByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var fetchRequestTemplatesByName: [String : NSFetchRequest] { get } ``` |

Modified [NSManagedObjectModel.init(byMergingModels: [NSManagedObjectModel]?)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506450-modelbymergingmodels)

|  | Declaration |
| --- | --- |
| From | ``` init?(byMergingModels models: [AnyObject]?) -> NSManagedObjectModel ``` |
| To | ``` init?(byMergingModels models: [NSManagedObjectModel]?) ``` |

Modified [NSManagedObjectModel.init(byMergingModels: [NSManagedObjectModel], forStoreMetadata: [String : AnyObject])](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506856-modelbymergingmodels)

|  | Declaration |
| --- | --- |
| From | ``` init?(byMergingModels models: [AnyObject], forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel ``` |
| To | ``` init?(byMergingModels models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject]) ``` |

Modified [NSManagedObjectModel.isConfiguration(_: String?, compatibleWithStoreMetadata: [String : AnyObject]) -> Bool](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506940-isconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [NSObject : AnyObject]?) -> Bool ``` |
| To | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [String : AnyObject]) -> Bool ``` |

Modified [NSManagedObjectModel.localizationDictionary](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506846-localizationdictionary)

|  | Declaration |
| --- | --- |
| From | ``` var localizationDictionary: [NSObject : AnyObject]? ``` |
| To | ``` var localizationDictionary: [String : String]? ``` |

Modified [NSManagedObjectModel.mergedModelFromBundles(_: [NSBundle]?) -> NSManagedObjectModel? [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506704-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?) -> NSManagedObjectModel? ``` |
| To | ``` class func mergedModelFromBundles(_ bundles: [NSBundle]?) -> NSManagedObjectModel? ``` |

Modified [NSManagedObjectModel.mergedModelFromBundles(_: [NSBundle]?, forStoreMetadata: [String : AnyObject]) -> NSManagedObjectModel? [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506788-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [AnyObject]?, forStoreMetadata metadata: [NSObject : AnyObject]) -> NSManagedObjectModel? ``` |
| To | ``` class func mergedModelFromBundles(_ bundles: [NSBundle]?, forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel? ``` |

Modified [NSManagedObjectModel.setEntities(_: [NSEntityDescription], forConfiguration: String)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506287-setentities)

|  | Declaration |
| --- | --- |
| From | ``` func setEntities(_ entities: [AnyObject], forConfiguration configuration: String) ``` |
| To | ``` func setEntities(_ entities: [NSEntityDescription], forConfiguration configuration: String) ``` |

Modified [NSMappingModel](https://developer.apple.com/documentation/coredata/nsmappingmodel)

|  | Declaration |
| --- | --- |
| From | ``` class NSMappingModel : NSObject {     init?(fromBundles bundles: [AnyObject]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel     class func mappingModelFromBundles(_ bundles: [AnyObject]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel?     class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel, error error: NSErrorPointer) -> NSMappingModel?     init?(contentsOfURL url: NSURL?)     var entityMappings: [AnyObject]?     var entityMappingsByName: [NSObject : AnyObject] { get } } ``` |
| To | ``` class NSMappingModel : NSObject {      init?(fromBundles bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?)     class func mappingModelFromBundles(_ bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel?     class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel     init?(contentsOfURL url: NSURL?)     var entityMappings: [NSEntityMapping]!     var entityMappingsByName: [String : NSEntityMapping] { get } } ``` |

Modified [NSMappingModel.entityMappings](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506196-entitymappings)

|  | Declaration |
| --- | --- |
| From | ``` var entityMappings: [AnyObject]? ``` |
| To | ``` var entityMappings: [NSEntityMapping]! ``` |

Modified [NSMappingModel.entityMappingsByName](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506179-entitymappingsbyname)

|  | Declaration |
| --- | --- |
| From | ``` var entityMappingsByName: [NSObject : AnyObject] { get } ``` |
| To | ``` var entityMappingsByName: [String : NSEntityMapping] { get } ``` |

Modified [NSMappingModel.inferredMappingModelForSourceModel(_: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel [class]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506468-inferredmappingmodelforsourcemod)

|  | Declaration |
| --- | --- |
| From | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel, error error: NSErrorPointer) -> NSMappingModel? ``` |
| To | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel ``` |

Modified [NSMappingModel.init(fromBundles: [NSBundle]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506930-mappingmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` init?(fromBundles bundles: [AnyObject]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel ``` |
| To | ``` init?(fromBundles bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) ``` |

Modified [NSMergeConflict](https://developer.apple.com/documentation/coredata/nsmergeconflict)

|  | Declaration |
| --- | --- |
| From | ``` class NSMergeConflict : NSObject {     var sourceObject: NSManagedObject { get }     var objectSnapshot: [NSObject : AnyObject]? { get }     var cachedSnapshot: [NSObject : AnyObject] { get }     var persistedSnapshot: [NSObject : AnyObject]? { get }     var newVersionNumber: Int { get }     var oldVersionNumber: Int { get }     init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject], persistedSnapshot persnap: [NSObject : AnyObject]?) } ``` |
| To | ``` class NSMergeConflict : NSObject {     var sourceObject: NSManagedObject { get }     var objectSnapshot: [String : AnyObject]? { get }     var cachedSnapshot: [String : AnyObject]? { get }     var persistedSnapshot: [String : AnyObject]? { get }     var newVersionNumber: Int { get }     var oldVersionNumber: Int { get }     init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : AnyObject]?, persistedSnapshot persnap: [String : AnyObject]?)     convenience init() } ``` |

Modified [NSMergeConflict.cachedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506685-cachedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var cachedSnapshot: [NSObject : AnyObject] { get } ``` |
| To | ``` var cachedSnapshot: [String : AnyObject]? { get } ``` |

Modified [NSMergeConflict.init(source: NSManagedObject, newVersion: Int, oldVersion: Int, cachedSnapshot: [String : AnyObject]?, persistedSnapshot: [String : AnyObject]?)](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506216-init)

|  | Declaration |
| --- | --- |
| From | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [NSObject : AnyObject], persistedSnapshot persnap: [NSObject : AnyObject]?) ``` |
| To | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : AnyObject]?, persistedSnapshot persnap: [String : AnyObject]?) ``` |

Modified [NSMergeConflict.objectSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506454-objectsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var objectSnapshot: [NSObject : AnyObject]? { get } ``` |
| To | ``` var objectSnapshot: [String : AnyObject]? { get } ``` |

Modified [NSMergeConflict.persistedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506412-persistedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var persistedSnapshot: [NSObject : AnyObject]? { get } ``` |
| To | ``` var persistedSnapshot: [String : AnyObject]? { get } ``` |

Modified [NSMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` class NSMergePolicy : NSObject {     var mergeType: NSMergePolicyType { get }     init(mergeType ty: NSMergePolicyType)     func resolveConflicts(_ list: [AnyObject], error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class NSMergePolicy : NSObject {     var mergeType: NSMergePolicyType { get }     init(mergeType ty: NSMergePolicyType)     convenience init()     func resolveConflicts(_ list: [AnyObject]) throws     func resolveOptimisticLockingVersionConflicts(_ list: [NSMergeConflict]) throws     func resolveConstraintConflicts(_ list: [NSConstraintConflict]) throws } ``` |

Modified [NSMergePolicy.resolveConflicts(_: [AnyObject]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506253-resolve)

|  | Declaration |
| --- | --- |
| From | ``` func resolveConflicts(_ list: [AnyObject], error error: NSErrorPointer) -> Bool ``` |
| To | ``` func resolveConflicts(_ list: [AnyObject]) throws ``` |

Modified [NSMergePolicyType [enum]](https://developer.apple.com/documentation/coredata/nsmergepolicytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSMigrationManager](https://developer.apple.com/documentation/coredata/nsmigrationmanager)

|  | Declaration |
| --- | --- |
| From | ``` class NSMigrationManager : NSObject {     init(sourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel)     func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool     var usesStoreSpecificMigrationManager: Bool     func reset()     var mappingModel: NSMappingModel { get }     var sourceModel: NSManagedObjectModel { get }     var destinationModel: NSManagedObjectModel { get }     var sourceContext: NSManagedObjectContext { get }     var destinationContext: NSManagedObjectContext { get }     func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func associateSourceInstance(_ sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, forEntityMapping entityMapping: NSEntityMapping)     func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [AnyObject]?) -> [AnyObject]     func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [AnyObject]?) -> [AnyObject]     var currentEntityMapping: NSEntityMapping { get }     var migrationProgress: Float { get }     var userInfo: [NSObject : AnyObject]?     func cancelMigrationWithError(_ error: NSError) } ``` |
| To | ``` class NSMigrationManager : NSObject {     init(sourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel)     func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?) throws     var usesStoreSpecificMigrationManager: Bool     func reset()     var mappingModel: NSMappingModel { get }     var sourceModel: NSManagedObjectModel { get }     var destinationModel: NSManagedObjectModel { get }     var sourceContext: NSManagedObjectContext { get }     var destinationContext: NSManagedObjectContext { get }     func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func associateSourceInstance(_ sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, forEntityMapping entityMapping: NSEntityMapping)     func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject]     func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject]     var currentEntityMapping: NSEntityMapping { get }     var migrationProgress: Float { get }     var userInfo: [NSObject : AnyObject]?     func cancelMigrationWithError(_ error: NSError) } ``` |

Modified [NSMigrationManager.destinationInstancesForEntityMappingNamed(_: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417594-destinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [AnyObject]?) -> [AnyObject] ``` |
| To | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |

Modified [NSMigrationManager.migrateStoreFromURL(_: NSURL, type: String, options: [NSObject : AnyObject]?, withMappingModel: NSMappingModel?, toDestinationURL: NSURL, destinationType: String, destinationOptions: [NSObject : AnyObject]?) throws](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417584-migratestore)

|  | Declaration |
| --- | --- |
| From | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?) throws ``` |

Modified [NSMigrationManager.sourceInstancesForEntityMappingNamed(_: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417580-sourceinstances)

|  | Declaration |
| --- | --- |
| From | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [AnyObject]?) -> [AnyObject] ``` |
| To | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |

Modified [NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` class NSPersistentStore : NSObject {     class func metadataForPersistentStoreWithURL(_ url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]?     class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreWithURL url: NSURL, error error: NSErrorPointer) -> Bool     class func migrationManagerClass() -> AnyClass     init(persistentStoreCoordinator root: NSPersistentStoreCoordinator, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     func loadMetadata(_ error: NSErrorPointer) -> Bool     weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }     var configurationName: String { get }     var options: [NSObject : AnyObject]? { get }     var URL: NSURL?     var identifier: String!     var type: String { get }     var readOnly: Bool     var metadata: [NSObject : AnyObject]!     func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator)     func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator) } ``` |
| To | ``` class NSPersistentStore : NSObject {     class func metadataForPersistentStoreWithURL(_ url: NSURL) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreWithURL url: NSURL) throws     class func migrationManagerClass() -> AnyClass     init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     convenience init()     func loadMetadata() throws     weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }     var configurationName: String { get }     var options: [NSObject : AnyObject]? { get }     var URL: NSURL?     var identifier: String!     var type: String { get }     var readOnly: Bool     var metadata: [String : AnyObject]!     func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator)     func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator?) } ``` |

Modified [NSPersistentStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, URL: NSURL, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/coredata/nspersistentstore/1506232-initwithpersistentstorecoordinat)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |

Modified [NSPersistentStore.loadMetadata() throws](https://developer.apple.com/documentation/coredata/nspersistentstore/1506273-loadmetadata)

|  | Declaration |
| --- | --- |
| From | ``` func loadMetadata(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func loadMetadata() throws ``` |

Modified [NSPersistentStore.metadata](https://developer.apple.com/documentation/coredata/nspersistentstore/1506564-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [NSObject : AnyObject]! ``` |
| To | ``` var metadata: [String : AnyObject]! ``` |

Modified [NSPersistentStore.metadataForPersistentStoreWithURL(_: NSURL) throws -> [String : AnyObject] [class]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506741-metadataforpersistentstorewithur)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataForPersistentStoreWithURL(_ url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` class func metadataForPersistentStoreWithURL(_ url: NSURL) throws -> [String : AnyObject] ``` |

Modified [NSPersistentStore.setMetadata(_: [String : AnyObject]?, forPersistentStoreWithURL: NSURL) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506824-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreWithURL url: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreWithURL url: NSURL) throws ``` |

Modified [NSPersistentStore.willRemoveFromPersistentStoreCoordinator(_: NSPersistentStoreCoordinator?)](https://developer.apple.com/documentation/coredata/nspersistentstore/1506731-willremove)

|  | Declaration |
| --- | --- |
| From | ``` func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator) ``` |
| To | ``` func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator?) ``` |

Modified [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator)

|  | Declaration |
| --- | --- |
| From | ``` class NSPersistentStoreCoordinator : NSObject, NSLocking {     init(managedObjectModel model: NSManagedObjectModel)     var managedObjectModel: NSManagedObjectModel { get }     var persistentStores: [AnyObject] { get }     var name: String!     func persistentStoreForURL(_ URL: NSURL) -> NSPersistentStore?     func URLForPersistentStore(_ store: NSPersistentStore) -> NSURL     func setURL(_ url: NSURL, forPersistentStore store: NSPersistentStore) -> Bool     func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> NSPersistentStore?     func removePersistentStore(_ store: NSPersistentStore, error error: NSErrorPointer) -> Bool     func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStore store: NSPersistentStore)     func metadataForPersistentStore(_ store: NSPersistentStore) -> [NSObject : AnyObject]     func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID?     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject?     class func registeredStoreTypes() -> [NSObject : AnyObject]     class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String)     class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]?     class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> Bool     class func elementsDerivedFromExternalRecordURL(_ fileURL: NSURL) -> [NSObject : AnyObject]     class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool     func importStoreWithIdentifier(_ storeIdentifier: String?, fromExternalRecordsDirectory externalRecordsURL: NSURL, toURL destinationURL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore?     func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore?     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     class func metadataForPersistentStoreWithURL(_ url: NSURL!, error error: NSErrorPointer) -> [NSObject : AnyObject]?     func lock()     func unlock()     func tryLock() -> Bool } extension NSPersistentStoreCoordinator {     func syncWithClient(_ client: ISyncClient!, inBackground flag: Bool, handler syncHandler: NSPersistentStoreCoordinatorSyncing!, error rError: NSErrorPointer) -> Bool     func setStoresFastSyncDetailsAtURL(_ url: NSURL!, forPersistentStore store: NSPersistentStore!) } ``` |
| To | ``` class NSPersistentStoreCoordinator : NSObject, NSLocking {     init(managedObjectModel model: NSManagedObjectModel)     var managedObjectModel: NSManagedObjectModel { get }     var persistentStores: [NSPersistentStore] { get }     var name: String?     func persistentStoreForURL(_ URL: NSURL) -> NSPersistentStore?     func URLForPersistentStore(_ store: NSPersistentStore) -> NSURL     func setURL(_ url: NSURL, forPersistentStore store: NSPersistentStore) -> Bool     func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?) throws -> NSPersistentStore     func removePersistentStore(_ store: NSPersistentStore) throws     func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStore store: NSPersistentStore)     func metadataForPersistentStore(_ store: NSPersistentStore) -> [String : AnyObject]     func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID?     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext) throws -> AnyObject     class func registeredStoreTypes() -> [String : NSValue]     class func registerStoreClass(_ storeClass: AnyClass, forStoreType storeType: String)     class func metadataForPersistentStoreOfType(_ storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws     class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL) throws     class func elementsDerivedFromExternalRecordURL(_ fileURL: NSURL) -> [NSObject : AnyObject]     class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?) throws     func importStoreWithIdentifier(_ storeIdentifier: String?, fromExternalRecordsDirectory externalRecordsURL: NSURL, toURL destinationURL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore     func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore     func destroyPersistentStoreAtURL(_ url: NSURL, withType storeType: String, options options: [NSObject : AnyObject]?) throws     func replacePersistentStoreAtURL(_ destinationURL: NSURL, destinationOptions destinationOptions: [NSObject : AnyObject]?, withPersistentStoreFromURL sourceURL: NSURL, sourceOptions sourceOptions: [NSObject : AnyObject]?, storeType storeType: String) throws     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     class func metadataForPersistentStoreWithURL(_ url: NSURL!) throws -> [NSObject : AnyObject]     func lock()     func unlock()     func tryLock() -> Bool } ``` |

Modified [NSPersistentStoreCoordinator.addPersistentStoreWithType(_: String, configuration: String?, URL: NSURL?, options: [NSObject : AnyObject]?) throws -> NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> NSPersistentStore? ``` |
| To | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?) throws -> NSPersistentStore ``` |

Modified [NSPersistentStoreCoordinator.executeRequest(_: NSPersistentStoreRequest, withContext: NSManagedObjectContext) throws -> AnyObject](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468872-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext) throws -> AnyObject ``` |

Modified [NSPersistentStoreCoordinator.importStoreWithIdentifier(_: String?, fromExternalRecordsDirectory: NSURL, toURL: NSURL, options: [NSObject : AnyObject]?, withType: String) throws -> NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468788-importstorewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func importStoreWithIdentifier(_ storeIdentifier: String?, fromExternalRecordsDirectory externalRecordsURL: NSURL, toURL destinationURL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore? ``` |
| To | ``` func importStoreWithIdentifier(_ storeIdentifier: String?, fromExternalRecordsDirectory externalRecordsURL: NSURL, toURL destinationURL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore ``` |

Modified [NSPersistentStoreCoordinator.metadataForPersistentStore(_: NSPersistentStore) -> [String : AnyObject]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468911-metadata)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForPersistentStore(_ store: NSPersistentStore) -> [NSObject : AnyObject] ``` |
| To | ``` func metadataForPersistentStore(_ store: NSPersistentStore) -> [String : AnyObject] ``` |

Modified [NSPersistentStoreCoordinator.metadataForPersistentStoreOfType(_: String?, URL: NSURL) throws -> [String : AnyObject] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468804-metadataforpersistentstoreoftype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> [NSObject : AnyObject]? ``` | -- |
| To | ``` class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL) throws -> [String : AnyObject] ``` | OS X 10.11 |

Modified [NSPersistentStoreCoordinator.migratePersistentStore(_: NSPersistentStore, toURL: NSURL, options: [NSObject : AnyObject]?, withType: String) throws -> NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String, error error: NSErrorPointer) -> NSPersistentStore? ``` |
| To | ``` func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore ``` |

Modified [NSPersistentStoreCoordinator.name](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468929-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [NSPersistentStoreCoordinator.persistentStores](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468790-persistentstores)

|  | Declaration |
| --- | --- |
| From | ``` var persistentStores: [AnyObject] { get } ``` |
| To | ``` var persistentStores: [NSPersistentStore] { get } ``` |

Modified [NSPersistentStoreCoordinator.registeredStoreTypes() -> [String : NSValue] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468870-registeredstoretypes)

|  | Declaration |
| --- | --- |
| From | ``` class func registeredStoreTypes() -> [NSObject : AnyObject] ``` |
| To | ``` class func registeredStoreTypes() -> [String : NSValue] ``` |

Modified [NSPersistentStoreCoordinator.registerStoreClass(_: AnyClass, forStoreType: String) [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468786-registerstoreclass)

|  | Declaration |
| --- | --- |
| From | ``` class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String) ``` |
| To | ``` class func registerStoreClass(_ storeClass: AnyClass, forStoreType storeType: String) ``` |

Modified [NSPersistentStoreCoordinator.removePersistentStore(_: NSPersistentStore) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468907-removepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func removePersistentStore(_ store: NSPersistentStore, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removePersistentStore(_ store: NSPersistentStore) throws ``` |

Modified [NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStoreAtURL(_: NSURL, options: [NSObject : AnyObject]?) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468923-removeubiquitouscontentandpersis)

|  | Declaration |
| --- | --- |
| From | ``` class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |
| To | ``` class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?) throws ``` |

Modified [NSPersistentStoreCoordinator.setMetadata(_: [String : AnyObject]?, forPersistentStore: NSPersistentStore)](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468899-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStore store: NSPersistentStore) ``` |
| To | ``` func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStore store: NSPersistentStore) ``` |

Modified [NSPersistentStoreCoordinator.setMetadata(_: [String : AnyObject]?, forPersistentStoreOfType: String?, URL: NSURL) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468897-setmetadata)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class func setMetadata(_ metadata: [NSObject : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL, error error: NSErrorPointer) -> Bool ``` | -- |
| To | ``` class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL) throws ``` | OS X 10.11 |

Modified [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSPersistentStoreRequest : NSObject, NSCopying {     var affectedStores: [AnyObject]?     var requestType: NSPersistentStoreRequestType { get } } ``` |
| To | ``` class NSPersistentStoreRequest : NSObject, NSCopying {     var affectedStores: [NSPersistentStore]?     var requestType: NSPersistentStoreRequestType { get } } ``` |

Modified [NSPersistentStoreRequest.affectedStores](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` var affectedStores: [AnyObject]? ``` |
| To | ``` var affectedStores: [NSPersistentStore]? ``` |

Modified [NSPersistentStoreRequestType [enum]](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSPersistentStoreRequestType : UInt {     case FetchRequestType     case SaveRequestType     case BatchUpdateRequestType } ``` | -- |
| To | ``` enum NSPersistentStoreRequestType : UInt {     case FetchRequestType     case SaveRequestType     case BatchUpdateRequestType     case BatchDeleteRequestType } ``` | UInt |

Modified [NSPersistentStoreUbiquitousTransitionType [enum]](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [NSPropertyDescription](https://developer.apple.com/documentation/coredata/nspropertydescription)

|  | Declaration |
| --- | --- |
| From | ``` class NSPropertyDescription : NSObject, NSCoding, NSCopying {     unowned(unsafe) var entity: NSEntityDescription { get }     var name: String     var optional: Bool     var transient: Bool     var validationPredicates: [AnyObject] { get }     var validationWarnings: [AnyObject] { get }     func setValidationPredicates(_ validationPredicates: [AnyObject]?, withValidationWarnings validationWarnings: [AnyObject]?)     var userInfo: [NSObject : AnyObject]?     var indexed: Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var indexedBySpotlight: Bool     var storedInExternalRecord: Bool     var renamingIdentifier: String? } ``` |
| To | ``` class NSPropertyDescription : NSObject, NSCoding, NSCopying {     unowned(unsafe) var entity: NSEntityDescription { get }     var name: String     var optional: Bool     var transient: Bool     var validationPredicates: [NSPredicate] { get }     var validationWarnings: [AnyObject] { get }     func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?)     var userInfo: [NSObject : AnyObject]?     var indexed: Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var indexedBySpotlight: Bool     var storedInExternalRecord: Bool     var renamingIdentifier: String? } ``` |

Modified [NSPropertyDescription.setValidationPredicates(_: [NSPredicate]?, withValidationWarnings: [String]?)](https://developer.apple.com/documentation/coredata/nspropertydescription/1506852-setvalidationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` func setValidationPredicates(_ validationPredicates: [AnyObject]?, withValidationWarnings validationWarnings: [AnyObject]?) ``` |
| To | ``` func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?) ``` |

Modified [NSPropertyDescription.validationPredicates](https://developer.apple.com/documentation/coredata/nspropertydescription/1506842-validationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` var validationPredicates: [AnyObject] { get } ``` |
| To | ``` var validationPredicates: [NSPredicate] { get } ``` |

Modified [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSSaveChangesRequest : NSPersistentStoreRequest {     init(insertedObjects insertedObjects: Set<NSObject>?, updatedObjects updatedObjects: Set<NSObject>?, deletedObjects deletedObjects: Set<NSObject>?, lockedObjects lockedObjects: Set<NSObject>?)     var insertedObjects: Set<NSObject>? { get }     var updatedObjects: Set<NSObject>? { get }     var deletedObjects: Set<NSObject>? { get }     var lockedObjects: Set<NSObject>? { get } } ``` |
| To | ``` class NSSaveChangesRequest : NSPersistentStoreRequest {     init(insertedObjects insertedObjects: Set<NSManagedObject>?, updatedObjects updatedObjects: Set<NSManagedObject>?, deletedObjects deletedObjects: Set<NSManagedObject>?, lockedObjects lockedObjects: Set<NSManagedObject>?)     var insertedObjects: Set<NSManagedObject>? { get }     var updatedObjects: Set<NSManagedObject>? { get }     var deletedObjects: Set<NSManagedObject>? { get }     var lockedObjects: Set<NSManagedObject>? { get } } ``` |

Modified [NSSaveChangesRequest.deletedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500420-deletedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var deletedObjects: Set<NSObject>? { get } ``` |
| To | ``` var deletedObjects: Set<NSManagedObject>? { get } ``` |

Modified [NSSaveChangesRequest.init(insertedObjects: Set<NSManagedObject>?, updatedObjects: Set<NSManagedObject>?, deletedObjects: Set<NSManagedObject>?, lockedObjects: Set<NSManagedObject>?)](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500418-init)

|  | Declaration |
| --- | --- |
| From | ``` init(insertedObjects insertedObjects: Set<NSObject>?, updatedObjects updatedObjects: Set<NSObject>?, deletedObjects deletedObjects: Set<NSObject>?, lockedObjects lockedObjects: Set<NSObject>?) ``` |
| To | ``` init(insertedObjects insertedObjects: Set<NSManagedObject>?, updatedObjects updatedObjects: Set<NSManagedObject>?, deletedObjects deletedObjects: Set<NSManagedObject>?, lockedObjects lockedObjects: Set<NSManagedObject>?) ``` |

Modified [NSSaveChangesRequest.insertedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500416-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: Set<NSObject>? { get } ``` |
| To | ``` var insertedObjects: Set<NSManagedObject>? { get } ``` |

Modified [NSSaveChangesRequest.lockedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500426-lockedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var lockedObjects: Set<NSObject>? { get } ``` |
| To | ``` var lockedObjects: Set<NSManagedObject>? { get } ``` |

Modified [NSSaveChangesRequest.updatedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500424-updatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var updatedObjects: Set<NSObject>? { get } ``` |
| To | ``` var updatedObjects: Set<NSManagedObject>? { get } ``` |

Modified [NSSnapshotEventType [struct]](https://developer.apple.com/documentation/coredata/nssnapshoteventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSnapshotEventType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` | RawOptionSetType |
| To | ``` struct NSSnapshotEventType : OptionSetType {     init(rawValue rawValue: UInt)     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` | OptionSetType |

Modified [NSErrorMergePolicy](https://developer.apple.com/documentation/coredata/nserrormergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var NSErrorMergePolicy: AnyObject! ``` |
| To | ``` var NSErrorMergePolicy: AnyObject ``` |

Modified [NSFetchRequestExpressionType](https://developer.apple.com/documentation/coredata/nsfetchrequestexpressiontype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var NSFetchRequestExpressionType: Int { get } ``` | OS X 10.10 |
| To | ``` let NSFetchRequestExpressionType: NSExpressionType ``` | OS X 10.11 |

Modified [NSMergeByPropertyObjectTrumpMergePolicy](https://developer.apple.com/documentation/coredata/nsmergebypropertyobjecttrumpmergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject! ``` |
| To | ``` var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject ``` |

Modified [NSMergeByPropertyStoreTrumpMergePolicy](https://developer.apple.com/documentation/coredata/nsmergebypropertystoretrumpmergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject! ``` |
| To | ``` var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject ``` |

Modified [NSOverwriteMergePolicy](https://developer.apple.com/documentation/coredata/nsoverwritemergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var NSOverwriteMergePolicy: AnyObject! ``` |
| To | ``` var NSOverwriteMergePolicy: AnyObject ``` |

Modified [NSPersistentStoreAsynchronousFetchResultCompletionBlock](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult!) -> Void ``` |
| To | ``` typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult) -> Void ``` |

Modified [NSRollbackMergePolicy](https://developer.apple.com/documentation/coredata/nsrollbackmergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var NSRollbackMergePolicy: AnyObject! ``` |
| To | ``` var NSRollbackMergePolicy: AnyObject ``` |

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
