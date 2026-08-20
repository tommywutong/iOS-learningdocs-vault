---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Photos.html
archived_at: '2026-07-18T02:56:15.716887Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Photos Changes

## Photos

Removed PHAssetBurstSelectionType.valueRemoved PHAssetMediaSubtype.valueRemoved PHFetchResult.objectAtIndexedSubscript(Int) -> AnyObject!Added PHAsset.locationAdded PHAssetBurstSelectionType.init(rawValue: UInt)Added PHAssetChangeRequest.locationAdded PHAssetCollection.approximateLocationAdded PHAssetCollectionSubtype.AlbumMyPhotoStreamAdded PHAssetCollectionSubtype.SmartAlbumUserLibraryAdded PHAssetMediaSubtype.init(rawValue: UInt)Added PHContentEditingInput.locationModified PHAdjustmentData.init(formatIdentifier: String!, formatVersion: String!, data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(formatIdentifier formatIdentifier: String!, formatVersion formatVersion: String!, data data: NSData!) ``` |
| To | ``` init!(formatIdentifier formatIdentifier: String!, formatVersion formatVersion: String!, data data: NSData!) ``` |

Modified PHAssetBurstSelectionType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PHAssetBurstSelectionType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: PHAssetBurstSelectionType { get }     static var AutoPick: PHAssetBurstSelectionType { get }     static var UserPick: PHAssetBurstSelectionType { get } } ``` |
| To | ``` struct PHAssetBurstSelectionType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PHAssetBurstSelectionType { get }     static var AutoPick: PHAssetBurstSelectionType { get }     static var UserPick: PHAssetBurstSelectionType { get } } ``` |

Modified PHAssetBurstSelectionType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified PHAssetChangeRequest.init(forAsset: PHAsset!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forAsset asset: PHAsset!) ``` |
| To | ``` convenience init!(forAsset asset: PHAsset!) ``` |

Modified PHAssetCollectionChangeRequest.init(forAssetCollection: PHAssetCollection!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forAssetCollection assetCollection: PHAssetCollection!) ``` |
| To | ``` convenience init!(forAssetCollection assetCollection: PHAssetCollection!) ``` |

Modified PHAssetCollectionChangeRequest.init(forAssetCollection: PHAssetCollection!, assets: PHFetchResult!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forAssetCollection assetCollection: PHAssetCollection!, assets assets: PHFetchResult!) ``` |
| To | ``` convenience init!(forAssetCollection assetCollection: PHAssetCollection!, assets assets: PHFetchResult!) ``` |

Modified PHAssetCollectionSubtype [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetCollectionSubtype : Int {     case AlbumRegular     case AlbumSyncedEvent     case AlbumSyncedFaces     case AlbumSyncedAlbum     case AlbumImported     case AlbumCloudShared     case SmartAlbumGeneric     case SmartAlbumPanoramas     case SmartAlbumVideos     case SmartAlbumFavorites     case SmartAlbumTimelapses     case SmartAlbumAllHidden     case SmartAlbumRecentlyAdded     case SmartAlbumBursts     case SmartAlbumSlomoVideos     case Any } ``` |
| To | ``` enum PHAssetCollectionSubtype : Int {     case AlbumRegular     case AlbumSyncedEvent     case AlbumSyncedFaces     case AlbumSyncedAlbum     case AlbumImported     case AlbumMyPhotoStream     case AlbumCloudShared     case SmartAlbumGeneric     case SmartAlbumPanoramas     case SmartAlbumVideos     case SmartAlbumFavorites     case SmartAlbumTimelapses     case SmartAlbumAllHidden     case SmartAlbumRecentlyAdded     case SmartAlbumBursts     case SmartAlbumSlomoVideos     case SmartAlbumUserLibrary     case Any } ``` |

Modified PHAssetMediaSubtype [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PHAssetMediaSubtype : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` |
| To | ``` struct PHAssetMediaSubtype : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` |

Modified PHAssetMediaSubtype.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified PHCollectionListChangeRequest.init(forCollectionList: PHCollectionList!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forCollectionList collectionList: PHCollectionList!) ``` |
| To | ``` convenience init!(forCollectionList collectionList: PHCollectionList!) ``` |

Modified PHCollectionListChangeRequest.init(forCollectionList: PHCollectionList!, childCollections: PHFetchResult!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forCollectionList collectionList: PHCollectionList!, childCollections childCollections: PHFetchResult!) ``` |
| To | ``` convenience init!(forCollectionList collectionList: PHCollectionList!, childCollections childCollections: PHFetchResult!) ``` |

Modified PHContentEditingOutput.init(contentEditingInput: PHContentEditingInput!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentEditingInput contentEditingInput: PHContentEditingInput!) ``` |
| To | ``` init!(contentEditingInput contentEditingInput: PHContentEditingInput!) ``` |

Modified PHContentEditingOutput.init(placeholderForCreatedAsset: PHObjectPlaceholder!)

|  | Declaration |
| --- | --- |
| From | ``` init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder!) ``` |
| To | ``` init!(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder!) ``` |

Modified PHFetchResultChangeDetails.init(fromFetchResult: PHFetchResult!, toFetchResult: PHFetchResult!, changedObjects:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromFetchResult fromResult: PHFetchResult!, toFetchResult toResult: PHFetchResult!, changedObjects changedObjects: [AnyObject]!) ``` |
| To | ``` convenience init!(fromFetchResult fromResult: PHFetchResult!, toFetchResult toResult: PHFetchResult!, changedObjects changedObjects: [AnyObject]!) ``` |

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
