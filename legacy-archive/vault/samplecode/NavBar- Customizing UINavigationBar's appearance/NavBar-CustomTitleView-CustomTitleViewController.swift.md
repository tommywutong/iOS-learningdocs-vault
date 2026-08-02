---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_CustomTitleView_CustomTitleViewController_swift.html
archived_at: '2026-07-18T03:16:53.167044Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-LargeTitle-LargeTitleViewController.swift.md)[Previous](LICENSE.txt.md)

# NavBar/CustomTitleView/CustomTitleViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates configuring the navigation bar to use a UIView
  as the title.
 */

import UIKit

class CustomTitleViewController: UIViewController {

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        return .portrait
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        let segmentTextContent = [
            NSLocalizedString("Image", comment: ""),
            NSLocalizedString("Text", comment: ""),
            NSLocalizedString("Video", comment: "")
        ]

        // Segmented control as the custom title view
        let segmentedControl = UISegmentedControl(items: segmentTextContent)
        segmentedControl.selectedSegmentIndex = 0
        segmentedControl.autoresizingMask = .flexibleWidth
        segmentedControl.frame = CGRect(x: 0, y: 0, width: 400, height: 30)
        segmentedControl.addTarget(self, action: #selector(action(_:)), for: .valueChanged)

        self.navigationItem.titleView = segmentedControl
    }

    // MARK: - Actions

    /**
     *  IBAction for the segmented control.
     */
    @IBAction func action(_ sender: AnyObject) {
        print("CustomTitleViewController IBAction invoked!")
    }
}
```

[Next](NavBar-LargeTitle-LargeTitleViewController.swift.md)[Previous](LICENSE.txt.md)

