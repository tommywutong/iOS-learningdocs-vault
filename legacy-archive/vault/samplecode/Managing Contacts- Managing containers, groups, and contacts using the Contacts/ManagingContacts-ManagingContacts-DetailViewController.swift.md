---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_DetailViewController_swift.html
archived_at: '2026-07-18T03:14:27.921118Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCContactStoreUtilities.swift.md)[Previous](ManagingContacts-ManagingContacts-PlainViewController.swift.md)

# ManagingContacts/ManagingContacts/DetailViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BaseViewController subclass that displays group or contact 
                information in a plain style table view.
                Destination view controller for the fetchAllGroups, 
                fetchGroupsPerContainer, fetchContactsPerContainer, and 
                fetchContactsPerGroup segues.
*/

import UIKit
import Contacts

class DetailViewController: BaseViewController {
    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        // Fetch the menu section object.
        let model = data[indexPath.section]

        /* Display groups if category is set to Groups and contacts if it is set 
           to Contacts.
        */
        if  let category = model.category, category == MGCAppConfiguration.Content.groups {

            let group = model.content[indexPath.row] as! CNGroup
            cell.textLabel!.text = group.name
        }
        else if let category = model.category, category == MGCAppConfiguration.Content.contacts {

            let contact = model.content[indexPath.row] as! CNContact
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName
        }
        else if let category = model.category, (category == MGCAppConfiguration.Content.NoItems.contacts.rawValue || category == MGCAppConfiguration.Content.NoItems.groups.rawValue) {
            cell.textLabel!.text = model.content[indexPath.row] as? String
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCContactStoreUtilities.swift.md)[Previous](ManagingContacts-ManagingContacts-PlainViewController.swift.md)

