---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_AlertsViewController_swift.html
archived_at: '2026-07-18T03:27:28.202082Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-CollectionViewContainerViewController.swift.md)[Previous](UIKitCatalog-DataItem.swift.md)

# UIKitCatalog/AlertsViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that demonstrates how to use `UIAlertController`.
*/

import UIKit

class AlertsViewController: UIViewController {
    // MARK: IB Actions

    /// Show a simple alert with a single "OK" button.
    @IBAction func showSimpleAlert(_: AnyObject) {
        let title = NSLocalizedString("A Short Title is Best", comment: "")
        let message = NSLocalizedString("A message should be a short, complete sentence.", comment: "")
        let acceptButtonTitle = NSLocalizedString("OK", comment: "")

        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)

        // Create the action.
        let acceptAction = UIAlertAction(title: acceptButtonTitle, style: .default) { _ in
            print("The simple alert's accept action occurred.")
        }

        // Add the action.
        alertController.addAction(acceptAction)

        present(alertController, animated: true, completion: nil)
    }

    /// Shows an alert with "OK" and "Cancel" buttons.
    @IBAction func showOKCancelAlert(_: AnyObject) {
        let title = NSLocalizedString("A Short Title is Best", comment: "")
        let message = NSLocalizedString("A message should be a short, complete sentence.", comment: "")
        let acceptButtonTitle = NSLocalizedString("OK", comment: "")
        let cancelButtonTitle = NSLocalizedString("Cancel", comment: "")

        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)

        // Create the actions.
        let acceptAction = UIAlertAction(title: acceptButtonTitle, style: .default) { _ in
            print("The \"OK/Cancel\" alert's other action occurred.")
        }

        let cancelAction = UIAlertAction(title: cancelButtonTitle, style: .cancel) { _ in
            print("The \"OK/Cancel\" alert's cancel action occurred.")
        }

        // Add the actions.
        alertController.addAction(acceptAction)
        alertController.addAction(cancelAction)

        present(alertController, animated: true, completion: nil)
    }

    /// Show an alert with "Delete" and "Cancel" buttons.
    @IBAction func showDestructiveAlert(_: AnyObject) {
        let title = NSLocalizedString("A Short Title is Best", comment: "")
        let message = NSLocalizedString("A message should be a short, complete sentence.", comment: "")
        let cancelButtonTitle = NSLocalizedString("Cancel", comment: "")
        let deleteButtonTitle = NSLocalizedString("Delete", comment: "")

        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)

        // Create the actions.
        let cancelAction = UIAlertAction(title: cancelButtonTitle, style: .cancel) { _ in
            print("The \"Other\" alert's cancel action occurred.")
        }

        let deleteAction = UIAlertAction(title: deleteButtonTitle, style: .destructive) { _ in
            print("The \"Other\" alert's other button one action occurred.")
        }

        // Add the actions.
        alertController.addAction(cancelAction)
        alertController.addAction(deleteAction)

        present(alertController, animated: true, completion: nil)
    }
}
```

[Next](UIKitCatalog-CollectionViewContainerViewController.swift.md)[Previous](UIKitCatalog-DataItem.swift.md)

