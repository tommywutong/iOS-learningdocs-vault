---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatReplyTransitionDelegate_swift.html
archived_at: '2026-07-18T03:01:06.035244Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatTableViewController.swift.md)[Previous](AppChat-NewChatDelegate.swift.md)

# AppChat/ChatReplyTransitionDelegate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The transitioning delegate used for the ChatReplyViewController presentation.
 */

import UIKit

class ChatReplyTransitionDelegate: NSObject, UIViewControllerTransitioningDelegate {
    var presentationIsInteractive = false
    var currentTransitionProgress: CGFloat = 0.0 {
        didSet {
            currentInteractionController?.update(currentTransitionProgress)
        }
    }
    func completeCurrentInteractiveTransition() {
        currentInteractionController?.finish()
    }
    func cancelCurrentInteractiveTransition() {
        currentInteractionController?.cancel()
    }

    private var currentInteractionController: ChatReplyInteractionController? = nil

    func animationController(forPresented presented: UIViewController, presenting: UIViewController, source: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return ChatReplyPresentAnimator()
    }

    func animationController(forDismissed dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return ChatReplyDismissAnimator()
    }

    func presentationController(forPresented presented: UIViewController, presenting: UIViewController?, source: UIViewController) -> UIPresentationController? {
        return ChatReplyPresentationController(presentedViewController: presented, presenting: presenting)
    }

    func interactionControllerForPresentation(using animator: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning? {
        if presentationIsInteractive {
            currentInteractionController = ChatReplyInteractionController()
            return currentInteractionController
        }
        else {
            return nil
        }
    }
}
```

[Next](AppChat-ChatTableViewController.swift.md)[Previous](AppChat-NewChatDelegate.swift.md)

