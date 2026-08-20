---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreData.html
archived_at: '2026-07-18T02:56:31.442656Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


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

Modified [-[NSAtomicStore cacheNodes]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388042-cachenodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)cacheNodes ``` |
| To | ``` - (NSSet<__kindof NSAtomicStoreCacheNode *> * _Nonnull)cacheNodes ``` |

Modified [-[NSAtomicStore willRemoveCacheNodes:]](https://developer.apple.com/documentation/coredata/nsatomicstore/1388064-willremovecachenodes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willRemoveCacheNodes:(NSSet *)cacheNodes ``` |
| To | ``` - (void)willRemoveCacheNodes:(NSSet<__kindof NSAtomicStoreCacheNode *> * _Nonnull)cacheNodes ``` |

#### NSAtomicStoreCacheNode.h

Modified [NSAtomicStoreCacheNode.propertyCache](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506283-propertycache)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSMutableDictionary *propertyCache ``` |
| To | ``` @property(nonatomic, strong, nullable) NSMutableDictionary<NSString *,id> *propertyCache ``` |

#### NSBatchDeleteRequest.h (Added)

Added [NSBatchDeleteRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest)Added [NSBatchDeleteRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506206-fetchrequest)Added [-[NSBatchDeleteRequest initWithFetchRequest:]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506302-initwithfetchrequest)Added [-[NSBatchDeleteRequest initWithObjectIDs:]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506746-initwithobjectids)Added [NSBatchDeleteRequest.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506389-resulttype)

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

Modified [+[NSEntityDescription insertNewObjectForEntityForName:inManagedObjectContext:]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425093-insertnewobject)

|  | Declaration |
| --- | --- |
| From | ``` + (id)insertNewObjectForEntityForName:(NSString *)entityName inManagedObjectContext:(NSManagedObjectContext *)context ``` |
| To | ``` + (__kindof NSManagedObject * _Nonnull)insertNewObjectForEntityForName:(NSString * _Nonnull)entityName inManagedObjectContext:(NSManagedObjectContext * _Nonnull)context ``` |

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

#### NSEntityMapping.h

Modified [NSEntityMapping.attributeMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443193-attributemappings)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *attributeMappings ``` |
| To | ``` @property(strong, nullable) NSArray<NSPropertyMapping *> *attributeMappings ``` |

Modified [NSEntityMapping.relationshipMappings](https://developer.apple.com/documentation/coredata/nsentitymapping/1443163-relationshipmappings)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSArray *relationshipMappings ``` |
| To | ``` @property(strong, nullable) NSArray<NSPropertyMapping *> *relationshipMappings ``` |

#### NSFetchedResultsController.h

Modified [-[NSFetchedResultsController initWithFetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:]](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622282-initwithfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFetchRequest:(NSFetchRequest *)fetchRequest managedObjectContext:(NSManagedObjectContext *)context sectionNameKeyPath:(NSString *)sectionNameKeyPath cacheName:(NSString *)name ``` |
| To | ``` - (instancetype _Nonnull)initWithFetchRequest:(NSFetchRequest * _Nonnull)fetchRequest managedObjectContext:(NSManagedObjectContext * _Nonnull)context sectionNameKeyPath:(NSString * _Nullable)sectionNameKeyPath cacheName:(NSString * _Nullable)name ``` |

Modified [NSFetchedResultsController.sectionIndexTitles](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622299-sectionindextitles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sectionIndexTitles ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *sectionIndexTitles ``` |

Modified [NSFetchedResultsController.sections](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622303-sections)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sections ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<id<NSFetchedResultsSectionInfo>> *sections ``` |

Modified [NSFetchedResultsControllerDelegate](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

#### NSFetchRequest.h

Modified [NSFetchRequest.affectedStores](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506518-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *affectedStores ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSPersistentStore *> *affectedStores ``` |

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

Removed NSFetchRequestExpressionTypeAdded [NSFetchRequestExpressionType](https://developer.apple.com/documentation/coredata/nsfetchrequestexpressiontype)

#### NSIncrementalStore.h

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

Modified [-[NSIncrementalStore obtainPermanentIDsForObjects:error:]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentids)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)obtainPermanentIDsForObjects:(NSArray *)array error:(NSError **)error ``` |
| To | ``` - (NSArray<NSManagedObjectID *> * _Nullable)obtainPermanentIDsForObjects:(NSArray<NSManagedObject *> * _Nonnull)array error:(NSError * _Nullable * _Nullable)error ``` |

#### NSIncrementalStoreNode.h

Modified [-[NSIncrementalStoreNode initWithObjectID:withValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithObjectID:(NSManagedObjectID *)objectID withValues:(NSDictionary *)values version:(uint64_t)version ``` |
| To | ``` - (instancetype _Nonnull)initWithObjectID:(NSManagedObjectID * _Nonnull)objectID withValues:(NSDictionary<NSString *,id> * _Nonnull)values version:(uint64_t)version ``` |

Modified [-[NSIncrementalStoreNode updateWithValues:version:]](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-updatewithvalues)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateWithValues:(NSDictionary *)values version:(uint64_t)version ``` |
| To | ``` - (void)updateWithValues:(NSDictionary<NSString *,id> * _Nonnull)values version:(uint64_t)version ``` |

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

Modified [-[NSManagedObject initWithEntity:insertIntoManagedObjectContext:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEntity:(NSEntityDescription *)entity insertIntoManagedObjectContext:(NSManagedObjectContext *)context ``` |
| To | ``` - (__kindof NSManagedObject * _Nonnull)initWithEntity:(NSEntityDescription * _Nonnull)entity insertIntoManagedObjectContext:(NSManagedObjectContext * _Nullable)context ``` |

#### NSManagedObjectContext.h

Added [+[NSManagedObjectContext mergeChangesFromRemoteContextSave:intoContexts:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506546-mergechanges)Added [+[NSManagedObjectContext new]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506632-new)Added [-[NSManagedObjectContext refreshAllObjects]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506217-refreshallobjects)Added [NSManagedObjectContext.shouldDeleteInaccessibleFaults](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506221-shoulddeleteinaccessiblefaults)Added [-[NSManagedObjectContext shouldHandleInaccessibleFault:forObjectID:triggeredByProperty:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506810-shouldhandleinaccessiblefault)Modified [NSManagedObjectContext.deletedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506699-deletedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *deletedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *deletedObjects ``` |

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

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [NSManagedObjectContext.insertedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506192-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *insertedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *insertedObjects ``` |

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

Modified [NSManagedObjectContext.registeredObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506493-registeredobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *registeredObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *registeredObjects ``` |

Modified [NSManagedObjectContext.updatedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506985-updatedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSSet *updatedObjects ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSSet<__kindof NSManagedObject *> *updatedObjects ``` |

Modified [NSConfinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

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

Modified [NSManagedObjectModel.fetchRequestTemplatesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506580-fetchrequesttemplatesbyname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *fetchRequestTemplatesByName ``` |
| To | ``` @property(readonly, copy, nonnull) NSDictionary<NSString *,NSFetchRequest *> *fetchRequestTemplatesByName ``` |

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

#### NSMigrationManager.h

Modified [-[NSMigrationManager destinationInstancesForEntityMappingNamed:sourceInstances:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417594-destinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)destinationInstancesForEntityMappingNamed:(NSString *)mappingName sourceInstances:(NSArray *)sourceInstances ``` |
| To | ``` - (NSArray<__kindof NSManagedObject *> * _Nonnull)destinationInstancesForEntityMappingNamed:(NSString * _Nonnull)mappingName sourceInstances:(NSArray<__kindof NSManagedObject *> * _Nullable)sourceInstances ``` |

Modified [-[NSMigrationManager sourceInstancesForEntityMappingNamed:destinationInstances:]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417580-sourceinstancesforentitymappingn)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)sourceInstancesForEntityMappingNamed:(NSString *)mappingName destinationInstances:(NSArray *)destinationInstances ``` |
| To | ``` - (NSArray<__kindof NSManagedObject *> * _Nonnull)sourceInstancesForEntityMappingNamed:(NSString * _Nonnull)mappingName destinationInstances:(NSArray<__kindof NSManagedObject *> * _Nullable)destinationInstances ``` |

#### NSPersistentStore.h

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

Modified [+[NSPersistentStore setMetadata:forPersistentStoreWithURL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506824-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)setMetadata:(NSDictionary *)metadata forPersistentStoreWithURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` + (BOOL)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStoreWithURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` |

#### NSPersistentStoreCoordinator.h

Added [-[NSPersistentStoreCoordinator destroyPersistentStoreAtURL:withType:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468888-destroypersistentstore)Added [+[NSPersistentStoreCoordinator metadataForPersistentStoreOfType:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468778-metadataforpersistentstore)Added [-[NSPersistentStoreCoordinator replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468917-replacepersistentstore)Added [+[NSPersistentStoreCoordinator setMetadata:forPersistentStoreOfType:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468893-setmetadata)Added [NSPersistentStoreForceDestroyOption](https://developer.apple.com/documentation/coredata/nspersistentstoreforcedestroyoption)Modified [-[NSPersistentStoreCoordinator addPersistentStoreWithType:configuration:URL:options:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` - (NSPersistentStore *)addPersistentStoreWithType:(NSString *)storeType configuration:(NSString *)configuration URL:(NSURL *)storeURL options:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` - (__kindof NSPersistentStore * _Nullable)addPersistentStoreWithType:(NSString * _Nonnull)storeType configuration:(NSString * _Nullable)configuration URL:(NSURL * _Nullable)storeURL options:(NSDictionary * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSPersistentStoreCoordinator metadataForPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468911-metadata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)metadataForPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (NSDictionary<NSString *,id> * _Nonnull)metadataForPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [+[NSPersistentStoreCoordinator metadataForPersistentStoreOfType:URL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468804-metadataforpersistentstore)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (NSDictionary *)metadataForPersistentStoreOfType:(NSString *)storeType URL:(NSURL *)url error:(NSError **)error ``` | -- |
| To | ``` + (NSDictionary<NSString *,id> * _Nullable)metadataForPersistentStoreOfType:(NSString * _Nullable)storeType URL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` | iOS 9.0 |

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

Modified [-[NSPersistentStoreCoordinator setMetadata:forPersistentStore:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468899-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMetadata:(NSDictionary *)metadata forPersistentStore:(NSPersistentStore *)store ``` |
| To | ``` - (void)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStore:(NSPersistentStore * _Nonnull)store ``` |

Modified [+[NSPersistentStoreCoordinator setMetadata:forPersistentStoreOfType:URL:error:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468897-setmetadata)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (BOOL)setMetadata:(NSDictionary *)metadata forPersistentStoreOfType:(NSString *)storeType URL:(NSURL *)url error:(NSError **)error ``` | -- |
| To | ``` + (BOOL)setMetadata:(NSDictionary<NSString *,id> * _Nullable)metadata forPersistentStoreOfType:(NSString * _Nullable)storeType URL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)error ``` | iOS 9.0 |

#### NSPersistentStoreRequest.h

Added [NSBatchDeleteRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/batchdeleterequesttype)Modified [NSPersistentStoreRequest.affectedStores](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/1506844-affectedstores)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *affectedStores ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSPersistentStore *> *affectedStores ``` |

#### NSPersistentStoreResult.h

Added [NSBatchDeleteResult](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)Added [NSBatchDeleteResult.result](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404922-result)Added [NSBatchDeleteResult.resultType](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404941-resulttype)Added [NSBatchDeleteRequestResultType](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)Added [NSBatchDeleteResultTypeCount](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/nsbatchdeleteresulttypecount)Added [NSBatchDeleteResultTypeObjectIDs](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypeobjectids)Added [NSBatchDeleteResultTypeStatusOnly](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/nsbatchdeleteresulttypestatusonly)

#### NSPropertyDescription.h

Modified [-[NSPropertyDescription setValidationPredicates:withValidationWarnings:]](https://developer.apple.com/documentation/coredata/nspropertydescription/1506852-setvalidationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setValidationPredicates:(NSArray *)validationPredicates withValidationWarnings:(NSArray *)validationWarnings ``` |
| To | ``` - (void)setValidationPredicates:(NSArray<NSPredicate *> * _Nullable)validationPredicates withValidationWarnings:(NSArray<NSString *> * _Nullable)validationWarnings ``` |

Modified [NSPropertyDescription.validationPredicates](https://developer.apple.com/documentation/coredata/nspropertydescription/1506842-validationpredicates)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *validationPredicates ``` |
| To | ``` @property(readonly, strong, nonnull) NSArray<NSPredicate *> *validationPredicates ``` |

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
