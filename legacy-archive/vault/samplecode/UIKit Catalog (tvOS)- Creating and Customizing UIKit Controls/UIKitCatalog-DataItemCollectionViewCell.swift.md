---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_DataItemCollectionViewCell_swift.html
archived_at: '2026-07-18T03:27:28.684423Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-CustomInputAccessoryView.swift.md)[Previous](UIKitCatalog-SegmentedControlsViewController.swift.md)

# UIKitCatalog/DataItemCollectionViewCell.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UICollectionViewCell` subclass used to display `DataItem`s within `UICollectionView`s.
*/

import UIKit

class DataItemCollectionViewCell: UICollectionViewCell {
    // MARK: Properties

    static let reuseIdentifier = "DataItemCell"

    @IBOutlet weak var label: UILabel!

    @IBOutlet weak var imageView: UIImageView!

    var representedDataItem: DataItem?

    // MARK: Initialization

    override func awakeFromNib() {
        super.awakeFromNib()

        // These properties are also exposed in Interface Builder.
        imageView.adjustsImageWhenAncestorFocused = true
        imageView.clipsToBounds = false

        label.alpha = 0.0
    }

    // MARK: UICollectionReusableView

    override func prepareForReuse() {
        super.prepareForReuse()

        // Reset the label's alpha value so it's initially hidden.
        label.alpha = 0.0
    }

    // MARK: UIFocusEnvironment

    override func didUpdateFocus(in context: UIFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator) {
        /*
            Update the label's alpha value using the `UIFocusAnimationCoordinator`.
            This will ensure all animations run alongside each other when the focus
            changes.
        */
        coordinator.addCoordinatedAnimations({
            if self.isFocused {
                self.label.alpha = 1.0
            }
            else {
                self.label.alpha = 0.0
            }
        }, completion: nil)
    }
}
```

[Next](UIKitCatalog-CustomInputAccessoryView.swift.md)[Previous](UIKitCatalog-SegmentedControlsViewController.swift.md)

