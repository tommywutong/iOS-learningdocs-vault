---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Photos.html
archived_at: '2026-07-18T02:57:10.210209Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Photos Changes for Swift

### Photos

Added [PHAssetMediaSubtype.PhotoLive](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1614007-photolive)Added [PHAssetResource.assetResourcesForLivePhoto(_: PHLivePhoto) -> [PHAssetResource] [class]](https://developer.apple.com/documentation/photokit/phassetresource/1623984-assetresourcesforlivephoto)Added [PHAssetResourceType.PairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypepairedvideo)Added [PHImageManager.requestLivePhotoForAsset(_: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: (PHLivePhoto?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616984-requestlivephotoforasset)Added [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto)Added [PHLivePhoto.cancelLivePhotoRequestWithRequestID(_: PHLivePhotoRequestID) [class]](https://developer.apple.com/documentation/photokit/phlivephoto/1616436-cancellivephotorequestwithreques)Added [PHLivePhoto.requestLivePhotoWithResourceFileURLs(_: [NSURL], placeholderImage: UIImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: (PHLivePhoto?, [NSObject : AnyObject]) -> Void) -> PHLivePhotoRequestID [class]](https://developer.apple.com/documentation/photokit/phlivephoto/1616434-requestlivephotowithresourcefile)Added [PHLivePhoto.size](https://developer.apple.com/documentation/photokit/phlivephoto/1616430-size)Added [PHLivePhotoRequestOptions](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions)Added [PHLivePhotoRequestOptions.deliveryMode](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616980-deliverymode)Added [PHLivePhotoRequestOptions.networkAccessAllowed](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616989-networkaccessallowed)Added [PHLivePhotoRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616961-progresshandler)Added [PHLivePhotoInfoCancelledKey](https://developer.apple.com/documentation/photokit/phlivephotoinfocancelledkey)Added [PHLivePhotoInfoErrorKey](https://developer.apple.com/documentation/photokit/phlivephotoinfoerrorkey)Added [PHLivePhotoInfoIsDegradedKey](https://developer.apple.com/documentation/photokit/phlivephotoinfoisdegradedkey)Added [PHLivePhotoRequestID](https://developer.apple.com/documentation/photokit/phlivephotorequestid)Added [PHLivePhotoRequestIDInvalid](https://developer.apple.com/documentation/photokit/phlivephotorequestidinvalid)Modified [PHAdjustmentData](https://developer.apple.com/documentation/photokit/phadjustmentdata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAsset](https://developer.apple.com/documentation/photokit/phasset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetChangeRequest](https://developer.apple.com/documentation/photokit/phassetchangerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetCollection](https://developer.apple.com/documentation/photokit/phassetcollection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetCollectionChangeRequest](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetCollectionSubtype [enum]](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHAssetCollectionType [enum]](https://developer.apple.com/documentation/photokit/phassetcollectiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHAssetCreationRequest](https://developer.apple.com/documentation/photokit/phassetcreationrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetEditOperation [enum]](https://developer.apple.com/documentation/photokit/phasseteditoperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHAssetMediaSubtype [struct]](https://developer.apple.com/documentation/photokit/phassetmediasubtype)

|  | Declaration |
| --- | --- |
| From | ``` struct PHAssetMediaSubtype : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var PhotoScreenshot: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` |
| To | ``` struct PHAssetMediaSubtype : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var PhotoScreenshot: PHAssetMediaSubtype { get }     static var PhotoLive: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` |

Modified [PHAssetMediaType [enum]](https://developer.apple.com/documentation/photokit/phassetmediatype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHAssetResource](https://developer.apple.com/documentation/photokit/phassetresource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetResource : NSObject {     var type: PHAssetResourceType { get }     var assetLocalIdentifier: String { get }     var uniformTypeIdentifier: String { get }     var originalFilename: String { get }     class func assetResourcesForAsset(_ asset: PHAsset) -> [PHAssetResource] } ``` | AnyObject |
| To | ``` class PHAssetResource : NSObject {     var type: PHAssetResourceType { get }     var assetLocalIdentifier: String { get }     var uniformTypeIdentifier: String { get }     var originalFilename: String { get }     class func assetResourcesForAsset(_ asset: PHAsset) -> [PHAssetResource]     class func assetResourcesForLivePhoto(_ livePhoto: PHLivePhoto) -> [PHAssetResource] } ``` | -- |

Modified [PHAssetResourceCreationOptions](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [PHAssetResourceManager](https://developer.apple.com/documentation/photokit/phassetresourcemanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHAssetResourceRequestOptions](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [PHAssetResourceType [enum]](https://developer.apple.com/documentation/photokit/phassetresourcetype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum PHAssetResourceType : Int {     case Photo     case Video     case Audio     case AlternatePhoto     case FullSizePhoto     case FullSizeVideo     case AdjustmentData     case AdjustmentBasePhoto } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum PHAssetResourceType : Int {     case Photo     case Video     case Audio     case AlternatePhoto     case FullSizePhoto     case FullSizeVideo     case AdjustmentData     case AdjustmentBasePhoto     case PairedVideo } ``` | -- |

Modified [PHAuthorizationStatus [enum]](https://developer.apple.com/documentation/photokit/phauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHCachingImageManager](https://developer.apple.com/documentation/photokit/phcachingimagemanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHChange](https://developer.apple.com/documentation/photokit/phchange)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHCollection](https://developer.apple.com/documentation/photokit/phcollection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHCollectionEditOperation [enum]](https://developer.apple.com/documentation/photokit/phcollectioneditoperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHCollectionList](https://developer.apple.com/documentation/photokit/phcollectionlist)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHCollectionListChangeRequest](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHCollectionListSubtype [enum]](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHCollectionListType [enum]](https://developer.apple.com/documentation/photokit/phcollectionlisttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHContentEditingInput](https://developer.apple.com/documentation/photokit/phcontenteditinginput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHContentEditingInputRequestOptions](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHContentEditingOutput](https://developer.apple.com/documentation/photokit/phcontenteditingoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHFetchOptions](https://developer.apple.com/documentation/photokit/phfetchoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [PHFetchResult](https://developer.apple.com/documentation/photokit/phfetchresult)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSFastEnumeration |
| To | NSCopying, NSFastEnumeration |

Modified [PHFetchResultChangeDetails](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHImageContentMode [enum]](https://developer.apple.com/documentation/photokit/phimagecontentmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHImageManager](https://developer.apple.com/documentation/photokit/phimagemanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHImageManager : NSObject {     class func defaultManager() -> PHImageManager     func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID } ``` | AnyObject |
| To | ``` class PHImageManager : NSObject {     class func defaultManager() -> PHImageManager     func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestLivePhotoForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHLivePhotoRequestOptions?, resultHandler resultHandler: (PHLivePhoto?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID } ``` | -- |

Modified [PHImageRequestOptions](https://developer.apple.com/documentation/photokit/phimagerequestoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [PHImageRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHImageRequestOptionsResizeMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHImageRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHObject](https://developer.apple.com/documentation/photokit/phobject)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [PHObjectChangeDetails](https://developer.apple.com/documentation/photokit/phobjectchangedetails)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHObjectPlaceholder](https://developer.apple.com/documentation/photokit/phobjectplaceholder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHPhotoLibrary](https://developer.apple.com/documentation/photokit/phphotolibrary)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHVideoRequestOptions](https://developer.apple.com/documentation/photokit/phvideorequestoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PHVideoRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PHVideoRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsversion)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
