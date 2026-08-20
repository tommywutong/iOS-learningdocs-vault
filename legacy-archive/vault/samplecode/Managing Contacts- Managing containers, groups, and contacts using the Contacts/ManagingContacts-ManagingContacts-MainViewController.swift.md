---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MainViewController_swift.html
archived_at: '2026-07-18T03:14:28.913275Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](README.md.md)[Previous](ManagingContacts-ManagingContacts-MGCAppConfiguration.swift.md)

# ManagingContacts/ManagingContacts/MainViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BaseViewController subclass that displays a list of containers, 
                contacts, or groups from which you can select an item.
                Destination view controller for the performFetchGroupsPerContainer,
                performFetchContactsPerContainer, performFetchContactsPerGroup,
                performUpdateGroup, performRemoveContactFromGroup, and 
                performUpdateContact segues.
                Source view controller for the fetchGroupsPerContainer,
                fetchContactsPerContainer, fetchContactsPerGroup, updateGroup,
                updateContact, and removeContactFromGroup segues.
                Implements the unwind updateGroup and updateContact segues that allow
                you to update a group and a contact, respectively.
*/

import UIKit
import Contacts

class MainViewController: BaseViewController {
    // MARK: - Properties

    /// Selected CNContact or CNGroup object.
    fileprivate var selectedItem: AnyObject?
    fileprivate var selectedIndexPath: IndexPath?
    fileprivate var contacStoretUtility = MGCContactStoreUtilities()


    // MARK: - UITableViewDelegate

     override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        if model.tab == MGCAppConfiguration.Content.containers {

            let container = model.content[indexPath.row] as! CNContainer
            cell.textLabel!.text = (container.type == .local) ? MGCAppConfiguration.MainStoryboard.Cells.local : container.name
        }
        else if model.tab == MGCAppConfiguration.Content.groups {

            let group = model.content[indexPath.row] as! CNGroup
            cell.textLabel!.text = group.name
        }
        else if model.tab == MGCAppConfiguration.Content.contacts {

            let contact = model.content[indexPath.row] as! CNContact
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName
        }
     }


    // MARK: - Convenience Method

    /// Builds data source for a given view controller.
    fileprivate func handleFetching(_ identifier: String, with viewController: BaseViewController, segue: String) {
        if segue == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchGroupsPerContainer {

            // Use the container's identifier to fetch its associated groups.
            MGCContactStore.sharedInstance.fetchGroupsInContainer(with: identifier, completion: ({(groups: [CNGroup]) in
                if groups.count > 0 {

                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers,
                                                content: groups,
                                               category: MGCAppConfiguration.Content.groups)]
                }
                else {
                    // Display "No groups" when the container does not have any groups.
                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers,
                                                content: [MGCAppConfiguration.Content.NoItems.groups.rawValue as AnyObject],
                                               category: MGCAppConfiguration.Content.NoItems.groups.rawValue)]
                }
            }))
        }
        else if segue == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchContactsPerContainer {

            // Use the container's identifier to fetch its associated contacts.
            MGCContactStore.sharedInstance.fetchContactsInContainer(with: identifier, completion: ({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers,
                                                content: contacts,
                                               category: MGCAppConfiguration.Content.contacts)]
                }
                else {
                    // Diplay "No contacts" when the container does not have any contacts.
                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.containers,
                                                content: [MGCAppConfiguration.Content.NoItems.contacts.rawValue as AnyObject],
                                               category: MGCAppConfiguration.Content.NoItems.contacts.rawValue)]
                }
            }))
        }
        else if segue == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.fetchContactsPerGroup
        {

            // Use the group's identifier to fetch its associated contacts.
            MGCContactStore.sharedInstance.fetchContactsInGroup(with: identifier, completion: ({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                content: contacts,
                                               category: MGCAppConfiguration.Content.contacts)]
                }
                else {
                    // Display "No contacts" when the group does not any contacts.
                    viewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                content: [MGCAppConfiguration.Content.NoItems.contacts.rawValue as AnyObject],
                                               category: MGCAppConfiguration.Content.NoItems.contacts.rawValue)]
                }
            }))
        }
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?)
    {
        selectedIndexPath = tableView.indexPathForSelectedRow!
        let model = data[selectedIndexPath!.section]

        /* Implement the "Fetch groups per container" and 
           "Fetch contacts per container" features.
        */
        if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchGroupsPerContainer || segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchContactsPerContainer {

            let container = model.content[selectedIndexPath!.row] as! CNContainer
            let detailViewController = segue.destination as! DetailViewController
            detailViewController.title = (container.type == .local) ? MGCAppConfiguration.MainStoryboard.Cells.local : container.name

            let segue = (segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchGroupsPerContainer) ? MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchGroupsPerContainer : MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Containers.fetchContactsPerContainer

            handleFetching(container.identifier, with: detailViewController, segue: segue)
        }
        // Implement the "Fetch contacts per group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.fetchContactsPerGroup {

            let group = model.content[selectedIndexPath!.row] as! CNGroup
            let detailViewController = segue.destination as! DetailViewController
            detailViewController.title = group.name

            handleFetching(group.identifier, with: detailViewController, segue: MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.fetchContactsPerGroup)
        }
        // Implement the "Update a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.updateGroup {

            selectedItem = model.content[selectedIndexPath!.row] as! CNGroup
            let updateGroupViewController = segue.destination as! UpdateGroupViewController
            updateGroupViewController.name = selectedItem!.name
        }
        // Implement the "Update a contact" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.updateContact {

            selectedItem = model.content[selectedIndexPath!.row] as! CNContact
            let updateContactViewController =  segue.destination as! UpdateContactViewController
            updateContactViewController.contact = contacStoretUtility.parse(selectedItem as! CNContact)
        }
        // Implement the "Remove contact from a group" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.removeContactFromGroup {

            let group = model.content[selectedIndexPath!.row] as! CNGroup
            let editViewController = segue.destination as! EditViewController
            editViewController.title = group.name
            editViewController.relatedGroup = group

            // Fetch contacts associated with the selected group.
            MGCContactStore.sharedInstance.fetchContactsInGroup(with: group.identifier, completion: ({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    editViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: contacts,
                                                      segue: model.segue!)]
                }
                else {

                    editViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.groups,
                                                    content: [MGCAppConfiguration.Content.NoItems.contacts.rawValue as AnyObject],
                                                   category: MGCAppConfiguration.Content.NoItems.contacts.rawValue)]

                    editViewController.enableEditButton = false
                }

                editViewController.enableEditButton = (contacts.count > 0) ? true : false
            }))
        }
    }


    // MARK: - Actions

    /// Attempt to update a group.
    @IBAction func updateGroup(_ sender: UIStoryboardSegue) {
        if  let updateGroupViewController = sender.source as? UpdateGroupViewController, let name = updateGroupViewController.name, let selectedGroup = selectedItem as? CNGroup {

                // Attempt to update the group in Contacts.
                MGCContactStore.sharedInstance.update(selectedGroup, with: name, completion: ({(group: CNGroup?) in
                    /* If the update operation was successful, refresh the UI 
                       with the updated info.
                    */
                    if let updatedGroup = group {

                        DispatchQueue.main.async {
                           self.data[self.selectedIndexPath!.section].content[self.selectedIndexPath!.row] = updatedGroup
                           self.tableView.reloadData()
                        }
                    }
            }))
        }
    }

    /// Attempt to update a contact.
    @IBAction func updateContact(_ sender: UIStoryboardSegue) {
         if let updateContactViewController = sender.source as? UpdateContactViewController, let contact = updateContactViewController.contact, let selectedContact = selectedItem as? CNContact {

            MGCContactStore.sharedInstance.update(selectedContact, with: contact, completion:({(contact: CNContact?) in
                if let updatedContact = contact {

                    DispatchQueue.main.async {
                       self.data[self.selectedIndexPath!.section].content[self.selectedIndexPath!.row] = updatedContact
                       self.tableView.reloadData()
                    }
                }
            }))
        }
    }
}
```

[Next](README.md.md)[Previous](ManagingContacts-ManagingContacts-MGCAppConfiguration.swift.md)

