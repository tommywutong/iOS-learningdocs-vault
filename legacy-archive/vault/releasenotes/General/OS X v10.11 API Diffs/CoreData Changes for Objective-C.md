---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreData.html
archived_at: '2026-07-18T02:52:57.787648Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreData Changes for Objective-C

### CoreData

#### CoreDataDefines.h

Added [#def NSCoreDataVersionNumber10_10](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10)Added [#def NSCoreDataVersionNumber10_10_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10_2)Added [#def NSCoreDataVersionNumber10_10_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_10_3)Added [#def NSCoreDataVersionNumber_iPhoneOS_8_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_8_0)Added [#def NSCoreDataVersionNumber_iPhoneOS_8_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_8_3)

#### CoreDataErrors.h

Added [NSManagedObjectConstraintMergeError](https://developer.apple.com/documentation/coredata/nsmanagedobjectconstraintmergeerror)Added [NSManagedObjectConstraintValidationError](https://developer.apple.com/documentation/coredata/nsmanagedobjectconstraintvalidationerror)Added [NSMigrationConstraintViolationError](https://developer.apple.com/documentation/coredata/1535452-validation_error_codes/nsmigrationconstraintviolationerror)

#### NSAtomicStore.h

Modified [-[NSAtomicStore addCacheNodes:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388062-addcachenodes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addCacheNodes:(NSSet *)cacheNodes ``` |
| To | ``` - (void)addCacheNodes:(NSSet<__kindof NSAtomicStoreCacheNode *> * _Nonnull)cacheNodes ``` |

Modified [-[NSAtomicStore cacheNodeForObjectID:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388040-cachenodeforobjectid)

|  | Declaration |
| --- | --- |
| From | ``` - (NSAtomicStoreCacheNode *)cacheNodeForObjectID:(NSManagedObjectID *)objectID ``` |
| To | ``` - (NSAtomicStoreCacheNode * _Nullable)cacheNodeForObjectID:(NSManagedObjectID * _Nonnull)objectID ``` |

Modified [-[NSAtomicStore cacheNodes]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388042-cachenodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)cacheNodes ``` |
| To | ``` - (NSSet<__kindof NSAtomicStoreCacheNode *> * _Nonnull)cacheNodes ``` |

Modified [-[NSAtomicStore initWithPersistentStoreCoordinator:configurationName:URL:options:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388054-initwithpersistentstorecoordinat)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator configurationName:(NSString *)configurationName URL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithPersistentStoreCoordinator:(NSPersistentStoreCoordinator * _Nullable)coordinator configurationName:(NSString * _Nullable)configurationName URL:(NSURL * _Nonnull)url options:(NSDictionary * _Nullable)options ``` |

Modified [-[NSAtomicStore load:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388060-load)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)load:(NSError **)error ``` |
| To | ``` - (BOOL)load:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSAtomicStore newCacheNodeForManagedObject:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388052-newcachenodeformanagedobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSAtomicStoreCacheNode *)newCacheNodeForManagedObject:(NSManagedObject *)managedObject ``` |
| To | ``` - (NSAtomicStoreCacheNode * _Nonnull)newCacheNodeForManagedObject:(NSManagedObject * _Nonnull)managedObject ``` |

Modified [-[NSAtomicStore newReferenceObjectForManagedObject:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388050-newreferenceobjectformanagedobje)

|  | Declaration |
| --- | --- |
| From | ``` - (id)newReferenceObjectForManagedObject:(NSManagedObject *)managedObject ``` |
| To | ``` - (id _Nonnull)newReferenceObjectForManagedObject:(NSManagedObject * _Nonnull)managedObject ``` |

Modified [-[NSAtomicStore objectIDForEntity:referenceObject:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388058-objectidforentity)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObjectID *)objectIDForEntity:(NSEntityDescription *)entity referenceObject:(id)data ``` |
| To | ``` - (NSManagedObjectID * _Nonnull)objectIDForEntity:(NSEntityDescription * _Nonnull)entity referenceObject:(id _Nonnull)data ``` |

Modified [-[NSAtomicStore referenceObjectForObjectID:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388046-referenceobjectforobjectid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)referenceObjectForObjectID:(NSManagedObjectID *)objectID ``` |
| To | ``` - (id _Nonnull)referenceObjectForObjectID:(NSManagedObjectID * _Nonnull)objectID ``` |

Modified [-[NSAtomicStore save:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388056-save)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)save:(NSError **)error ``` |
| To | ``` - (BOOL)save:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSAtomicStore updateCacheNode:fromManagedObject:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388044-updatecachenode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateCacheNode:(NSAtomicStoreCacheNode *)node fromManagedObject:(NSManagedObject *)managedObject ``` |
| To | ``` - (void)updateCacheNode:(NSAtomicStoreCacheNode * _Nonnull)node fromManagedObject:(NSManagedObject * _Nonnull)managedObject ``` |

Modified [-[NSAtomicStore willRemoveCacheNodes:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388064-willremovecachenodes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willRemoveCacheNodes:(NSSet *)cacheNodes ``` |
| To | ``` - (void)willRemoveCacheNodes:(NSSet<__kindof NSAtomicStoreCacheNode *> * _Nonnull)cacheNodes ``` |

#### NSAtomicStoreCacheNode.h

Modified [-[NSAtomicStoreCacheNode initWithObjectID:]](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506754-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjectID:(NSManagedObjectID *)moid ``` |
| To | ``` - (instancetype _Nonnull)initWithObjectID:(NSManagedObjectID * _Nonnull)moid ``` |

Modified [NSAtomicStoreCacheNode.objectID](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506627-objectid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSManagedObjectID *objectID ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSManagedObjectID *objectID ``` |

Modified [NSAtomicStoreCacheNode.propertyCache](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506283-propertycache)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSMutableDictionary *propertyCache ``` |
| To | ``` @property(nonatomic, strong, nullable) NSMutableDictionary<NSString *,id> *propertyCache ``` |

Modified [-[NSAtomicStoreCacheNode setValue:forKey:]](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506456-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValue:(id)value forKey:(NSString *)key ``` |
| To | ``` - (void)setValue:(id _Nullable)value forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSAtomicStoreCacheNode valueForKey:]](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506550-value)

|  | Declaration |
| --- | --- |
| From | ``` - (id)valueForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)valueForKey:(NSString * _Nonnull)key ``` |

#### NSAttributeDescription.h

Modified [NSAttributeDescription.attributeValueClassName](https://developer.apple.com/documentation/coredata/nsattributedescription/1498309-attributevalueclassname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *attributeValueClassName ``` |
| To | ``` @property(copy, nullable) NSString *attributeValueClassName ``` |

Modified [NSAttributeDescription.defaultValue](https://developer.apple.com/documentation/coredata/nsattributedescription/1498302-defaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id defaultValue ``` |
| To | ``` @property(retain, nullable) id defaultValue ``` |

Modified [NSAttributeDescription.valueTransformerName](https://developer.apple.com/documentation/coredata/nsattributedescription/1498305-valuetransformername)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *valueTransformerName ``` |
| To | ``` @property(copy, nullable) NSString *valueTransformerName ``` |

Modified [NSAttributeDescription.versionHash](https://developer.apple.com/documentation/coredata/nsattributedescription/1498310-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSData *versionHash ``` |
| To | ``` @property(readonly, copy, nonnull) NSData *versionHash ``` |

#### NSBatchDeleteRequest.h (Added)

Added [NSBatchDeleteRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest)Added [NSBatchDeleteRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506206-fetchrequest)Added [-[NSBatchDeleteRequest initWithFetchRequest:]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506302-initwithfetchrequest)Added [-[NSBatchDeleteRequest initWithObjectIDs:]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506746-initwithobjectids)Added [NSBatchDeleteRequest.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506389-resulttype)

#### NSBatchUpdateRequest.h

Modified [+[NSBatchUpdateRequest batchUpdateRequestWithEntityName:]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1526273-batchupdaterequestwithentityname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)batchUpdateRequestWithEntityName:(NSString *)entityName ``` |
| To | ``` + (instancetype _Nonnull)batchUpdateRequestWithEntityName:(NSString * _Nonnull)entityName ``` |

Modified [NSBatchUpdateRequest.entity](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506664-entity)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSEntityDescription *entity ``` |
| To | ``` @property(strong, readonly, nonnull) NSEntityDescription *entity ``` |

Modified [NSBatchUpdateRequest.entityName](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506796-entityname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *entityName ``` |
| To | ``` @property(copy, readonly, nonnull) NSString *entityName ``` |

Modified [-[NSBatchUpdateRequest initWithEntity:]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506374-initwithentity)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEntity:(NSEntityDescription *)entity ``` |
| To | ``` - (instancetype _Nonnull)initWithEntity:(NSEntityDescription * _Nonnull)entity ``` |

Modified [-[NSBatchUpdateRequest initWithEntityName:]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506702-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEntityName:(NSString *)entityName ``` |
| To | ``` - (instancetype _Nonnull)initWithEntityName:(NSString * _Nonnull)entityName ``` |

Modified [NSBatchUpdateRequest.predicate](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506659-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSPredicate *predicate ``` |
| To | ``` @property(strong, nullable) NSPredicate *predicate ``` |

Modified [NSBatchUpdateRequest.propertiesToUpdate](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506582-propertiestoupdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *propertiesToUpdate ``` |
| To | ``` @property(copy, nullable) NSDictionary *propertiesToUpdate ``` |

#### NSEntityDescription.h

Added [NSEntityDescription.uniquenessConstraints](https://developer.apple.com/documentation/coredata/nsentitydescription/1425095-uniquenessconstraints)Modified [NSEntityDescription.attributesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425099-attributesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *attributesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSAttributeDescription *> *attributesByName ``` |

Modified [NSEntityDescription.compoundIndexes](https://developer.apple.com/documentation/coredata/nsentitydescription/1425115-compoundindexes)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *compoundIndexes ``` |
| To | ``` @property(strong, nonnull) NSArray<NSArray<id> *> *compoundIndexes ``` |

Modified [+[NSEntityDescription entityForName:inManagedObjectContext:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425111-entity)

|  | Declaration |
| --- | --- |
| From | ``` + (NSEntityDescription *)entityForName:(NSString *)entityName inManagedObjectContext:(NSManagedObjectContext *)context ``` |
| To | ``` + (NSEntityDescription * _Nullable)entityForName:(NSString * _Nonnull)entityName inManagedObjectContext:(NSManagedObjectContext * _Nonnull)context ``` |

Modified [+[NSEntityDescription insertNewObjectForEntityForName:inManagedObjectContext:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425093-insertnewobject)

|  | Declaration |
| --- | --- |
| From | ``` + (id)insertNewObjectForEntityForName:(NSString *)entityName inManagedObjectContext:(NSManagedObjectContext *)context ``` |
| To | ``` + (__kindof NSManagedObject * _Nonnull)insertNewObjectForEntityForName:(NSString * _Nonnull)entityName inManagedObjectContext:(NSManagedObjectContext * _Nonnull)context ``` |

Modified [-[NSEntityDescription isKindOfEntity:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425113-iskindof)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isKindOfEntity:(NSEntityDescription *)entity ``` |
| To | ``` - (BOOL)isKindOfEntity:(NSEntityDescription * _Nonnull)entity ``` |

Modified [NSEntityDescription.managedObjectClassName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425131-managedobjectclassname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *managedObjectClassName ``` |
| To | ``` @property(copy) NSString * _Null_unspecified managedObjectClassName ``` |

Modified [NSEntityDescription.managedObjectModel](https://developer.apple.com/documentation/coredata/nsentitydescription/1425121-managedobjectmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) NSManagedObjectModel *managedObjectModel ``` |
| To | ``` @property(readonly, assign, nonnull) NSManagedObjectModel *managedObjectModel ``` |

Modified [NSEntityDescription.name](https://developer.apple.com/documentation/coredata/nsentitydescription/1425101-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [NSEntityDescription.properties](https://developer.apple.com/documentation/coredata/nsentitydescription/1425125-properties)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *properties ``` |
| To | ``` @property(strong, nonnull) NSArray<__kindof NSPropertyDescription *> *properties ``` |

Modified [NSEntityDescription.propertiesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425137-propertiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *propertiesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,__kindof NSPropertyDescription *> *propertiesByName ``` |

Modified [NSEntityDescription.relationshipsByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425106-relationshipsbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *relationshipsByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSRelationshipDescription *> *relationshipsByName ``` |

Modified [-[NSEntityDescription relationshipsWithDestinationEntity:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425127-relationshipswithdestinationenti)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)relationshipsWithDestinationEntity:(NSEntityDescription *)entity ``` |
| To | ``` - (NSArray<NSRelationshipDescription *> * _Nonnull)relationshipsWithDestinationEntity:(NSEntityDescription * _Nonnull)entity ``` |

Modified [NSEntityDescription.renamingIdentifier](https://developer.apple.com/documentation/coredata/nsentitydescription/1425135-renamingidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *renamingIdentifier ``` |
| To | ``` @property(copy, nullable) NSString *renamingIdentifier ``` |

Modified [NSEntityDescription.subentities](https://developer.apple.com/documentation/coredata/nsentitydescription/1425104-subentities)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *subentities ``` |
| To | ``` @property(strong, nonnull) NSArray<NSEntityDescription *> *subentities ``` |

Modified [NSEntityDescription.subentitiesByName](https://developer.apple.com/documentation/coredata/nsentitydescription/1425123-subentitiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *subentitiesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSEntityDescription *> *subentitiesByName ``` |

Modified [NSEntityDescription.superentity](https://developer.apple.com/documentation/coredata/nsentitydescription/1425129-superentity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) NSEntityDescription *superentity ``` |
| To | ``` @property(readonly, assign, nullable) NSEntityDescription *superentity ``` |

Modified [NSEntityDescription.userInfo](https://developer.apple.com/documentation/coredata/nsentitydescription/1425117-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSDictionary *userInfo ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDictionary *userInfo ``` |

Modified [NSEntityDescription.versionHash](https://developer.apple.com/documentation/coredata/nsentitydescription/1425133-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSData *versionHash ``` |
| To | ``` @property(readonly, copy, nonnull) NSData *versionHash ``` |

Modified [NSEntityDescription.versionHashModifier](https://developer.apple.com/documentation/coredata/nsentitydescription/1425119-versionhashmodifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *versionHashModifier ``` |
| To | ``` @property(copy, nullable) NSString *versionHashModifier ``` |

#### NSEntityMapping.h

Modified [NSEntityMapping.attributeMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443193-attributemappings)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *attributeMappings ``` |
| To | ``` @property(strong, nullable) NSArray<NSPropertyMapping *> *attributeMappings ``` |

Modified [NSEntityMapping.destinationEntityName](https://developer.apple.com/documentation/coredata/nsentitymapping/1443176-destinationentityname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *destinationEntityName ``` |
| To | ``` @property(copy, nullable) NSString *destinationEntityName ``` |

Modified [NSEntityMapping.destinationEntityVersionHash](https://developer.apple.com/documentation/coredata/nsentitymapping/1443169-destinationentityversionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *destinationEntityVersionHash ``` |
| To | ``` @property(copy, nullable) NSData *destinationEntityVersionHash ``` |

Modified [NSEntityMapping.entityMigrationPolicyClassName](https://developer.apple.com/documentation/coredata/nsentitymapping/1443171-entitymigrationpolicyclassname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *entityMigrationPolicyClassName ``` |
| To | ``` @property(copy, nullable) NSString *entityMigrationPolicyClassName ``` |

Modified [NSEntityMapping.name](https://developer.apple.com/documentation/coredata/nsentitymapping/1443167-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy) NSString * _Null_unspecified name ``` |

Modified [NSEntityMapping.relationshipMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443163-relationshipmappings)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *relationshipMappings ``` |
| To | ``` @property(strong, nullable) NSArray<NSPropertyMapping *> *relationshipMappings ``` |

Modified [NSEntityMapping.sourceEntityName](https://developer.apple.com/documentation/coredata/nsentitymapping/1443187-sourceentityname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *sourceEntityName ``` |
| To | ``` @property(copy, nullable) NSString *sourceEntityName ``` |

Modified [NSEntityMapping.sourceEntityVersionHash](https://developer.apple.com/documentation/coredata/nsentitymapping/1443182-sourceentityversionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *sourceEntityVersionHash ``` |
| To | ``` @property(copy, nullable) NSData *sourceEntityVersionHash ``` |

Modified [NSEntityMapping.sourceExpression](https://developer.apple.com/documentation/coredata/nsentitymapping/1443180-sourceexpression)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSExpression *sourceExpression ``` |
| To | ``` @property(strong, nullable) NSExpression *sourceExpression ``` |

Modified [NSEntityMapping.userInfo](https://developer.apple.com/documentation/coredata/nsentitymapping/1443184-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSDictionary *userInfo ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDictionary *userInfo ``` |

#### NSEntityMigrationPolicy.h

Modified [-[NSEntityMigrationPolicy beginEntityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423785-beginentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)beginEntityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)beginEntityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy createDestinationInstancesForSourceInstance:entityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423801-createdestinationinstancesforsou)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)createDestinationInstancesForSourceInstance:(NSManagedObject *)sInstance entityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)createDestinationInstancesForSourceInstance:(NSManagedObject * _Nonnull)sInstance entityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy createRelationshipsForDestinationInstance:entityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423783-createrelationships)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)createRelationshipsForDestinationInstance:(NSManagedObject *)dInstance entityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)createRelationshipsForDestinationInstance:(NSManagedObject * _Nonnull)dInstance entityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy endEntityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423787-endentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)endEntityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)endEntityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy endInstanceCreationForEntityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423805-endinstancecreationforentitymapp)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)endInstanceCreationForEntityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)endInstanceCreationForEntityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy endRelationshipCreationForEntityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423793-endrelationshipcreation)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)endRelationshipCreationForEntityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)endRelationshipCreationForEntityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSEntityMigrationPolicy performCustomValidationForEntityMapping:manager:error:]](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423791-performcustomvalidationforentity)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)performCustomValidationForEntityMapping:(NSEntityMapping *)mapping manager:(NSMigrationManager *)manager error:(NSError **)error ``` |
| To | ``` - (BOOL)performCustomValidationForEntityMapping:(NSEntityMapping * _Nonnull)mapping manager:(NSMigrationManager * _Nonnull)manager error:(NSError * _Nullable * _Nullable)error ``` |

#### NSExpressionDescription.h

Modified [NSExpressionDescription.expression](https://developer.apple.com/documentation/coredata/nsexpressiondescription/1506817-expression)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSExpression *expression ``` |
| To | ``` @property(strong, nullable) NSExpression *expression ``` |

#### NSFetchedPropertyDescription.h

Modified [NSFetchedPropertyDescription.fetchRequest](https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription/1494679-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSFetchRequest *fetchRequest ``` |
| To | ``` @property(strong, nullable) NSFetchRequest *fetchRequest ``` |

#### NSFetchRequest.h

Modified [NSFetchRequest.affectedStores](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506518-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *affectedStores ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSPersistentStore *> *affectedStores ``` |

Modified [NSFetchRequest.entity](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506979-entity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSEntityDescription *entity ``` |
| To | ``` @property(nonatomic, strong, nullable) NSEntityDescription *entity ``` |

Modified [NSFetchRequest.entityName](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506233-entityname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSString *entityName ``` |
| To | ``` @property(nonatomic, readonly, strong, nullable) NSString *entityName ``` |

Modified [+[NSFetchRequest fetchRequestWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1563437-fetchrequestwithentityname)

|  | Declaration |
| --- | --- |
| From | ``` + (NSFetchRequest *)fetchRequestWithEntityName:(NSString *)entityName ``` |
| To | ``` + (instancetype _Nonnull)fetchRequestWithEntityName:(NSString * _Nonnull)entityName ``` |

Modified [NSFetchRequest.havingPredicate](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506429-havingpredicate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSPredicate *havingPredicate ``` |
| To | ``` @property(nonatomic, strong, nullable) NSPredicate *havingPredicate ``` |

Modified [-[NSFetchRequest init]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506679-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[NSFetchRequest initWithEntityName:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506802-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEntityName:(NSString *)entityName ``` |
| To | ``` - (instancetype _Nonnull)initWithEntityName:(NSString * _Nonnull)entityName ``` |

Modified [NSFetchRequest.predicate](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506638-predicate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSPredicate *predicate ``` |
| To | ``` @property(nonatomic, strong, nullable) NSPredicate *predicate ``` |

Modified [NSFetchRequest.propertiesToFetch](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506851-propertiestofetch)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *propertiesToFetch ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray *propertiesToFetch ``` |

Modified [NSFetchRequest.propertiesToGroupBy](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *propertiesToGroupBy ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray *propertiesToGroupBy ``` |

Modified [NSFetchRequest.relationshipKeyPathsForPrefetching](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506813-relationshipkeypathsforprefetchi)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *relationshipKeyPathsForPrefetching ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *relationshipKeyPathsForPrefetching ``` |

Modified [NSFetchRequest.sortDescriptors](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506262-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *sortDescriptors ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

#### NSFetchRequestExpression.h

Removed NSFetchRequestExpressionTypeAdded [NSFetchRequestExpressionType](https://developer.apple.com/documentation/coredata/nsfetchrequestexpressiontype)Modified [NSFetchRequestExpression.contextExpression](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/1391665-contextexpression)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSExpression *contextExpression ``` |
| To | ``` @property(readonly, strong, nonnull) NSExpression *contextExpression ``` |

Modified [+[NSFetchRequestExpression expressionForFetch:context:countOnly:]](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/1391661-expressionforfetch)

|  | Declaration |
| --- | --- |
| From | ``` + (NSExpression *)expressionForFetch:(NSExpression *)fetch context:(NSExpression *)context countOnly:(BOOL)countFlag ``` |
| To | ``` + (NSExpression * _Nonnull)expressionForFetch:(NSExpression * _Nonnull)fetch context:(NSExpression * _Nonnull)context countOnly:(BOOL)countFlag ``` |

Modified [NSFetchRequestExpression.requestExpression](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/1391672-requestexpression)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSExpression *requestExpression ``` |
| To | ``` @property(readonly, strong, nonnull) NSExpression *requestExpression ``` |

#### NSIncrementalStore.h

Modified [-[NSIncrementalStore executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506653-execute)

|  | Declaration |
| --- | --- |
| From | ``` - (id)executeRequest:(NSPersistentStoreRequest *)request withContext:(NSManagedObjectContext *)context error:(NSError **)error ``` |
| To | ``` - (id _Nullable)executeRequest:(NSPersistentStoreRequest * _Nonnull)request withContext:(NSManagedObjectContext * _Nullable)context error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSIncrementalStore identifierForNewStoreAtURL:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506781-identifierfornewstore)

|  | Declaration |
| --- | --- |
| From | ``` + (id)identifierForNewStoreAtURL:(NSURL *)storeURL ``` |
| To | ``` + (id _Nonnull)identifierForNewStoreAtURL:(NSURL * _Nonnull)storeURL ``` |

Modified [-[NSIncrementalStore loadMetadata:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506708-loadmetadata)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadMetadata:(NSError **)error ``` |
| To | ``` - (BOOL)loadMetadata:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSIncrementalStore managedObjectContextDidRegisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506199-managedobjectcontextdidregistero)

|  | Declaration |
| --- | --- |
| From | ``` - (void)managedObjectContextDidRegisterObjectsWithIDs:(NSArray *)objectIDs ``` |
| To | ``` - (void)managedObjectContextDidRegisterObjectsWithIDs:(NSArray<NSManagedObjectID *> * _Nonnull)objectIDs ``` |

Modified [-[NSIncrementalStore managedObjectContextDidUnregisterObjectsWithIDs:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506878-managedobjectcontextdidunregiste)

|  | Declaration |
| --- | --- |
| From | ``` - (void)managedObjectContextDidUnregisterObjectsWithIDs:(NSArray *)objectIDs ``` |
| To | ``` - (void)managedObjectContextDidUnregisterObjectsWithIDs:(NSArray<NSManagedObjectID *> * _Nonnull)objectIDs ``` |

Modified [-[NSIncrementalStore newObjectIDForEntity:referenceObject:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506666-newobjectidforentity)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObjectID *)newObjectIDForEntity:(NSEntityDescription *)entity referenceObject:(id)data ``` |
| To | ``` - (NSManagedObjectID * _Nonnull)newObjectIDForEntity:(NSEntityDescription * _Nonnull)entity referenceObject:(id _Nonnull)data ``` |

Modified [-[NSIncrementalStore newValueForRelationship:forObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506438-newvalueforrelationship)

|  | Declaration |
| --- | --- |
| From | ``` - (id)newValueForRelationship:(NSRelationshipDescription *)relationship forObjectWithID:(NSManagedObjectID *)objectID withContext:(NSManagedObjectContext *)context error:(NSError **)error ``` |
| To | ``` - (id _Nullable)newValueForRelationship:(NSRelationshipDescription * _Nonnull)relationship forObjectWithID:(NSManagedObjectID * _Nonnull)objectID withContext:(NSManagedObjectContext * _Nullable)context error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSIncrementalStore newValuesForObjectWithID:withContext:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobjectwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIncrementalStoreNode *)newValuesForObjectWithID:(NSManagedObjectID *)objectID withContext:(NSManagedObjectContext *)context error:(NSError **)error ``` |
| To | ``` - (NSIncrementalStoreNode * _Nullable)newValuesForObjectWithID:(NSManagedObjectID * _Nonnull)objectID withContext:(NSManagedObjectContext * _Nonnull)context error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSIncrementalStore obtainPermanentIDsForObjects:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentids)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)obtainPermanentIDsForObjects:(NSArray *)array error:(NSError **)error ``` |
| To | ``` - (NSArray<NSManagedObjectID *> * _Nullable)obtainPermanentIDsForObjects:(NSArray<NSManagedObject *> * _Nonnull)array error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSIncrementalStore referenceObjectForObjectID:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506828-referenceobjectforobjectid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)referenceObjectForObjectID:(NSManagedObjectID *)objectID ``` |
| To | ``` - (id _Nonnull)referenceObjectForObjectID:(NSManagedObjectID * _Nonnull)objectID ``` |

#### NSIncrementalStoreNode.h

Modified [-[NSIncrementalStoreNode initWithObjectID:withValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjectID:(NSManagedObjectID *)objectID withValues:(NSDictionary *)values version:(uint64_t)version ``` |
| To | ``` - (instancetype _Nonnull)initWithObjectID:(NSManagedObjectID * _Nonnull)objectID withValues:(NSDictionary<NSString *,id> * _Nonnull)values version:(uint64_t)version ``` |

Modified [NSIncrementalStoreNode.objectID](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506827-objectid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSManagedObjectID *objectID ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSManagedObjectID *objectID ``` |

Modified [-[NSIncrementalStoreNode updateWithValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-updatewithvalues)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateWithValues:(NSDictionary *)values version:(uint64_t)version ``` |
| To | ``` - (void)updateWithValues:(NSDictionary<NSString *,id> * _Nonnull)values version:(uint64_t)version ``` |

Modified [-[NSIncrementalStoreNode valueForPropertyDescription:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506442-value)

|  | Declaration |
| --- | --- |
| From | ``` - (id)valueForPropertyDescription:(NSPropertyDescription *)prop ``` |
| To | ``` - (id _Nullable)valueForPropertyDescription:(NSPropertyDescription * _Nonnull)prop ``` |

#### NSManagedObject.h

Added [NSManagedObject.hasPersistentChangedValues](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506240-haspersistentchangedvalues)Added [-[NSManagedObject objectIDsForRelationshipNamed:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506201-objectidsforrelationshipnamed)Modified [-[NSManagedObject changedValues]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506775-changedvalues)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)changedValues ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)changedValues ``` |

Modified [-[NSManagedObject changedValuesForCurrentEvent]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506472-changedvaluesforcurrentevent)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)changedValuesForCurrentEvent ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)changedValuesForCurrentEvent ``` |

Modified [-[NSManagedObject committedValuesForKeys:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506771-committedvaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)committedValuesForKeys:(NSArray *)keys ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)committedValuesForKeys:(NSArray<NSString *> * _Nullable)keys ``` |

Modified [-[NSManagedObject didAccessValueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506865-didaccessvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didAccessValueForKey:(NSString *)key ``` |
| To | ``` - (void)didAccessValueForKey:(NSString * _Nullable)key ``` |

Modified [-[NSManagedObject didChangeValueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506976-didchangevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didChangeValueForKey:(NSString *)key ``` |
| To | ``` - (void)didChangeValueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject didChangeValueForKey:withSetMutation:usingObjects:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506936-didchangevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didChangeValueForKey:(NSString *)inKey withSetMutation:(NSKeyValueSetMutationKind)inMutationKind usingObjects:(NSSet *)inObjects ``` |
| To | ``` - (void)didChangeValueForKey:(NSString * _Nonnull)inKey withSetMutation:(NSKeyValueSetMutationKind)inMutationKind usingObjects:(NSSet * _Nonnull)inObjects ``` |

Modified [NSManagedObject.entity](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506562-entity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSEntityDescription *entity ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSEntityDescription *entity ``` |

Modified [-[NSManagedObject hasFaultForRelationshipNamed:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506973-hasfault)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasFaultForRelationshipNamed:(NSString *)key ``` |
| To | ``` - (BOOL)hasFaultForRelationshipNamed:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject initWithEntity:insertIntoManagedObjectContext:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEntity:(NSEntityDescription *)entity insertIntoManagedObjectContext:(NSManagedObjectContext *)context ``` |
| To | ``` - (__kindof NSManagedObject * _Nonnull)initWithEntity:(NSEntityDescription * _Nonnull)entity insertIntoManagedObjectContext:(NSManagedObjectContext * _Nullable)context ``` |

Modified [NSManagedObject.managedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506677-managedobjectcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, assign) NSManagedObjectContext *managedObjectContext ``` |
| To | ``` @property(nonatomic, readonly, assign, nullable) NSManagedObjectContext *managedObjectContext ``` |

Modified [NSManagedObject.objectID](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506848-objectid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSManagedObjectID *objectID ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSManagedObjectID *objectID ``` |

Modified [-[NSManagedObject observationInfo]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506210-observationinfo)

|  | Declaration |
| --- | --- |
| From | ``` - (id)observationInfo ``` |
| To | ``` - (void * _Nullable)observationInfo ``` |

Modified [-[NSManagedObject primitiveValueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506728-primitivevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)primitiveValueForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)primitiveValueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject setObservationInfo:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506535-setobservationinfo)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setObservationInfo:(id)inObservationInfo ``` |
| To | ``` - (void)setObservationInfo:(void * _Nullable)inObservationInfo ``` |

Modified [-[NSManagedObject setPrimitiveValue:forKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506960-setprimitivevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setPrimitiveValue:(id)value forKey:(NSString *)key ``` |
| To | ``` - (void)setPrimitiveValue:(id _Nullable)value forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject setValue:forKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506397-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValue:(id)value forKey:(NSString *)key ``` |
| To | ``` - (void)setValue:(id _Nullable)value forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject validateForDelete:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506195-validatefordelete)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateForDelete:(NSError **)error ``` |
| To | ``` - (BOOL)validateForDelete:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObject validateForInsert:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506683-validateforinsert)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateForInsert:(NSError **)error ``` |
| To | ``` - (BOOL)validateForInsert:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObject validateForUpdate:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506998-validateforupdate)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateForUpdate:(NSError **)error ``` |
| To | ``` - (BOOL)validateForUpdate:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObject validateValue:forKey:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506776-validatevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateValue:(id *)value forKey:(NSString *)key error:(NSError **)error ``` |
| To | ``` - (BOOL)validateValue:(id  _Nullable * _Nonnull)value forKey:(NSString * _Nonnull)key error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObject valueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506613-value)

|  | Declaration |
| --- | --- |
| From | ``` - (id)valueForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)valueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject willAccessValueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1507001-willaccessvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willAccessValueForKey:(NSString *)key ``` |
| To | ``` - (void)willAccessValueForKey:(NSString * _Nullable)key ``` |

Modified [-[NSManagedObject willChangeValueForKey:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506229-willchangevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willChangeValueForKey:(NSString *)key ``` |
| To | ``` - (void)willChangeValueForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSManagedObject willChangeValueForKey:withSetMutation:usingObjects:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506801-willchangevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willChangeValueForKey:(NSString *)inKey withSetMutation:(NSKeyValueSetMutationKind)inMutationKind usingObjects:(NSSet *)inObjects ``` |
| To | ``` - (void)willChangeValueForKey:(NSString * _Nonnull)inKey withSetMutation:(NSKeyValueSetMutationKind)inMutationKind usingObjects:(NSSet * _Nonnull)inObjects ``` |

#### NSManagedObjectContext.h

Added [+[NSManagedObjectContext mergeChangesFromRemoteContextSave:intoContexts:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506546-mergechanges)Added [+[NSManagedObjectContext new]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506632-new)Added [-[NSManagedObjectContext refreshAllObjects]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506217-refreshallobjects)Added [NSManagedObjectContext.shouldDeleteInaccessibleFaults](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506221-shoulddeleteinaccessiblefaults)Added [-[NSManagedObjectContext shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506810-shouldhandleinaccessiblefault)Modified [-[NSManagedObjectContext assignObject:toPersistentStore:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506436-assign)

|  | Declaration |
| --- | --- |
| From | ``` - (void)assignObject:(id)object toPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (void)assignObject:(id _Nonnull)object toPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [-[NSManagedObjectContext countForFetchRequest:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506868-countforfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)countForFetchRequest:(NSFetchRequest *)request error:(NSError **)error ``` |
| To | ``` - (NSUInteger)countForFetchRequest:(NSFetchRequest * _Nonnull)request error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSManagedObjectContext.deletedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506699-deletedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *deletedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *deletedObjects ``` |

Modified [-[NSManagedObjectContext deleteObject:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506847-deleteobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteObject:(NSManagedObject *)object ``` |
| To | ``` - (void)deleteObject:(NSManagedObject * _Nonnull)object ``` |

Modified [-[NSManagedObjectContext detectConflictsForObject:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506843-detectconflicts)

|  | Declaration |
| --- | --- |
| From | ``` - (void)detectConflictsForObject:(NSManagedObject *)object ``` |
| To | ``` - (void)detectConflictsForObject:(NSManagedObject * _Nonnull)object ``` |

Modified [-[NSManagedObjectContext executeFetchRequest:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)executeFetchRequest:(NSFetchRequest *)request error:(NSError **)error ``` |
| To | ``` - (NSArray * _Nullable)executeFetchRequest:(NSFetchRequest * _Nonnull)request error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObjectContext executeRequest:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506834-executerequest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStoreResult *)executeRequest:(NSPersistentStoreRequest *)request error:(NSError **)error ``` |
| To | ``` - (__kindof NSPersistentStoreResult * _Nullable)executeRequest:(NSPersistentStoreRequest * _Nonnull)request error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObjectContext existingObjectWithID:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506686-existingobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObject *)existingObjectWithID:(NSManagedObjectID *)objectID error:(NSError **)error ``` |
| To | ``` - (__kindof NSManagedObject * _Nullable)existingObjectWithID:(NSManagedObjectID * _Nonnull)objectID error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSManagedObjectContext init]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506673-init)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` - (instancetype)init ``` | OS X 10.10 | -- |
| To | ``` - (instancetype _Nonnull)init ``` | OS X 10.4 | OS X 10.11 |

Modified [-[NSManagedObjectContext initWithConcurrencyType:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506709-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithConcurrencyType:(NSManagedObjectContextConcurrencyType)ct ``` |
| To | ``` - (instancetype _Nonnull)initWithConcurrencyType:(NSManagedObjectContextConcurrencyType)ct ``` |

Modified [NSManagedObjectContext.insertedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506192-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *insertedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *insertedObjects ``` |

Modified [-[NSManagedObjectContext insertObject:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506794-insertobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertObject:(NSManagedObject *)object ``` |
| To | ``` - (void)insertObject:(NSManagedObject * _Nonnull)object ``` |

Modified [-[NSManagedObjectContext mergeChangesFromContextDidSaveNotification:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506606-mergechanges)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mergeChangesFromContextDidSaveNotification:(NSNotification *)notification ``` |
| To | ``` - (void)mergeChangesFromContextDidSaveNotification:(NSNotification * _Nonnull)notification ``` |

Modified [NSManagedObjectContext.mergePolicy](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506490-mergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id mergePolicy ``` |
| To | ``` @property(strong, nonnull) id mergePolicy ``` |

Modified [NSManagedObjectContext.name](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506231-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [-[NSManagedObjectContext objectRegisteredForID:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506789-registeredobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObject *)objectRegisteredForID:(NSManagedObjectID *)objectID ``` |
| To | ``` - (__kindof NSManagedObject * _Nullable)objectRegisteredForID:(NSManagedObjectID * _Nonnull)objectID ``` |

Modified [-[NSManagedObjectContext objectWithID:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506197-object)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObject *)objectWithID:(NSManagedObjectID *)objectID ``` |
| To | ``` - (__kindof NSManagedObject * _Nonnull)objectWithID:(NSManagedObjectID * _Nonnull)objectID ``` |

Modified [-[NSManagedObjectContext observeValueForKeyPath:ofObject:change:context:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506849-observevalueforkeypath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context ``` |
| To | ``` - (void)observeValueForKeyPath:(NSString * _Nullable)keyPath ofObject:(id _Nullable)object change:(NSDictionary<NSString *,id> * _Nullable)change context:(void * _Nullable)context ``` |

Modified [-[NSManagedObjectContext obtainPermanentIDsForObjects:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506793-obtainpermanentids)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)obtainPermanentIDsForObjects:(NSArray *)objects error:(NSError **)error ``` |
| To | ``` - (BOOL)obtainPermanentIDsForObjects:(NSArray<NSManagedObject *> * _Nonnull)objects error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSManagedObjectContext.parentContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506529-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSManagedObjectContext *parentContext ``` |
| To | ``` @property(strong, nullable) NSManagedObjectContext *parentContext ``` |

Modified [-[NSManagedObjectContext performBlock:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performBlock:(void (^)(void))block ``` |
| To | ``` - (void)performBlock:(void (^ _Nonnull)(void))block ``` |

Modified [-[NSManagedObjectContext performBlockAndWait:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performBlockAndWait:(void (^)(void))block ``` |
| To | ``` - (void)performBlockAndWait:(void (^ _Nonnull)(void))block ``` |

Modified [NSManagedObjectContext.persistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506618-persistentstorecoordinator)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSPersistentStoreCoordinator *persistentStoreCoordinator ``` |
| To | ``` @property(strong, nullable) NSPersistentStoreCoordinator *persistentStoreCoordinator ``` |

Modified [-[NSManagedObjectContext refreshObject:mergeChanges:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refreshobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)refreshObject:(NSManagedObject *)object mergeChanges:(BOOL)flag ``` |
| To | ``` - (void)refreshObject:(NSManagedObject * _Nonnull)object mergeChanges:(BOOL)flag ``` |

Modified [NSManagedObjectContext.registeredObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506493-registeredobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *registeredObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *registeredObjects ``` |

Modified [-[NSManagedObjectContext save:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)save:(NSError **)error ``` |
| To | ``` - (BOOL)save:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSManagedObjectContext.undoManager](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506663-undomanager)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSUndoManager *undoManager ``` |
| To | ``` @property(nonatomic, strong, nullable) NSUndoManager *undoManager ``` |

Modified [NSManagedObjectContext.updatedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506985-updatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *updatedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *updatedObjects ``` |

Modified [NSManagedObjectContext.userInfo](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506740-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSMutableDictionary *userInfo ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSMutableDictionary *userInfo ``` |

Modified [NSConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.4 | OS X 10.11 |

#### NSManagedObjectID.h

Modified [NSManagedObjectID.entity](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391684-entity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSEntityDescription *entity ``` |
| To | ``` @property(readonly, strong, nonnull) NSEntityDescription *entity ``` |

Modified [NSManagedObjectID.persistentStore](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391693-persistentstore)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, weak) NSPersistentStore *persistentStore ``` |
| To | ``` @property(readonly, weak, nullable) NSPersistentStore *persistentStore ``` |

Modified [-[NSManagedObjectID URIRepresentation]](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391689-urirepresentation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)URIRepresentation ``` |
| To | ``` - (NSURL * _Nonnull)URIRepresentation ``` |

#### NSManagedObjectModel.h

Modified [NSManagedObjectModel.configurations](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506804-configurations)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *configurations ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<NSString *> *configurations ``` |

Modified [NSManagedObjectModel.entities](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506318-entities)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *entities ``` |
| To | ``` @property(strong, nonnull) NSArray<NSEntityDescription *> *entities ``` |

Modified [NSManagedObjectModel.entitiesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506203-entitiesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *entitiesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSEntityDescription *> *entitiesByName ``` |

Modified [-[NSManagedObjectModel entitiesForConfiguration:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506693-entitiesforconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)entitiesForConfiguration:(NSString *)configuration ``` |
| To | ``` - (NSArray<NSEntityDescription *> * _Nullable)entitiesForConfiguration:(NSString * _Nullable)configuration ``` |

Modified [NSManagedObjectModel.entityVersionHashesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506992-entityversionhashesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *entityVersionHashesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSData *> *entityVersionHashesByName ``` |

Modified [-[NSManagedObjectModel fetchRequestFromTemplateWithName:substitutionVariables:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506422-fetchrequestfromtemplatewithname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSFetchRequest *)fetchRequestFromTemplateWithName:(NSString *)name substitutionVariables:(NSDictionary *)variables ``` |
| To | ``` - (NSFetchRequest * _Nullable)fetchRequestFromTemplateWithName:(NSString * _Nonnull)name substitutionVariables:(NSDictionary<NSString *,id> * _Nonnull)variables ``` |

Modified [-[NSManagedObjectModel fetchRequestTemplateForName:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506369-fetchrequesttemplateforname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSFetchRequest *)fetchRequestTemplateForName:(NSString *)name ``` |
| To | ``` - (NSFetchRequest * _Nullable)fetchRequestTemplateForName:(NSString * _Nonnull)name ``` |

Modified [NSManagedObjectModel.fetchRequestTemplatesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506580-fetchrequesttemplatesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *fetchRequestTemplatesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSFetchRequest *> *fetchRequestTemplatesByName ``` |

Modified [-[NSManagedObjectModel init]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506410-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[NSManagedObjectModel initWithContentsOfURL:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506225-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[NSManagedObjectModel isConfiguration:compatibleWithStoreMetadata:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506940-isconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isConfiguration:(NSString *)configuration compatibleWithStoreMetadata:(NSDictionary *)metadata ``` |
| To | ``` - (BOOL)isConfiguration:(NSString * _Nullable)configuration compatibleWithStoreMetadata:(NSDictionary<NSString *,id> * _Nonnull)metadata ``` |

Modified [NSManagedObjectModel.localizationDictionary](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506846-localizationdictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSDictionary *localizationDictionary ``` |
| To | ``` @property(strong, nullable) NSDictionary<NSString *,NSString *> *localizationDictionary ``` |

Modified [+[NSManagedObjectModel mergedModelFromBundles:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506704-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` + (NSManagedObjectModel *)mergedModelFromBundles:(NSArray *)bundles ``` |
| To | ``` + (NSManagedObjectModel * _Nullable)mergedModelFromBundles:(NSArray<NSBundle *> * _Nullable)bundles ``` |

Modified [+[NSManagedObjectModel mergedModelFromBundles:forStoreMetadata:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506788-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` + (NSManagedObjectModel *)mergedModelFromBundles:(NSArray *)bundles forStoreMetadata:(NSDictionary *)metadata ``` |
| To | ``` + (NSManagedObjectModel * _Nullable)mergedModelFromBundles:(NSArray<NSBundle *> * _Nullable)bundles forStoreMetadata:(NSDictionary<NSString *,id> * _Nonnull)metadata ``` |

Modified [+[NSManagedObjectModel modelByMergingModels:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506450-modelbymergingmodels)

|  | Declaration |
| --- | --- |
| From | ``` + (NSManagedObjectModel *)modelByMergingModels:(NSArray *)models ``` |
| To | ``` + (NSManagedObjectModel * _Nullable)modelByMergingModels:(NSArray<NSManagedObjectModel *> * _Nullable)models ``` |

Modified [+[NSManagedObjectModel modelByMergingModels:forStoreMetadata:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506856-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSManagedObjectModel *)modelByMergingModels:(NSArray *)models forStoreMetadata:(NSDictionary *)metadata ``` |
| To | ``` + (NSManagedObjectModel * _Nullable)modelByMergingModels:(NSArray<NSManagedObjectModel *> * _Nonnull)models forStoreMetadata:(NSDictionary<NSString *,id> * _Nonnull)metadata ``` |

Modified [-[NSManagedObjectModel setEntities:forConfiguration:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506287-setentities)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setEntities:(NSArray *)entities forConfiguration:(NSString *)configuration ``` |
| To | ``` - (void)setEntities:(NSArray<NSEntityDescription *> * _Nonnull)entities forConfiguration:(NSString * _Nonnull)configuration ``` |

Modified [-[NSManagedObjectModel setFetchRequestTemplate:forName:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506695-setfetchrequesttemplate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFetchRequestTemplate:(NSFetchRequest *)fetchRequestTemplate forName:(NSString *)name ``` |
| To | ``` - (void)setFetchRequestTemplate:(NSFetchRequest * _Nullable)fetchRequestTemplate forName:(NSString * _Nonnull)name ``` |

Modified [NSManagedObjectModel.versionIdentifiers](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506268-versionidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSSet *versionIdentifiers ``` |
| To | ``` @property(copy, nonnull) NSSet *versionIdentifiers ``` |

#### NSMappingModel.h

Modified [NSMappingModel.entityMappings](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506196-entitymappings)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *entityMappings ``` |
| To | ``` @property(strong) NSArray<NSEntityMapping *> * _Null_unspecified entityMappings ``` |

Modified [NSMappingModel.entityMappingsByName](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506179-entitymappingsbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *entityMappingsByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSEntityMapping *> *entityMappingsByName ``` |

Modified [+[NSMappingModel inferredMappingModelForSourceModel:destinationModel:error:]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506468-inferredmappingmodel)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMappingModel *)inferredMappingModelForSourceModel:(NSManagedObjectModel *)sourceModel destinationModel:(NSManagedObjectModel *)destinationModel error:(NSError **)error ``` |
| To | ``` + (NSMappingModel * _Nullable)inferredMappingModelForSourceModel:(NSManagedObjectModel * _Nonnull)sourceModel destinationModel:(NSManagedObjectModel * _Nonnull)destinationModel error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSMappingModel initWithContentsOfURL:]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506304-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nullable)url ``` |

Modified [+[NSMappingModel mappingModelFromBundles:forSourceModel:destinationModel:]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506930-mappingmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` + (NSMappingModel *)mappingModelFromBundles:(NSArray *)bundles forSourceModel:(NSManagedObjectModel *)sourceModel destinationModel:(NSManagedObjectModel *)destinationModel ``` |
| To | ``` + (NSMappingModel * _Nullable)mappingModelFromBundles:(NSArray<NSBundle *> * _Nullable)bundles forSourceModel:(NSManagedObjectModel * _Nullable)sourceModel destinationModel:(NSManagedObjectModel * _Nullable)destinationModel ``` |

#### NSMergePolicy.h

Added [NSConstraintConflict](https://developer.apple.com/documentation/coredata/nsconstraintconflict)Added [NSConstraintConflict.conflictingObjects](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506707-conflictingobjects)Added [NSConstraintConflict.conflictingSnapshots](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506774-conflictingsnapshots)Added [NSConstraintConflict.constraint](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506902-constraint)Added [NSConstraintConflict.constraintValues](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506399-constraintvalues)Added [NSConstraintConflict.databaseObject](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506665-databaseobject)Added [NSConstraintConflict.databaseSnapshot](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506687-databasesnapshot)Added [-[NSConstraintConflict initWithConstraint:databaseObject:databaseSnapshot:conflictingObjects:conflictingSnapshots:]](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506668-initwithconstraint)Added [-[NSMergePolicy resolveConstraintConflicts:error:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506678-resolve)Added [-[NSMergePolicy resolveOptimisticLockingVersionConflicts:error:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506787-resolve)Modified [NSMergeConflict.cachedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506685-cachedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSDictionary *cachedSnapshot ``` |
| To | ``` @property(readonly, retain, nullable) NSDictionary<NSString *,id> *cachedSnapshot ``` |

Modified [-[NSMergeConflict initWithSource:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:]](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506216-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSManagedObject *)srcObject newVersion:(NSUInteger)newvers oldVersion:(NSUInteger)oldvers cachedSnapshot:(NSDictionary *)cachesnap persistedSnapshot:(NSDictionary *)persnap ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSManagedObject * _Nonnull)srcObject newVersion:(NSUInteger)newvers oldVersion:(NSUInteger)oldvers cachedSnapshot:(NSDictionary<NSString *,id> * _Nullable)cachesnap persistedSnapshot:(NSDictionary<NSString *,id> * _Nullable)persnap ``` |

Modified [NSMergeConflict.objectSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506454-objectsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSDictionary *objectSnapshot ``` |
| To | ``` @property(readonly, retain, nullable) NSDictionary<NSString *,id> *objectSnapshot ``` |

Modified [NSMergeConflict.persistedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506412-persistedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSDictionary *persistedSnapshot ``` |
| To | ``` @property(readonly, retain, nullable) NSDictionary<NSString *,id> *persistedSnapshot ``` |

Modified [NSMergeConflict.sourceObject](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506809-sourceobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) NSManagedObject *sourceObject ``` |
| To | ``` @property(readonly, retain, nonnull) NSManagedObject *sourceObject ``` |

Modified [-[NSMergePolicy initWithMergeType:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506763-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMergeType:(NSMergePolicyType)ty ``` |
| To | ``` - (id _Nonnull)initWithMergeType:(NSMergePolicyType)ty ``` |

Modified [-[NSMergePolicy resolveConflicts:error:]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506253-resolveconflicts)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)resolveConflicts:(NSArray *)list error:(NSError **)error ``` |
| To | ``` - (BOOL)resolveConflicts:(NSArray * _Nonnull)list error:(NSError * _Nullable * _Nullable)error ``` |

#### NSMigrationManager.h

Modified [-[NSMigrationManager associateSourceInstance:withDestinationInstance:forEntityMapping:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417604-associate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)associateSourceInstance:(NSManagedObject *)sourceInstance withDestinationInstance:(NSManagedObject *)destinationInstance forEntityMapping:(NSEntityMapping *)entityMapping ``` |
| To | ``` - (void)associateSourceInstance:(NSManagedObject * _Nonnull)sourceInstance withDestinationInstance:(NSManagedObject * _Nonnull)destinationInstance forEntityMapping:(NSEntityMapping * _Nonnull)entityMapping ``` |

Modified [-[NSMigrationManager cancelMigrationWithError:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417608-cancelmigrationwitherror)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelMigrationWithError:(NSError *)error ``` |
| To | ``` - (void)cancelMigrationWithError:(NSError * _Nonnull)error ``` |

Modified [NSMigrationManager.currentEntityMapping](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417582-currententitymapping)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSEntityMapping *currentEntityMapping ``` |
| To | ``` @property(readonly, strong, nonnull) NSEntityMapping *currentEntityMapping ``` |

Modified [NSMigrationManager.destinationContext](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417578-destinationcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSManagedObjectContext *destinationContext ``` |
| To | ``` @property(readonly, strong, nonnull) NSManagedObjectContext *destinationContext ``` |

Modified [-[NSMigrationManager destinationEntityForEntityMapping:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417598-destinationentityforentitymappin)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEntityDescription *)destinationEntityForEntityMapping:(NSEntityMapping *)mEntity ``` |
| To | ``` - (NSEntityDescription * _Nullable)destinationEntityForEntityMapping:(NSEntityMapping * _Nonnull)mEntity ``` |

Modified [-[NSMigrationManager destinationInstancesForEntityMappingNamed:sourceInstances:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417594-destinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)destinationInstancesForEntityMappingNamed:(NSString *)mappingName sourceInstances:(NSArray *)sourceInstances ``` |
| To | ``` - (NSArray<__kindof NSManagedObject *> * _Nonnull)destinationInstancesForEntityMappingNamed:(NSString * _Nonnull)mappingName sourceInstances:(NSArray<__kindof NSManagedObject *> * _Nullable)sourceInstances ``` |

Modified [NSMigrationManager.destinationModel](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417610-destinationmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSManagedObjectModel *destinationModel ``` |
| To | ``` @property(readonly, strong, nonnull) NSManagedObjectModel *destinationModel ``` |

Modified [-[NSMigrationManager initWithSourceModel:destinationModel:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417583-initwithsourcemodel)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSourceModel:(NSManagedObjectModel *)sourceModel destinationModel:(NSManagedObjectModel *)destinationModel ``` |
| To | ``` - (instancetype _Nonnull)initWithSourceModel:(NSManagedObjectModel * _Nonnull)sourceModel destinationModel:(NSManagedObjectModel * _Nonnull)destinationModel ``` |

Modified [NSMigrationManager.mappingModel](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417600-mappingmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSMappingModel *mappingModel ``` |
| To | ``` @property(readonly, strong, nonnull) NSMappingModel *mappingModel ``` |

Modified [-[NSMigrationManager migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417584-migratestorefromurl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)migrateStoreFromURL:(NSURL *)sourceURL type:(NSString *)sStoreType options:(NSDictionary *)sOptions withMappingModel:(NSMappingModel *)mappings toDestinationURL:(NSURL *)dURL destinationType:(NSString *)dStoreType destinationOptions:(NSDictionary *)dOptions error:(NSError **)error ``` |
| To | ``` - (BOOL)migrateStoreFromURL:(NSURL * _Nonnull)sourceURL type:(NSString * _Nonnull)sStoreType options:(NSDictionary * _Nullable)sOptions withMappingModel:(NSMappingModel * _Nullable)mappings toDestinationURL:(NSURL * _Nonnull)dURL destinationType:(NSString * _Nonnull)dStoreType destinationOptions:(NSDictionary * _Nullable)dOptions error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSMigrationManager.sourceContext](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417576-sourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSManagedObjectContext *sourceContext ``` |
| To | ``` @property(readonly, strong, nonnull) NSManagedObjectContext *sourceContext ``` |

Modified [-[NSMigrationManager sourceEntityForEntityMapping:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417596-sourceentity)

|  | Declaration |
| --- | --- |
| From | ``` - (NSEntityDescription *)sourceEntityForEntityMapping:(NSEntityMapping *)mEntity ``` |
| To | ``` - (NSEntityDescription * _Nullable)sourceEntityForEntityMapping:(NSEntityMapping * _Nonnull)mEntity ``` |

Modified [-[NSMigrationManager sourceInstancesForEntityMappingNamed:destinationInstances:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417580-sourceinstancesforentitymappingn)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sourceInstancesForEntityMappingNamed:(NSString *)mappingName destinationInstances:(NSArray *)destinationInstances ``` |
| To | ``` - (NSArray<__kindof NSManagedObject *> * _Nonnull)sourceInstancesForEntityMappingNamed:(NSString * _Nonnull)mappingName destinationInstances:(NSArray<__kindof NSManagedObject *> * _Nullable)destinationInstances ``` |

Modified [NSMigrationManager.sourceModel](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417592-sourcemodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSManagedObjectModel *sourceModel ``` |
| To | ``` @property(readonly, strong, nonnull) NSManagedObjectModel *sourceModel ``` |

Modified [NSMigrationManager.userInfo](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417588-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSDictionary *userInfo ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDictionary *userInfo ``` |

#### NSPersistentStore.h

Modified [NSPersistentStore.configurationName](https://developer.apple.com/documentation/coredata/nspersistentstore/1506620-configurationname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *configurationName ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *configurationName ``` |

Modified [-[NSPersistentStore didAddToPersistentStoreCoordinator:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506873-didaddtopersistentstorecoordinat)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didAddToPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator ``` |
| To | ``` - (void)didAddToPersistentStoreCoordinator:(NSPersistentStoreCoordinator * _Nonnull)coordinator ``` |

Modified [NSPersistentStore.identifier](https://developer.apple.com/documentation/coredata/nspersistentstore/1506215-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *identifier ``` |
| To | ``` @property(copy) NSString * _Null_unspecified identifier ``` |

Modified [-[NSPersistentStore initWithPersistentStoreCoordinator:configurationName:URL:options:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506232-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)root configurationName:(NSString *)name URL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithPersistentStoreCoordinator:(NSPersistentStoreCoordinator * _Nullable)root configurationName:(NSString * _Nullable)name URL:(NSURL * _Nonnull)url options:(NSDictionary * _Nullable)options ``` |

Modified [-[NSPersistentStore loadMetadata:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506273-loadmetadata)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadMetadata:(NSError **)error ``` |
| To | ``` - (BOOL)loadMetadata:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSPersistentStore.metadata](https://developer.apple.com/documentation/coredata/nspersistentstore/1506564-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSDictionary *metadata ``` |
| To | ``` @property(nonatomic, strong) NSDictionary<NSString *,id> * _Null_unspecified metadata ``` |

Modified [+[NSPersistentStore metadataForPersistentStoreWithURL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506741-metadataforpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)metadataForPersistentStoreWithURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (NSDictionary<NSString *,id> * _Nullable)metadataForPersistentStoreWithURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSPersistentStore migrationManagerClass]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506361-migrationmanagerclass)

|  | Declaration |
| --- | --- |
| From | ``` + (Class)migrationManagerClass ``` |
| To | ``` + (Class _Nonnull)migrationManagerClass ``` |

Modified [NSPersistentStore.options](https://developer.apple.com/documentation/coredata/nspersistentstore/1506821-options)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSDictionary *options ``` |
| To | ``` @property(readonly, strong, nullable) NSDictionary *options ``` |

Modified [NSPersistentStore.persistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstore/1506226-persistentstorecoordinator)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, weak) NSPersistentStoreCoordinator *persistentStoreCoordinator ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) NSPersistentStoreCoordinator *persistentStoreCoordinator ``` |

Modified [+[NSPersistentStore setMetadata:forPersistentStoreWithURL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506824-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)setMetadata:(NSDictionary *)metadata forPersistentStoreWithURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (BOOL)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStoreWithURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSPersistentStore.type](https://developer.apple.com/documentation/coredata/nspersistentstore/1506250-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *type ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *type ``` |

Modified [NSPersistentStore.URL](https://developer.apple.com/documentation/coredata/nspersistentstore/1506700-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSURL *URL ``` |
| To | ``` @property(strong, nullable) NSURL *URL ``` |

Modified [-[NSPersistentStore willRemoveFromPersistentStoreCoordinator:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506731-willremovefrompersistentstorecoo)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willRemoveFromPersistentStoreCoordinator:(NSPersistentStoreCoordinator *)coordinator ``` |
| To | ``` - (void)willRemoveFromPersistentStoreCoordinator:(NSPersistentStoreCoordinator * _Nullable)coordinator ``` |

#### NSPersistentStoreCoordinator.h

Added [-[NSPersistentStoreCoordinator destroyPersistentStoreAtURL:withType:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468888-destroypersistentstore)Added [+[NSPersistentStoreCoordinator metadataForPersistentStoreOfType:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468778-metadataforpersistentstore)Added [-[NSPersistentStoreCoordinator replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468917-replacepersistentstore)Added [+[NSPersistentStoreCoordinator setMetadata:forPersistentStoreOfType:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468893-setmetadata)Added [NSPersistentStoreForceDestroyOption](https://developer.apple.com/documentation/coredata/nspersistentstoreforcedestroyoption)Modified [-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStore *)addPersistentStoreWithType:(NSString *)storeType configuration:(NSString *)configuration URL:(NSURL *)storeURL options:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` - (__kindof NSPersistentStore * _Nullable)addPersistentStoreWithType:(NSString * _Nonnull)storeType configuration:(NSString * _Nullable)configuration URL:(NSURL * _Nullable)storeURL options:(NSDictionary * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSPersistentStoreCoordinator elementsDerivedFromExternalRecordURL:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468919-elementsderived)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)elementsDerivedFromExternalRecordURL:(NSURL *)fileURL ``` |
| To | ``` + (NSDictionary * _Nonnull)elementsDerivedFromExternalRecordURL:(NSURL * _Nonnull)fileURL ``` |

Modified [-[NSPersistentStoreCoordinator executeRequest:withContext:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468872-execute)

|  | Declaration |
| --- | --- |
| From | ``` - (id)executeRequest:(NSPersistentStoreRequest *)request withContext:(NSManagedObjectContext *)context error:(NSError **)error ``` |
| To | ``` - (id _Nullable)executeRequest:(NSPersistentStoreRequest * _Nonnull)request withContext:(NSManagedObjectContext * _Nonnull)context error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSPersistentStoreCoordinator importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468788-importstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStore *)importStoreWithIdentifier:(NSString *)storeIdentifier fromExternalRecordsDirectory:(NSURL *)externalRecordsURL toURL:(NSURL *)destinationURL options:(NSDictionary *)options withType:(NSString *)storeType error:(NSError **)error ``` |
| To | ``` - (NSPersistentStore * _Nullable)importStoreWithIdentifier:(NSString * _Nullable)storeIdentifier fromExternalRecordsDirectory:(NSURL * _Nonnull)externalRecordsURL toURL:(NSURL * _Nonnull)destinationURL options:(NSDictionary * _Nullable)options withType:(NSString * _Nonnull)storeType error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSPersistentStoreCoordinator initWithManagedObjectModel:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468895-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithManagedObjectModel:(NSManagedObjectModel *)model ``` |
| To | ``` - (instancetype _Nonnull)initWithManagedObjectModel:(NSManagedObjectModel * _Nonnull)model ``` |

Modified [-[NSPersistentStoreCoordinator managedObjectIDForURIRepresentation:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468882-managedobjectidforurirepresentat)

|  | Declaration |
| --- | --- |
| From | ``` - (NSManagedObjectID *)managedObjectIDForURIRepresentation:(NSURL *)url ``` |
| To | ``` - (NSManagedObjectID * _Nullable)managedObjectIDForURIRepresentation:(NSURL * _Nonnull)url ``` |

Modified [NSPersistentStoreCoordinator.managedObjectModel](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468834-managedobjectmodel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSManagedObjectModel *managedObjectModel ``` |
| To | ``` @property(readonly, strong, nonnull) NSManagedObjectModel *managedObjectModel ``` |

Modified [-[NSPersistentStoreCoordinator metadataForPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468911-metadata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)metadataForPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)metadataForPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [+[NSPersistentStoreCoordinator metadataForPersistentStoreOfType:URL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468804-metadataforpersistentstore)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (NSDictionary *)metadataForPersistentStoreOfType:(NSString *)storeType URL:(NSURL *)url error:(NSError **)error ``` | -- |
| To | ``` + (NSDictionary<NSString *,id> * _Nullable)metadataForPersistentStoreOfType:(NSString * _Nullable)storeType URL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` | OS X 10.11 |

Modified [+[NSPersistentStoreCoordinator metadataForPersistentStoreWithURL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468915-metadataforpersistentstorewithur)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)metadataForPersistentStoreWithURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (NSDictionary * _Null_unspecified)metadataForPersistentStoreWithURL:(NSURL * _Null_unspecified)url error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSPersistentStoreCoordinator migratePersistentStore:toURL:options:withType:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStore *)migratePersistentStore:(NSPersistentStore *)store toURL:(NSURL *)URL options:(NSDictionary *)options withType:(NSString *)storeType error:(NSError **)error ``` |
| To | ``` - (NSPersistentStore * _Nullable)migratePersistentStore:(NSPersistentStore * _Nonnull)store toURL:(NSURL * _Nonnull)URL options:(NSDictionary * _Nullable)options withType:(NSString * _Nonnull)storeType error:(NSError * _Nullable * _Nullable)error ``` |

Modified [NSPersistentStoreCoordinator.name](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468929-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [-[NSPersistentStoreCoordinator performBlock:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468794-perform)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performBlock:(void (^)(void))block ``` |
| To | ``` - (void)performBlock:(void (^ _Nonnull)(void))block ``` |

Modified [-[NSPersistentStoreCoordinator performBlockAndWait:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468862-performblockandwait)

|  | Declaration |
| --- | --- |
| From | ``` - (void)performBlockAndWait:(void (^)(void))block ``` |
| To | ``` - (void)performBlockAndWait:(void (^ _Nonnull)(void))block ``` |

Modified [-[NSPersistentStoreCoordinator persistentStoreForURL:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468824-persistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStore *)persistentStoreForURL:(NSURL *)URL ``` |
| To | ``` - (__kindof NSPersistentStore * _Nullable)persistentStoreForURL:(NSURL * _Nonnull)URL ``` |

Modified [NSPersistentStoreCoordinator.persistentStores](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468790-persistentstores)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *persistentStores ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<__kindof NSPersistentStore *> *persistentStores ``` |

Modified [+[NSPersistentStoreCoordinator registeredStoreTypes]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468870-registeredstoretypes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)registeredStoreTypes ``` |
| To | ``` + (NSDictionary<NSString *,NSValue *> * _Nonnull)registeredStoreTypes ``` |

Modified [+[NSPersistentStoreCoordinator registerStoreClass:forStoreType:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468786-registerstoreclass)

|  | Declaration |
| --- | --- |
| From | ``` + (void)registerStoreClass:(Class)storeClass forStoreType:(NSString *)storeType ``` |
| To | ``` + (void)registerStoreClass:(Class _Nonnull)storeClass forStoreType:(NSString * _Nonnull)storeType ``` |

Modified [-[NSPersistentStoreCoordinator removePersistentStore:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468907-removepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)removePersistentStore:(NSPersistentStore *)store error:(NSError **)error ``` |
| To | ``` - (BOOL)removePersistentStore:(NSPersistentStore * _Nonnull)store error:(NSError * _Nullable * _Nullable)error ``` |

Modified [+[NSPersistentStoreCoordinator removeUbiquitousContentAndPersistentStoreAtURL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468923-removeubiquitouscontentandpersis)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)removeUbiquitousContentAndPersistentStoreAtURL:(NSURL *)storeURL options:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` + (BOOL)removeUbiquitousContentAndPersistentStoreAtURL:(NSURL * _Nonnull)storeURL options:(NSDictionary * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSPersistentStoreCoordinator setMetadata:forPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468899-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMetadata:(NSDictionary *)metadata forPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (void)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [+[NSPersistentStoreCoordinator setMetadata:forPersistentStoreOfType:URL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468897-setmetadata)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (BOOL)setMetadata:(NSDictionary *)metadata forPersistentStoreOfType:(NSString *)storeType URL:(NSURL *)url error:(NSError **)error ``` | -- |
| To | ``` + (BOOL)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStoreOfType:(NSString * _Nullable)storeType URL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` | OS X 10.11 |

Modified [-[NSPersistentStoreCoordinator setURL:forPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468858-seturl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setURL:(NSURL *)url forPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (BOOL)setURL:(NSURL * _Nonnull)url forPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [-[NSPersistentStoreCoordinator URLForPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468865-urlforpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)URLForPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (NSURL * _Nonnull)URLForPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

#### NSPersistentStoreRequest.h

Added [NSBatchDeleteRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/batchdeleterequesttype)Modified [NSAsynchronousFetchRequest.completionBlock](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506815-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSPersistentStoreAsynchronousFetchResultCompletionBlock completionBlock ``` |
| To | ``` @property(strong, readonly, nullable) NSPersistentStoreAsynchronousFetchResultCompletionBlock completionBlock ``` |

Modified [NSAsynchronousFetchRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506719-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSFetchRequest *fetchRequest ``` |
| To | ``` @property(strong, readonly, nonnull) NSFetchRequest *fetchRequest ``` |

Modified [-[NSAsynchronousFetchRequest initWithFetchRequest:completionBlock:]](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506218-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest *)request completionBlock:(NSPersistentStoreAsynchronousFetchResultCompletionBlock)blk ``` |
| To | ``` - (instancetype _Nonnull)initWithFetchRequest:(NSFetchRequest * _Nonnull)request completionBlock:(NSPersistentStoreAsynchronousFetchResultCompletionBlock _Nullable)blk ``` |

Modified [NSPersistentStoreRequest.affectedStores](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *affectedStores ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSPersistentStore *> *affectedStores ``` |

#### NSPersistentStoreResult.h

Added [NSBatchDeleteResult](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)Added [NSBatchDeleteResult.result](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404922-result)Added [NSBatchDeleteResult.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404941-resulttype)Added [NSBatchDeleteRequestResultType](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)Added [NSBatchDeleteResultTypeCount](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/nsbatchdeleteresulttypecount)Added [NSBatchDeleteResultTypeObjectIDs](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypeobjectids)Added [NSBatchDeleteResultTypeStatusOnly](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/nsbatchdeleteresulttypestatusonly)Modified [NSAsynchronousFetchResult.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404906-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSAsynchronousFetchRequest *fetchRequest ``` |
| To | ``` @property(strong, readonly, nonnull) NSAsynchronousFetchRequest *fetchRequest ``` |

Modified [NSAsynchronousFetchResult.finalResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404930-finalresult)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSArray *finalResult ``` |
| To | ``` @property(strong, readonly, nullable) NSArray *finalResult ``` |

Modified [NSBatchUpdateResult.result](https://developer.apple.com/documentation/coredata/nsbatchupdateresult/1404946-result)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) id result ``` |
| To | ``` @property(strong, readonly, nullable) id result ``` |

Modified [NSPersistentStoreAsynchronousResult.managedObjectContext](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/1404916-managedobjectcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSManagedObjectContext *managedObjectContext ``` |
| To | ``` @property(strong, readonly, nonnull) NSManagedObjectContext *managedObjectContext ``` |

Modified [NSPersistentStoreAsynchronousResult.operationError](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/1404904-operationerror)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSError *operationError ``` |
| To | ``` @property(strong, readonly, nullable) NSError *operationError ``` |

Modified [NSPersistentStoreAsynchronousResult.progress](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/1404920-progress)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSProgress *progress ``` |
| To | ``` @property(strong, readonly, nullable) NSProgress *progress ``` |

#### NSPropertyDescription.h

Modified [NSPropertyDescription.entity](https://developer.apple.com/documentation/coredata/nspropertydescription/1506745-entity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, assign) NSEntityDescription *entity ``` |
| To | ``` @property(nonatomic, readonly, assign, nonnull) NSEntityDescription *entity ``` |

Modified [NSPropertyDescription.name](https://developer.apple.com/documentation/coredata/nspropertydescription/1506759-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *name ``` |

Modified [NSPropertyDescription.renamingIdentifier](https://developer.apple.com/documentation/coredata/nspropertydescription/1506641-renamingidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *renamingIdentifier ``` |
| To | ``` @property(copy, nullable) NSString *renamingIdentifier ``` |

Modified [-[NSPropertyDescription setValidationPredicates:withValidationWarnings:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506852-setvalidationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValidationPredicates:(NSArray *)validationPredicates withValidationWarnings:(NSArray *)validationWarnings ``` |
| To | ``` - (void)setValidationPredicates:(NSArray<NSPredicate *> * _Nullable)validationPredicates withValidationWarnings:(NSArray<NSString *> * _Nullable)validationWarnings ``` |

Modified [NSPropertyDescription.userInfo](https://developer.apple.com/documentation/coredata/nspropertydescription/1506833-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSDictionary *userInfo ``` |
| To | ``` @property(nonatomic, strong, nullable) NSDictionary *userInfo ``` |

Modified [NSPropertyDescription.validationPredicates](https://developer.apple.com/documentation/coredata/nspropertydescription/1506842-validationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *validationPredicates ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<NSPredicate *> *validationPredicates ``` |

Modified [NSPropertyDescription.validationWarnings](https://developer.apple.com/documentation/coredata/nspropertydescription/1506886-validationwarnings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *validationWarnings ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray *validationWarnings ``` |

Modified [NSPropertyDescription.versionHash](https://developer.apple.com/documentation/coredata/nspropertydescription/1506198-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSData *versionHash ``` |
| To | ``` @property(readonly, copy, nonnull) NSData *versionHash ``` |

Modified [NSPropertyDescription.versionHashModifier](https://developer.apple.com/documentation/coredata/nspropertydescription/1506214-versionhashmodifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *versionHashModifier ``` |
| To | ``` @property(copy, nullable) NSString *versionHashModifier ``` |

#### NSPropertyMapping.h

Modified [NSPropertyMapping.name](https://developer.apple.com/documentation/coredata/nspropertymapping/1506748-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [NSPropertyMapping.userInfo](https://developer.apple.com/documentation/coredata/nspropertymapping/1506516-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSDictionary *userInfo ``` |
| To | ``` @property(strong, nullable) NSDictionary *userInfo ``` |

Modified [NSPropertyMapping.valueExpression](https://developer.apple.com/documentation/coredata/nspropertymapping/1506819-valueexpression)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSExpression *valueExpression ``` |
| To | ``` @property(strong, nullable) NSExpression *valueExpression ``` |

#### NSRelationshipDescription.h

Modified [NSRelationshipDescription.destinationEntity](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506652-destinationentity)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSEntityDescription *destinationEntity ``` |
| To | ``` @property(nonatomic, assign, nullable) NSEntityDescription *destinationEntity ``` |

Modified [NSRelationshipDescription.inverseRelationship](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506596-inverserelationship)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSRelationshipDescription *inverseRelationship ``` |
| To | ``` @property(nonatomic, assign, nullable) NSRelationshipDescription *inverseRelationship ``` |

Modified [NSRelationshipDescription.versionHash](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506791-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSData *versionHash ``` |
| To | ``` @property(readonly, copy, nonnull) NSData *versionHash ``` |

#### NSSaveChangesRequest.h

Modified [NSSaveChangesRequest.deletedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500420-deletedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSSet *deletedObjects ``` |
| To | ``` @property(readonly, strong, nullable) NSSet<__kindof NSManagedObject *> *deletedObjects ``` |

Modified [-[NSSaveChangesRequest initWithInsertedObjects:updatedObjects:deletedObjects:lockedObjects:]](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500418-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithInsertedObjects:(NSSet *)insertedObjects updatedObjects:(NSSet *)updatedObjects deletedObjects:(NSSet *)deletedObjects lockedObjects:(NSSet *)lockedObjects ``` |
| To | ``` - (instancetype _Nonnull)initWithInsertedObjects:(NSSet<NSManagedObject *> * _Nullable)insertedObjects updatedObjects:(NSSet<NSManagedObject *> * _Nullable)updatedObjects deletedObjects:(NSSet<NSManagedObject *> * _Nullable)deletedObjects lockedObjects:(NSSet<NSManagedObject *> * _Nullable)lockedObjects ``` |

Modified [NSSaveChangesRequest.insertedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500416-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSSet *insertedObjects ``` |
| To | ``` @property(readonly, strong, nullable) NSSet<__kindof NSManagedObject *> *insertedObjects ``` |

Modified [NSSaveChangesRequest.lockedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500426-lockedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSSet *lockedObjects ``` |
| To | ``` @property(readonly, strong, nullable) NSSet<__kindof NSManagedObject *> *lockedObjects ``` |

Modified [NSSaveChangesRequest.updatedObjects](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500424-updatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSSet *updatedObjects ``` |
| To | ``` @property(readonly, strong, nullable) NSSet<__kindof NSManagedObject *> *updatedObjects ``` |

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
