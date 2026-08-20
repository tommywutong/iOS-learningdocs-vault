---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewController_SelectMultipleProperties_swift.html
archived_at: '2026-07-18T03:14:30.023815Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewController-SelectSingleContact.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectSingleProperty.swift.md)

# ManagingContactsUI/ContactPickerViewController/SelectMultipleProperties.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A BaseViewController subclass that implements the Multiple Properties tab. Creates
  and presents a contact picker view controller when tapping "Show Picker" in the
  UI. Use CNContactPickerDelegate's contactPicker(_ picker: CNContactPickerViewController,
  didSelectContactProperties contactProperties: [CNContactProperty]) to allow
  users to select one or more properties from a contact detail card. Also use
  CNContactPickerViewController's predicateForSelectionOfProperty instance
  property to specify which contact property to select in the contact detail card.
 */

import UIKit
import ContactsUI

class SelectMultipleProperties: BaseViewController {
    // MARK: - Display Picker

    @IBAction func showPicker(_ sender: UIButton) {
        hideStackView(true)

        let picker = CNContactPickerViewController()
        //Select contacts' email addresses.
        picker.predicateForSelectionOfProperty = NSPredicate(format: "key == 'emailAddresses'")
        picker.delegate = self
        present(picker, animated: true, completion: nil)
    }

    // MARK: - UITableViewDelegate

    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let section = data[indexPath.section].section
        let item = section[indexPath.row]

        cell.textLabel?.text = item.label
        cell.detailTextLabel?.text = item.value
    }
}

/**
    Extends `SelectMultipleProperties` to conform to the `CNContactPickerDelegate`
    protocol.
*/
extension SelectMultipleProperties: CNContactPickerDelegate {
    func contactPicker(_ picker: CNContactPickerViewController, didSelectContactProperties contactProperties: [CNContactProperty]) {
        // Iterate through all properties if contactProperties is not empty.
        if !contactProperties.isEmpty {
            for property in contactProperties {
                var section = [LabelValue]()

                // Attempt to fetch the contact property key name.
                if let name = property.nameMatchingKey {
                    let formattedName = property.contact.formattedName
                    section = [LabelValue(label: AppConfiguration.TableViewCellLabels.contact, value: formattedName),
                               LabelValue(label: AppConfiguration.TableViewCellLabels.key, value: name)]
                }

                // Attempt to fetch the localized label of the property.
                if let localizedLabel = property.nameMatchingLocalizedLabel {
                    section.append(LabelValue(label: AppConfiguration.TableViewCellLabels.label, value: localizedLabel))
                }

                // Attempt to fetch the value of the property.
                if let value = property.nameMatchingValue {
                    section.append(LabelValue(label: AppConfiguration.TableViewCellLabels.value, value: value))
                }

                if !section.isEmpty {
                    data.append(Section(section: section))
                }
            }
            hideStackView(false)
        }
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewController-SelectSingleContact.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectSingleProperty.swift.md)

