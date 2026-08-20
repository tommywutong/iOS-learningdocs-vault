---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/frameworks/UIKit.html
archived_at: '2026-07-18T02:56:20.335138Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# UIKit Changes

## UIKit

UIApplication.hRemoved #def UIInterfaceOrientationIsLandscapeRemoved #def UIInterfaceOrientationIsPortraitAdded [UIInterfaceOrientationIsLandscape()](https://developer.apple.com/documentation/uikit/uiinterfaceorientation/1623001-islandscape)Added [UIInterfaceOrientationIsPortrait()](https://developer.apple.com/documentation/uikit/uiinterfaceorientation/1623046-isportrait)UIDevice.hRemoved #def UIDeviceOrientationIsLandscapeRemoved #def UIDeviceOrientationIsPortraitRemoved #def UI_USER_INTERFACE_IDIOMAdded [UIDeviceOrientationIsLandscape()](https://developer.apple.com/documentation/uikit/1620061-uideviceorientationislandscape)Added [UIDeviceOrientationIsPortrait()](https://developer.apple.com/documentation/uikit/uideviceorientation/1620057-isportrait)Added [UI_USER_INTERFACE_IDIOM()](https://developer.apple.com/documentation/uikit/1620016-ui_user_interface_idiom)UIPresentationController.hAdded [-[UIAdaptivePresentationControllerDelegate adaptivePresentationStyleForPresentationController:traitCollection:]](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618334-adaptivepresentationstyle)Added [-[UIAdaptivePresentationControllerDelegate presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:]](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618324-presentationcontroller)Added [-[UIPresentationController adaptivePresentationStyleForTraitCollection:]](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618325-adaptivepresentationstyle)UITableViewController.hAdded [-[UITableViewController initWithCoder:]](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614760-initwithcoder)Added [-[UITableViewController initWithNibName:bundle:]](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614757-initwithnibname)Modified [-[UITableViewController initWithStyle:]](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614754-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

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
