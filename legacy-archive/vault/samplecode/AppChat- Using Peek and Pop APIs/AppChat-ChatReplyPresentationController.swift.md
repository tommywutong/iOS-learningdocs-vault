---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatReplyPresentationController_swift.html
archived_at: '2026-07-18T03:01:05.966515Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatItem.swift.md)[Previous](AppChat-ChatItemManager.swift.md)

# AppChat/ChatReplyPresentationController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The presentation controller used for the ChatReplyViewController presentation.
 */

import UIKit

class ChatReplyPresentationController: UIPresentationController {
    let blurView = UIVisualEffectView()

    override init(presentedViewController: UIViewController, presenting presentingViewController: UIViewController?) {
        super.init(presentedViewController: presentedViewController, presenting: presentingViewController)

        blurView.autoresizingMask = [.flexibleHeight, .flexibleWidth]
    }

    override func presentationTransitionWillBegin() {
        blurView.frame = containerView!.bounds
        containerView!.insertSubview(blurView, at: 0)

        presentedViewController.transitionCoordinator?.animate(alongsideTransition: { _ in
            self.blurView.effect = UIBlurEffect(style: .light)
        })
    }

    override func dismissalTransitionWillBegin() {
        presentedViewController.transitionCoordinator?.animate(alongsideTransition: { _ in
            self.blurView.effect = nil
        })
    }

    override var frameOfPresentedViewInContainerView: CGRect {
        return containerView!.bounds
    }
}
```

[Next](AppChat-ChatItem.swift.md)[Previous](AppChat-ChatItemManager.swift.md)

