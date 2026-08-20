---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/Photos.html
archived_at: '2026-07-18T02:56:36.154037Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Photos Changes for Objective-C

### Photos

#### PHAsset.h

Added [PHAsset.sourceType](https://developer.apple.com/documentation/photokit/phasset/1624785-sourcetype)Modified [+[PHAsset fetchAssetsInAssetCollection:options:]](https://developer.apple.com/documentation/photokit/phasset/1624757-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsInAssetCollection:(PHAssetCollection *)assetCollection options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsInAssetCollection:(PHAssetCollection * _Nonnull)assetCollection options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchAssetsWithALAssetURLs:options:]](https://developer.apple.com/documentation/photokit/phasset/1624782-fetchassetswithalasseturls)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsWithALAssetURLs:(NSArray *)assetURLs options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsWithALAssetURLs:(NSArray<NSURL *> * _Nonnull)assetURLs options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchAssetsWithBurstIdentifier:options:]](https://developer.apple.com/documentation/photokit/phasset/1624723-fetchassetswithburstidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsWithBurstIdentifier:(NSString *)burstIdentifier options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsWithBurstIdentifier:(NSString * _Nonnull)burstIdentifier options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchAssetsWithLocalIdentifiers:options:]](https://developer.apple.com/documentation/photokit/phasset/1624732-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsWithLocalIdentifiers:(NSArray *)identifiers options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsWithLocalIdentifiers:(NSArray<NSString *> * _Nonnull)identifiers options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchAssetsWithMediaType:options:]](https://developer.apple.com/documentation/photokit/phasset/1624725-fetchassetswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsWithMediaType:(PHAssetMediaType)mediaType options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsWithMediaType:(PHAssetMediaType)mediaType options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchAssetsWithOptions:]](https://developer.apple.com/documentation/photokit/phasset/1624783-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetsWithOptions:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nonnull)fetchAssetsWithOptions:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAsset fetchKeyAssetsInAssetCollection:options:]](https://developer.apple.com/documentation/photokit/phasset/1624778-fetchkeyassetsinassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchKeyAssetsInAssetCollection:(PHAssetCollection *)assetCollection options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAsset *> * _Nullable)fetchKeyAssetsInAssetCollection:(PHAssetCollection * _Nonnull)assetCollection options:(PHFetchOptions * _Nullable)options ``` |

#### PHAssetCreationRequest.h (Added)

Added [PHAssetCreationRequest](https://developer.apple.com/documentation/photokit/phassetcreationrequest)Added [-[PHAssetCreationRequest addResourceWithType:data:options:]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622684-addresourcewithtype)Added [-[PHAssetCreationRequest addResourceWithType:fileURL:options:]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622681-addresourcewithtype)Added [+[PHAssetCreationRequest creationRequestForAsset]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622682-creationrequestforasset)Added [+[PHAssetCreationRequest supportsAssetResourceTypes:]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622685-supportsassetresourcetypes)Added [PHAssetResourceCreationOptions](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions)Added [PHAssetResourceCreationOptions.originalFilename](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622683-originalfilename)Added [PHAssetResourceCreationOptions.shouldMoveFile](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622687-shouldmovefile)Added [PHAssetResourceCreationOptions.uniformTypeIdentifier](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622686-uniformtypeidentifier)

#### PHAssetResource.h (Added)

Added [PHAssetResource](https://developer.apple.com/documentation/photokit/phassetresource)Added [PHAssetResource.assetLocalIdentifier](https://developer.apple.com/documentation/photokit/phassetresource/1623990-assetlocalidentifier)Added [+[PHAssetResource assetResourcesForAsset:]](https://developer.apple.com/documentation/photokit/phassetresource/1623988-assetresourcesforasset)Added [PHAssetResource.originalFilename](https://developer.apple.com/documentation/photokit/phassetresource/1623985-originalfilename)Added [PHAssetResource.type](https://developer.apple.com/documentation/photokit/phassetresource/1623987-type)Added [PHAssetResource.uniformTypeIdentifier](https://developer.apple.com/documentation/photokit/phassetresource/1623989-uniformtypeidentifier)

#### PHAssetResourceManager.h (Added)

Added [PHAssetResourceManager](https://developer.apple.com/documentation/photokit/phassetresourcemanager)Added [-[PHAssetResourceManager cancelDataRequest:]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616269-canceldatarequest)Added [+[PHAssetResourceManager defaultManager]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616270-defaultmanager)Added [-[PHAssetResourceManager requestDataForAssetResource:options:dataReceivedHandler:completionHandler:]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616279-requestdataforassetresource)Added [-[PHAssetResourceManager writeDataForAssetResource:toFile:options:completionHandler:]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616280-writedataforassetresource)Added [PHAssetResourceRequestOptions](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions)Added [PHAssetResourceRequestOptions.networkAccessAllowed](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616275-isnetworkaccessallowed)Added [PHAssetResourceRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616272-progresshandler)Added [PHAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phassetresourcedatarequestid)Added [PHAssetResourceProgressHandler](https://developer.apple.com/documentation/photokit/phassetresourceprogresshandler)Added [PHInvalidAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phinvalidassetresourcedatarequestid)

#### PHChange.h

Modified [+[PHFetchResultChangeDetails changeDetailsFromFetchResult:toFetchResult:changedObjects:]](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613921-changedetailsfromfetchresult)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)changeDetailsFromFetchResult:(PHFetchResult *)fromResult toFetchResult:(PHFetchResult *)toResult changedObjects:(NSArray *)changedObjects ``` |
| To | ``` + (instancetype _Nonnull)changeDetailsFromFetchResult:(PHFetchResult * _Nonnull)fromResult toFetchResult:(PHFetchResult * _Nonnull)toResult changedObjects:(NSArray<PHObject *> * _Nonnull)changedObjects ``` |

Modified [PHFetchResultChangeDetails.changedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613910-changedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray *changedObjects ``` |
| To | ``` @property(atomic, strong, readonly, nonnull) NSArray<__kindof PHObject *> *changedObjects ``` |

Modified [PHFetchResultChangeDetails.insertedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613908-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray *insertedObjects ``` |
| To | ``` @property(atomic, strong, readonly, nonnull) NSArray<__kindof PHObject *> *insertedObjects ``` |

Modified [PHFetchResultChangeDetails.removedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613902-removedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray *removedObjects ``` |
| To | ``` @property(atomic, strong, readonly, nonnull) NSArray<__kindof PHObject *> *removedObjects ``` |

Modified [PHObjectChangeDetails.objectAfterChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613888-objectafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) id objectAfterChanges ``` |
| To | ``` @property(atomic, strong, readonly, nullable) __kindof PHObject *objectAfterChanges ``` |

Modified [PHObjectChangeDetails.objectBeforeChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613890-objectbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) id objectBeforeChanges ``` |
| To | ``` @property(atomic, strong, readonly, nonnull) __kindof PHObject *objectBeforeChanges ``` |

#### PHCollection.h

Modified [+[PHAssetCollection fetchAssetCollectionsContainingAsset:withType:options:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618530-fetchassetcollectionscontaininga)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetCollectionsContainingAsset:(PHAsset *)asset withType:(PHAssetCollectionType)type options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchAssetCollectionsContainingAsset:(PHAsset * _Nonnull)asset withType:(PHAssetCollectionType)type options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAssetCollection fetchAssetCollectionsWithALAssetGroupURLs:options:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618533-fetchassetcollectionswithalasset)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetCollectionsWithALAssetGroupURLs:(NSArray *)assetGroupURLs options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchAssetCollectionsWithALAssetGroupURLs:(NSArray<NSURL *> * _Nonnull)assetGroupURLs options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAssetCollection fetchAssetCollectionsWithLocalIdentifiers:options:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618510-fetchassetcollections)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetCollectionsWithLocalIdentifiers:(NSArray *)identifiers options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchAssetCollectionsWithLocalIdentifiers:(NSArray<NSString *> * _Nonnull)identifiers options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAssetCollection fetchAssetCollectionsWithType:subtype:options:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618544-fetchassetcollectionswithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchAssetCollectionsWithType:(PHAssetCollectionType)type subtype:(PHAssetCollectionSubtype)subtype options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchAssetCollectionsWithType:(PHAssetCollectionType)type subtype:(PHAssetCollectionSubtype)subtype options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAssetCollection fetchMomentsInMomentList:options:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618522-fetchmomentsinmomentlist)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchMomentsInMomentList:(PHCollectionList *)momentList options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchMomentsInMomentList:(PHCollectionList * _Nonnull)momentList options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHAssetCollection fetchMomentsWithOptions:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618531-fetchmoments)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchMomentsWithOptions:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHAssetCollection *> * _Nonnull)fetchMomentsWithOptions:(PHFetchOptions * _Nullable)options ``` |

Modified [PHAssetCollection.localizedLocationNames](https://developer.apple.com/documentation/photokit/phassetcollection/1618516-localizedlocationnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong, readonly) NSArray *localizedLocationNames ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) NSArray<NSString *> *localizedLocationNames ``` |

Modified [+[PHAssetCollection transientAssetCollectionWithAssetFetchResult:title:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618511-transientassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` + (PHAssetCollection *)transientAssetCollectionWithAssetFetchResult:(PHFetchResult *)fetchResult title:(NSString *)title ``` |
| To | ``` + (PHAssetCollection * _Nonnull)transientAssetCollectionWithAssetFetchResult:(PHFetchResult<PHAsset *> * _Nonnull)fetchResult title:(NSString * _Nullable)title ``` |

Modified [+[PHAssetCollection transientAssetCollectionWithAssets:title:]](https://developer.apple.com/documentation/photokit/phassetcollection/1618529-transientassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` + (PHAssetCollection *)transientAssetCollectionWithAssets:(NSArray *)assets title:(NSString *)title ``` |
| To | ``` + (PHAssetCollection * _Nonnull)transientAssetCollectionWithAssets:(NSArray<PHAsset *> * _Nonnull)assets title:(NSString * _Nullable)title ``` |

Modified [+[PHCollection fetchCollectionsInCollectionList:options:]](https://developer.apple.com/documentation/photokit/phcollection/1618515-fetchcollections)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchCollectionsInCollectionList:(PHCollectionList *)collectionList options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollection *> * _Nonnull)fetchCollectionsInCollectionList:(PHCollectionList * _Nonnull)collectionList options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollection fetchTopLevelUserCollectionsWithOptions:]](https://developer.apple.com/documentation/photokit/phcollection/1618513-fetchtoplevelusercollections)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchTopLevelUserCollectionsWithOptions:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollection *> * _Nonnull)fetchTopLevelUserCollectionsWithOptions:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollectionList fetchCollectionListsContainingCollection:options:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618523-fetchcollectionlistscontaining)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchCollectionListsContainingCollection:(PHCollection *)collection options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollectionList *> * _Nonnull)fetchCollectionListsContainingCollection:(PHCollection * _Nonnull)collection options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollectionList fetchCollectionListsWithLocalIdentifiers:options:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618525-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchCollectionListsWithLocalIdentifiers:(NSArray *)identifiers options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollectionList *> * _Nonnull)fetchCollectionListsWithLocalIdentifiers:(NSArray<NSString *> * _Nonnull)identifiers options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollectionList fetchCollectionListsWithType:subtype:options:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618520-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchCollectionListsWithType:(PHCollectionListType)collectionListType subtype:(PHCollectionListSubtype)subtype options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollectionList *> * _Nonnull)fetchCollectionListsWithType:(PHCollectionListType)collectionListType subtype:(PHCollectionListSubtype)subtype options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollectionList fetchMomentListsWithSubtype:containingMoment:options:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618536-fetchmomentlists)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchMomentListsWithSubtype:(PHCollectionListSubtype)momentListSubtype containingMoment:(PHAssetCollection *)moment options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollectionList *> * _Nonnull)fetchMomentListsWithSubtype:(PHCollectionListSubtype)momentListSubtype containingMoment:(PHAssetCollection * _Nonnull)moment options:(PHFetchOptions * _Nullable)options ``` |

Modified [+[PHCollectionList fetchMomentListsWithSubtype:options:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618540-fetchmomentlistswithsubtype)

|  | Declaration |
| --- | --- |
| From | ``` + (PHFetchResult *)fetchMomentListsWithSubtype:(PHCollectionListSubtype)momentListSubtype options:(PHFetchOptions *)options ``` |
| To | ``` + (PHFetchResult<PHCollectionList *> * _Nonnull)fetchMomentListsWithSubtype:(PHCollectionListSubtype)momentListSubtype options:(PHFetchOptions * _Nullable)options ``` |

Modified [PHCollectionList.localizedLocationNames](https://developer.apple.com/documentation/photokit/phcollectionlist/1618524-localizedlocationnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong, readonly) NSArray *localizedLocationNames ``` |
| To | ``` @property(nonatomic, strong, readonly, nonnull) NSArray<NSString *> *localizedLocationNames ``` |

Modified [+[PHCollectionList transientCollectionListWithCollections:title:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618537-transientcollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` + (PHCollectionList *)transientCollectionListWithCollections:(NSArray *)collections title:(NSString *)title ``` |
| To | ``` + (PHCollectionList * _Nonnull)transientCollectionListWithCollections:(NSArray<PHCollection *> * _Nonnull)collections title:(NSString * _Nullable)title ``` |

Modified [+[PHCollectionList transientCollectionListWithCollectionsFetchResult:title:]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618526-transientcollectionlistwithcolle)

|  | Declaration |
| --- | --- |
| From | ``` + (PHCollectionList *)transientCollectionListWithCollectionsFetchResult:(PHFetchResult *)fetchResult title:(NSString *)title ``` |
| To | ``` + (PHCollectionList * _Nonnull)transientCollectionListWithCollectionsFetchResult:(PHFetchResult<PHCollection *> * _Nonnull)fetchResult title:(NSString * _Nullable)title ``` |

#### PHContentEditingInput.h

Added [PHContentEditingInput.audiovisualAsset](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518648-audiovisualasset)Modified [PHContentEditingInput.avAsset](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1618636-avasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### PHFetchOptions.h

Added [PHFetchOptions.fetchLimit](https://developer.apple.com/documentation/photokit/phfetchoptions/1624761-fetchlimit)Added [PHFetchOptions.includeAssetSourceTypes](https://developer.apple.com/documentation/photokit/phfetchoptions/1624772-includeassetsourcetypes)Modified [PHFetchOptions.sortDescriptors](https://developer.apple.com/documentation/photokit/phfetchoptions/1624771-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSArray *sortDescriptors ``` |
| To | ``` @property(nonatomic, strong, nullable) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

#### PHFetchResult.h

Modified [-[PHFetchResult containsObject:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621005-containsobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)containsObject:(id)anObject ``` |
| To | ``` - (BOOL)containsObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[PHFetchResult enumerateObjectsAtIndexes:options:usingBlock:]](https://developer.apple.com/documentation/photokit/phfetchresult/1620998-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet *)s options:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsAtIndexes:(NSIndexSet * _Nonnull)s options:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[PHFetchResult enumerateObjectsUsingBlock:]](https://developer.apple.com/documentation/photokit/phfetchresult/1620999-enumerateobjectsusingblock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsUsingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsUsingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [-[PHFetchResult enumerateObjectsWithOptions:usingBlock:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621006-enumerateobjectswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(id obj, NSUInteger idx, BOOL *stop))block ``` |
| To | ``` - (void)enumerateObjectsWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^ _Nonnull)(ObjectType _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop))block ``` |

Modified [PHFetchResult.firstObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621003-firstobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id firstObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType firstObject ``` |

Modified [-[PHFetchResult indexOfObject:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621007-index)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)anObject ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)anObject ``` |

Modified [-[PHFetchResult indexOfObject:inRange:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621009-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` - (NSUInteger)indexOfObject:(id)anObject inRange:(NSRange)range ``` |
| To | ``` - (NSUInteger)indexOfObject:(ObjectType _Nonnull)anObject inRange:(NSRange)range ``` |

Modified [PHFetchResult.lastObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621001-lastobject)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id lastObject ``` |
| To | ``` @property(nonatomic, readonly, nullable) ObjectType lastObject ``` |

Modified [-[PHFetchResult objectAtIndex:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621002-objectatindex)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndex:(NSUInteger)index ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndex:(NSUInteger)index ``` |

Modified [-[PHFetchResult objectAtIndexedSubscript:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621000-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtIndexedSubscript:(NSUInteger)idx ``` |
| To | ``` - (ObjectType _Nonnull)objectAtIndexedSubscript:(NSUInteger)idx ``` |

Modified [-[PHFetchResult objectsAtIndexes:]](https://developer.apple.com/documentation/photokit/phfetchresult/1621008-objectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectsAtIndexes:(NSIndexSet *)indexes ``` |
| To | ``` - (NSArray<ObjectType> * _Nonnull)objectsAtIndexes:(NSIndexSet * _Nonnull)indexes ``` |

#### PHImageManager.h

Removed #def PHInvalidImageRequestIDAdded [PHInvalidImageRequestID](https://developer.apple.com/documentation/photokit/phinvalidimagerequestid)Modified [-[PHCachingImageManager startCachingImagesForAssets:targetSize:contentMode:options:]](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616986-startcachingimages)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startCachingImagesForAssets:(NSArray *)assets targetSize:(CGSize)targetSize contentMode:(PHImageContentMode)contentMode options:(PHImageRequestOptions *)options ``` |
| To | ``` - (void)startCachingImagesForAssets:(NSArray<PHAsset *> * _Nonnull)assets targetSize:(CGSize)targetSize contentMode:(PHImageContentMode)contentMode options:(PHImageRequestOptions * _Nullable)options ``` |

Modified [-[PHCachingImageManager stopCachingImagesForAssets:targetSize:contentMode:options:]](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616968-stopcachingimagesforassets)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopCachingImagesForAssets:(NSArray *)assets targetSize:(CGSize)targetSize contentMode:(PHImageContentMode)contentMode options:(PHImageRequestOptions *)options ``` |
| To | ``` - (void)stopCachingImagesForAssets:(NSArray<PHAsset *> * _Nonnull)assets targetSize:(CGSize)targetSize contentMode:(PHImageContentMode)contentMode options:(PHImageRequestOptions * _Nullable)options ``` |

#### PhotosTypes.h

Added [PHAssetCollectionSubtypeSmartAlbumScreenshots](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumscreenshots)Added [PHAssetCollectionSubtypeSmartAlbumSelfPortraits](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumselfportraits)Added [PHAssetMediaSubtypePhotoScreenshot](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518653-photoscreenshot)Added [PHAssetResourceType](https://developer.apple.com/documentation/photokit/phassetresourcetype)Added [PHAssetResourceTypeAdjustmentBasePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/adjustmentbasephoto)Added [PHAssetResourceTypeAdjustmentData](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentdata)Added [PHAssetResourceTypeAlternatePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/alternatephoto)Added [PHAssetResourceTypeAudio](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeaudio)Added [PHAssetResourceTypeFullSizePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/fullsizephoto)Added [PHAssetResourceTypeFullSizeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizevideo)Added [PHAssetResourceTypePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypephoto)Added [PHAssetResourceTypeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypevideo)Added [PHAssetSourceType](https://developer.apple.com/documentation/photokit/phassetsourcetype)Added [PHAssetSourceTypeCloudShared](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypecloudshared)Added [PHAssetSourceTypeiTunesSynced](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeitunessynced)Added [PHAssetSourceTypeNone](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypenone)Added [PHAssetSourceTypeUserLibrary](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeuserlibrary)

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
