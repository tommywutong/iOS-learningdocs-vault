---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_CreatureCollectionViewCell_swift.html
archived_at: '2026-07-15T04:56:06.864528Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-DreamListViewControllerModel.swift.md)[Previous](LucidDreams-DecoratingLayout.swift.md)

# LucidDreams/CreatureCollectionViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides a simple collection view cell that displays a `Creature`'s
                image. This is used in the `DreamDetailViewController`.
*/

import UIKit

/// A collection view cell that displays a `Dream.Creature`'s image.
class CreatureCollectionViewCell: UICollectionViewCell {
    // MARK: Properties

    static let reuseIdentifier = "\(CreatureCollectionViewCell.self)"

    @IBOutlet var imageView: UIImageView!

    var creature: Dream.Creature! {
        didSet {
            imageView.image = creature?.image
        }
    }

    override var isSelected: Bool {
        set {
            super.isSelected = newValue

            if newValue {
                contentView.layer.borderWidth = 1
                contentView.layer.borderColor = UIColor.blue.cgColor
            }
            else {
                contentView.layer.borderWidth = 0
                contentView.layer.borderColor = nil
            }
        }

        get { return super.isSelected }
    }
}
```

[Next](LucidDreams-DreamListViewControllerModel.swift.md)[Previous](LucidDreams-DecoratingLayout.swift.md)

