---
title: 'AppChat: Using Peek and Pop APIs'
apple_id: TP40017298
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppChat/Listings/AppChat_ChatReplyPresentAnimator_swift.html
archived_at: '2026-07-18T03:01:05.885488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppChat: Using Peek and Pop APIs](AppChat-%20Using%20Peek%20and%20Pop%20APIs.md)


[Next](AppChat-ChatTableViewCell.swift.md)[Previous](AppChat-ChatItem.swift.md)

# AppChat/ChatReplyPresentAnimator.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The animator used when the ChatReplyViewController is presented.
 */

import UIKit

private enum AnimationParameters {
    static let duration = 0.4
    static let damping: CGFloat = 0.7
}

class ChatReplyPresentAnimator: NSObject, UIViewControllerAnimatedTransitioning {    
    func transitionDuration(using transitionContext: UIViewControllerContextTransitioning?) -> TimeInterval {
        return AnimationParameters.duration
    }

    func animateTransition(using transitionContext: UIViewControllerContextTransitioning) {
        if let replyView = transitionContext.view(forKey: UITransitionContextViewKey.to) {
            transitionContext.containerView.addSubview(replyView)
            replyView.layoutIfNeeded()
            replyView.alpha = 1.0
        }

        let replyViewController = transitionContext.viewController(forKey: UITransitionContextViewControllerKey.to) as! ChatReplyViewController

        let animations = {
            replyViewController.isExpanded = true
        }

        let completion = { (finished: Bool) in
            transitionContext.completeTransition(finished)
        }

        replyViewController.isExpanded = false

        if transitionContext.isAnimated {
            let duration = transitionDuration(using: transitionContext)
            let runAnimations = {
                UIView.animate(withDuration: duration, delay: 0, usingSpringWithDamping: AnimationParameters.damping, initialSpringVelocity: 0, options: [], animations: animations, completion: completion)
            }
            if transitionContext.isInteractive {
                UIView.animate(withDuration: duration, delay: 0, options: [], animations: {}, completion: { (finished) in
                    if transitionContext.transitionWasCancelled {
                        completion(false)
                    }
                    else {
                        runAnimations()
                    }
                })
            }
            else {
                runAnimations()
            }
        }
        else {
            animations()
            completion(true)
        }
    }
}
```

[Next](AppChat-ChatTableViewCell.swift.md)[Previous](AppChat-ChatItem.swift.md)

