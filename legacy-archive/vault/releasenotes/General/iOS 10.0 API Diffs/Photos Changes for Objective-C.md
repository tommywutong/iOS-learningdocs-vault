---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/Photos.html
archived_at: '2026-07-18T02:54:58.089915Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Photos Changes for Objective-C

### Photos

#### PHAssetCollectionChangeRequest.h

Modified [+[PHAssetCollectionChangeRequest changeRequestForAssetCollection:assets:]](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619445-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)changeRequestForAssetCollection:(PHAssetCollection *)assetCollection assets:(PHFetchResult *)assets ``` |
| To | ``` + (instancetype)changeRequestForAssetCollection:(PHAssetCollection *)assetCollection assets:(PHFetchResult<PHAsset *> *)assets ``` |

#### PHChange.h

Modified [+[PHFetchResultChangeDetails changeDetailsFromFetchResult:toFetchResult:changedObjects:]](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613921-changedetailsfromfetchresult)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)changeDetailsFromFetchResult:(PHFetchResult *)fromResult toFetchResult:(PHFetchResult *)toResult changedObjects:(NSArray<PHObject *> *)changedObjects ``` |
| To | ``` + (instancetype)changeDetailsFromFetchResult:(PHFetchResult<ObjectType> *)fromResult toFetchResult:(PHFetchResult<ObjectType> *)toResult changedObjects:(NSArray<ObjectType> *)changedObjects ``` |

Modified [PHFetchResultChangeDetails.changedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613910-changedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray<__kindof PHObject *> *changedObjects ``` |
| To | ``` @property(atomic, strong, readonly) NSArray<ObjectType> *changedObjects ``` |

Modified [PHFetchResultChangeDetails.fetchResultAfterChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613894-fetchresultafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) PHFetchResult *fetchResultAfterChanges ``` |
| To | ``` @property(atomic, strong, readonly) PHFetchResult<ObjectType> *fetchResultAfterChanges ``` |

Modified [PHFetchResultChangeDetails.fetchResultBeforeChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613892-fetchresultbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) PHFetchResult *fetchResultBeforeChanges ``` |
| To | ``` @property(atomic, strong, readonly) PHFetchResult<ObjectType> *fetchResultBeforeChanges ``` |

Modified [PHFetchResultChangeDetails.insertedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613908-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray<__kindof PHObject *> *insertedObjects ``` |
| To | ``` @property(atomic, strong, readonly) NSArray<ObjectType> *insertedObjects ``` |

Modified [PHFetchResultChangeDetails.removedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613902-removedobjects)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) NSArray<__kindof PHObject *> *removedObjects ``` |
| To | ``` @property(atomic, strong, readonly) NSArray<ObjectType> *removedObjects ``` |

Modified [PHObjectChangeDetails.objectAfterChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613888-objectafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) __kindof PHObject *objectAfterChanges ``` |
| To | ``` @property(atomic, strong, readonly) ObjectType objectAfterChanges ``` |

Modified [PHObjectChangeDetails.objectBeforeChanges](https://developer.apple.com/documentation/photokit/phobjectchangedetails/1613890-objectbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, strong, readonly) __kindof PHObject *objectBeforeChanges ``` |
| To | ``` @property(atomic, strong, readonly) ObjectType objectBeforeChanges ``` |

#### PHCollectionListChangeRequest.h

Modified [+[PHCollectionListChangeRequest changeRequestForCollectionList:childCollections:]](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622850-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)changeRequestForCollectionList:(PHCollectionList *)collectionList childCollections:(PHFetchResult *)childCollections ``` |
| To | ``` + (instancetype)changeRequestForCollectionList:(PHCollectionList *)collectionList childCollections:(PHFetchResult<__kindof PHCollection *> *)childCollections ``` |

#### PHContentEditingInput.h

Added [PHContentEditingInput.livePhoto](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1638106-livephoto)

#### PHImageManager.h

Added [PHLivePhotoRequestOptions.version](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1648591-version)

#### PHLivePhotoEditingContext.h (Added)

Added [PHLivePhotoEditingContext](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext)Added [PHLivePhotoEditingContext.audioVolume](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642113-audiovolume)Added [-[PHLivePhotoEditingContext cancel]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642083-cancel)Added [PHLivePhotoEditingContext.duration](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642109-duration)Added [PHLivePhotoEditingContext.frameProcessor](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642132-frameprocessor)Added [PHLivePhotoEditingContext.fullSizeImage](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642106-fullsizeimage)Added [-[PHLivePhotoEditingContext initWithLivePhotoEditingInput:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642121-initwithlivephotoeditinginput)Added [PHLivePhotoEditingContext.orientation](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642093-orientation)Added [PHLivePhotoEditingContext.photoTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642131-phototime)Added [-[PHLivePhotoEditingContext prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642101-preparelivephotoforplayback)Added [-[PHLivePhotoEditingContext saveLivePhotoToOutput:options:completionHandler:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642082-savelivephototooutput)Added [PHLivePhotoFrame](https://developer.apple.com/documentation/photokit/phlivephotoframe)Added [PHLivePhotoFrame.image](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642114-image)Added [PHLivePhotoFrame.renderScale](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642123-renderscale)Added [PHLivePhotoFrame.time](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642126-time)Added [PHLivePhotoFrame.type](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642087-type)Added [PHLivePhotoEditingOption](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption)Added [PHLivePhotoFrameProcessingBlock](https://developer.apple.com/documentation/photokit/phlivephotoframeprocessingblock)Added [PHLivePhotoFrameType](https://developer.apple.com/documentation/photokit/phlivephotoframetype)Added [PHLivePhotoFrameTypePhoto](https://developer.apple.com/documentation/photokit/phlivephotoframetype/photo)Added [PHLivePhotoFrameTypeVideo](https://developer.apple.com/documentation/photokit/phlivephotoframetype/phlivephotoframetypevideo)Added [PHLivePhotoShouldRenderAtPlaybackTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption/1642124-shouldrenderatplaybacktime)

#### PhotosTypes.h

Added [PHAssetResourceTypeAdjustmentBasePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentbasepairedvideo)Added [PHAssetResourceTypeFullSizePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/fullsizepairedvideo)

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
