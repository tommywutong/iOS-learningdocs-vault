---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MenuViewController_swift.html
archived_at: '2026-07-18T03:14:29.012649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-ContactsMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-ContainersMenu.swift.md)

# ManagingContacts/ManagingContacts/MenuViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A base table view controller to share a data model and a table view
                cell prototype between subclasses.
                Allows its subclasses to display the navigation menu for each tab.
*/

import UIKit
import Contacts

class MenuViewController: UITableViewController {
    // MARK: - Types

    struct MainStoryboard {
        struct TableViewCellIdentifiers {
            // Cell Identifier used by all subclasses.
            static let cellIdentifier = "cellID"
        }
    }


    // MARK: - Properties

    var menuContactStoreUtilities = MGCContactStoreUtilities()

    /// Data model used by all MenuViewController subclasses.
    var navigationMenuContent: [MGCMenuSection] = [MGCMenuSection]() {
        didSet {
            tableView.reloadData()
        }
    }


    // MARK: - Initialization

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        // Register for TabBarViewController's refresh tab notifications.
        NotificationCenter.default.addObserver(forName: NSNotification.Name(rawValue: MGCAppConfiguration.MGCNotifications.refreshTab), object: nil, queue: OperationQueue.main) {[unowned self] (note: Notification) in
                                                                                                                                                                                        self.handleRefreshTabNotification(note)
                                                                                                                                                                                 }
    }


    // MARK: - Handle refreshTabNotification 

    func handleRefreshTabNotification(_ notification: Notification) {
    }


    // MARK: - UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        // Return the number of sections.
        return navigationMenuContent.count
    }



    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return navigationMenuContent[section].section.count
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellIdentifier, for: indexPath)
    }

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let item = navigationMenuContent[indexPath.section].section[indexPath.row]

        cell.textLabel!.text = item.label
        // Enable the cell if item.enabled is set to true and disable it, otherwise.
        cell.isUserInteractionEnabled = item.enabled

         /* Show a disclosure indicator control if item.enabled is set to
            true and remove any existing accessory control, otherwise.
        */
        cell.accessoryType = (item.enabled) ? UITableViewCellAccessoryType.disclosureIndicator : UITableViewCellAccessoryType.none
    }

     override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        // Fetch the menu section object associated the selected feature.
        let item = navigationMenuContent[indexPath.section].section[indexPath.row]

        // Initiate the segue specified by item.segue.main.
        performSegue(withIdentifier: item.segue.main, sender: self)
     }


     // MARK: - Lifetime

    deinit {
        NotificationCenter.default.removeObserver(self, name: NSNotification.Name(rawValue: MGCAppConfiguration.MGCNotifications.refreshTab), object: nil)
    }
}
```

[Next](ManagingContacts-ManagingContacts-ContactsMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-ContainersMenu.swift.md)

