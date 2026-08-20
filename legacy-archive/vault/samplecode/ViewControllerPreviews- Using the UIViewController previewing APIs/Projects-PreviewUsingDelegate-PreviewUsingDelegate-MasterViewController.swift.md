---
title: 'ViewControllerPreviews: Using the UIViewController previewing APIs'
apple_id: TP40016546
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ViewControllerPreviews/Listings/Projects_PreviewUsingDelegate_PreviewUsingDelegate_MasterViewController_swift.html
archived_at: '2026-07-18T03:27:57.426108Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewControllerPreviews: Using the UIViewController previewing APIs](ViewControllerPreviews-%20Using%20the%20UIViewController%20previewing%20APIs.md)


[Next](Projects-PreviewUsingDelegate-PreviewUsingDelegate-MasterViewController%2BUIViewCo.md)[Previous](Projects-PreviewUsingDelegate-PreviewUsingDelegate-DetailViewController.swift.md)

# Projects/PreviewUsingDelegate/PreviewUsingDelegate/MasterViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The master view controller.
*/

import UIKit

class MasterViewController: UITableViewController {
    // MARK: Types 

    /// A simple data structure to populate the table view.
    struct PreviewDetail {
        let title: String
        let preferredHeight: Double
    }

    // MARK: Properties

    let sampleData = [
        PreviewDetail(title: "Small", preferredHeight: 160.0),
        PreviewDetail(title: "Medium", preferredHeight: 320.0),
        PreviewDetail(title: "Large", preferredHeight: 0.0) // 0.0 to get the default height.
    ]

    /// An alert controller used to notify the user if 3D touch is not available.
    var alertController: UIAlertController?

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        // Check for force touch feature, and add force touch/previewing capability.
        if traitCollection.forceTouchCapability == .available {
            /*  
                Register for `UIViewControllerPreviewingDelegate` to enable
                "Peek" and "Pop".
                (see: MasterViewController+UIViewControllerPreviewing.swift)

                The view controller will be automatically unregistered when it is
                deallocated.
            */
            registerForPreviewing(with: self, sourceView: view)
        }
        else {
            // Create an alert to display to the user.
            alertController = UIAlertController(title: "3D Touch Not Available", message: "Unsupported device.", preferredStyle: .alert)
        }
    }

    override func viewWillAppear(_ animated: Bool) {
        // Clear the selection if the split view is only showing one view controller.
        clearsSelectionOnViewWillAppear = splitViewController!.isCollapsed

        super.viewWillAppear(animated)
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        // Present the alert if necessary.
        if let alertController = alertController {
            alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            present(alertController, animated: true, completion: nil)

            // Clear the `alertController` to ensure it's not presented multiple times.
            self.alertController = nil
        }
    }

    // MARK: UIStoryboardSegue Handling

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        super.prepare(for: segue, sender: sender)

        if segue.identifier == "showDetail", let indexPath = tableView.indexPathForSelectedRow {
            let previewDetail = sampleData[(indexPath as NSIndexPath).row]

            let detailViewController = (segue.destination as! UINavigationController).topViewController as! DetailViewController

            // Pass the `title` to the `detailViewController`.
            detailViewController.sampleTitle = previewDetail.title
        }
    }

    // MARK: Table View

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of items in the sample data structure.
        return sampleData.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)

        let previewDetail = sampleData[(indexPath as NSIndexPath).row]
        cell.textLabel!.text = previewDetail.title

        return cell
    }
}
```

[Next](Projects-PreviewUsingDelegate-PreviewUsingDelegate-MasterViewController%2BUIViewCo.md)[Previous](Projects-PreviewUsingDelegate-PreviewUsingDelegate-DetailViewController.swift.md)

