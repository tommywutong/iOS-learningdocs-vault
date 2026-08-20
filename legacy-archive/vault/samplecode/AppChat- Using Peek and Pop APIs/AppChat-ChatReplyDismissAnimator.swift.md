---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatReplyDismissAnimator_swift.html
archived_at: '2026-07-18T03:01:05.776242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-MathUtilities.swift.md)[Previous](AppChat-AppDelegate.swift.md)

# AppChat/ChatReplyDismissAnimator.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The animator used when the ChatReplyViewController is dismissed.
 */

import UIKit

private enum AnimationParameters {
    static let duration = 0.4
    static let damping: CGFloat = 0.8
}

class ChatReplyDismissAnimator: NSObject, UIViewControllerAnimatedTransitioning {    
    func transitionDuration(using transitionContext: UIViewControllerContextTransitioning?) -> TimeInterval {
        return AnimationParameters.duration
    }

    func animateTransition(using transitionContext: UIViewControllerContextTransitioning) {
        let replyViewController = transitionContext.viewController(forKey: UITransitionContextViewControllerKey.from) as! ChatReplyViewController

        let animations: () -> ()
        if transitionContext.isInteractive {
            animations = {
                replyViewController.view.alpha = 0.0
            }
        }
        else {
            animations = {
                replyViewController.isExpanded = false
            }
        }

        let completion = { (finished: Bool) in
            transitionContext.completeTransition(true)
        }

        if transitionContext.isAnimated {
            let duration = transitionDuration(using: transitionContext)
            if transitionContext.isInteractive {
                UIView.animate(withDuration: duration, delay: 0, options: [], animations: animations, completion: completion)
            }
            else {
                UIView.animate(withDuration: duration, delay: 0, usingSpringWithDamping: AnimationParameters.damping, initialSpringVelocity: 0, options: [], animations: animations, completion: completion)
            }
        }
        else {
            animations()
            completion(true)
        }
    }
}
```

[Next](AppChat-MathUtilities.swift.md)[Previous](AppChat-AppDelegate.swift.md)

