---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_ExtendedNavBar_ExtendedNavBarViewController_swift.html
archived_at: '2026-07-18T03:16:53.211773Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-ExtendedNavBar-ExtendedNavBarView.swift.md)[Previous](NavBar-AppDelegate.swift.md)

# NavBar/ExtendedNavBar/ExtendedNavBarViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates vertically extending the navigation bar.
 */

import UIKit

class ExtendedNavBarViewController: UITableViewController {

    /// Our data source is an array of city names, populated from Cities.json.
    let dataSource = CitiesDataSource()

    override func viewDidLoad() {
        super.viewDidLoad()

        tableView.dataSource = dataSource

        // For the extended navigation bar effect to work, a few changes
        // must be made to the actual navigation bar.  Some of these changes could
        // be applied in the storyboard but are made in code for clarity.

        // Translucency of the navigation bar is disabled so that it matches with
        // the non-translucent background of the extension view.
        navigationController!.navigationBar.isTranslucent = false

        // The navigation bar's shadowImage is set to a transparent image.  In
        // addition to providing a custom background image, this removes
        // the grey hairline at the bottom of the navigation bar.  The
        // ExtendedNavBarView will draw its own hairline.
        navigationController!.navigationBar.shadowImage = UIImage(named: "TransparentPixel")
        // "Pixel" is a solid white 1x1 image.
        //navigationController!.navigationBar.setBackgroundImage(#imageLiteral(resourceName: "Pixel"), for: .default)
    }
}
```

[Next](NavBar-ExtendedNavBar-ExtendedNavBarView.swift.md)[Previous](NavBar-AppDelegate.swift.md)

