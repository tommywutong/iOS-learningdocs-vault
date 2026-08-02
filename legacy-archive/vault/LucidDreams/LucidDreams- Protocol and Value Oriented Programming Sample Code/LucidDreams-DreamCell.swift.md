---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreams_DreamCell_swift.html
archived_at: '2026-07-15T04:56:06.888753Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreams-InsetLayout.swift.md)[Previous](LucidDreams-Dream%2BDiff.swift.md)

# LucidDreams/DreamCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines a table view cell used in the `DreamListViewController` to
                display a summary of a dream. Note that this cell uses a `MultiPaneLayout` 
                to layout its content.
*/

import UIKit

/// A table view cell that displays a summary of a `Dream`.
class DreamCell: UITableViewCell {
    // MARK: Properties

    static let reuseIdentifier = "\(DreamCell.self)"

    var content = UILabel()
    var accessories = [UIImageView]()

    var dream: Dream! {
        didSet {
            // Update the UI when the `dream` changes.
            accessories = (0..<dream.numberOfCreatures).map { _ in
                let imageView = UIImageView(image: dream.creature.image)
                imageView.contentMode = .scaleAspectFit
                return imageView
            }
            content.text = dream.description
            for subview in contentView.subviews {
                subview.removeFromSuperview()
            }
            addSubviews()
            setNeedsLayout()
        }
    }

    // MARK: Initialization

    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)

        addSubviews()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("\(#function) has not been implemented")
    }

    // MARK: Layout

    private func addSubviews() {
        let multiPaneLayout = MultiPaneLayout(content: content, accessories: accessories)
        for view in multiPaneLayout.contents {
            contentView.addSubview(view)
        }
    }

    override func layoutSubviews() {
        super.layoutSubviews()

        /*
            This is the intersection between the UIKit view code and this sample's
            value based layout system.
        */
        var multiPaneLayout = MultiPaneLayout(content: content, accessories: accessories)
        multiPaneLayout.layout(in: contentView.bounds)
    }
}
```

[Next](LucidDreams-InsetLayout.swift.md)[Previous](LucidDreams-Dream%2BDiff.swift.md)

