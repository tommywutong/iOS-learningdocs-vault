---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewController_BaseViewController_swift.html
archived_at: '2026-07-18T03:14:29.909088Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewController-SelectSingleProperty.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-AppDelegate.swift.md)

# ManagingContactsUI/ContactPickerViewController/BaseViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A base view controller to share a data model and a table view between subclas-
  ses. Allows its subclasses to display selected contacts and properties.
*/

import UIKit

class BaseViewController: UIViewController {
    // MARK: - Properties

    /**
        Contains a tableview and a label. The label describes the content of the
        tableview. The table view displays the selected contacts or properties.
    */
    @IBOutlet var stackView: UIStackView!
    @IBOutlet var tableView: UITableView!

    /// Data model used by all BaseViewController subclasses.
    var data = [Section]()

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
        hideStackView(true)
    }

    // MARK: - Update UI

    /**
        Shows the stack view and refreshes the table view when they are selected
        contacts or properties. Hides it otherwise.
    */
    func hideStackView(_ status: Bool) {
        if status {
            data.removeAll()
            tableView.reloadData()
            stackView.isHidden = true
        } else {
            if !data.isEmpty {
                stackView.isHidden = false
                tableView.reloadData()
            }
        }
    }
}

/**
    Extends `BaseViewController` to conform to the ` UITableViewDataSource` and
    `UITableViewDelegate` protocols.
*/
extension BaseViewController: UITableViewDataSource, UITableViewDelegate {
    // MARK: - UITableViewDataSource

    func numberOfSections(in tableView: UITableView) -> Int {
        return data.count
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data[section].section.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return tableView.dequeueReusableCell(withIdentifier: AppConfiguration.TableViewCellIdentifiers.cell, for: indexPath)
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewController-SelectSingleProperty.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-AppDelegate.swift.md)

