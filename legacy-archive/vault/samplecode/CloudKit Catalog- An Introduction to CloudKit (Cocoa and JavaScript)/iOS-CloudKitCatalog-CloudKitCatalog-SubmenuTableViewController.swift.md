---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_SubmenuTableViewController_swift.html
archived_at: '2026-07-18T03:03:29.550256Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-NestedAttributeTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchUserRecordIDSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/SubmenuTableViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A SubmenuTableViewController displays a second-level menu for those code sample groups that have 
                more than one code sample.
*/

import UIKit

class SubmenuTableViewController: UITableViewController {

    // MARK: - Properties

    var codeSamples = [CodeSample]()
    var groupTitle: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        if let groupTitle = groupTitle {
            navigationItem.title = groupTitle
        }
        navigationItem.hidesBackButton = (navigationController!.viewControllers.first?.navigationItem.hidesBackButton)!
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return codeSamples.count
    }


    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let codeSample = codeSamples[indexPath.row]
        let cell = tableView.dequeueReusableCellWithIdentifier("SubmenuItem", forIndexPath: indexPath) as! SubmenuTableViewCell
        cell.submenuLabel.text = codeSample.title
        return cell
    }


    // MARK: - Navigation

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "ShowCodeSampleFromSubmenu" {
            let codeSampleViewController = segue.destinationViewController as! CodeSampleViewController
            if let selectedCell = sender as? SubmenuTableViewCell {
                let indexPath = tableView.indexPathForCell(selectedCell)!
                codeSampleViewController.selectedCodeSample = codeSamples[indexPath.row]

            }
        }
    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-NestedAttributeTableViewCell.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-FetchUserRecordIDSample.swift.md)

