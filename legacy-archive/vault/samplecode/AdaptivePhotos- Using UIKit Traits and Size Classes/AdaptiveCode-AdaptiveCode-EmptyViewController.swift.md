---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveCode_AdaptiveCode_EmptyViewController_swift.html
archived_at: '2026-07-18T03:00:43.873749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveCode-AdaptiveCode-UIViewController%2BViewControllerShowing.swift.md)[Previous](AdaptiveCode-AdaptiveCode-AppDelegate.swift.md)

# AdaptiveCode/AdaptiveCode/EmptyViewController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A view controller that shows placeholder text.
*/

import UIKit

class EmptyViewController: UIViewController {
    override func loadView() {
        let view = UIView()
        view.backgroundColor = UIColor.white

        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = NSLocalizedString("No Conversation Selected", comment: "No Conversation Selected")
        label.textColor = UIColor(white: 0.0, alpha: 0.4)
        label.font = UIFont.preferredFont(forTextStyle: UIFontTextStyle.headline)
        view.addSubview(label)

        let xConstraint = NSLayoutConstraint(item: label, attribute: .centerX, relatedBy: .equal, toItem: view, attribute: .centerX, multiplier: 1, constant: 0)
        let yConstraint = NSLayoutConstraint(item: label, attribute: .centerY, relatedBy: .equal, toItem: view, attribute: .centerY, multiplier: 1, constant: 0)
        NSLayoutConstraint.activate([xConstraint, yConstraint])

        self.view = view
    }
}
```

[Next](AdaptiveCode-AdaptiveCode-UIViewController%2BViewControllerShowing.swift.md)[Previous](AdaptiveCode-AdaptiveCode-AppDelegate.swift.md)

