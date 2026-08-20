---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_EditViewController_swift.html
archived_at: '2026-07-18T03:14:27.971428Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-AddContactViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-AddGroupViewController.swift.md)

# ManagingContacts/ManagingContacts/EditViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to delete one or more groups
                or contacts.
*/

import UIKit
import Contacts

class EditViewController: UITableViewController {
    // MARK: - Types

    fileprivate struct MainStoryboard {
        struct TableViewCellIdentifiers {
            // Cell Identifier.
            static let cellIdentifier = "cellID"
        }
    }


    // MARK: - Properties

    /// Group from which contacts will be removed.
    var relatedGroup: CNGroup?

    /// Data model
    var data: [MGCModel] = [MGCModel]() {
        didSet {
            tableView.reloadData()
        }
    }

    /// Allows us to enable or disable the Edit button in the navigation bar.
    var enableEditButton: Bool = false {
        didSet {
            navigationItem.rightBarButtonItem!.isEnabled = enableEditButton
        }
    }


    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
        // Display an Edit button.
        navigationItem.rightBarButtonItem = editButtonItem

        // Create a toolbar that allows us to delete everything at once.
        toolbarItems = [UIBarButtonItem(title: NSLocalizedString(MGCAppConfiguration.Messages.deleteAll, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString),
                                        style: .plain,
                                       target: self,
                                       action: #selector(EditViewController.deleteAll(_:)))]
    }


    // MARK: - UITableView

    override func setEditing(_ editing: Bool, animated: Bool) {
        super.setEditing(editing, animated: animated)
        // Show the toolbar only when editing.
        navigationController!.isToolbarHidden = !editing;
    }


    // MARK: - Delete Everything

    /// Called when the user tapped "Delete All" in the toolbar.
    func deleteAll(_ sender: UIBarButtonItem) {
        for model in data {
            if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.deleteGroup {

               // Delete all groups.
                MGCContactStore.sharedInstance.delete(model.content as! [CNGroup])
                data.removeAll()
            }
            else if model.segue!.related == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.removeContactFromGroup {

                // Delete all contacts that are members of relatedGroup.
                MGCContactStore.sharedInstance.remove(model.content as! [CNContact], from: relatedGroup!)
                data.removeAll()
            }
            else if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.deleteContact {

                // Delete all contacts.
                MGCContactStore.sharedInstance.delete(model.content as! [CNContact])
                data.removeAll()
            }
        }
        tableView.reloadData()
        enableEditButton = false

        // Disable editing. All rows were removed.
        setEditing(false, animated: true)
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

    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {

            let model = data[indexPath.section]

            // Delete a group.
            if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.deleteGroup {

                var groups = model.content as! [CNGroup]
                let group = groups[indexPath.row]

                tableView.beginUpdates()
                groups.remove(at: indexPath.row)
                data[indexPath.section].content = groups

                tableView.deleteRows(at: [indexPath], with: .fade)
                tableView.endUpdates()

                MGCContactStore.sharedInstance.delete([group])
            }
            else if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.deleteContact || model.segue!.related == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.removeContactFromGroup {

                var contacts = model.content as! [CNContact]
                let contact = contacts[indexPath.row]

                tableView.beginUpdates()
                contacts.remove(at: indexPath.row)
                data[indexPath.section].content = contacts

                tableView.deleteRows(at: [indexPath], with: .fade)
                tableView.endUpdates()

                // Delete the contact if the received main segue was "deleteContact."
                if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.deleteContact {
                    MGCContactStore.sharedInstance.delete([contact])
                }
                /* Remove the contact as a member of relatedGroup if the 
                   received related segue was "removeContactFromGroup."
                */
                else {
                    MGCContactStore.sharedInstance.remove([contact], from: relatedGroup!)
                }
            }

            if (model.content.count == 0) {

                enableEditButton = false
                setEditing(false, animated: true)
            }
        }
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, editingStyleForRowAt indexPath: IndexPath) -> UITableViewCellEditingStyle {
        return .delete
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.cellIdentifier, for: indexPath)
    }

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        // Display "No contacts" if relatedGroup does not have any associated contacts.
        if let category = model.category, category == MGCAppConfiguration.Content.NoItems.contacts.rawValue {
            cell.textLabel!.text = model.content[indexPath.row] as? String
        }
        else if model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.deleteGroup {

            let group = model.content[indexPath.row] as! CNGroup
            cell.textLabel!.text = group.name
        }
        else if model.segue!.related == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Groups.removeContactFromGroup ||
                model.segue!.main == MGCAppConfiguration.MainStoryboard.SegueIdentifiers.Contacts.deleteContact {

            let contact = model.content[indexPath.row] as! CNContact
            cell.textLabel!.text = (contact.isPerson) ? contact.formattedName : contact.organizationName
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-AddContactViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-AddGroupViewController.swift.md)

