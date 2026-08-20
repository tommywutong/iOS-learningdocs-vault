---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Photos.html
archived_at: '2026-07-18T02:56:57.082316Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Photos Changes for Swift

### Photos

Removed PHAssetBurstSelectionType.init(_: UInt)Removed PHAssetMediaSubtype.init(_: UInt)Added [PHAsset.sourceType](https://developer.apple.com/documentation/photokit/phasset/1624785-sourcetype)Added [PHAssetCollectionSubtype.SmartAlbumScreenshots](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumscreenshots)Added [PHAssetCollectionSubtype.SmartAlbumSelfPortraits](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumselfportraits)Added [PHAssetCreationRequest](https://developer.apple.com/documentation/photokit/phassetcreationrequest)Added [PHAssetCreationRequest.addResourceWithType(_: PHAssetResourceType, data: NSData, options: PHAssetResourceCreationOptions?)](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622684-addresourcewithtype)Added [PHAssetCreationRequest.addResourceWithType(_: PHAssetResourceType, fileURL: NSURL, options: PHAssetResourceCreationOptions?)](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622681-addresourcewithtype)Added [PHAssetCreationRequest.creationRequestForAsset() -> Self [class]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622682-creationrequestforasset)Added [PHAssetCreationRequest.supportsAssetResourceTypes(_: [NSNumber]) -> Bool [class]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622685-supportsassetresourcetypes)Added [PHAssetMediaSubtype.PhotoScreenshot](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518653-photoscreenshot)Added [PHAssetResource](https://developer.apple.com/documentation/photokit/phassetresource)Added [PHAssetResource.assetLocalIdentifier](https://developer.apple.com/documentation/photokit/phassetresource/1623990-assetlocalidentifier)Added [PHAssetResource.assetResourcesForAsset(_: PHAsset) -> [PHAssetResource] [class]](https://developer.apple.com/documentation/photokit/phassetresource/1623988-assetresourcesforasset)Added [PHAssetResource.originalFilename](https://developer.apple.com/documentation/photokit/phassetresource/1623985-originalfilename)Added [PHAssetResource.type](https://developer.apple.com/documentation/photokit/phassetresource/1623987-type)Added [PHAssetResource.uniformTypeIdentifier](https://developer.apple.com/documentation/photokit/phassetresource/1623989-uniformtypeidentifier)Added [PHAssetResourceCreationOptions](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions)Added [PHAssetResourceCreationOptions.originalFilename](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622683-originalfilename)Added [PHAssetResourceCreationOptions.shouldMoveFile](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622687-shouldmovefile)Added [PHAssetResourceCreationOptions.uniformTypeIdentifier](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions/1622686-uniformtypeidentifier)Added [PHAssetResourceManager](https://developer.apple.com/documentation/photokit/phassetresourcemanager)Added [PHAssetResourceManager.cancelDataRequest(_: PHAssetResourceDataRequestID)](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616269-canceldatarequest)Added [PHAssetResourceManager.defaultManager() -> PHAssetResourceManager [class]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616270-defaultmanager)Added [PHAssetResourceManager.requestDataForAssetResource(_: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler: (NSData) -> Void, completionHandler: (NSError?) -> Void) -> PHAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616279-requestdataforassetresource)Added [PHAssetResourceManager.writeDataForAssetResource(_: PHAssetResource, toFile: NSURL, options: PHAssetResourceRequestOptions?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616280-writedataforassetresource)Added [PHAssetResourceRequestOptions](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions)Added [PHAssetResourceRequestOptions.networkAccessAllowed](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616275-networkaccessallowed)Added [PHAssetResourceRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616272-progresshandler)Added [PHAssetResourceType [enum]](https://developer.apple.com/documentation/photokit/phassetresourcetype)Added [PHAssetResourceType.AdjustmentBasePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentbasephoto)Added [PHAssetResourceType.AdjustmentData](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentdata)Added [PHAssetResourceType.AlternatePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypealternatephoto)Added [PHAssetResourceType.Audio](https://developer.apple.com/documentation/photokit/phassetresourcetype/audio)Added [PHAssetResourceType.FullSizePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizephoto)Added [PHAssetResourceType.FullSizeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizevideo)Added [PHAssetResourceType.Photo](https://developer.apple.com/documentation/photokit/phassetresourcetype/photo)Added [PHAssetResourceType.Video](https://developer.apple.com/documentation/photokit/phassetresourcetype/video)Added [PHAssetSourceType [struct]](https://developer.apple.com/documentation/photokit/phassetsourcetype)Added PHAssetSourceType.init(rawValue: UInt)Added [PHAssetSourceType.TypeCloudShared](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypecloudshared)Added [PHAssetSourceType.TypeiTunesSynced](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeitunessynced)Added [PHAssetSourceType.TypeNone](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypenone)Added [PHAssetSourceType.TypeUserLibrary](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeuserlibrary)Added [PHContentEditingInput.audiovisualAsset](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518648-audiovisualasset)Added [PHFetchOptions.fetchLimit](https://developer.apple.com/documentation/photokit/phfetchoptions/1624761-fetchlimit)Added [PHFetchOptions.includeAssetSourceTypes](https://developer.apple.com/documentation/photokit/phfetchoptions/1624772-includeassetsourcetypes)Added [PHImageContentMode.Default](https://developer.apple.com/documentation/photokit/phimagecontentmode/1614052-default)Added [PHAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phassetresourcedatarequestid)Added [PHAssetResourceProgressHandler](https://developer.apple.com/documentation/photokit/phassetresourceprogresshandler)Added [PHInvalidAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phinvalidassetresourcedatarequestid)Added [PHInvalidImageRequestID](https://developer.apple.com/documentation/photokit/phinvalidimagerequestid)Modified [PHAdjustmentData](https://developer.apple.com/documentation/photokit/phadjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` class PHAdjustmentData : NSObject {     init!(formatIdentifier formatIdentifier: String!, formatVersion formatVersion: String!, data data: NSData!)     var formatIdentifier: String! { get }     var formatVersion: String! { get }     var data: NSData! { get } } ``` |
| To | ``` class PHAdjustmentData : NSObject {     init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: NSData)     var formatIdentifier: String { get }     var formatVersion: String { get }     var data: NSData { get } } ``` |

Modified [PHAdjustmentData.data](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518617-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData { get } ``` |

Modified [PHAdjustmentData.formatIdentifier](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518608-formatidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var formatIdentifier: String! { get } ``` |
| To | ``` var formatIdentifier: String { get } ``` |

Modified [PHAdjustmentData.formatVersion](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518633-formatversion)

|  | Declaration |
| --- | --- |
| From | ``` var formatVersion: String! { get } ``` |
| To | ``` var formatVersion: String { get } ``` |

Modified [PHAdjustmentData.init(formatIdentifier: String, formatVersion: String, data: NSData)](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518669-initwithformatidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(formatIdentifier formatIdentifier: String!, formatVersion formatVersion: String!, data data: NSData!) ``` |
| To | ``` init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: NSData) ``` |

Modified [PHAsset](https://developer.apple.com/documentation/photokit/phasset)

|  | Declaration |
| --- | --- |
| From | ``` class PHAsset : PHObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     var pixelWidth: Int { get }     var pixelHeight: Int { get }     var creationDate: NSDate! { get }     var modificationDate: NSDate! { get }     var location: CLLocation! { get }     var duration: NSTimeInterval { get }     var hidden: Bool { get }     var favorite: Bool { get }     var burstIdentifier: String! { get }     var burstSelectionTypes: PHAssetBurstSelectionType { get }     var representsBurst: Bool { get }     func canPerformEditOperation(_ editOperation: PHAssetEditOperation) -> Bool     class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetsWithALAssetURLs(_ assetURLs: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! } extension PHAsset {     func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions!, completionHandler completionHandler: ((PHContentEditingInput!, [NSObject : AnyObject]!) -> Void)!) -> PHContentEditingInputRequestID     func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID) } ``` |
| To | ``` class PHAsset : PHObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     var pixelWidth: Int { get }     var pixelHeight: Int { get }     var creationDate: NSDate? { get }     var modificationDate: NSDate? { get }     var location: CLLocation? { get }     var duration: NSTimeInterval { get }     var hidden: Bool { get }     var favorite: Bool { get }     var burstIdentifier: String? { get }     var burstSelectionTypes: PHAssetBurstSelectionType { get }     var representsBurst: Bool { get }     var sourceType: PHAssetSourceType { get }     func canPerformEditOperation(_ editOperation: PHAssetEditOperation) -> Bool     class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult?     class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithALAssetURLs(_ assetURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult } extension PHAsset {     func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: (PHContentEditingInput?, [NSObject : AnyObject]) -> Void) -> PHContentEditingInputRequestID     func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID) } ``` |

Modified [PHAsset.burstIdentifier](https://developer.apple.com/documentation/photokit/phasset/1624770-burstidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var burstIdentifier: String! { get } ``` |
| To | ``` var burstIdentifier: String? { get } ``` |

Modified [PHAsset.creationDate](https://developer.apple.com/documentation/photokit/phasset/1624776-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! { get } ``` |
| To | ``` var creationDate: NSDate? { get } ``` |

Modified [PHAsset.fetchAssetsInAssetCollection(_: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624757-fetchassetsinassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchAssetsWithALAssetURLs(_: [NSURL], options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624782-fetchassetswithalasseturls)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithALAssetURLs(_ assetURLs: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsWithALAssetURLs(_ assetURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchAssetsWithBurstIdentifier(_: String, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624723-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchAssetsWithLocalIdentifiers(_: [String], options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624732-fetchassetswithlocalidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchAssetsWithMediaType(_: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624725-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchAssetsWithOptions(_: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phasset/1624783-fetchassetswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAsset.fetchKeyAssetsInAssetCollection(_: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult? [class]](https://developer.apple.com/documentation/photokit/phasset/1624778-fetchkeyassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult? ``` |

Modified [PHAsset.location](https://developer.apple.com/documentation/photokit/phasset/1624788-location)

|  | Declaration |
| --- | --- |
| From | ``` var location: CLLocation! { get } ``` |
| To | ``` var location: CLLocation? { get } ``` |

Modified [PHAsset.modificationDate](https://developer.apple.com/documentation/photokit/phasset/1624731-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` var modificationDate: NSDate? { get } ``` |

Modified [PHAsset.requestContentEditingInputWithOptions(_: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [NSObject : AnyObject]) -> Void) -> PHContentEditingInputRequestID](https://developer.apple.com/documentation/photokit/phasset/1624061-requestcontenteditinginputwithop)

|  | Declaration |
| --- | --- |
| From | ``` func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions!, completionHandler completionHandler: ((PHContentEditingInput!, [NSObject : AnyObject]!) -> Void)!) -> PHContentEditingInputRequestID ``` |
| To | ``` func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: (PHContentEditingInput?, [NSObject : AnyObject]) -> Void) -> PHContentEditingInputRequestID ``` |

Modified [PHAssetBurstSelectionType [struct]](https://developer.apple.com/documentation/photokit/phassetburstselectiontype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHAssetBurstSelectionType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PHAssetBurstSelectionType { get }     static var AutoPick: PHAssetBurstSelectionType { get }     static var UserPick: PHAssetBurstSelectionType { get } } ``` | RawOptionSetType |
| To | ``` struct PHAssetBurstSelectionType : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetBurstSelectionType { get }     static var AutoPick: PHAssetBurstSelectionType { get }     static var UserPick: PHAssetBurstSelectionType { get } } ``` | OptionSetType |

Modified [PHAssetChangeRequest](https://developer.apple.com/documentation/photokit/phassetchangerequest)

|  | Declaration |
| --- | --- |
| From | ``` class PHAssetChangeRequest : NSObject {     class func creationRequestForAssetFromImage(_ image: UIImage!) -> Self!     class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL!) -> Self!     class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL!) -> Self!     var placeholderForCreatedAsset: PHObjectPlaceholder! { get }     class func deleteAssets(_ assets: NSFastEnumeration!)     convenience init!(forAsset asset: PHAsset!)     class func changeRequestForAsset(_ asset: PHAsset!) -> Self!     var creationDate: NSDate!     var location: CLLocation!     var favorite: Bool     var hidden: Bool     var contentEditingOutput: PHContentEditingOutput!     func revertAssetContentToOriginal() } ``` |
| To | ``` class PHAssetChangeRequest : NSObject {     class func creationRequestForAssetFromImage(_ image: UIImage) -> Self     class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL) -> Self?     class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL) -> Self?     var placeholderForCreatedAsset: PHObjectPlaceholder? { get }     class func deleteAssets(_ assets: NSFastEnumeration)     convenience init(forAsset asset: PHAsset)     class func changeRequestForAsset(_ asset: PHAsset) -> Self     var creationDate: NSDate?     var location: CLLocation?     var favorite: Bool     var hidden: Bool     var contentEditingOutput: PHContentEditingOutput?     func revertAssetContentToOriginal() } ``` |

Modified [PHAssetChangeRequest.contentEditingOutput](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624047-contenteditingoutput)

|  | Declaration |
| --- | --- |
| From | ``` var contentEditingOutput: PHContentEditingOutput! ``` |
| To | ``` var contentEditingOutput: PHContentEditingOutput? ``` |

Modified [PHAssetChangeRequest.creationDate](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624054-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! ``` |
| To | ``` var creationDate: NSDate? ``` |

Modified [PHAssetChangeRequest.creationRequestForAssetFromImage(_: UIImage) -> Self [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624060-creationrequestforassetfromimage)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromImage(_ image: UIImage!) -> Self! ``` |
| To | ``` class func creationRequestForAssetFromImage(_ image: UIImage) -> Self ``` |

Modified [PHAssetChangeRequest.creationRequestForAssetFromImageAtFileURL(_: NSURL) -> Self? [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624059-creationrequestforassetfromimage)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL!) -> Self! ``` |
| To | ``` class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL) -> Self? ``` |

Modified [PHAssetChangeRequest.creationRequestForAssetFromVideoAtFileURL(_: NSURL) -> Self? [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624057-creationrequestforassetfromvideo)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL!) -> Self! ``` |
| To | ``` class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL) -> Self? ``` |

Modified [PHAssetChangeRequest.deleteAssets(_: NSFastEnumeration) [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624062-deleteassets)

|  | Declaration |
| --- | --- |
| From | ``` class func deleteAssets(_ assets: NSFastEnumeration!) ``` |
| To | ``` class func deleteAssets(_ assets: NSFastEnumeration) ``` |

Modified [PHAssetChangeRequest.init(forAsset: PHAsset)](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624050-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(forAsset asset: PHAsset!) ``` |
| To | ``` convenience init(forAsset asset: PHAsset) ``` |

Modified [PHAssetChangeRequest.location](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624048-location)

|  | Declaration |
| --- | --- |
| From | ``` var location: CLLocation! ``` |
| To | ``` var location: CLLocation? ``` |

Modified [PHAssetChangeRequest.placeholderForCreatedAsset](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624056-placeholderforcreatedasset)

|  | Declaration |
| --- | --- |
| From | ``` var placeholderForCreatedAsset: PHObjectPlaceholder! { get } ``` |
| To | ``` var placeholderForCreatedAsset: PHObjectPlaceholder? { get } ``` |

Modified [PHAssetCollection](https://developer.apple.com/documentation/photokit/phassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class PHAssetCollection : PHCollection {     var assetCollectionType: PHAssetCollectionType { get }     var assetCollectionSubtype: PHAssetCollectionSubtype { get }     var estimatedAssetCount: Int { get }     var startDate: NSDate! { get }     var endDate: NSDate! { get }     var approximateLocation: CLLocation! { get }     var localizedLocationNames: [AnyObject]! { get }     class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset!, withType type: PHAssetCollectionType, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchMomentsInMomentList(_ momentList: PHCollectionList!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchMomentsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult!     class func transientAssetCollectionWithAssets(_ assets: [AnyObject]!, title title: String!) -> PHAssetCollection!     class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult!, title title: String!) -> PHAssetCollection! } ``` |
| To | ``` class PHAssetCollection : PHCollection {     var assetCollectionType: PHAssetCollectionType { get }     var assetCollectionSubtype: PHAssetCollectionSubtype { get }     var estimatedAssetCount: Int { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     var approximateLocation: CLLocation? { get }     var localizedLocationNames: [String] { get }     class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset, withType type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentsInMomentList(_ momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult     class func transientAssetCollectionWithAssets(_ assets: [PHAsset], title title: String?) -> PHAssetCollection     class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHAssetCollection } ``` |

Modified [PHAssetCollection.approximateLocation](https://developer.apple.com/documentation/photokit/phassetcollection/1618532-approximatelocation)

|  | Declaration |
| --- | --- |
| From | ``` var approximateLocation: CLLocation! { get } ``` |
| To | ``` var approximateLocation: CLLocation? { get } ``` |

Modified [PHAssetCollection.endDate](https://developer.apple.com/documentation/photokit/phassetcollection/1618517-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate? { get } ``` |

Modified [PHAssetCollection.fetchAssetCollectionsContainingAsset(_: PHAsset, withType: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618530-fetchassetcollectionscontaininga)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset!, withType type: PHAssetCollectionType, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset, withType type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.fetchAssetCollectionsWithALAssetGroupURLs(_: [NSURL], options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618533-fetchassetcollectionswithalasset)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.fetchAssetCollectionsWithLocalIdentifiers(_: [String], options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618510-fetchassetcollections)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.fetchAssetCollectionsWithType(_: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618544-fetchassetcollectionswithtype)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.fetchMomentsInMomentList(_: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618522-fetchmoments)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentsInMomentList(_ momentList: PHCollectionList!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchMomentsInMomentList(_ momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.fetchMomentsWithOptions(_: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618531-fetchmoments)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchMomentsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHAssetCollection.localizedLocationNames](https://developer.apple.com/documentation/photokit/phassetcollection/1618516-localizedlocationnames)

|  | Declaration |
| --- | --- |
| From | ``` var localizedLocationNames: [AnyObject]! { get } ``` |
| To | ``` var localizedLocationNames: [String] { get } ``` |

Modified [PHAssetCollection.startDate](https://developer.apple.com/documentation/photokit/phassetcollection/1618514-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate? { get } ``` |

Modified [PHAssetCollection.transientAssetCollectionWithAssetFetchResult(_: PHFetchResult, title: String?) -> PHAssetCollection [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618511-transientassetcollectionwithasse)

|  | Declaration |
| --- | --- |
| From | ``` class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult!, title title: String!) -> PHAssetCollection! ``` |
| To | ``` class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHAssetCollection ``` |

Modified [PHAssetCollection.transientAssetCollectionWithAssets(_: [PHAsset], title: String?) -> PHAssetCollection [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618529-transientassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class func transientAssetCollectionWithAssets(_ assets: [AnyObject]!, title title: String!) -> PHAssetCollection! ``` |
| To | ``` class func transientAssetCollectionWithAssets(_ assets: [PHAsset], title title: String?) -> PHAssetCollection ``` |

Modified [PHAssetCollectionChangeRequest](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest)

|  | Declaration |
| --- | --- |
| From | ``` class PHAssetCollectionChangeRequest : NSObject {     class func creationRequestForAssetCollectionWithTitle(_ title: String!) -> Self!     var placeholderForCreatedAssetCollection: PHObjectPlaceholder! { get }     class func deleteAssetCollections(_ assetCollections: NSFastEnumeration!)     convenience init!(forAssetCollection assetCollection: PHAssetCollection!)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection!) -> Self!     convenience init!(forAssetCollection assetCollection: PHAssetCollection!, assets assets: PHFetchResult!)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection!, assets assets: PHFetchResult!) -> Self!     var title: String!     func addAssets(_ assets: NSFastEnumeration!)     func insertAssets(_ assets: NSFastEnumeration!, atIndexes indexes: NSIndexSet!)     func removeAssets(_ assets: NSFastEnumeration!)     func removeAssetsAtIndexes(_ indexes: NSIndexSet!)     func replaceAssetsAtIndexes(_ indexes: NSIndexSet!, withAssets assets: NSFastEnumeration!)     func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet!, toIndex toIndex: Int) } ``` |
| To | ``` class PHAssetCollectionChangeRequest : NSObject {     class func creationRequestForAssetCollectionWithTitle(_ title: String) -> Self     var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get }     class func deleteAssetCollections(_ assetCollections: NSFastEnumeration)     convenience init?(forAssetCollection assetCollection: PHAssetCollection)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection) -> Self?     convenience init?(forAssetCollection assetCollection: PHAssetCollection, assets assets: PHFetchResult)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection, assets assets: PHFetchResult) -> Self?     var title: String     func addAssets(_ assets: NSFastEnumeration)     func insertAssets(_ assets: NSFastEnumeration, atIndexes indexes: NSIndexSet)     func removeAssets(_ assets: NSFastEnumeration)     func removeAssetsAtIndexes(_ indexes: NSIndexSet)     func replaceAssetsAtIndexes(_ indexes: NSIndexSet, withAssets assets: NSFastEnumeration)     func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet, toIndex toIndex: Int) } ``` |

Modified [PHAssetCollectionChangeRequest.addAssets(_: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619446-addassets)

|  | Declaration |
| --- | --- |
| From | ``` func addAssets(_ assets: NSFastEnumeration!) ``` |
| To | ``` func addAssets(_ assets: NSFastEnumeration) ``` |

Modified [PHAssetCollectionChangeRequest.creationRequestForAssetCollectionWithTitle(_: String) -> Self [class]](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619454-creationrequestforassetcollectio)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetCollectionWithTitle(_ title: String!) -> Self! ``` |
| To | ``` class func creationRequestForAssetCollectionWithTitle(_ title: String) -> Self ``` |

Modified [PHAssetCollectionChangeRequest.deleteAssetCollections(_: NSFastEnumeration) [class]](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619453-deleteassetcollections)

|  | Declaration |
| --- | --- |
| From | ``` class func deleteAssetCollections(_ assetCollections: NSFastEnumeration!) ``` |
| To | ``` class func deleteAssetCollections(_ assetCollections: NSFastEnumeration) ``` |

Modified [PHAssetCollectionChangeRequest.init(forAssetCollection: PHAssetCollection)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619451-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(forAssetCollection assetCollection: PHAssetCollection!) ``` |
| To | ``` convenience init?(forAssetCollection assetCollection: PHAssetCollection) ``` |

Modified [PHAssetCollectionChangeRequest.init(forAssetCollection: PHAssetCollection, assets: PHFetchResult)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619445-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(forAssetCollection assetCollection: PHAssetCollection!, assets assets: PHFetchResult!) ``` |
| To | ``` convenience init?(forAssetCollection assetCollection: PHAssetCollection, assets assets: PHFetchResult) ``` |

Modified [PHAssetCollectionChangeRequest.insertAssets(_: NSFastEnumeration, atIndexes: NSIndexSet)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619447-insertassets)

|  | Declaration |
| --- | --- |
| From | ``` func insertAssets(_ assets: NSFastEnumeration!, atIndexes indexes: NSIndexSet!) ``` |
| To | ``` func insertAssets(_ assets: NSFastEnumeration, atIndexes indexes: NSIndexSet) ``` |

Modified [PHAssetCollectionChangeRequest.moveAssetsAtIndexes(_: NSIndexSet, toIndex: Int)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619443-moveassets)

|  | Declaration |
| --- | --- |
| From | ``` func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet!, toIndex toIndex: Int) ``` |
| To | ``` func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet, toIndex toIndex: Int) ``` |

Modified [PHAssetCollectionChangeRequest.placeholderForCreatedAssetCollection](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619442-placeholderforcreatedassetcollec)

|  | Declaration |
| --- | --- |
| From | ``` var placeholderForCreatedAssetCollection: PHObjectPlaceholder! { get } ``` |
| To | ``` var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get } ``` |

Modified [PHAssetCollectionChangeRequest.removeAssets(_: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619452-removeassets)

|  | Declaration |
| --- | --- |
| From | ``` func removeAssets(_ assets: NSFastEnumeration!) ``` |
| To | ``` func removeAssets(_ assets: NSFastEnumeration) ``` |

Modified [PHAssetCollectionChangeRequest.removeAssetsAtIndexes(_: NSIndexSet)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619444-removeassets)

|  | Declaration |
| --- | --- |
| From | ``` func removeAssetsAtIndexes(_ indexes: NSIndexSet!) ``` |
| To | ``` func removeAssetsAtIndexes(_ indexes: NSIndexSet) ``` |

Modified [PHAssetCollectionChangeRequest.replaceAssetsAtIndexes(_: NSIndexSet, withAssets: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619448-replaceassets)

|  | Declaration |
| --- | --- |
| From | ``` func replaceAssetsAtIndexes(_ indexes: NSIndexSet!, withAssets assets: NSFastEnumeration!) ``` |
| To | ``` func replaceAssetsAtIndexes(_ indexes: NSIndexSet, withAssets assets: NSFastEnumeration) ``` |

Modified [PHAssetCollectionChangeRequest.title](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619450-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [PHAssetCollectionSubtype [enum]](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum PHAssetCollectionSubtype : Int {     case AlbumRegular     case AlbumSyncedEvent     case AlbumSyncedFaces     case AlbumSyncedAlbum     case AlbumImported     case AlbumMyPhotoStream     case AlbumCloudShared     case SmartAlbumGeneric     case SmartAlbumPanoramas     case SmartAlbumVideos     case SmartAlbumFavorites     case SmartAlbumTimelapses     case SmartAlbumAllHidden     case SmartAlbumRecentlyAdded     case SmartAlbumBursts     case SmartAlbumSlomoVideos     case SmartAlbumUserLibrary     case Any } ``` | -- |
| To | ``` enum PHAssetCollectionSubtype : Int {     case AlbumRegular     case AlbumSyncedEvent     case AlbumSyncedFaces     case AlbumSyncedAlbum     case AlbumImported     case AlbumMyPhotoStream     case AlbumCloudShared     case SmartAlbumGeneric     case SmartAlbumPanoramas     case SmartAlbumVideos     case SmartAlbumFavorites     case SmartAlbumTimelapses     case SmartAlbumAllHidden     case SmartAlbumRecentlyAdded     case SmartAlbumBursts     case SmartAlbumSlomoVideos     case SmartAlbumUserLibrary     case SmartAlbumSelfPortraits     case SmartAlbumScreenshots     case Any } ``` | Int |

Modified [PHAssetCollectionType [enum]](https://developer.apple.com/documentation/photokit/phassetcollectiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHAssetEditOperation [enum]](https://developer.apple.com/documentation/photokit/phasseteditoperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHAssetMediaSubtype [struct]](https://developer.apple.com/documentation/photokit/phassetmediasubtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHAssetMediaSubtype : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` | RawOptionSetType |
| To | ``` struct PHAssetMediaSubtype : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var PhotoScreenshot: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` | OptionSetType |

Modified [PHAssetMediaType [enum]](https://developer.apple.com/documentation/photokit/phassetmediatype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHAuthorizationStatus [enum]](https://developer.apple.com/documentation/photokit/phauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHCachingImageManager](https://developer.apple.com/documentation/photokit/phcachingimagemanager)

|  | Declaration |
| --- | --- |
| From | ``` class PHCachingImageManager : PHImageManager {     var allowsCachingHighQualityImages: Bool     func startCachingImagesForAssets(_ assets: [AnyObject]!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!)     func stopCachingImagesForAssets(_ assets: [AnyObject]!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!)     func stopCachingImagesForAllAssets() } ``` |
| To | ``` class PHCachingImageManager : PHImageManager {     var allowsCachingHighQualityImages: Bool     func startCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImagesForAllAssets() } ``` |

Modified [PHCachingImageManager.startCachingImagesForAssets(_: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616986-startcachingimagesforassets)

|  | Declaration |
| --- | --- |
| From | ``` func startCachingImagesForAssets(_ assets: [AnyObject]!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!) ``` |
| To | ``` func startCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |

Modified [PHCachingImageManager.stopCachingImagesForAssets(_: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616968-stopcachingimages)

|  | Declaration |
| --- | --- |
| From | ``` func stopCachingImagesForAssets(_ assets: [AnyObject]!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!) ``` |
| To | ``` func stopCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |

Modified [PHChange](https://developer.apple.com/documentation/photokit/phchange)

|  | Declaration |
| --- | --- |
| From | ``` class PHChange : NSObject {     func changeDetailsForObject(_ object: PHObject!) -> PHObjectChangeDetails!     func changeDetailsForFetchResult(_ object: PHFetchResult!) -> PHFetchResultChangeDetails! } ``` |
| To | ``` class PHChange : NSObject {     func changeDetailsForObject(_ object: PHObject) -> PHObjectChangeDetails?     func changeDetailsForFetchResult(_ object: PHFetchResult) -> PHFetchResultChangeDetails? } ``` |

Modified [PHChange.changeDetailsForFetchResult(_: PHFetchResult) -> PHFetchResultChangeDetails?](https://developer.apple.com/documentation/photokit/phchange/1613912-changedetails)

|  | Declaration |
| --- | --- |
| From | ``` func changeDetailsForFetchResult(_ object: PHFetchResult!) -> PHFetchResultChangeDetails! ``` |
| To | ``` func changeDetailsForFetchResult(_ object: PHFetchResult) -> PHFetchResultChangeDetails? ``` |

Modified [PHChange.changeDetailsForObject(_: PHObject) -> PHObjectChangeDetails?](https://developer.apple.com/documentation/photokit/phchange/1613918-changedetails)

|  | Declaration |
| --- | --- |
| From | ``` func changeDetailsForObject(_ object: PHObject!) -> PHObjectChangeDetails! ``` |
| To | ``` func changeDetailsForObject(_ object: PHObject) -> PHObjectChangeDetails? ``` |

Modified [PHCollection](https://developer.apple.com/documentation/photokit/phcollection)

|  | Declaration |
| --- | --- |
| From | ``` class PHCollection : PHObject {     var canContainAssets: Bool { get }     var canContainCollections: Bool { get }     var localizedTitle: String! { get }     func canPerformEditOperation(_ anOperation: PHCollectionEditOperation) -> Bool     class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult! } ``` |
| To | ``` class PHCollection : PHObject {     var canContainAssets: Bool { get }     var canContainCollections: Bool { get }     var localizedTitle: String? { get }     func canPerformEditOperation(_ anOperation: PHCollectionEditOperation) -> Bool     class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult     class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult } ``` |

Modified [PHCollection.fetchCollectionsInCollectionList(_: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollection/1618515-fetchcollectionsincollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollection.fetchTopLevelUserCollectionsWithOptions(_: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollection/1618513-fetchtoplevelusercollections)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollection.localizedTitle](https://developer.apple.com/documentation/photokit/phcollection/1618541-localizedtitle)

|  | Declaration |
| --- | --- |
| From | ``` var localizedTitle: String! { get } ``` |
| To | ``` var localizedTitle: String? { get } ``` |

Modified [PHCollectionEditOperation [enum]](https://developer.apple.com/documentation/photokit/phcollectioneditoperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHCollectionList](https://developer.apple.com/documentation/photokit/phcollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class PHCollectionList : PHCollection {     var collectionListType: PHCollectionListType { get }     var collectionListSubtype: PHCollectionListSubtype { get }     var startDate: NSDate! { get }     var endDate: NSDate! { get }     var localizedLocationNames: [AnyObject]! { get }     class func fetchCollectionListsContainingCollection(_ collection: PHCollection!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult!     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions!) -> PHFetchResult!     class func transientCollectionListWithCollections(_ collections: [AnyObject]!, title title: String!) -> PHCollectionList!     class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult!, title title: String!) -> PHCollectionList! } ``` |
| To | ``` class PHCollectionList : PHCollection {     var collectionListType: PHCollectionListType { get }     var collectionListSubtype: PHCollectionListSubtype { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     var localizedLocationNames: [String] { get }     class func fetchCollectionListsContainingCollection(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func transientCollectionListWithCollections(_ collections: [PHCollection], title title: String?) -> PHCollectionList     class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHCollectionList } ``` |

Modified [PHCollectionList.endDate](https://developer.apple.com/documentation/photokit/phcollectionlist/1618509-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate? { get } ``` |

Modified [PHCollectionList.fetchCollectionListsContainingCollection(_: PHCollection, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618523-fetchcollectionlistscontainingco)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsContainingCollection(_ collection: PHCollection!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchCollectionListsContainingCollection(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollectionList.fetchCollectionListsWithLocalIdentifiers(_: [String], options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618525-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [AnyObject]!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollectionList.fetchCollectionListsWithType(_: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618520-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollectionList.fetchMomentListsWithSubtype(_: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618536-fetchmomentlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection!, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollectionList.fetchMomentListsWithSubtype(_: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618540-fetchmomentlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions!) -> PHFetchResult! ``` |
| To | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |

Modified [PHCollectionList.localizedLocationNames](https://developer.apple.com/documentation/photokit/phcollectionlist/1618524-localizedlocationnames)

|  | Declaration |
| --- | --- |
| From | ``` var localizedLocationNames: [AnyObject]! { get } ``` |
| To | ``` var localizedLocationNames: [String] { get } ``` |

Modified [PHCollectionList.startDate](https://developer.apple.com/documentation/photokit/phcollectionlist/1618521-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate? { get } ``` |

Modified [PHCollectionList.transientCollectionListWithCollections(_: [PHCollection], title: String?) -> PHCollectionList [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618537-transientcollectionlistwithcolle)

|  | Declaration |
| --- | --- |
| From | ``` class func transientCollectionListWithCollections(_ collections: [AnyObject]!, title title: String!) -> PHCollectionList! ``` |
| To | ``` class func transientCollectionListWithCollections(_ collections: [PHCollection], title title: String?) -> PHCollectionList ``` |

Modified [PHCollectionList.transientCollectionListWithCollectionsFetchResult(_: PHFetchResult, title: String?) -> PHCollectionList [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618526-transientcollectionlistwithcolle)

|  | Declaration |
| --- | --- |
| From | ``` class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult!, title title: String!) -> PHCollectionList! ``` |
| To | ``` class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHCollectionList ``` |

Modified [PHCollectionListChangeRequest](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest)

|  | Declaration |
| --- | --- |
| From | ``` class PHCollectionListChangeRequest : NSObject {     class func creationRequestForCollectionListWithTitle(_ title: String!) -> Self!     var placeholderForCreatedCollectionList: PHObjectPlaceholder! { get }     class func deleteCollectionLists(_ collectionLists: NSFastEnumeration!)     convenience init!(forCollectionList collectionList: PHCollectionList!)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList!) -> Self!     convenience init!(forCollectionList collectionList: PHCollectionList!, childCollections childCollections: PHFetchResult!)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList!, childCollections childCollections: PHFetchResult!) -> Self!     var title: String!     func addChildCollections(_ collections: NSFastEnumeration!)     func insertChildCollections(_ collections: NSFastEnumeration!, atIndexes indexes: NSIndexSet!)     func removeChildCollections(_ collections: NSFastEnumeration!)     func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet!)     func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet!, withChildCollections collections: NSFastEnumeration!)     func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet!, toIndex toIndex: Int) } ``` |
| To | ``` class PHCollectionListChangeRequest : NSObject {     class func creationRequestForCollectionListWithTitle(_ title: String) -> Self     var placeholderForCreatedCollectionList: PHObjectPlaceholder { get }     class func deleteCollectionLists(_ collectionLists: NSFastEnumeration)     convenience init?(forCollectionList collectionList: PHCollectionList)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList) -> Self?     convenience init?(forCollectionList collectionList: PHCollectionList, childCollections childCollections: PHFetchResult)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList, childCollections childCollections: PHFetchResult) -> Self?     var title: String     func addChildCollections(_ collections: NSFastEnumeration)     func insertChildCollections(_ collections: NSFastEnumeration, atIndexes indexes: NSIndexSet)     func removeChildCollections(_ collections: NSFastEnumeration)     func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet)     func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet, withChildCollections collections: NSFastEnumeration)     func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet, toIndex toIndex: Int) } ``` |

Modified [PHCollectionListChangeRequest.addChildCollections(_: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622851-addchildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func addChildCollections(_ collections: NSFastEnumeration!) ``` |
| To | ``` func addChildCollections(_ collections: NSFastEnumeration) ``` |

Modified [PHCollectionListChangeRequest.creationRequestForCollectionListWithTitle(_: String) -> Self [class]](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622858-creationrequestforcollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForCollectionListWithTitle(_ title: String!) -> Self! ``` |
| To | ``` class func creationRequestForCollectionListWithTitle(_ title: String) -> Self ``` |

Modified [PHCollectionListChangeRequest.deleteCollectionLists(_: NSFastEnumeration) [class]](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622861-deletecollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` class func deleteCollectionLists(_ collectionLists: NSFastEnumeration!) ``` |
| To | ``` class func deleteCollectionLists(_ collectionLists: NSFastEnumeration) ``` |

Modified [PHCollectionListChangeRequest.init(forCollectionList: PHCollectionList)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622855-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(forCollectionList collectionList: PHCollectionList!) ``` |
| To | ``` convenience init?(forCollectionList collectionList: PHCollectionList) ``` |

Modified [PHCollectionListChangeRequest.init(forCollectionList: PHCollectionList, childCollections: PHFetchResult)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622850-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(forCollectionList collectionList: PHCollectionList!, childCollections childCollections: PHFetchResult!) ``` |
| To | ``` convenience init?(forCollectionList collectionList: PHCollectionList, childCollections childCollections: PHFetchResult) ``` |

Modified [PHCollectionListChangeRequest.insertChildCollections(_: NSFastEnumeration, atIndexes: NSIndexSet)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622862-insertchildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildCollections(_ collections: NSFastEnumeration!, atIndexes indexes: NSIndexSet!) ``` |
| To | ``` func insertChildCollections(_ collections: NSFastEnumeration, atIndexes indexes: NSIndexSet) ``` |

Modified [PHCollectionListChangeRequest.moveChildCollectionsAtIndexes(_: NSIndexSet, toIndex: Int)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622859-movechildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet!, toIndex toIndex: Int) ``` |
| To | ``` func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet, toIndex toIndex: Int) ``` |

Modified [PHCollectionListChangeRequest.placeholderForCreatedCollectionList](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622860-placeholderforcreatedcollectionl)

|  | Declaration |
| --- | --- |
| From | ``` var placeholderForCreatedCollectionList: PHObjectPlaceholder! { get } ``` |
| To | ``` var placeholderForCreatedCollectionList: PHObjectPlaceholder { get } ``` |

Modified [PHCollectionListChangeRequest.removeChildCollections(_: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622854-removechildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func removeChildCollections(_ collections: NSFastEnumeration!) ``` |
| To | ``` func removeChildCollections(_ collections: NSFastEnumeration) ``` |

Modified [PHCollectionListChangeRequest.removeChildCollectionsAtIndexes(_: NSIndexSet)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622857-removechildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet!) ``` |
| To | ``` func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet) ``` |

Modified [PHCollectionListChangeRequest.replaceChildCollectionsAtIndexes(_: NSIndexSet, withChildCollections: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622856-replacechildcollectionsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet!, withChildCollections collections: NSFastEnumeration!) ``` |
| To | ``` func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet, withChildCollections collections: NSFastEnumeration) ``` |

Modified [PHCollectionListChangeRequest.title](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622853-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [PHCollectionListSubtype [enum]](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHCollectionListType [enum]](https://developer.apple.com/documentation/photokit/phcollectionlisttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHContentEditingInput](https://developer.apple.com/documentation/photokit/phcontenteditinginput)

|  | Declaration |
| --- | --- |
| From | ``` class PHContentEditingInput : NSObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     @NSCopying var creationDate: NSDate! { get }     @NSCopying var location: CLLocation! { get }     var uniformTypeIdentifier: String! { get }     var adjustmentData: PHAdjustmentData! { get }     var displaySizeImage: UIImage! { get }     @NSCopying var fullSizeImageURL: NSURL! { get }     var fullSizeImageOrientation: Int32 { get }     var avAsset: AVAsset! { get } } ``` |
| To | ``` class PHContentEditingInput : NSObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var location: CLLocation? { get }     var uniformTypeIdentifier: String? { get }     var adjustmentData: PHAdjustmentData { get }     var displaySizeImage: UIImage? { get }     @NSCopying var fullSizeImageURL: NSURL? { get }     var fullSizeImageOrientation: Int32 { get }     var avAsset: AVAsset? { get }     var audiovisualAsset: AVAsset? { get } } ``` |

Modified [PHContentEditingInput.adjustmentData](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518657-adjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` var adjustmentData: PHAdjustmentData! { get } ``` |
| To | ``` var adjustmentData: PHAdjustmentData { get } ``` |

Modified [PHContentEditingInput.avAsset](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1618636-avasset)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var avAsset: AVAsset! { get } ``` | -- |
| To | ``` var avAsset: AVAsset? { get } ``` | iOS 9.0 |

Modified [PHContentEditingInput.creationDate](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518619-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var creationDate: NSDate? { get } ``` |

Modified [PHContentEditingInput.displaySizeImage](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518635-displaysizeimage)

|  | Declaration |
| --- | --- |
| From | ``` var displaySizeImage: UIImage! { get } ``` |
| To | ``` var displaySizeImage: UIImage? { get } ``` |

Modified [PHContentEditingInput.fullSizeImageURL](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518671-fullsizeimageurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fullSizeImageURL: NSURL! { get } ``` |
| To | ``` @NSCopying var fullSizeImageURL: NSURL? { get } ``` |

Modified [PHContentEditingInput.location](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518621-location)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var location: CLLocation! { get } ``` |
| To | ``` @NSCopying var location: CLLocation? { get } ``` |

Modified [PHContentEditingInput.uniformTypeIdentifier](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518675-uniformtypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var uniformTypeIdentifier: String! { get } ``` |
| To | ``` var uniformTypeIdentifier: String? { get } ``` |

Modified [PHContentEditingInputRequestOptions](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions)

|  | Declaration |
| --- | --- |
| From | ``` class PHContentEditingInputRequestOptions : NSObject {     var canHandleAdjustmentData: ((PHAdjustmentData!) -> Bool)!     var networkAccessAllowed: Bool     var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)! } ``` |
| To | ``` class PHContentEditingInputRequestOptions : NSObject {     var canHandleAdjustmentData: (PHAdjustmentData) -> Bool     var networkAccessAllowed: Bool     var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? } ``` |

Modified [PHContentEditingInputRequestOptions.canHandleAdjustmentData](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions/1624055-canhandleadjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` var canHandleAdjustmentData: ((PHAdjustmentData!) -> Bool)! ``` |
| To | ``` var canHandleAdjustmentData: (PHAdjustmentData) -> Bool ``` |

Modified [PHContentEditingInputRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions/1624053-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)! ``` |
| To | ``` var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? ``` |

Modified [PHContentEditingOutput](https://developer.apple.com/documentation/photokit/phcontenteditingoutput)

|  | Declaration |
| --- | --- |
| From | ``` class PHContentEditingOutput : NSObject {     init!(contentEditingInput contentEditingInput: PHContentEditingInput!)     var adjustmentData: PHAdjustmentData!     @NSCopying var renderedContentURL: NSURL! { get } } extension PHContentEditingOutput {     init!(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder!) } ``` |
| To | ``` class PHContentEditingOutput : NSObject {     init(contentEditingInput contentEditingInput: PHContentEditingInput)     var adjustmentData: PHAdjustmentData?     @NSCopying var renderedContentURL: NSURL { get } } extension PHContentEditingOutput {     init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder) } ``` |

Modified [PHContentEditingOutput.adjustmentData](https://developer.apple.com/documentation/photokit/phcontenteditingoutput/1518684-adjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` var adjustmentData: PHAdjustmentData! ``` |
| To | ``` var adjustmentData: PHAdjustmentData? ``` |

Modified [PHContentEditingOutput.init(contentEditingInput: PHContentEditingInput)](https://developer.apple.com/documentation/photokit/phcontenteditingoutput/1518650-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentEditingInput contentEditingInput: PHContentEditingInput!) ``` |
| To | ``` init(contentEditingInput contentEditingInput: PHContentEditingInput) ``` |

Modified [PHContentEditingOutput.init(placeholderForCreatedAsset: PHObjectPlaceholder)](https://developer.apple.com/documentation/photokit/phcontenteditingoutput/1624046-initwithplaceholderforcreatedass)

|  | Declaration |
| --- | --- |
| From | ``` init!(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder!) ``` |
| To | ``` init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder) ``` |

Modified [PHContentEditingOutput.renderedContentURL](https://developer.apple.com/documentation/photokit/phcontenteditingoutput/1518655-renderedcontenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var renderedContentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var renderedContentURL: NSURL { get } ``` |

Modified [PHFetchOptions](https://developer.apple.com/documentation/photokit/phfetchoptions)

|  | Declaration |
| --- | --- |
| From | ``` class PHFetchOptions : NSObject, NSCopying {     var predicate: NSPredicate!     var sortDescriptors: [AnyObject]!     var includeHiddenAssets: Bool     var includeAllBurstAssets: Bool     var wantsIncrementalChangeDetails: Bool } ``` |
| To | ``` class PHFetchOptions : NSObject, NSCopying {     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var includeHiddenAssets: Bool     var includeAllBurstAssets: Bool     var includeAssetSourceTypes: PHAssetSourceType     var fetchLimit: Int     var wantsIncrementalChangeDetails: Bool } ``` |

Modified [PHFetchOptions.predicate](https://developer.apple.com/documentation/photokit/phfetchoptions/1624709-predicate)

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! ``` |
| To | ``` var predicate: NSPredicate? ``` |

Modified [PHFetchOptions.sortDescriptors](https://developer.apple.com/documentation/photokit/phfetchoptions/1624771-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! ``` |
| To | ``` var sortDescriptors: [NSSortDescriptor]? ``` |

Modified [PHFetchResult](https://developer.apple.com/documentation/photokit/phfetchresult)

|  | Declaration |
| --- | --- |
| From | ``` class PHFetchResult : NSObject, NSCopying, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject!     subscript (idx: Int) -> AnyObject! { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject!     func containsObject(_ anObject: AnyObject!) -> Bool     func indexOfObject(_ anObject: AnyObject!) -> Int     func indexOfObject(_ anObject: AnyObject!, inRange range: NSRange) -> Int     var firstObject: AnyObject! { get }     var lastObject: AnyObject! { get }     func objectsAtIndexes(_ indexes: NSIndexSet!) -> [AnyObject]!     func enumerateObjectsUsingBlock(_ block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func enumerateObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func countOfAssetsWithMediaType(_ mediaType: PHAssetMediaType) -> Int } ``` |
| To | ``` class PHFetchResult : NSObject, NSCopying, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func containsObject(_ anObject: AnyObject) -> Bool     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func countOfAssetsWithMediaType(_ mediaType: PHAssetMediaType) -> Int } ``` |

Modified [PHFetchResult.containsObject(_: AnyObject) -> Bool](https://developer.apple.com/documentation/photokit/phfetchresult/1621005-contains)

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject!) -> Bool ``` |
| To | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |

Modified [PHFetchResult.enumerateObjectsAtIndexes(_: NSIndexSet, options: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1620998-enumerateobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet!, options opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [PHFetchResult.enumerateObjectsUsingBlock(_: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1620999-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [PHFetchResult.enumerateObjectsWithOptions(_: NSEnumerationOptions, usingBlock: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1621006-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: ((AnyObject!, Int, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [PHFetchResult.firstObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621003-firstobject)

|  | Declaration |
| --- | --- |
| From | ``` var firstObject: AnyObject! { get } ``` |
| To | ``` var firstObject: AnyObject? { get } ``` |

Modified [PHFetchResult.indexOfObject(_: AnyObject) -> Int](https://developer.apple.com/documentation/photokit/phfetchresult/1621007-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject!) -> Int ``` |
| To | ``` func indexOfObject(_ anObject: AnyObject) -> Int ``` |

Modified [PHFetchResult.indexOfObject(_: AnyObject, inRange: NSRange) -> Int](https://developer.apple.com/documentation/photokit/phfetchresult/1621009-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject!, inRange range: NSRange) -> Int ``` |
| To | ``` func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int ``` |

Modified [PHFetchResult.lastObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621001-lastobject)

|  | Declaration |
| --- | --- |
| From | ``` var lastObject: AnyObject! { get } ``` |
| To | ``` var lastObject: AnyObject? { get } ``` |

Modified [PHFetchResult.objectAtIndex(_: Int) -> AnyObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621002-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndex(_ index: Int) -> AnyObject! ``` |
| To | ``` func objectAtIndex(_ index: Int) -> AnyObject ``` |

Modified [PHFetchResult.objectsAtIndexes(_: NSIndexSet) -> [AnyObject]](https://developer.apple.com/documentation/photokit/phfetchresult/1621008-objectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func objectsAtIndexes(_ indexes: NSIndexSet!) -> [AnyObject]! ``` |
| To | ``` func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject] ``` |

Modified [PHFetchResult.subscript(_: Int) -> AnyObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621000-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (idx: Int) -> AnyObject! { get } ``` |
| To | ``` subscript (_ idx: Int) -> AnyObject { get } ``` |

Modified [PHFetchResultChangeDetails](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails)

|  | Declaration |
| --- | --- |
| From | ``` class PHFetchResultChangeDetails : NSObject {     var fetchResultBeforeChanges: PHFetchResult! { get }     var fetchResultAfterChanges: PHFetchResult! { get }     var hasIncrementalChanges: Bool { get }     var removedIndexes: NSIndexSet! { get }     var removedObjects: [AnyObject]! { get }     var insertedIndexes: NSIndexSet! { get }     var insertedObjects: [AnyObject]! { get }     var changedIndexes: NSIndexSet! { get }     var changedObjects: [AnyObject]! { get }     func enumerateMovesWithBlock(_ handler: ((Int, Int) -> Void)!)     var hasMoves: Bool { get }     convenience init!(fromFetchResult fromResult: PHFetchResult!, toFetchResult toResult: PHFetchResult!, changedObjects changedObjects: [AnyObject]!)     class func changeDetailsFromFetchResult(_ fromResult: PHFetchResult!, toFetchResult toResult: PHFetchResult!, changedObjects changedObjects: [AnyObject]!) -> Self! } ``` |
| To | ``` class PHFetchResultChangeDetails : NSObject {     var fetchResultBeforeChanges: PHFetchResult { get }     var fetchResultAfterChanges: PHFetchResult { get }     var hasIncrementalChanges: Bool { get }     var removedIndexes: NSIndexSet? { get }     var removedObjects: [PHObject] { get }     var insertedIndexes: NSIndexSet? { get }     var insertedObjects: [PHObject] { get }     var changedIndexes: NSIndexSet? { get }     var changedObjects: [PHObject] { get }     func enumerateMovesWithBlock(_ handler: (Int, Int) -> Void)     var hasMoves: Bool { get }     convenience init(fromFetchResult fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject])     class func changeDetailsFromFetchResult(_ fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject]) -> Self } ``` |

Modified [PHFetchResultChangeDetails.changedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613922-changedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var changedIndexes: NSIndexSet! { get } ``` |
| To | ``` var changedIndexes: NSIndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.changedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613910-changedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var changedObjects: [AnyObject]! { get } ``` |
| To | ``` var changedObjects: [PHObject] { get } ``` |

Modified [PHFetchResultChangeDetails.enumerateMovesWithBlock(_: (Int, Int) -> Void)](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613898-enumeratemoves)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateMovesWithBlock(_ handler: ((Int, Int) -> Void)!) ``` |
| To | ``` func enumerateMovesWithBlock(_ handler: (Int, Int) -> Void) ``` |

Modified [PHFetchResultChangeDetails.fetchResultAfterChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613894-fetchresultafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` var fetchResultAfterChanges: PHFetchResult! { get } ``` |
| To | ``` var fetchResultAfterChanges: PHFetchResult { get } ``` |

Modified [PHFetchResultChangeDetails.fetchResultBeforeChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613892-fetchresultbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` var fetchResultBeforeChanges: PHFetchResult! { get } ``` |
| To | ``` var fetchResultBeforeChanges: PHFetchResult { get } ``` |

Modified [PHFetchResultChangeDetails.init(fromFetchResult: PHFetchResult, toFetchResult: PHFetchResult, changedObjects: [PHObject])](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613921-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromFetchResult fromResult: PHFetchResult!, toFetchResult toResult: PHFetchResult!, changedObjects changedObjects: [AnyObject]!) ``` |
| To | ``` convenience init(fromFetchResult fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject]) ``` |

Modified [PHFetchResultChangeDetails.insertedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613919-insertedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var insertedIndexes: NSIndexSet! { get } ``` |
| To | ``` var insertedIndexes: NSIndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.insertedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613908-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: [AnyObject]! { get } ``` |
| To | ``` var insertedObjects: [PHObject] { get } ``` |

Modified [PHFetchResultChangeDetails.removedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613920-removedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var removedIndexes: NSIndexSet! { get } ``` |
| To | ``` var removedIndexes: NSIndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.removedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613902-removedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var removedObjects: [AnyObject]! { get } ``` |
| To | ``` var removedObjects: [PHObject] { get } ``` |

Modified [PHImageContentMode [enum]](https://developer.apple.com/documentation/photokit/phimagecontentmode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum PHImageContentMode : Int {     case AspectFit     case AspectFill } ``` | -- |
| To | ``` enum PHImageContentMode : Int {     case AspectFit     case AspectFill     static var Default: PHImageContentMode { get } } ``` | Int |

Modified [PHImageManager](https://developer.apple.com/documentation/photokit/phimagemanager)

|  | Declaration |
| --- | --- |
| From | ``` class PHImageManager : NSObject {     class func defaultManager() -> PHImageManager!     func requestImageForAsset(_ asset: PHAsset!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!, resultHandler resultHandler: ((UIImage!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID     func requestImageDataForAsset(_ asset: PHAsset!, options options: PHImageRequestOptions!, resultHandler resultHandler: ((NSData!, String!, UIImageOrientation, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestPlayerItemForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, resultHandler resultHandler: ((AVPlayerItem!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID     func requestExportSessionForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, exportPreset exportPreset: String!, resultHandler resultHandler: ((AVAssetExportSession!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID     func requestAVAssetForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, resultHandler resultHandler: ((AVAsset!, AVAudioMix!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID } ``` |
| To | ``` class PHImageManager : NSObject {     class func defaultManager() -> PHImageManager     func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID } ``` |

Modified [PHImageManager.defaultManager() -> PHImageManager [class]](https://developer.apple.com/documentation/photokit/phimagemanager/1616933-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultManager() -> PHImageManager! ``` |
| To | ``` class func defaultManager() -> PHImageManager ``` |

Modified [PHImageManager.requestAVAssetForVideo(_: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616935-requestavassetforvideo)

|  | Declaration |
| --- | --- |
| From | ``` func requestAVAssetForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, resultHandler resultHandler: ((AVAsset!, AVAudioMix!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID ``` |
| To | ``` func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestExportSessionForVideo(_: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616981-requestexportsessionforvideo)

|  | Declaration |
| --- | --- |
| From | ``` func requestExportSessionForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, exportPreset exportPreset: String!, resultHandler resultHandler: ((AVAssetExportSession!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID ``` |
| To | ``` func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestImageDataForAsset(_: PHAsset, options: PHImageRequestOptions?, resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616957-requestimagedataforasset)

|  | Declaration |
| --- | --- |
| From | ``` func requestImageDataForAsset(_ asset: PHAsset!, options options: PHImageRequestOptions!, resultHandler resultHandler: ((NSData!, String!, UIImageOrientation, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID ``` |
| To | ``` func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestImageForAsset(_: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616964-requestimageforasset)

|  | Declaration |
| --- | --- |
| From | ``` func requestImageForAsset(_ asset: PHAsset!, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions!, resultHandler resultHandler: ((UIImage!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID ``` |
| To | ``` func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestPlayerItemForVideo(_: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616958-requestplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` func requestPlayerItemForVideo(_ asset: PHAsset!, options options: PHVideoRequestOptions!, resultHandler resultHandler: ((AVPlayerItem!, [NSObject : AnyObject]!) -> Void)!) -> PHImageRequestID ``` |
| To | ``` func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |

Modified [PHImageRequestOptions](https://developer.apple.com/documentation/photokit/phimagerequestoptions)

|  | Declaration |
| --- | --- |
| From | ``` class PHImageRequestOptions : NSObject, NSCopying {     var version: PHImageRequestOptionsVersion     var deliveryMode: PHImageRequestOptionsDeliveryMode     var resizeMode: PHImageRequestOptionsResizeMode     var normalizedCropRect: CGRect     var networkAccessAllowed: Bool     var synchronous: Bool     var progressHandler: PHAssetImageProgressHandler! } ``` |
| To | ``` class PHImageRequestOptions : NSObject, NSCopying {     var version: PHImageRequestOptionsVersion     var deliveryMode: PHImageRequestOptionsDeliveryMode     var resizeMode: PHImageRequestOptionsResizeMode     var normalizedCropRect: CGRect     var networkAccessAllowed: Bool     var synchronous: Bool     var progressHandler: PHAssetImageProgressHandler? } ``` |

Modified [PHImageRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phimagerequestoptions/1616939-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetImageProgressHandler! ``` |
| To | ``` var progressHandler: PHAssetImageProgressHandler? ``` |

Modified [PHImageRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHImageRequestOptionsResizeMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHImageRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHObject](https://developer.apple.com/documentation/photokit/phobject)

|  | Declaration |
| --- | --- |
| From | ``` class PHObject : NSObject, NSCopying {     var localIdentifier: String! { get } } ``` |
| To | ``` class PHObject : NSObject, NSCopying {     var localIdentifier: String { get } } ``` |

Modified [PHObject.localIdentifier](https://developer.apple.com/documentation/photokit/phobject/1622400-localidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var localIdentifier: String! { get } ``` |
| To | ``` var localIdentifier: String { get } ``` |

Modified [PHObjectChangeDetails](https://developer.apple.com/documentation/photokit/phobjectchangedetails)

|  | Declaration |
| --- | --- |
| From | ``` class PHObjectChangeDetails : NSObject {     var objectBeforeChanges: AnyObject! { get }     var objectAfterChanges: AnyObject! { get }     var assetContentChanged: Bool { get }     var objectWasDeleted: Bool { get } } ``` |
| To | ``` class PHObjectChangeDetails : NSObject {     var objectBeforeChanges: PHObject { get }     var objectAfterChanges: PHObject? { get }     var assetContentChanged: Bool { get }     var objectWasDeleted: Bool { get } } ``` |

Modified [PHObjectChangeDetails.objectAfterChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613888-objectafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` var objectAfterChanges: AnyObject! { get } ``` |
| To | ``` var objectAfterChanges: PHObject? { get } ``` |

Modified [PHObjectChangeDetails.objectBeforeChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613890-objectbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` var objectBeforeChanges: AnyObject! { get } ``` |
| To | ``` var objectBeforeChanges: PHObject { get } ``` |

Modified [PHPhotoLibrary](https://developer.apple.com/documentation/photokit/phphotolibrary)

|  | Declaration |
| --- | --- |
| From | ``` class PHPhotoLibrary : NSObject {     class func sharedPhotoLibrary() -> PHPhotoLibrary!     class func authorizationStatus() -> PHAuthorizationStatus     class func requestAuthorization(_ handler: ((PHAuthorizationStatus) -> Void)!)     func performChanges(_ changeBlock: dispatch_block_t!, completionHandler completionHandler: ((Bool, NSError!) -> Void)!)     func performChangesAndWait(_ changeBlock: dispatch_block_t!, error error: NSErrorPointer) -> Bool     func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver!)     func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver!) } ``` |
| To | ``` class PHPhotoLibrary : NSObject {     class func sharedPhotoLibrary() -> PHPhotoLibrary     class func authorizationStatus() -> PHAuthorizationStatus     class func requestAuthorization(_ handler: (PHAuthorizationStatus) -> Void)     func performChanges(_ changeBlock: dispatch_block_t, completionHandler completionHandler: ((Bool, NSError?) -> Void)?)     func performChangesAndWait(_ changeBlock: dispatch_block_t) throws     func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver)     func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver) } ``` |

Modified [PHPhotoLibrary.performChanges(_: dispatch_block_t, completionHandler: ((Bool, NSError?) -> Void)?)](https://developer.apple.com/documentation/photokit/phphotolibrary/1620743-performchanges)

|  | Declaration |
| --- | --- |
| From | ``` func performChanges(_ changeBlock: dispatch_block_t!, completionHandler completionHandler: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func performChanges(_ changeBlock: dispatch_block_t, completionHandler completionHandler: ((Bool, NSError?) -> Void)?) ``` |

Modified [PHPhotoLibrary.performChangesAndWait(_: dispatch_block_t) throws](https://developer.apple.com/documentation/photokit/phphotolibrary/1620747-performchangesandwait)

|  | Declaration |
| --- | --- |
| From | ``` func performChangesAndWait(_ changeBlock: dispatch_block_t!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func performChangesAndWait(_ changeBlock: dispatch_block_t) throws ``` |

Modified [PHPhotoLibrary.registerChangeObserver(_: PHPhotoLibraryChangeObserver)](https://developer.apple.com/documentation/photokit/phphotolibrary/1620741-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver!) ``` |
| To | ``` func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver) ``` |

Modified [PHPhotoLibrary.requestAuthorization(_: (PHAuthorizationStatus) -> Void) [class]](https://developer.apple.com/documentation/photokit/phphotolibrary/1620736-requestauthorization)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAuthorization(_ handler: ((PHAuthorizationStatus) -> Void)!) ``` |
| To | ``` class func requestAuthorization(_ handler: (PHAuthorizationStatus) -> Void) ``` |

Modified [PHPhotoLibrary.sharedPhotoLibrary() -> PHPhotoLibrary [class]](https://developer.apple.com/documentation/photokit/phphotolibrary/1620737-sharedphotolibrary)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedPhotoLibrary() -> PHPhotoLibrary! ``` |
| To | ``` class func sharedPhotoLibrary() -> PHPhotoLibrary ``` |

Modified [PHPhotoLibrary.unregisterChangeObserver(_: PHPhotoLibraryChangeObserver)](https://developer.apple.com/documentation/photokit/phphotolibrary/1620748-unregisterchangeobserver)

|  | Declaration |
| --- | --- |
| From | ``` func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver!) ``` |
| To | ``` func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver) ``` |

Modified [PHPhotoLibraryChangeObserver](https://developer.apple.com/documentation/photokit/phphotolibrarychangeobserver)

|  | Declaration |
| --- | --- |
| From | ``` protocol PHPhotoLibraryChangeObserver : NSObjectProtocol {     func photoLibraryDidChange(_ changeInstance: PHChange!) } ``` |
| To | ``` protocol PHPhotoLibraryChangeObserver : NSObjectProtocol {     func photoLibraryDidChange(_ changeInstance: PHChange) } ``` |

Modified [PHPhotoLibraryChangeObserver.photoLibraryDidChange(_: PHChange)](https://developer.apple.com/documentation/photokit/phphotolibrarychangeobserver/1620746-photolibrarydidchange)

|  | Declaration |
| --- | --- |
| From | ``` func photoLibraryDidChange(_ changeInstance: PHChange!) ``` |
| To | ``` func photoLibraryDidChange(_ changeInstance: PHChange) ``` |

Modified [PHVideoRequestOptions](https://developer.apple.com/documentation/photokit/phvideorequestoptions)

|  | Declaration |
| --- | --- |
| From | ``` class PHVideoRequestOptions : NSObject {     var networkAccessAllowed: Bool     var version: PHVideoRequestOptionsVersion     var deliveryMode: PHVideoRequestOptionsDeliveryMode     var progressHandler: PHAssetVideoProgressHandler! } ``` |
| To | ``` class PHVideoRequestOptions : NSObject {     var networkAccessAllowed: Bool     var version: PHVideoRequestOptionsVersion     var deliveryMode: PHVideoRequestOptionsDeliveryMode     var progressHandler: PHAssetVideoProgressHandler? } ``` |

Modified [PHVideoRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phvideorequestoptions/1616930-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetVideoProgressHandler! ``` |
| To | ``` var progressHandler: PHAssetVideoProgressHandler? ``` |

Modified [PHVideoRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHVideoRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsversion)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PHAssetImageProgressHandler](https://developer.apple.com/documentation/photokit/phassetimageprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias PHAssetImageProgressHandler = (Double, NSError!, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]!) -> Void ``` |
| To | ``` typealias PHAssetImageProgressHandler = (Double, NSError?, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]?) -> Void ``` |

Modified [PHAssetVideoProgressHandler](https://developer.apple.com/documentation/photokit/phassetvideoprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias PHAssetVideoProgressHandler = (Double, NSError!, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]!) -> Void ``` |
| To | ``` typealias PHAssetVideoProgressHandler = (Double, NSError?, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]?) -> Void ``` |

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
