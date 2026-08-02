---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewController_SelectMultipleContacts_swift.html
archived_at: '2026-07-18T03:14:29.970779Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewController-AppDelegate.swift.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForEnablingContactV.md)

# ManagingContactsUI/ContactPickerViewController/SelectMultipleContacts.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A BaseViewController subclass that implements the Multiple Contacts tab. Creates
  and presents a contact picker view controller when tapping "Show Picker" in the
  UI. Use CNContactPickerDelegate's contactPicker(_ picker: CNContactPickerViewController,
  didSelect contacts: [CNContact]) to allow users to select and return one or
  more contacts.
 */

import UIKit
import ContactsUI

class SelectMultipleContacts: BaseViewController {
    // MARK: - Display Picker

    /**
        Displays a contacts picker view when users tap "Show Picker" in the
        Multiple Contacts tab. Select one or more contacts in the picker
        to continue.
    */
    @IBAction func showPicker(_ sender: UIButton) {
        // Hide the stackview and remove everything from the table view.
        hideStackView(true)

        let picker = CNContactPickerViewController()
        picker.delegate = self
        present(picker, animated: true, completion: nil)
    }

    // MARK: - UITableViewDelegate

    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let  section = data[indexPath.section].section
        let item = section[indexPath.row]
        cell.textLabel?.text = item.value
    }
}

/**
    Extends `SelectMultipleContacts` to conform to the `CNContactPickerDelegate`
    protocol.
*/
extension SelectMultipleContacts: CNContactPickerDelegate {
    /**
        Called when users tap one or more contacts in the picker, then Done in
        the picker view. Calls hideStackView(_:) to update the table view with
        the full names of the selected contacts.
    */
    func contactPicker(_ picker: CNContactPickerViewController, didSelect contacts: [CNContact]) {
        if !contacts.isEmpty {

            var section = [LabelValue]()
            // Iterate through all the selected contacts.
            for contact in contacts {
                let item = LabelValue(value: contact.formattedName)
                section.append(item)
            }
            data = [Section(section: section)]

            // Show and update the table view with the above contacts.
            hideStackView(false)
        }
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewController-AppDelegate.swift.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForEnablingContactV.md)

