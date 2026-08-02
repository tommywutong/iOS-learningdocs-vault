---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/CoreData.html
archived_at: '2026-07-18T02:57:25.355868Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreData Changes for Objective-C

### CoreData

#### CoreDataDefines.h

Added [#def NSCoreDataVersionNumber10_11](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_11)Added [#def NSCoreDataVersionNumber10_11_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_11_3)Added [#def NSCoreDataVersionNumber_iPhoneOS_9_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_0)Added [#def NSCoreDataVersionNumber_iPhoneOS_9_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_2)Added [#def NSCoreDataVersionNumber_iPhoneOS_9_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_3)

#### NSBatchUpdateRequest.h

Modified [-[NSBatchUpdateRequest initWithEntity:]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506374-initwithentity)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[NSBatchUpdateRequest initWithEntityName:]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506702-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### NSFetchedResultsController.h

Modified [NSFetchedResultsController.fetchedObjects](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622278-fetchedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *fetchedObjects ``` |
| To | ``` @property(nonatomic, readonly) NSArray<ResultType> *fetchedObjects ``` |

Modified [NSFetchedResultsController.fetchRequest](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622287-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSFetchRequest *fetchRequest ``` |
| To | ``` @property(nonatomic, readonly) NSFetchRequest<ResultType> *fetchRequest ``` |

Modified [-[NSFetchedResultsController indexPathForObject:]](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622306-indexpath)

|  | Declaration |
| --- | --- |
| From | ``` - (NSIndexPath *)indexPathForObject:(id)object ``` |
| To | ``` - (NSIndexPath *)indexPathForObject:(ResultType)object ``` |

Modified [-[NSFetchedResultsController initWithFetchRequest:managedObjectContext:sectionNameKeyPath:cacheName:]](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622282-initwithfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest *)fetchRequest managedObjectContext:(NSManagedObjectContext *)context sectionNameKeyPath:(NSString *)sectionNameKeyPath cacheName:(NSString *)name ``` |
| To | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest<ResultType> *)fetchRequest managedObjectContext:(NSManagedObjectContext *)context sectionNameKeyPath:(NSString *)sectionNameKeyPath cacheName:(NSString *)name ``` |

Modified [-[NSFetchedResultsController objectAtIndexPath:]](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622281-objectatindexpath)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndexPath:(NSIndexPath *)indexPath ``` |
| To | ``` - (ResultType)objectAtIndexPath:(NSIndexPath *)indexPath ``` |

#### NSFetchRequest.h

Added [-[NSFetchRequest execute:]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1640594-execute)Added [NSFetchRequestResult](https://developer.apple.com/documentation/coredata/nsfetchrequestresult)Added NSDictionary(NSFetchedResultSupport)Added NSManagedObject(NSFetchedResultSupport)Added NSManagedObjectID(NSFetchedResultSupport)Added NSNumber(NSFetchedResultSupport)Modified [NSAsynchronousFetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.completionBlock](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506815-completionblock)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.estimatedResultCount](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506474-estimatedresultcount)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506719-fetchrequest)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(strong, readonly) NSFetchRequest *fetchRequest ``` | CoreData/NSPersistentStoreRequest.h |
| To | ``` @property(strong, readonly) NSFetchRequest<ResultType> *fetchRequest ``` | CoreData/NSFetchRequest.h |

Modified [-[NSAsynchronousFetchRequest initWithFetchRequest:completionBlock:]](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506218-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest *)request completionBlock:(NSPersistentStoreAsynchronousFetchResultCompletionBlock)blk ``` | CoreData/NSPersistentStoreRequest.h |
| To | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest<ResultType> *)request completionBlock:(void (^)(NSAsynchronousFetchResult<ResultType> *))blk ``` | CoreData/NSFetchRequest.h |

Modified [NSPersistentStoreAsynchronousFetchResultCompletionBlock](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

#### NSManagedObject.h

Added [NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506727-contextshouldignoreunmodeledprop)Added [+[NSManagedObject entity]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640588-entity)Added [+[NSManagedObject fetchRequest]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640605-fetchrequest)Added [-[NSManagedObject initWithContext:]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640602-initwithcontext)

#### NSManagedObjectContext.h

Added [NSManagedObjectContext.automaticallyMergesChangesFromParent](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1845237-automaticallymergeschangesfrompa)Added [NSManagedObjectContext.queryGenerationToken](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1640477-querygenerationtoken)Added [-[NSManagedObjectContext setQueryGenerationFromToken:error:]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1640469-setquerygenerationfromtoken)Added [NSManagedObjectContextQueryGenerationKey](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextquerygenerationkey)

#### NSMergePolicy.h

Added [+[NSMergePolicy errorMergePolicy]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690612-errormergepolicy)Added [NSMergePolicy.errorMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690612-error)Added [+[NSMergePolicy mergeByPropertyObjectTrumpMergePolicy]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690607-mergebypropertyobjecttrumpmergep)Added [NSMergePolicy.mergeByPropertyObjectTrumpMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690607-mergebypropertyobjecttrumpmergep)Added [+[NSMergePolicy mergeByPropertyStoreTrumpMergePolicy]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690609-mergebypropertystoretrumpmergepo)Added [NSMergePolicy.mergeByPropertyStoreTrumpMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690609-mergebypropertystoretrump)Added [+[NSMergePolicy overwriteMergePolicy]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690610-overwrite)Added [NSMergePolicy.overwriteMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690610-overwrite)Added [+[NSMergePolicy rollbackMergePolicy]](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690613-rollbackmergepolicy)Added [NSMergePolicy.rollbackMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690613-rollbackmergepolicy)

#### NSPersistentContainer.h (Added)

Added [NSPersistentContainer](https://developer.apple.com/documentation/coredata/nspersistentcontainer)Added [+[NSPersistentContainer defaultDirectoryURL]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640597-defaultdirectoryurl)Added [-[NSPersistentContainer initWithName:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640557-initwithname)Added [-[NSPersistentContainer initWithName:managedObjectModel:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640584-init)Added [-[NSPersistentContainer loadPersistentStoresWithCompletionHandler:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640568-loadpersistentstoreswithcompleti)Added [NSPersistentContainer.managedObjectModel](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640561-managedobjectmodel)Added [NSPersistentContainer.name](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640579-name)Added [-[NSPersistentContainer newBackgroundContext]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640581-newbackgroundcontext)Added [-[NSPersistentContainer performBackgroundTask:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640564-performbackgroundtask)Added [+[NSPersistentContainer persistentContainerWithName:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1646295-persistentcontainerwithname)Added [+[NSPersistentContainer persistentContainerWithName:managedObjectModel:]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1646296-persistentcontainerwithname)Added [NSPersistentContainer.persistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640567-persistentstorecoordinator)Added [NSPersistentContainer.persistentStoreDescriptions](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640577-persistentstoredescriptions)Added [NSPersistentContainer.viewContext](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640622-viewcontext)

#### NSPersistentStoreCoordinator.h

Added [-[NSPersistentStoreCoordinator addPersistentStoreWithDescription:completionHandler:]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1640556-addpersistentstorewithdescriptio)Added [NSPersistentStoreCoordinator.registeredStoreTypes](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468870-registeredstoretypes)Added [NSPersistentStoreConnectionPoolMaxSizeKey](https://developer.apple.com/documentation/coredata/nspersistentstoreconnectionpoolmaxsizekey)

#### NSPersistentStoreDescription.h (Added)

Added [NSPersistentStoreDescription](https://developer.apple.com/documentation/coredata/nspersistentstoredescription)Added [NSPersistentStoreDescription.configuration](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640634-configuration)Added [-[NSPersistentStoreDescription initWithURL:]](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640563-initwithurl)Added [NSPersistentStoreDescription.options](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640571-options)Added [+[NSPersistentStoreDescription persistentStoreDescriptionWithURL:]](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1646473-persistentstoredescriptionwithur)Added [NSPersistentStoreDescription.readOnly](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640626-readonly)Added [-[NSPersistentStoreDescription setOption:forKey:]](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640574-setoption)Added [-[NSPersistentStoreDescription setValue:forPragmaNamed:]](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640598-setvalue)Added [NSPersistentStoreDescription.shouldAddStoreAsynchronously](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640599-shouldaddstoreasynchronously)Added [NSPersistentStoreDescription.shouldInferMappingModelAutomatically](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640623-shouldinfermappingmodelautomatic)Added [NSPersistentStoreDescription.shouldMigrateStoreAutomatically](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640566-shouldmigratestoreautomatically)Added [NSPersistentStoreDescription.sqlitePragmas](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640614-sqlitepragmas)Added [NSPersistentStoreDescription.timeout](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640587-timeout)Added [NSPersistentStoreDescription.type](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640609-type)Added [NSPersistentStoreDescription.URL](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640616-url)

#### NSPersistentStoreRequest.h

Modified [NSAsynchronousFetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.completionBlock](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506815-completionblock)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.estimatedResultCount](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506474-estimatedresultcount)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

Modified [NSAsynchronousFetchRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506719-fetchrequest)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(strong, readonly) NSFetchRequest *fetchRequest ``` | CoreData/NSPersistentStoreRequest.h |
| To | ``` @property(strong, readonly) NSFetchRequest<ResultType> *fetchRequest ``` | CoreData/NSFetchRequest.h |

Modified [-[NSAsynchronousFetchRequest initWithFetchRequest:completionBlock:]](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506218-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest *)request completionBlock:(NSPersistentStoreAsynchronousFetchResultCompletionBlock)blk ``` | CoreData/NSPersistentStoreRequest.h |
| To | ``` - (instancetype)initWithFetchRequest:(NSFetchRequest<ResultType> *)request completionBlock:(void (^)(NSAsynchronousFetchResult<ResultType> *))blk ``` | CoreData/NSFetchRequest.h |

Modified [NSPersistentStoreAsynchronousFetchResultCompletionBlock](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock)

|  | Header |
| --- | --- |
| From | CoreData/NSPersistentStoreRequest.h |
| To | CoreData/NSFetchRequest.h |

#### NSPersistentStoreResult.h

Modified [NSAsynchronousFetchResult.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404906-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSAsynchronousFetchRequest *fetchRequest ``` |
| To | ``` @property(strong, readonly) NSAsynchronousFetchRequest<ResultType> *fetchRequest ``` |

Modified [NSAsynchronousFetchResult.finalResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404930-finalresult)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, readonly) NSArray *finalResult ``` |
| To | ``` @property(strong, readonly) NSArray<ResultType> *finalResult ``` |

#### NSQueryGenerationToken.h (Added)

Added [NSQueryGenerationToken](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken)Added [+[NSQueryGenerationToken currentQueryGenerationToken]](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken/1640578-currentquerygenerationtoken)Added [NSQueryGenerationToken.currentQueryGenerationToken](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken/1640578-currentquerygenerationtoken)

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
