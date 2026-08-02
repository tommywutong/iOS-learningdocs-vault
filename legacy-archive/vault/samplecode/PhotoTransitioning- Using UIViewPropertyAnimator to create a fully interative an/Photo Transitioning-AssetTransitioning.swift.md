---
title: 'PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative
  and interruptible custom view controller transition'
apple_id: TP40017554
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoTransitioning/Listings/Photo_Transitioning_AssetTransitioning_swift.html
archived_at: '2026-07-18T03:18:55.680829Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative and interruptible custom view controller transition](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)


[Next](Photo%20Transitioning-AssetTransitioningMath.swift.md)[Previous](Photo%20Transitioning-AppDelegate.swift.md)

# Photo Transitioning/AssetTransitioning.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The AssetTransitionItem class represets a data object used to pass transition information between view controllers. The AssetTransitioning protocol
                is the contract each view controller involved in the transition must conform to. This protocol gives each view controller the chance to negotiate
                what transition items it can support for a given transition.
*/

import UIKit
import Photos

class AssetTransitionItem: NSObject {
    var initialFrame: CGRect
    var image: UIImage {
        didSet {
            imageView?.image = image
        }
    }
    var indexPath: IndexPath
    var asset: PHAsset
    var targetFrame: CGRect?
    var imageView: UIImageView?
    var touchOffset: CGVector = CGVector.zero

    init(initialFrame: CGRect, image: UIImage, indexPath: IndexPath, asset: PHAsset) {
        self.initialFrame = initialFrame
        self.image = image
        self.indexPath = indexPath
        self.asset = asset
        super.init()
    }
}

protocol AssetTransitioning {
    func itemsForTransition(context: UIViewControllerContextTransitioning) -> Array<AssetTransitionItem>
    func targetFrame(transitionItem: AssetTransitionItem) -> CGRect?
    func willTransition(fromController: UIViewController, toController: UIViewController, items: Array<AssetTransitionItem>)
    func didTransition(fromController: UIViewController, toController: UIViewController, items: Array<AssetTransitionItem>)
}
```

[Next](Photo%20Transitioning-AssetTransitioningMath.swift.md)[Previous](Photo%20Transitioning-AppDelegate.swift.md)

