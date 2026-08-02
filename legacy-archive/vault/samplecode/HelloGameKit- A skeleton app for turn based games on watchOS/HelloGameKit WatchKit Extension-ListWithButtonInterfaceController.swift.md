---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_ListWithButtonInterfaceController_swift.html
archived_at: '2026-07-18T03:11:48.914834Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-PlayersInterfaceController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ExtensionDelegate.swift.md)

# HelloGameKit WatchKit Extension/ListWithButtonInterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Base class for rendering our two table based interfaces (PlayersInterfaceController and MatchesInterfaceController).  To use this you adopt ListDataSource to load the items and return a button title.  Whatever items you wish to display should adopt the protocol ListItem (see PlayersInterfaceController and MatchesInterfaceController for examples)
 */

import WatchKit
import Foundation

@objc protocol ListItem {
    var title: String { get }
    var detail: String { get }
}

@objc protocol ListItemRowController {
    func setRepresentedItem(_ item: ListItem)
}

@objc protocol ListDataSource {
    func buttonTitle() -> String
    func loadItems(completionHandler: @escaping (([ListItem]) -> Swift.Void))
}

enum LoadingState {
    case initial
    case loading
    case failed
    case complete
    case exiting
}

class ListWithButtonInterfaceController: WKInterfaceController {
    // MARK: Properties

    var dataSource: ListDataSource?
    var presentingController: InterfaceController?

    private var _items = [ListItem]()
    var buttonRow: ButtonRowController? {
        return self.table.rowController(at: 0) as? ButtonRowController
    }

    var items: [ListItem] {
        get {
            return _items
        }

        set {
            _items = newValue
        }
    }

    private var _loadingState: LoadingState = .initial
    var loadingState: LoadingState {
        get {
            return _loadingState
        }

        set {
            _loadingState = newValue
            self.updateUI()
        }
    }

    // MARK: IB Outlets

    @IBOutlet weak var table: WKInterfaceTable!
    @IBOutlet weak var statusLabel: WKInterfaceLabel!

    // MARK: WKInterfaceController
    override func awake(withContext context: Any?) {
        print("***** awake")
        super.awake(withContext: context)
        presentingController = context as? InterfaceController
        table?.setRowTypes(["buttonRow"])

        if let buttonController = table?.rowController(at: 0) as? ButtonRowController {
            let buttonLabel = buttonController.buttonLabel!
            let buttonTitle = dataSource!.buttonTitle()
            buttonLabel.setText(buttonTitle)
        }
    }

    override func willActivate() {
        // This method is called when watch view controller is about to be visible to user
        super.willActivate()
        self.dataSource?.loadItems() { [unowned self] items in
            self.items = items
            self.itemsDidLoad()
        }
    }

    override func didDeactivate() {
        // This method is called when watch view controller is no longer visible
        super.didDeactivate()
    }

    func itemsDidLoad() {
        guard let table = table else { return }
        var rowTypes = ["buttonRow"]
        for _ in items {
            rowTypes.append("itemRow")
        }
        table.setRowTypes(rowTypes)

        if let buttonController = table.rowController(at: 0) as? ButtonRowController {
            let buttonLabel = buttonController.buttonLabel!
            let buttonTitle = dataSource!.buttonTitle()
            buttonLabel.setText(buttonTitle)
        }

        let count = items.count
        if count > 0 {
            for index in 1...count {
                let item = items[index-1]
                if let rowController = table.rowController(at: index) as? TitleWithDetailRowController {
                    let titleLabel = rowController.titleLabel!
                    titleLabel.setText(item.title)
                    let detailLabel = rowController.detailLabel!
                    detailLabel.setText(item.detail)
                }
            }
        }
    }

    // MARK: WKInterfaceTable

    override func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int) {
        var item: ListItem? = nil
        if rowIndex > 0 {
            item = items[rowIndex - 1]
        }
        didSelect(item: item)
    }

    // MARK: UI Refresh

    func updateUI() {
        switch loadingState {
            case .initial, .loading:
                statusLabel?.setText("Loading")
                statusLabel?.setHidden(false)
                table?.setHidden(true)

            case .failed:
                statusLabel?.setText("Failed to load items")
                statusLabel?.setHidden(false)
                table?.setHidden(true)

            case .complete:
                statusLabel?.setHidden(true)
                itemsDidLoad()
                table?.setHidden(false)

            case .exiting:
                statusLabel?.setText("Starting")
                statusLabel?.setHidden(true)
                table?.setHidden(false)
        }
    }

    // MARK: Subclass Interface

    func didSelect(item: ListItem?) {
        fatalError("Must be implemented by a subclass.")
    }
}
```

[Next](HelloGameKit%20WatchKit%20Extension-PlayersInterfaceController.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-ExtensionDelegate.swift.md)

