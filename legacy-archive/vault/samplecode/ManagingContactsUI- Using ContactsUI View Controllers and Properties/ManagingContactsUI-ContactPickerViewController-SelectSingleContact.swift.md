---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewController_SelectSingleContact_swift.html
archived_at: '2026-07-18T03:14:30.112017Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-Shared-Section.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectMultipleProperties.swift.md)

# ManagingContactsUI/ContactPickerViewController/SelectSingleContact.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A BaseViewController subclass that implements the Single Contact tab. Creates
  and presents a contact picker view controller when tapping "Show Picker" in the
  UI. Uses CNContactPickerDelegate's contact​Picker(_ picker: CNContactPickerViewController,
  didSelect contact: CNContact​) to allow users to select and return a single contact.
*/

import UIKit
import ContactsUI

class SelectSingleContact: BaseViewController {
    // MARK: - Display Picker

    /**
        Presents a contacts picker view when users tap "Show Picker" in the
        Single Contact tab. Select a contact in the picker to continue.
    */
    @IBAction func showPicker(_ sender: UIButton) {
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
    Extends `SelectSingleContact` to conform to the `CNContactPickerDelegate`
    protocol.
*/
extension SelectSingleContact: CNContactPickerDelegate {
    /**
        Called when users select a single contact. Calls hideStackView(_:) to
        update the table view with the selection.
    */
    func contactPicker(_ picker: CNContactPickerViewController, didSelect contact: CNContact) {
        let item = [LabelValue(value: contact.formattedName)]
        data = [Section(section: item)]

        // Show and update the table view with the above contact.
        hideStackView(false)
    }
}
```

[Next](ManagingContactsUI-Shared-Section.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectMultipleProperties.swift.md)

