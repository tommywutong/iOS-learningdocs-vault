---
title: 'PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative
  and interruptible custom view controller transition'
apple_id: TP40017554
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoTransitioning/Listings/Photo_Transitioning_AssetCell_swift.html
archived_at: '2026-07-18T03:18:55.440963Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative and interruptible custom view controller transition](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)


[Next](Photo%20Transitioning-AppDelegate.swift.md)[Previous](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)

# Photo Transitioning/AssetCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AssetCell is a basic UICollectionViewCell sublass to display a photo.
*/

import UIKit

class AssetCell: UICollectionViewCell {

    var assetIdentifier: String = ""
    let imageView: UIImageView

    override init(frame: CGRect) {
        imageView = UIImageView(frame: CGRect(origin: CGPoint.zero, size: frame.size))
        imageView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        imageView.contentMode = .scaleAspectFill
        imageView.clipsToBounds = true

        super.init(frame: frame)

        backgroundView = imageView
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func prepareForReuse() {
        super.prepareForReuse()
        imageView.image = nil;
        assetIdentifier = ""
    }
}
```

[Next](Photo%20Transitioning-AppDelegate.swift.md)[Previous](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)

