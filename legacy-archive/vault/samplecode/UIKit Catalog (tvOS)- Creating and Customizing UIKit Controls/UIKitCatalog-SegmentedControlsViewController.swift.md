---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_SegmentedControlsViewController_swift.html
archived_at: '2026-07-18T03:27:29.367121Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-DataItemCollectionViewCell.swift.md)[Previous](UIKitCatalog-DataItem%2BSampleData.swift.md)

# UIKitCatalog/SegmentedControlsViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that demonstrates how to use `UISegmentedControl`.
*/

import UIKit

class SegmentedControlsViewController: UIViewController {
    // MARK: Properties

    @IBOutlet weak var plainSegmentedControl: UISegmentedControl!

    @IBOutlet weak var customBackgroundSegmentedControl: UISegmentedControl!

    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        return [plainSegmentedControl]
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        configureCustomBackgroundSegmentedControl()
    }

    private func configureCustomBackgroundSegmentedControl() {
        // Set the background images for each control state.
        let normalSegmentBackgroundImage = UIImage(named: "stepper_and_segment_background")
        customBackgroundSegmentedControl.setBackgroundImage(normalSegmentBackgroundImage, for: UIControlState(), barMetrics: .default)

        let disabledSegmentBackgroundImage = UIImage(named: "stepper_and_segment_background_disabled")
        customBackgroundSegmentedControl.setBackgroundImage(disabledSegmentBackgroundImage, for: .disabled, barMetrics: .default)

        let highlightedSegmentBackgroundImage = UIImage(named: "stepper_and_segment_background_highlighted")
        customBackgroundSegmentedControl.setBackgroundImage(highlightedSegmentBackgroundImage, for: .highlighted, barMetrics: .default)

        // Set the divider image.
        let segmentDividerImage = UIImage(named: "stepper_and_segment_divider")
        customBackgroundSegmentedControl.setDividerImage(segmentDividerImage, forLeftSegmentState: UIControlState(), rightSegmentState: UIControlState(), barMetrics: .default)

        // Create a font to use for the attributed title (both normal and highlighted states).
        let captionFontDescriptor = UIFontDescriptor.preferredFontDescriptor(withTextStyle: UIFontTextStyle.caption1)
        let font = UIFont(descriptor: captionFontDescriptor, size: 0)

        let normalTextAttributes = [
            NSForegroundColorAttributeName: UIColor.purple,
            NSFontAttributeName: font
        ]
        customBackgroundSegmentedControl.setTitleTextAttributes(normalTextAttributes, for: UIControlState())

        let highlightedTextAttributes = [
            NSForegroundColorAttributeName: UIColor.purple,
            NSFontAttributeName: font
        ]
        customBackgroundSegmentedControl.setTitleTextAttributes(highlightedTextAttributes, for: .highlighted)
    }
}
```

[Next](UIKitCatalog-DataItemCollectionViewCell.swift.md)[Previous](UIKitCatalog-DataItem%2BSampleData.swift.md)

