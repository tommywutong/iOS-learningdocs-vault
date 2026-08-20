---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_PlainViewController_swift.html
archived_at: '2026-07-18T03:14:29.045657Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-DetailViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-GroupedViewController.swift.md)

# ManagingContacts/ManagingContacts/PlainViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BaseViewController subclass that displays a list of groups from 
                which you can you select a group.
                Destination view controller for the performAddContactToGroup segue.
                Executes the addContactToGroup segue when tapping any group in its UI.
*/

import UIKit
import Contacts

class PlainViewController: BaseViewController {
    // MARK: - Properties

    /// Group selected by the user.
    fileprivate var selectedGroup: CNGroup?


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]
        let group = data[indexPath.section].content[indexPath.row] as! CNGroup

        cell.textLabel!.text = group.name

        if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.performAddContactToGroup {

            cell.accessoryType = .disclosureIndicator
            cell.isUserInteractionEnabled = true
        }
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let selectedIndex = tableView.indexPathForSelectedRow!
        let model = data[selectedIndex.section]

        if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.addContactToGroup {

            let groups = model.content as! [CNGroup]

            // Fetch the current selected group.
            selectedGroup = groups[selectedIndex.row]

            let addContactToGroupViewController = segue.destination as! AddContactToGroupViewController

            /* Groups and contacts must belong to the same container. For 
               instance, you cannot add Exchange contacts to an iCloud group. 
               Fetch the container associated with the selected group. 
            */
            MGCContactStore.sharedInstance.fetchContainerOfGroup(with: selectedGroup!.identifier, completion: ({(container: CNContainer?) in

                if let container = container {

                    let containerID = container.identifier
                    // Fetch and display contacts associated with the above container.
                    MGCContactStore.sharedInstance.fetchContactsInContainer(with: containerID, completion: ({(contacts: [CNContact]) in

                        let withContacts = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectAllContacts,
                                                   segue: model.segue!),
                                            MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                 content: contacts,
                                                category: MGCAppConfiguration.Content.contacts,
                                                   segue: model.segue!)]

                        let noContacts = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                               content: [MGCAppConfiguration.Content.NoItems.contacts.rawValue as AnyObject],
                                              category: MGCAppConfiguration.Content.NoItems.contacts.rawValue)]

                        addContactToGroupViewController.data = (contacts.count > 0) ? withContacts : noContacts
                        addContactToGroupViewController.title = self.selectedGroup!.name

                        /* Enable the Save button in the navigation bar if we
                           have some contacts. Disable it, otherwise.
                        */
                        addContactToGroupViewController.enableSaveButton = (contacts.count > 0) ? true : false
                    }))
                }
            }))
        }
    }


    // MARK: - Actions

    /// Attempt to add one or more contacts to a group.
    @IBAction func saveContactToGroup(_ sender: UIStoryboardSegue) {
        if let addContactToGroupViewController = sender.source as? AddContactToGroupViewController, let group = selectedGroup {

            // Attempt to add the selected contacts to group.
            if addContactToGroupViewController.selectedContacts.count > 0 {
                MGCContactStore.sharedInstance.save(addContactToGroupViewController.selectedContacts, to: group)
            }
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-DetailViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-GroupedViewController.swift.md)

