---
title: 'AdaptiveElements: Implementing Your Own Adaptive Design with UIKit'
apple_id: TP40017300
resource_type: Sample Code
platform: iOS
topic: General
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptiveElements/Listings/AdaptiveElements_LargeElementViewController_swift.html
archived_at: '2026-07-18T03:00:43.314221Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptiveElements: Implementing Your Own Adaptive Design with UIKit](AdaptiveElements-%20Implementing%20Your%20Own%20Adaptive%20Design%20with%20UIKit.md)


[Next](AdaptiveElements-SmallElementViewController.swift.md)[Previous](AdaptiveElements-%20Implementing%20Your%20Own%20Adaptive%20Design%20with%20UIKit.md)

# AdaptiveElements/LargeElementViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    LargeElementViewController is used in two different ways:
     1. Contained within ExampleContainerViewController, when its width is large.
     2. Presented by SmallElementViewController, when the ExampleContainerViewController's width is small.
     It shows a large version of the element. When it is presented, tapping on it will dismiss it.
 */

import UIKit

class LargeElementViewController: UIViewController {

    var widthConstraint: NSLayoutConstraint?

    override func updateViewConstraints() {
        super.updateViewConstraints()

        /*
            If we are not being presented full-screen,
            then add a constraint to make this view no wider than our superview's readable content guide.
         */

        if presentingViewController == nil && widthConstraint == nil, let superview = view.superview {
            widthConstraint = view.widthAnchor.constraint(lessThanOrEqualTo: superview.readableContentGuide.widthAnchor)
            widthConstraint?.isActive = true
        }
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)

        /*
            When this view appears, if we are being presented,
            add a tap gesture recognizer so we can dismiss when we are tapped.
         */

        if isBeingPresented {
            let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(self.tapped))
            view.addGestureRecognizer(tapGestureRecognizer)
        }
    }

    func tapped(_ gestureRecognizer: UITapGestureRecognizer) {
        if gestureRecognizer.state == .ended {
            dismiss(animated: true, completion: nil)
        }
    }

}
```

[Next](AdaptiveElements-SmallElementViewController.swift.md)[Previous](AdaptiveElements-%20Implementing%20Your%20Own%20Adaptive%20Design%20with%20UIKit.md)

