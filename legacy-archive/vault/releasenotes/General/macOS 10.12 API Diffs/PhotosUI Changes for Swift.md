---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/PhotosUI.html
archived_at: '2026-07-18T02:51:32.275186Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# PhotosUI Changes for Swift

### PhotosUI

Added [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview)Added [PHLivePhotoView.audioVolume](https://developer.apple.com/documentation/photokit/phlivephotoview/1641914-audiovolume)Added [PHLivePhotoView.contentMode](https://developer.apple.com/documentation/photokit/phlivephotoview/2097056-contentmode)Added [PHLivePhotoView.delegate](https://developer.apple.com/documentation/photokit/phlivephotoview/1623433-delegate)Added [PHLivePhotoView.isMuted](https://developer.apple.com/documentation/photokit/phlivephotoview/1623430-muted)Added [PHLivePhotoView.livePhoto](https://developer.apple.com/documentation/photokit/phlivephotoview/1623424-livephoto)Added [PHLivePhotoView.livePhotoBadgeView](https://developer.apple.com/documentation/photokit/phlivephotoview/1641913-livephotobadgeview)Added [PHLivePhotoView.startPlayback(with: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoview/1623419-startplaybackwithstyle)Added [PHLivePhotoView.stopPlayback()](https://developer.apple.com/documentation/photokit/phlivephotoview/1623418-stopplayback)Added [PHLivePhotoView.stopPlayback(animated: Bool)](https://developer.apple.com/documentation/photokit/phlivephotoview/2097059-stopplayback)Added [PHLivePhotoViewContentMode [enum]](https://developer.apple.com/documentation/photokit/phlivephotoviewcontentmode)Added [PHLivePhotoViewContentMode.aspectFill](https://developer.apple.com/documentation/photokit/phlivephotoviewcontentmode/aspectfill)Added [PHLivePhotoViewContentMode.aspectFit](https://developer.apple.com/documentation/photokit/phlivephotoviewcontentmode/aspectfit)Added [PHLivePhotoViewDelegate](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate)Added [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, didEndPlaybackWith: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623431-livephotoview)Added [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, willBeginPlaybackWith: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623421-livephotoview)Added [PHLivePhotoViewPlaybackStyle [enum]](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle)Added [PHLivePhotoViewPlaybackStyle.full](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/full)Added [PHLivePhotoViewPlaybackStyle.hint](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstylehint)Added [PHLivePhotoViewPlaybackStyle.undefined](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstyleundefined)Modified [PHContentEditingController](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller)

|  | Declaration |
| --- | --- |
| From | ``` protocol PHContentEditingController : NSObjectProtocol {     func canHandleAdjustmentData(_ adjustmentData: PHAdjustmentData!) -> Bool     func startContentEditingWithInput(_ contentEditingInput: PHContentEditingInput!, placeholderImage placeholderImage: NSImage!)     func finishContentEditingWithCompletionHandler(_ completionHandler: ((PHContentEditingOutput!) -> Void)!)     func cancelContentEditing()     var shouldShowCancelConfirmation: Bool { get } } ``` |
| To | ``` protocol PHContentEditingController : NSObjectProtocol {     func canHandle(_ adjustmentData: PHAdjustmentData) -> Bool     func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage placeholderImage: NSImage)     func finishContentEditing(completionHandler completionHandler: @escaping (PHContentEditingOutput?) -> Swift.Void)     func cancelContentEditing()     var shouldShowCancelConfirmation: Bool { get } } ``` |

Modified [PHContentEditingController.canHandle(_: PHAdjustmentData) -> Bool](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501739-canhandle)

|  | Declaration |
| --- | --- |
| From | ``` func canHandleAdjustmentData(_ adjustmentData: PHAdjustmentData!) -> Bool ``` |
| To | ``` func canHandle(_ adjustmentData: PHAdjustmentData) -> Bool ``` |

Modified [PHContentEditingController.finishContentEditing(completionHandler: (PHContentEditingOutput?) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501741-finishcontentediting)

|  | Declaration |
| --- | --- |
| From | ``` func finishContentEditingWithCompletionHandler(_ completionHandler: ((PHContentEditingOutput!) -> Void)!) ``` |
| To | ``` func finishContentEditing(completionHandler completionHandler: @escaping (PHContentEditingOutput?) -> Swift.Void) ``` |

Modified [PHContentEditingController.startContentEditing(with: PHContentEditingInput, placeholderImage: NSImage)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501738-startcontenteditingwithinput)

|  | Declaration |
| --- | --- |
| From | ``` func startContentEditingWithInput(_ contentEditingInput: PHContentEditingInput!, placeholderImage placeholderImage: NSImage!) ``` |
| To | ``` func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage placeholderImage: NSImage) ``` |

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
