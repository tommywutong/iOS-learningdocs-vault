---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/AVKit.html
archived_at: '2026-07-18T02:56:29.395934Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AVKit Changes for Objective-C

### AVKit

#### AVError.h (Added)

Added [AVKitError](https://developer.apple.com/documentation/avkit/avkiterror)Added [AVKitErrorDomain](https://developer.apple.com/documentation/avkit/avkiterrordomain)Added [AVKitErrorPictureInPictureStartFailed](https://developer.apple.com/documentation/avkit/avkiterror/avkiterrorpictureinpicturestartfailed)Added [AVKitErrorUnknown](https://developer.apple.com/documentation/avkit/avkiterror/code/unknown)

#### AVPictureInPictureController.h (Added)

Added [AVPictureInPictureController](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller)Added [AVPictureInPictureController.delegate](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614709-delegate)Added [-[AVPictureInPictureController initWithPlayerLayer:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614707-initwithplayerlayer)Added [+[AVPictureInPictureController isPictureInPictureSupported]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614693-ispictureinpicturesupported)Added [AVPictureInPictureController.pictureInPictureActive](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614720-pictureinpictureactive)Added [+[AVPictureInPictureController pictureInPictureButtonStartImageCompatibleWithTraitCollection:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614699-pictureinpicturebuttonstartimage)Added [+[AVPictureInPictureController pictureInPictureButtonStopImageCompatibleWithTraitCollection:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614713-pictureinpicturebuttonstopimagec)Added [AVPictureInPictureController.pictureInPicturePossible](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614691-ispictureinpicturepossible)Added [AVPictureInPictureController.pictureInPictureSuspended](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614689-pictureinpicturesuspended)Added [AVPictureInPictureController.playerLayer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614706-playerlayer)Added [-[AVPictureInPictureController startPictureInPicture]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614687-startpictureinpicture)Added [-[AVPictureInPictureController stopPictureInPicture]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614701-stoppictureinpicture)Added [AVPictureInPictureControllerDelegate](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate)Added [-[AVPictureInPictureControllerDelegate pictureInPictureController:failedToStartPictureInPictureWithError:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614697-pictureinpicturecontroller)Added [-[AVPictureInPictureControllerDelegate pictureInPictureController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614703-picture)Added [-[AVPictureInPictureControllerDelegate pictureInPictureControllerDidStartPictureInPicture:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614695-pictureinpicturecontrollerdidsta)Added [-[AVPictureInPictureControllerDelegate pictureInPictureControllerDidStopPictureInPicture:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614717-pictureinpicturecontrollerdidsto)Added [-[AVPictureInPictureControllerDelegate pictureInPictureControllerWillStartPictureInPicture:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614711-pictureinpicturecontrollerwillst)Added [-[AVPictureInPictureControllerDelegate pictureInPictureControllerWillStopPictureInPicture:]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614719-pictureinpicturecontrollerwillst)

#### AVPlayerViewController.h

Added [AVPlayerViewController.allowsPictureInPicturePlayback](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1615821-allowspictureinpictureplayback)Added [AVPlayerViewController.delegate](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1615840-delegate)Added [AVPlayerViewControllerDelegate](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate)Added [-[AVPlayerViewControllerDelegate playerViewController:failedToStartPictureInPictureWithError:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615822-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615838-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate playerViewControllerDidStartPictureInPicture:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615842-playerviewcontrollerdidstartpict)Added [-[AVPlayerViewControllerDelegate playerViewControllerDidStopPictureInPicture:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615819-playerviewcontrollerdidstoppictu)Added [-[AVPlayerViewControllerDelegate playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615817-playerviewcontrollershouldautoma)Added [-[AVPlayerViewControllerDelegate playerViewControllerWillStartPictureInPicture:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615815-playerviewcontrollerwillstartpic)Added [-[AVPlayerViewControllerDelegate playerViewControllerWillStopPictureInPicture:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615827-playerviewcontrollerwillstoppict)

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
