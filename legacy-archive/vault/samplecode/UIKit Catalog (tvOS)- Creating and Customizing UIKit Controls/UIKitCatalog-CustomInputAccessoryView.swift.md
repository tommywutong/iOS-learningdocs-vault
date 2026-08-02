---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_CustomInputAccessoryView_swift.html
archived_at: '2026-07-18T03:27:28.573378Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-VideoPlayerViewController.swift.md)[Previous](UIKitCatalog-DataItemCollectionViewCell.swift.md)

# UIKitCatalog/CustomInputAccessoryView.swift

```
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UIView` subclass that is used to add a custom title to the text input screens for `UITextField`s.
*/

import UIKit

class CustomInputAccessoryView: UIView {
    // MARK: Properties

    let titleLabel = UILabel(frame: CGRect.zero)

    // MARK: Initialization

    init(title: String) {
        /*
            Call the designated initializer with an inital zero frame. The final
            frame will be determined by the layout constraints added later.
        */
        super.init(frame: CGRect.zero)

        // Setup the label and add it to the view.
        titleLabel.font = UIFont.systemFont(ofSize: 60, weight: UIFontWeightMedium)
        titleLabel.text = title

        addSubview(titleLabel)

        /*
            Turn off automatic transaltion of resizing masks into constraints as
            we'll be specifying our own layout constraints.
        */
        translatesAutoresizingMaskIntoConstraints = false
        titleLabel.translatesAutoresizingMaskIntoConstraints = false

        /*
            Add layout constraints to the label that specifies it must fill the
            containing view with an additional 60pts of bottom padding.
        */
        let viewsDictionary = ["titleLabel": titleLabel]
        addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "H:|-[titleLabel]-|", options: [], metrics: nil, views: viewsDictionary))
        addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:|-[titleLabel]-60-|", options: [], metrics: nil, views: viewsDictionary))
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented.")
    }
}
```

[Next](UIKitCatalog-VideoPlayerViewController.swift.md)[Previous](UIKitCatalog-DataItemCollectionViewCell.swift.md)

