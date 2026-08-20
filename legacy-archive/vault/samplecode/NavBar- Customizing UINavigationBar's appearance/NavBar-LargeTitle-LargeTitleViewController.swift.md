---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_LargeTitle_LargeTitleViewController_swift.html
archived_at: '2026-07-18T03:16:53.293984Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-CustomAppearance-CustomAppearanceViewController.swift.md)[Previous](NavBar-CustomTitleView-CustomTitleViewController.swift.md)

# NavBar/LargeTitle/LargeTitleViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates applying a large title to the UINavigationBar.
 */

import UIKit

class LargeTitleViewController: UITableViewController {

    /// Our data source is an array of city names, populated from Cities.json.
    let dataSource = CitiesDataSource()

    override func viewDidLoad() {
        super.viewDidLoad()

        tableView.dataSource = dataSource

        if #available(iOS 11.0, *) {
            self.navigationController?.navigationBar.prefersLargeTitles = true
        }
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "pushSeque" {
            // This segue is pushing a detailed view controller.
            if let indexPath = self.tableView.indexPathForSelectedRow {
                segue.destination.title = dataSource.city(index: indexPath.row)
            }
            if #available(iOS 11.0, *) {
                // We choose not to have a large title for the destination view controller.
                segue.destination.navigationItem.largeTitleDisplayMode = .never
            }
        } else {
            // This segue is popping us back up the navigation stack.
        }
    }

}
```

[Next](NavBar-CustomAppearance-CustomAppearanceViewController.swift.md)[Previous](NavBar-CustomTitleView-CustomTitleViewController.swift.md)

