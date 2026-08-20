---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewControllerWithPredicates_ForSelectionOfContactViewController_swift.html
archived_at: '2026-07-18T03:14:29.741043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-BaseTableViewContro.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfPrope.md)

# ManagingContactsUI/ContactPickerViewControllerWithPredicates/ForSelectionOfContactViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements CNContactPickerViewController's predicateForSelectionOfContact
  instance property. Allows users to select all contacts, contacts that
  have an email address, contacts with a postal address, contacts that have
  2 or more phone numbers, and contacts that have a profile picture in
  the contact picker view. When the user selects a contact, the contact picker
  view controller is dismissed and CNContactPickerDelegate's
  contact​Picker(_:​did​Select:​) returns the selected contact.
  Contacts, which don't meet the above criteria, will be selectable in the picker
  view. Furthermore, the picker view will show their detail card upon selection.
  However, the contact information will not be returned upon dismissing the
  contact picker view controller.
 */

import UIKit
import ContactsUI

class ForSelectionOfContactViewController: BaseTableViewController {
     // MARK: - Handle All Contacts

    /// Shows all contacts in the contacts picker view.
    override func handleAllContacts() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Email Addresses

    /**
        Allows users to select contacts with email addresses. Uses
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​) to return the
        selected contact information upon the view controller dismissal.
        Users will be able to select contacts without email addresses. However,
        the selected contact's information will not be returned.
    */
    override func handleContactsWithEmailAddresses() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfContact = NSPredicate(format: "emailAddresses.@count > 0")
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Postal Addresses

    /**
        Allows users to select contacts with postal addresses. Uses
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​) to return the
        selected contact information upon the view controller dismissal.
        Users will be able to select contacts without birthday. However, the
        selected contact's information will not be returned.
    */
    override func handleContactsWithPostalAddresses() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfContact = NSPredicate(format: "postalAddresses.@count > 0")
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Two or More Phone Numbers

    /**
        Allows users to select contacts with two or more phone numbers. Uses
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​) to return the
        selected contact information upon the view controller dismissal.
        Users will be able to select contacts without birthday. However,
        the selected contact's information will not be returned.
    */
    override func handleContactsWithPhoneNumbers() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfContact = NSPredicate(format: "phoneNumbers.@count > 1")
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Profile Picture
    /**
        Allows users to select contacts with a profile picture. Uses
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​) to return the
        selected contact information upon the view controller dismissal.
        Users will be able to select contacts without a profile picture. However,
        the selected contact's information will not be returned.
    */
    override func handleContactsWithProfilePicture() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfContact = NSPredicate(format: "imageDataAvailable == true")
        navigationController?.present(picker, animated: true, completion: nil)
    }
}

/**
    Extends `ForSelectionOfContactViewController` to conform to the
    `CNContactPickerDelegate` protocol.
*/
extension ForSelectionOfContactViewController: CNContactPickerDelegate {
    /**
        Returns the selected contact meeting the predicateForSelectionOfContact
        predicate.
    */
    func contactPicker(_ picker: CNContactPickerViewController, didSelect contact: CNContact) {
        selectedContact = contact
    }

    /// Called when tapping "Cancel" in the contacts picker view.
    func contactPickerDidCancel(_ picker: CNContactPickerViewController) {
        print("\(AppConfiguration.Messages.dismissPicker)")
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-BaseTableViewContro.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfPrope.md)

