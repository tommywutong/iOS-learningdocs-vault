---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_BaseViewController_swift.html
archived_at: '2026-07-18T03:14:27.521857Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-TextFieldCell.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCHelperClass.swift.md)

# ManagingContacts/ManagingContacts/BaseViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A base table view controller to share a data model and a table view 
                cell prototype between subclasses. Allows its subclasses to display 
                container, contact, and group information.
*/

import UIKit

class BaseViewController: UITableViewController {
    // MARK: - Types

    fileprivate struct MainStoryboard {
        struct TableViewCellIdentifiers {
            // Cell Identifier used by all subclasses.
            static let cellIdentifier = "cellID"
        }
    }


    // MARK: - Properties

    /// Data model used by all BaseViewController subclasses.
    var data: [MGCModel] = [MGCModel]() {
        didSet {
            tableView.reloadData()
        }
    }


    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }


    // MARK: - UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        // Return the number of sections.
        return data.count
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return data[section].content.count
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
       return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellIdentifier, for: indexPath)
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let segue = data[indexPath.section].segue, let relatedSegue = segue.related {
            performSegue(withIdentifier: relatedSegue, sender: self)
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-TextFieldCell.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCHelperClass.swift.md)

