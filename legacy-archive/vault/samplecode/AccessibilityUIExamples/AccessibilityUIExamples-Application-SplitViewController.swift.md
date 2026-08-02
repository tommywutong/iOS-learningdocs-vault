---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Application_SplitViewController_swift.html
archived_at: '2026-07-18T03:00:35.098595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsViewController.swift.md)[Previous](AccessibilityUIExamples-Application-Example.swift.md)

# AccessibilityUIExamples/Application/SplitViewController.swift

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
This sample's split view managing both the master and detail view controllers.
*/

import Cocoa

class SplitViewController: NSSplitViewController, MasterViewControllerDelegate {

    var masterViewController: MasterViewController!
    var detailViewController: DetailViewController!

    // MARK: - View Controller Lifecycle

    override func viewDidLoad() {
        super.viewDidLoad()

        // Note: we keep the left split view item from growing as the window grows by setting its hugging priority to 200,
        // and the right to 199. The view with the lowest priority will be the first to take on additional width if the
        // split view grows or shrinks.
        //
        splitView.adjustSubviews()

        masterViewController = splitViewItems[0].viewController as? MasterViewController
        masterViewController.delegate = self   // Listen for table view selection changes

        if let detailViewController = splitViewItems[1].viewController as? DetailViewController {
            self.detailViewController = detailViewController
        } else {
            fatalError("SplitViewController is not configured correctly.")
        }

        splitView.autosaveName = NSSplitView.AutosaveName(rawValue: "SplitViewAutoSave")   // Remember the split view position.
    }

    // MARK: - MasterViewControllerDelegate

    func didChangeExampleSelection(masterViewController: MasterViewController, selection: Example?) {
        detailViewController.detailItemRecord = selection
    }
}
```

[Next](AccessibilityUIExamples-RadioButtons-CustomRadioButtonsViewController.swift.md)[Previous](AccessibilityUIExamples-Application-Example.swift.md)

