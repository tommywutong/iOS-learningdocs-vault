---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_ContactsMenu_swift.html
archived_at: '2026-07-18T03:14:27.585403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCModel.swift.md)[Previous](ManagingContacts-ManagingContacts-MenuViewController.swift.md)

# ManagingContacts/ManagingContacts/ContactsMenu.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A MenuViewController subclass that displays and manages navigation 
                menu features in the Contacts tab.
                Implements the unwind saveContact segue to create and save a contact
                to the default container.
                Source view conroller for the fetchAllContacts, fetchContactsMatchingName, 
                addContact, performUpdateContact, and deleteContact segues.
*/

import UIKit
import Contacts

class ContactsMenu: MenuViewController {
    // MARK: - Handle refreshTabNotification

    override func handleRefreshTabNotification(_ notification: Notification) {
        let tabBarNotification = notification.object as! TabBarViewController
         // Update the data model for this tab.
        navigationMenuContent = tabBarNotification.contactsMenu
        tableView.reloadData()
    }


    // MARK: - UITableViewDataSource
    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return navigationMenuContent[section].title
    }


    // MARK: - Convenience Method

    /// Create a data model object that organize contacts into person and organization.
    fileprivate func buildDataModel(with contacts: [CNContact]) -> [MGCModel] {
        var result = [MGCModel]()
        // Parse contacts according to their type: Person or Organization.
        let persons = menuContactStoreUtilities.filter(contacts, for: .person)
        let organization = menuContactStoreUtilities.filter(contacts, for: .organization)

        if !persons.isEmpty {
            result.append(MGCModel(tab: MGCAppConfiguration.Content.contacts,
                               content: persons,
                              category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Contacts.person))
        }

        if !organization.isEmpty {
            result.append(MGCModel(tab: MGCAppConfiguration.Content.contacts,
                               content: organization,
                              category: MGCAppConfiguration.MainStoryboard.TableHeaderSection.Contacts.organization))
        }
        return result
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let item = navigationMenuContent[tableView.indexPathForSelectedRow!.section].section[tableView.indexPathForSelectedRow!.row]

        // Implement the "Fetch all contacts" feature.
        if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.fetchAllContacts {

            let groupedViewController = segue.destination as! GroupedViewController
            groupedViewController.title = item.title

            MGCContactStore.sharedInstance.fetchContacts(({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    groupedViewController.data = self.buildDataModel(with: contacts)
                }
            }))
        }
        // Implement the "Fetch contacts matching a name" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.fetchContactsMatchingName {
            let searchViewController = segue.destination as! SearchViewController
            MGCContactStore.sharedInstance.fetchContacts(({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    searchViewController.data = contacts
                }
            }))
        }
        // Implement the "Update a contact" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.performUpdateContact {
            let mainViewController = segue.destination as! MainViewController
            mainViewController.title = item.title

            MGCContactStore.sharedInstance.fetchContacts(({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    mainViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.contacts,
                                                    content: contacts,
                                                      segue: item.segue)]
                }
            }))
        }
        // Implement the "Delete a contact" feature.
        else if segue.identifier == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.deleteContact {
            let editViewController = segue.destination as! EditViewController
            editViewController.title = item.title

            MGCContactStore.sharedInstance.fetchContacts(({(contacts: [CNContact]) in
                if contacts.count > 0 {
                    editViewController.data = [MGCModel(tab: MGCAppConfiguration.Content.contacts,
                                                    content: contacts,
                                                      segue: item.segue)]
                }
            }))
        }
    }


    // MARK: - Actions

    /// Dismiss the Add Contact view controller.
    @IBAction func cancel(_ sender: UIStoryboardSegue) {
        dismiss(animated: true, completion: nil)
    }

    /// Add a new contact.
    @IBAction func saveContact(_ sender: UIStoryboardSegue) {
        if let addContactViewController = sender.source as? AddContactViewController, let newContact = addContactViewController.contact {
            MGCContactStore.sharedInstance.add(newContact)
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCModel.swift.md)[Previous](ManagingContacts-ManagingContacts-MenuViewController.swift.md)

