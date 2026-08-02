---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_AddContactToGroupViewController_swift.html
archived_at: '2026-07-18T03:14:27.195721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCAppConfiguration.swift.md)[Previous](ManagingContacts-ManagingContacts-AddContactViewController.swift.md)

# ManagingContacts/ManagingContacts/AddContactToGroupViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to select one or more 
                contacts to be added to a selected group.
                Destination view controller for the addContactToGroup segue.
*/

import UIKit
import Contacts

class AddContactToGroupViewController: UITableViewController {
    // MARK: - Types

    fileprivate struct MainStoryboard {
        struct TableViewCellIdentifiers {
            static let cellIdentifier = "cellID"
            static let selectAllContacts = "selectAllContacts"
        }
    }


    // MARK: - Properties

    /// Keep track of all contacts selected by the user.
    var selectedContacts = [CNContact]()

    var data: [MGCModel] = [MGCModel]() {
        didSet {
            tableView.reloadData()
        }
    }

    /// Allows us to enable or disable the Save button in the navigation bar.
    var enableSaveButton: Bool = false {
        didSet {
            navigationItem.rightBarButtonItem!.isEnabled = enableSaveButton
        }
    }

    /**
        - returns: a Boolean value that indicates whether the user tapped 
                   "Select All Contacts" in the "selectAllContacts" cell.
    */
    fileprivate var didSelectAllContacts: Bool? {
        didSet {
            /* The text label of the "selectAllContacts" cell switches between 
               "Select All Contacts" and "Deselect All Contacts." We set 
               selectedContacts to all contacts when the cell displays 
               "Select All Contacts."
            */
            if didSelectAllContacts! {
                // Let's get all contacts for the user has tapped "Select All Contacts."
                selectedContacts = data[1].content as! [CNContact]
            }
            else {
                /* Let's empty selectedContacts for the user has tapped 
                   "Deselect All Contacts."
                */
                selectedContacts.removeAll()
            }
        }
    }


    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }


    // MARK: - UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        return data.count
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        let model = data[section]
        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectAllContacts {
           return 1
        }
        return model.content.count
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let model = data[indexPath.section]

        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectAllContacts {
            return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.selectAllContacts, for: indexPath)
        }

        return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellIdentifier, for: indexPath)
    }

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        if let category = model.category, category == MGCAppConfiguration.Content.NoItems.contacts.rawValue {
            cell.textLabel!.text = model.content[indexPath.row] as? String
        }
        else {

            if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectAllContacts {

                if let status = didSelectAllContacts {
                    /* Switch between "Select All Contacts" and 
                       "Deselect All Contacts" according to the user's selection.
                    */
                    cell.textLabel!.text = (status) ? MGCAppConfiguration.MainStoryboard.Cells.deselectAllContacts : MGCAppConfiguration.MainStoryboard.Cells.selectAllContatcs
                }
            }

            if let category = model.category, category == MGCAppConfiguration.Content.contacts {

                let contact = model.content[indexPath.row] as! CNContact

                /* Display the formatted name if the contact is of type Person
                   and the organization name if the contact is type of Organization.
                */
                cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName

                /* Display a checkmark if the user chose to select all contacts. 
                   Display no accessory if the user chose to deselect all contacts.
                */
                if let status = didSelectAllContacts {
                    cell.accessoryType = (status) ? .checkmark : .none
                }
            }
        }
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: tableView.indexPathForSelectedRow!, animated: false)
        let model = data[indexPath.section]

        // The user selected the "Select All Contacts" cell.
        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectAllContacts {

            /* The initial value of didSelectAllContacts is nil as the user has 
               not chosen to select all contacts, yet. Its value switches between 
               true and false after the user choose to do so.
            */
            if let status = didSelectAllContacts {
                 didSelectAllContacts = !status
            }
            else {
                didSelectAllContacts = true
            }
            tableView.reloadData()
        }
        // The user selected a contact among the list.
        else if let category = model.category, category == MGCAppConfiguration.Content.contacts {

            let contact = model.content[indexPath.row] as! CNContact

            if let cell = tableView.cellForRow(at: indexPath) {

                if cell.accessoryType == UITableViewCellAccessoryType.none {

                    cell.accessoryType = UITableViewCellAccessoryType.checkmark
                    selectedContacts.append(contact)
                }
                /* Remove the checkmark from the cell and remove the contact from
                   selectedContacts if the user tapped an already selected contact.
                */
                else if cell.accessoryType == UITableViewCellAccessoryType.checkmark {

                    cell.accessoryType = UITableViewCellAccessoryType.none

                    if let selectedIndex = selectedContacts.index(of: contact) {
                        selectedContacts.remove(at: selectedIndex)
                    }
                }
            }
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCAppConfiguration.swift.md)[Previous](ManagingContacts-ManagingContacts-AddContactViewController.swift.md)

