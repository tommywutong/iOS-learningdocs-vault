---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_AddGroupViewController_swift.html
archived_at: '2026-07-18T03:14:27.344316Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-EditViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCPostalAddress.swift.md)

# ManagingContacts/ManagingContacts/AddGroupViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A BaseViewController subclass that allows users to enter a name and 
                select a container for a new group.
*/

import UIKit
import Contacts

class AddGroupViewController: BaseViewController, UITextFieldDelegate {
    // MARK: - Types

    fileprivate struct MainStoryboard {
        struct TableViewCellIdentifiers {
            // Identifies the cell used to display containers.
            static let containerCellIdentifier = "containerID"
            // Identifies the cell used to enter a group name.
            static let groupCellIdentifier = "groupID"
        }
    }


    // MARK: - Properties

    /// Name of the group entered by the user.
    var group: String?

    /// Identifier of the selected container.
    var containerID: String?

    /// Keep track of the user input.
    fileprivate weak var textField: UITextField?

    /// - returns: The container selected by the user.
    fileprivate var selectedContainer: CNContainer? {
        didSet {
            if let textField = self.textField {
                /* Enable the Save button if the user has selected a container 
                   and entered a name in the textfield. Disable it, otherwise.
                */
                navigationItem.rightBarButtonItem!.isEnabled = !(textField.text!.isEmpty)
            }
        }
    }


    // MARK: - UITextFieldDelegate

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // Hide the keyboard.
        textField.resignFirstResponder()

        if let _ = selectedContainer {
           /* Enable the Save button if the user has selected a container and 
              entered a name in the textfield. Disable it, otherwise.
            */
           navigationItem.rightBarButtonItem!.isEnabled = !(textField.text!.isEmpty)
        }
        return true
    }

    func textFieldDidBeginEditing(_ textField: UITextField) {
        // Disable the "Save" button when the user starts typing in the textfield.
        navigationItem.rightBarButtonItem!.isEnabled = false
    }

    func textFieldDidEndEditing(_ textField: UITextField) {
        self.textField = textField
    }


    // MARK: - UITableViewDataSource

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        let model = data[section]

        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.addGroup {
            return 1
        }
        return model.content.count
    }

     /// Return the header title for this section.
    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        let model = data[section]

        // Return the header title for this section.
        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.addGroup {
            return MGCAppConfiguration.MainStoryboard.Cells.emptyString
        }
        return model.category
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let model = data[indexPath.section]

        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.addGroup {
            return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.groupCellIdentifier, for: indexPath) as! TextFieldCell
        }
        return tableView.dequeueReusableCell(withIdentifier: MainStoryboard.TableViewCellIdentifiers.containerCellIdentifier, for: indexPath)
    }

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        // Display all containers that can be used to add a group.
        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectContainer {

            let container = model.content[indexPath.row] as! CNContainer
            cell.textLabel!.text = (container.type == .local) ? MGCAppConfiguration.MainStoryboard.Cells.local : container.name

            // Show the default container as selected by default. 
            if container.identifier == MGCContactStore.sharedInstance.defaultContainerID {
                selectedContainer = container
                cell.accessoryType = UITableViewCellAccessoryType.checkmark
                tableView.selectRow(at: indexPath, animated: true, scrollPosition: .none)
            }
        }
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let model = data[indexPath.section]

        if let category = model.category, category == MGCAppConfiguration.MainStoryboard.TableHeaderSection.Groups.selectContainer {

            let containers = model.content as! [CNContainer]

            if let container = selectedContainer {

                let indexOfSelectedContainer = containers.index(of: container)

                guard indexOfSelectedContainer == indexPath.row else {
                    let oldIndexPath = IndexPath(row: indexOfSelectedContainer!, section: indexPath.section)

                    let newCell = tableView.cellForRow(at: indexPath)

                    if newCell?.accessoryType == UITableViewCellAccessoryType.none {
                        newCell?.accessoryType = UITableViewCellAccessoryType.checkmark
                        selectedContainer = containers[indexPath.row]
                    }

                    let oldCell = tableView.cellForRow(at: oldIndexPath)
                    if oldCell?.accessoryType == UITableViewCellAccessoryType.checkmark {
                        oldCell?.accessoryType = UITableViewCellAccessoryType.none
                    }
                    return
                }
            }
            else {

                let newCell = tableView.cellForRow(at: indexPath)
                newCell?.accessoryType = .checkmark
                selectedContainer = containers[indexPath.row]
            }
        }
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
         // Send back the entered name and the selected container's identifier.
         if navigationItem.rightBarButtonItem == sender as? UIBarButtonItem {

            group = textField!.text
            containerID = selectedContainer?.identifier
        }
    }
}
```

[Next](ManagingContacts-ManagingContacts-EditViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCPostalAddress.swift.md)

