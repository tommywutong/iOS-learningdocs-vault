---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_UpdateGroupViewController_swift.html
archived_at: '2026-07-18T03:14:29.339534Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCMenuSectionFeature.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCMenuSection.swift.md)

# ManagingContacts/ManagingContacts/UpdateGroupViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to update the name of an 
               existing group.
*/

import UIKit
import Contacts

class UpdateGroupViewController: UITableViewController {
    // MARK: - Properties

    /// Name of the group to be updated.
    var name: String?

    /// Textfield used to enter a group name.
    @IBOutlet weak fileprivate var textField: UITextField!


    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        // Show the name of the group.
        if let displayedName = name {
            textField.text = displayedName
        }
    }


    // MARK: - UITextFieldDelegate

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // Hide the keyboard.
        textField.resignFirstResponder()

        // Show the Save button if the user has entered a name.
        navigationItem.rightBarButtonItem!.isEnabled = !(textField.text!.isEmpty)
        return true
    }


    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if indexPath.section == 0 && indexPath.row == 0 {
            textField.becomeFirstResponder()
        }
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Send back the entered/updated name for the group.
        if navigationItem.rightBarButtonItem == sender as? UIBarButtonItem {
            name = textField.text
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCMenuSectionFeature.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCMenuSection.swift.md)

