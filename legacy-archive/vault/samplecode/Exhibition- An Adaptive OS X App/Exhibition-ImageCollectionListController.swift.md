---
title: 'Exhibition: An Adaptive OS X App'
apple_id: TP40016178
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Exhibition/Listings/Exhibition_ImageCollectionListController_swift.html
archived_at: '2026-07-18T03:08:00.795002Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Exhibition: An Adaptive OS X App](Exhibition-%20An%20Adaptive%20OS%20X%20App.md)


[Next](Exhibition-CenteringClipView.swift.md)[Previous](Exhibition-ImageToolsViewController.swift.md)

# Exhibition/ImageCollectionListController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains the `ImageCollectionListController` view controller subclass, which displays a list of `ImageCollection`s.
*/

import Cocoa

/**
    `ImageCollectionListController` displays a list of `ImageCollection`s in an
    `NSOutlineView`. It can be given a selection handler to report when an 
    `ImageCollection` is selected.
*/
class ImageCollectionListController: NSViewController, NSOutlineViewDataSource, NSOutlineViewDelegate {
    // MARK: Properties

    @IBOutlet var outlineView: NSOutlineView!

    override var nibName: String {
        return "ImageCollectionListController"
    }

    /// The identifier used for collection rows in the outline view
    static let collectionCellIdentifier = "DataCell"

    // MARK: Image Collection Management

    var imageCollectionSelectionHandler: (([ImageCollection]) -> Void)?

    var imageCollections = [ImageCollection]() {
        didSet {
            guard isViewLoaded else { return }

            reloadOutlineAndSelectFirstItemIfNecessary()
        }
    }

    // MARK: Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        reloadOutlineAndSelectFirstItemIfNecessary()
    }

    func reloadOutlineAndSelectFirstItemIfNecessary() {
        let oldSelection = outlineView.selectedRowIndexes

        outlineView.reloadData()

        if oldSelection.count == 0 {
            /*
                If the outline view didn't already have a selection, select the
                first `ImageCollection` (if one exists).
            */
            guard !imageCollections.isEmpty else { return }

            let firstIndexSet = IndexSet(integer: 0)

            outlineView.selectRowIndexes(firstIndexSet, byExtendingSelection: false)

            /*
                Programmatically changing the selection doesn't send a notification (it only
                happens when the user changes it). So, explicitly handle the new selection.
            */
            handleSelectionChanged()
        }
        else {
            // If there was an old selection, restore that old selection.
            outlineView.selectRowIndexes(oldSelection, byExtendingSelection: false)
        }
    }

    // MARK: OutlineView Data Source / Delegate

    func outlineView(_ outlineView: NSOutlineView, child index: Int, ofItem item: Any?) -> Any {
        return imageCollections[index]
    }

    func outlineView(_ outlineView: NSOutlineView, numberOfChildrenOfItem item: Any?) -> Int {
        // The root item has each collection as its children.
        if item == nil {
            return imageCollections.count
        }

        return 0
    }

    func outlineView(_ outlineView: NSOutlineView, viewFor tableColumn: NSTableColumn?, item: Any) -> NSView? {
        guard let collection = item as? ImageCollection else { return nil }

        let view = outlineView.make(withIdentifier: ImageCollectionListController.collectionCellIdentifier, owner: self) as! NSTableCellView

        view.textField?.stringValue = collection.name
        view.imageView?.image = collection.tableViewIcon

        /*
            Turn on `translatesAutoresizingMaskIntoConstraints` so the outline view
            can manage the size and position of the views, specifically when the
            'Sidebar Icon Size' changes. With this on, the source nib must not be
            adding any runtime constraints to these views.
        */
        view.textField?.translatesAutoresizingMaskIntoConstraints = true
        view.imageView?.translatesAutoresizingMaskIntoConstraints = true

        return view
    }

    func outlineView(_ outlineView: NSOutlineView, isItemExpandable item: Any) -> Bool {
        return false
    }

    func outlineView(_ outlineView: NSOutlineView, isGroupItem item: Any) -> Bool {
        return false
    }

    func outlineView(_ outlineView: NSOutlineView, shouldSelectItem item: Any) -> Bool {
        return item is ImageCollection
    }

    func outlineViewSelectionDidChange(_ notification: Notification) {
        guard outlineView == notification.object as? NSOutlineView else { return }

        handleSelectionChanged()
    }

    fileprivate func handleSelectionChanged() {
        guard let imageCollectionSelectionHandler = imageCollectionSelectionHandler else { return }

        let selectedRows = outlineView.selectedRowIndexes

        // Of the selected rows, get the ones that represent an `ImageCollection`.
        let imageCollections = selectedRows.flatMap { row in
            /*
                If the row doesn't represent an image collection, the result will
                be filtered out.
            */
            return outlineView.item(atRow: row) as? ImageCollection
        }

        imageCollectionSelectionHandler(imageCollections)
    }

    // MARK: IBActions

    @IBAction func showOpenPanelToAddImageCollection(_ sender: AnyObject?) {
        /// Show an `NSOpenPanel` to select a directory to create an `ImageCollection`.
        let openPanel = NSOpenPanel()
        openPanel.canChooseDirectories = true
        openPanel.canChooseFiles = false

        func modalCompletionHandler(_ modalResponse: NSModalResponse) {
            // Check that the response was OK, rather than Cancel.
            if modalResponse == NSFileHandlingPanelOKButton {
                /*
                    For every URL selected, create an `ImageCollection` and add
                    that to the list of displayed collections.
                */
                imageCollections += openPanel.urls.map { ImageCollection(rootURL: $0) }
            }
        }

        if let sheetParent = view.window {
            openPanel.beginSheetModal(for: sheetParent, completionHandler: modalCompletionHandler)
        }
        else {
            openPanel.begin(completionHandler: modalCompletionHandler)
        }
    }
}
```

[Next](Exhibition-CenteringClipView.swift.md)[Previous](Exhibition-ImageToolsViewController.swift.md)

