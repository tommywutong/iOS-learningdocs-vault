---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Objective-C/Photos.html
archived_at: '2026-07-18T02:57:05.104304Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Photos Changes for Objective-C

### Photos

#### PHAssetResource.h

Added [+[PHAssetResource assetResourcesForLivePhoto:]](https://developer.apple.com/documentation/photokit/phassetresource/1623984-assetresources)

#### PHImageManager.h

Added [-[PHImageManager requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:]](https://developer.apple.com/documentation/photokit/phimagemanager/1616984-requestlivephoto)Added [PHLivePhotoRequestOptions](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions)Added [PHLivePhotoRequestOptions.deliveryMode](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616980-deliverymode)Added [PHLivePhotoRequestOptions.networkAccessAllowed](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616989-isnetworkaccessallowed)Added [PHLivePhotoRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616961-progresshandler)Modified [PHImageContentMode](https://developer.apple.com/documentation/photokit/phimagecontentmode)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeAspectFill](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodeaspectfill)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeAspectFit](https://developer.apple.com/documentation/photokit/phimagecontentmode/aspectfit)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeDefault](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodedefault)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

#### PHLivePhoto.h (Added)

Added [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto)Added [+[PHLivePhoto cancelLivePhotoRequestWithRequestID:]](https://developer.apple.com/documentation/photokit/phlivephoto/1616436-cancellivephotorequestwithreques)Added [+[PHLivePhoto requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:]](https://developer.apple.com/documentation/photokit/phlivephoto/1616434-request)Added [PHLivePhoto.size](https://developer.apple.com/documentation/photokit/phlivephoto/1616430-size)Added [PHLivePhotoInfoCancelledKey](https://developer.apple.com/documentation/photokit/phlivephotoinfocancelledkey)Added [PHLivePhotoInfoErrorKey](https://developer.apple.com/documentation/photokit/phlivephotoinfoerrorkey)Added [PHLivePhotoInfoIsDegradedKey](https://developer.apple.com/documentation/photokit/phlivephotoinfoisdegradedkey)Added [PHLivePhotoRequestID](https://developer.apple.com/documentation/photokit/phlivephotorequestid)Added [PHLivePhotoRequestIDInvalid](https://developer.apple.com/documentation/photokit/phlivephotorequestidinvalid)

#### PhotosTypes.h

Added [PHAssetMediaSubtypePhotoLive](https://developer.apple.com/documentation/photokit/phassetmediasubtype/phassetmediasubtypephotolive)Added [PHAssetResourceTypePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/pairedvideo)Modified [PHImageContentMode](https://developer.apple.com/documentation/photokit/phimagecontentmode)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeAspectFill](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodeaspectfill)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeAspectFit](https://developer.apple.com/documentation/photokit/phimagecontentmode/aspectfit)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

Modified [PHImageContentModeDefault](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodedefault)

|  | Header |
| --- | --- |
| From | Photos/PHImageManager.h |
| To | Photos/PhotosTypes.h |

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
