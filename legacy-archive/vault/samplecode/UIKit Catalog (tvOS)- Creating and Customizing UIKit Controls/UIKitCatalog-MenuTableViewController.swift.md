---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_MenuTableViewController_swift.html
archived_at: '2026-07-18T03:27:29.129869Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-DataItemViewController.swift.md)[Previous](UIKitCatalog-DataItemCellComposer.swift.md)

# UIKitCatalog/MenuTableViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UITableViewController` that, when subclassed, is used as the master view of `MenuSplitViewController` instances. Each subclass specifies a mapping of segue names to perform for each static cell in its storyboard instance.
*/

import UIKit

class MenuTableViewController: UITableViewController {
    // MARK: Properties

    /**
        A matrix of segue identifiers that should be performed when a cell
        becomes focused.

        Overridden by subclasses.
    */
    var segueIdentifierMap: [[String]] {
        return [[]]
    }

    private var lastPerformedSegueIdentifier: String?

    private let delayedSeguesOperationQueue = OperationQueue()

    private static let performSegueDelay: TimeInterval = 0.1

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        /*
            Set `remembersLastFocusedIndexPath` to `true` to ensure the same row
            becomes focused whenever focus is returned to the table view.
        */
        tableView.remembersLastFocusedIndexPath = true

        /*
            Adjust the layout margins of the `tableView` to add a horizontal inset
            to the cells. This will allow for overscan on older TVs and space for
            the focus effect.
        */
        tableView.layoutMargins.left = 90
        tableView.layoutMargins.right = 20
    }

    override func shouldPerformSegue(withIdentifier identifier: String, sender: Any?) -> Bool {
        // Check if the requested segue is a segue contained in our mapping.
        guard segueIdentifierMap.contains(where: { $0.contains(identifier) }) else { return true }

        // Don't perform the segue if it's the same as the last performed segue.
        return identifier != lastPerformedSegueIdentifier
    }

    // MARK: UITableViewDelegate

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        guard let menuSplitViewController = splitViewController as? MenuSplitViewController else { return }

        /*
            Ask the containing `MenuSplitViewController` to move the focus to the
            current detail view controller.
        */
        menuSplitViewController.updateFocusToDetailViewController()
    }

    override func tableView(_ tableView: UITableView, didUpdateFocusIn context: UITableViewFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator) {
        // Check that the next focus view is a child of the table view.
        guard let nextFocusedView = context.nextFocusedView, nextFocusedView.isDescendant(of: tableView) else { return }
        guard let indexPath = context.nextFocusedIndexPath else { return }

        // Cancel any previously queued segues.
        delayedSeguesOperationQueue.cancelAllOperations()

        // Create a `BlockOperation` to perform the detail segue after a delay.
        let performSegueOperation = BlockOperation()
        let segueIdentifier = segueIdentifierMap[indexPath.section][indexPath.row]

        performSegueOperation.addExecutionBlock { [weak self, unowned performSegueOperation] in
            // Pause the block so the segue isn't immediately performed.
            Thread.sleep(forTimeInterval: MenuTableViewController.performSegueDelay)

            /*
                Check that the operation wasn't cancelled and that the segue identifier
                is different to the last performed segue identifier.
            */
            guard !performSegueOperation.isCancelled && segueIdentifier != self?.lastPerformedSegueIdentifier else { return }

            OperationQueue.main.addOperation {
                // Perform the segue to show the detail view controller.
                self?.performSegue(withIdentifier: segueIdentifier, sender: nextFocusedView)

                // Record the last performed segue identifier.
                self?.lastPerformedSegueIdentifier = segueIdentifier

                /*
                    Select the focused cell so that the table view visibly reflects
                    which detail view is being shown.
                */
                self?.tableView.selectRow(at: indexPath, animated: true, scrollPosition: .none)
            }
        }

        delayedSeguesOperationQueue.addOperation(performSegueOperation)
    }
}
```

[Next](UIKitCatalog-DataItemViewController.swift.md)[Previous](UIKitCatalog-DataItemCellComposer.swift.md)

