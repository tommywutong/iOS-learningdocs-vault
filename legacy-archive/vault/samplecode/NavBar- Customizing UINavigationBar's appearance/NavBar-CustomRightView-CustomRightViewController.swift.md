---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_CustomRightView_CustomRightViewController_swift.html
archived_at: '2026-07-18T03:16:53.096498Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-CustomBackButton-CustomBackButtonViewController.m.md)[Previous](NavBar-MainViewController.swift.md)

# NavBar/CustomRightView/CustomRightViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates configuring various types of controls as the right
  bar item of the navigation bar.
 */

import UIKit

class CustomRightViewController: UIViewController {

    struct SegmentedControl {
        static let textButton = 0
        static let imageButton = 1
        static let controlButton = 2
    }

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        return .portrait
    }

    /**
     *  IBAction for the segemented control.
     */
    @IBAction func changeRightBarItem(_ sender: UISegmentedControl) {
        switch sender.selectedSegmentIndex {
        case SegmentedControl.textButton:
            // Add a custom add button as the nav bar's custom right view
            let addButton = UIBarButtonItem(title: NSLocalizedString("AddTitle", comment: ""),
                                            style: .plain,
                                            target: self,
                                            action: #selector(action(_:)))
            navigationItem.rightBarButtonItem = addButton

        case SegmentedControl.imageButton:
            // add our custom image button as the nav bar's custom right view
            let emailButton = UIBarButtonItem(image: #imageLiteral(resourceName: "Email"),
                                              style: .plain,
                                              target: self,
                                              action: #selector(action(_:)))
            navigationItem.rightBarButtonItem = emailButton

        case SegmentedControl.controlButton:
            // "Segmented" control to the right
            let segmentedControl = UISegmentedControl(items: [
                #imageLiteral(resourceName: "UpArrow"),
                #imageLiteral(resourceName: "DownArrow")
            ])

            segmentedControl.addTarget(self, action: #selector(action), for: .valueChanged)
            segmentedControl.frame = CGRect(x: 0, y: 0, width: 90, height: 30)
            segmentedControl.isMomentary = true

            let segmentBarItem = UIBarButtonItem(customView: segmentedControl)
            navigationItem.rightBarButtonItem = segmentBarItem

        default:
            break
        }
    }

    // MARK: - Actions

    /**
     *  IBAction for the various bar button items shown in this example.
     */
    @IBAction func action(_ sender: AnyObject) {
        print("CustomRightViewController IBAction invoked!")
    }
}
```

[Next](NavBar-CustomBackButton-CustomBackButtonViewController.m.md)[Previous](NavBar-MainViewController.swift.md)

