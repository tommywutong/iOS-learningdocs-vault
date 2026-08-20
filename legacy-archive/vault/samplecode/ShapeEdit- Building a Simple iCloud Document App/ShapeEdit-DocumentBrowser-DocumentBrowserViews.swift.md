---
title: 'ShapeEdit: Building a Simple iCloud Document App'
apple_id: TP40016100
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ShapeEdit/Listings/ShapeEdit_DocumentBrowser_DocumentBrowserViews_swift.html
archived_at: '2026-07-18T03:23:43.449650Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ShapeEdit: Building a Simple iCloud Document App](ShapeEdit-%20Building%20a%20Simple%20iCloud%20Document%20App.md)


[Next](ShapeEdit-DocumentBrowser-DocumentBrowserQuery.swift.md)[Previous](ShapeEdit-AppDelegate.swift.md)

# ShapeEdit/DocumentBrowser/DocumentBrowserViews.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains simple cell elements for display in our UICollectionViewController
*/

import UIKit

/**
    The `DocumentCell` class reflects the content of one document in our collection
    view. It manages an image view to display the thumbnail as well as two labels
    for the display name and container name (for external documents) of the document
    respectively.
*/
class DocumentCell: UICollectionViewCell {
    // MARK: - Properties

    @IBOutlet var imageView: UIImageView!
    @IBOutlet var label: UILabel!
    @IBOutlet var subtitleLabel: UILabel!

    var thumbnail: UIImage? {
        didSet {
            imageView.image = thumbnail
            contentView.backgroundColor = thumbnail != nil ? UIColor.whiteColor() : UIColor.lightGrayColor()
        }
    }

    var title = "" {
        didSet {
            label.text = title
        }
    }

    var subtitle = "" {
        didSet {
            subtitleLabel.text = subtitle
        }
    }

    // MARK: - Overrides

    override func prepareForReuse() {
        title = ""
        subtitle = ""
        thumbnail = nil
    }
}


/**
    The `HeaderView` class is a simple view for displaying our section headers in
    the collection view.
*/
class HeaderView : UICollectionReusableView {
    @IBOutlet var label: UILabel!

    var title = "" {
        didSet {
            label.text = title
        }
    }

    override func prepareForReuse() {
        title = ""
    }
}
```

[Next](ShapeEdit-DocumentBrowser-DocumentBrowserQuery.swift.md)[Previous](ShapeEdit-AppDelegate.swift.md)

