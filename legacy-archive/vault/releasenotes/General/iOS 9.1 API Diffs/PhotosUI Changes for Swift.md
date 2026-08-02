---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/PhotosUI.html
archived_at: '2026-07-18T02:57:10.369884Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# PhotosUI Changes for Swift

### PhotosUI

Added [PHLivePhotoBadgeOptions [struct]](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions)Added PHLivePhotoBadgeOptions.init(rawValue: UInt)Added [PHLivePhotoBadgeOptions.LiveOff](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions/phlivephotobadgeoptionsliveoff)Added [PHLivePhotoBadgeOptions.OverContent](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions/1623422-overcontent)Added [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview)Added [PHLivePhotoView.delegate](https://developer.apple.com/documentation/photokit/phlivephotoview/1623433-delegate)Added [PHLivePhotoView.livePhoto](https://developer.apple.com/documentation/photokit/phlivephotoview/1623424-livephoto)Added [PHLivePhotoView.livePhotoBadgeImageWithOptions(_: PHLivePhotoBadgeOptions) -> UIImage [class]](https://developer.apple.com/documentation/photokit/phlivephotoview/1623417-livephotobadgeimage)Added [PHLivePhotoView.muted](https://developer.apple.com/documentation/photokit/phlivephotoview/1623430-muted)Added [PHLivePhotoView.playbackGestureRecognizer](https://developer.apple.com/documentation/photokit/phlivephotoview/1623426-playbackgesturerecognizer)Added [PHLivePhotoView.startPlaybackWithStyle(_: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoview/1623419-startplaybackwithstyle)Added [PHLivePhotoView.stopPlayback()](https://developer.apple.com/documentation/photokit/phlivephotoview/1623418-stopplayback)Added [PHLivePhotoViewDelegate](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate)Added [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, didEndPlaybackWithStyle: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623431-livephotoview)Added [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, willBeginPlaybackWithStyle: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623421-livephotoview)Added [PHLivePhotoViewPlaybackStyle [enum]](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle)Added [PHLivePhotoViewPlaybackStyle.Full](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/full)Added [PHLivePhotoViewPlaybackStyle.Hint](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstylehint)Added [PHLivePhotoViewPlaybackStyle.Undefined](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstyleundefined)Modified [PHContentEditingController.canHandleAdjustmentData(_: PHAdjustmentData!) -> Bool](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501739-canhandle)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified [PHContentEditingController.finishContentEditingWithCompletionHandler(_: ((PHContentEditingOutput!) -> Void)!)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501741-finishcontentediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 8.0 |

Modified [PHContentEditingController.startContentEditingWithInput(_: PHContentEditingInput!, placeholderImage: UIImage!)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501738-startcontenteditingwithinput)

|  | Introduction |
| --- | --- |
| From | iOS 2.0 |
| To | iOS 8.0 |

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
