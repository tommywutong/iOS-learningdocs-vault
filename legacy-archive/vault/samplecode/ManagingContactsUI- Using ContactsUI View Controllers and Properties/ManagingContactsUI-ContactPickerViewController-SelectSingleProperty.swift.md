---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewController_SelectSingleProperty_swift.html
archived_at: '2026-07-18T03:14:30.164146Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewController-SelectMultipleProperties.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-BaseViewController.swift.md)

# ManagingContactsUI/ContactPickerViewController/SelectSingleProperty.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A BaseViewController subclass that implements the Single Property tab. Creates
  a contact picker view controller, sets its displayedPropertyKeys
  property to only display the following properties in a contact detail card:
  givenName, familyName, emailAddresses, phoneNumbers, and postalAddresses, then
  presents it. Uses CNContactPickerDelegate's contactPicker(_ picker: CNContactPickerViewController,
  didSelect contactProperty: CNContactProperty) to allow users to select and
  return a single property.
*/

import UIKit
import ContactsUI

class SelectSingleProperty: BaseViewController {
    // MARK: - Display Picker

    /**
        Presents a contacts picker view when users tap "Show Picker" in the
        Single Property tab. Select a contact in the picker, then one of its
        properties to continue.
    */
    @IBAction func showPicker(_ sender: UIButton) {
        hideStackView(true)

        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.displayedPropertyKeys = [CNContactGivenNameKey, CNContactFamilyNameKey, CNContactEmailAddressesKey,
                                        CNContactPhoneNumbersKey, CNContactPostalAddressesKey]
        // Presents the contact picker view controller.
        present(picker, animated: true, completion: nil)
    }

    // MARK: - UITableViewDelegate

    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let  section = data[indexPath.section].section
        let item = section[indexPath.row]

        cell.textLabel?.text = item.label
        cell.detailTextLabel?.text = item.value
    }
}

/**
    Extends `SelectSingleProperty` to conform to the `CNContactPickerDelegate`
    protocol.
*/
extension SelectSingleProperty: CNContactPickerDelegate {
    /**
        Called when users tap a single property in the contact detail card.
        Calls hideStackView(_:) to update the table view with the name, value,
        and property key of the selected property and also with its associated
        contact's full name.
    */
    func contactPicker(_ picker: CNContactPickerViewController, didSelect contactProperty: CNContactProperty) {
        var section = [LabelValue]()

        // Attempt to fetch the contact property key name.
        if let name = contactProperty.nameMatchingKey {
            section = [LabelValue(label: AppConfiguration.TableViewCellLabels.contact, value: contactProperty.contact.formattedName),
                       LabelValue(label: AppConfiguration.TableViewCellLabels.key, value: name)]
        }

        // Attempt to fetch the localized label of the property.
        if let localizedLabel = contactProperty.nameMatchingLocalizedLabel {
            section.append(LabelValue(label: AppConfiguration.TableViewCellLabels.label, value: localizedLabel))
        }

        // Attempt to fetch the value of the property.
        if let value = contactProperty.nameMatchingValue {
            section.append(LabelValue(label: AppConfiguration.TableViewCellLabels.value, value: value))
        }

        data = [Section(section: section)]

        // Show and update the table view with the above property information.
        hideStackView(false)
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewController-SelectMultipleProperties.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-BaseViewController.swift.md)

