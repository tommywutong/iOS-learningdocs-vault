---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_GroupedViewController_swift.html
archived_at: '2026-07-18T03:14:28.062101Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-PlainViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-GroupsMenu.swift.md)

# ManagingContacts/ManagingContacts/GroupedViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BaseViewController subclass that displays contact or container
                information in a grouped style table view.
                It organizes contacts by type, which is either Person or Organization.
                Containers are organized by Local, Exchange, and CarDAV types.
                Destination view controller for the fetchAllContacts, 
                fetchAllContainers, and fetchDefaultContainer segues.
*/

import UIKit
import Contacts

class GroupedViewController: BaseViewController {
    // MARK: - UITableViewDataSource

    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        // Return the header title for this section.
        return data[section].category
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        // Display containers if tab is set to Containers.
        if model.tab == MGCAppConfiguration.Content.containers {

            let container = model.content[indexPath.row] as! CNContainer
            cell.textLabel!.text = (container.type == .local) ? MGCAppConfiguration.MainStoryboard.Cells.local : container.name
        }
        // Display contacts if tab is set to Contacts.
        else if model.tab == MGCAppConfiguration.Content.contacts {

            let contact = model.content[indexPath.row] as! CNContact
            /* Display the formatted name if the contact is of type Person and
               the organization name if the contact is type of Organization. 
            */
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-PlainViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-GroupsMenu.swift.md)

