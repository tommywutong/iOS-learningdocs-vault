---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewControllerWithPredicates_ForSelectionOfPropertyViewController_swift.html
archived_at: '2026-07-18T03:14:29.818437Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfConta.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-AppDelegate.swift.md)

# ManagingContactsUI/ContactPickerViewControllerWithPredicates/ForSelectionOfPropertyViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements CNContactPickerViewController's predicateForSelectionOfProperty
  instance property. Allows users to select and return any contact property when
  using the "All Contacts" feature and specific contact properties
  (emailAddresses, postalAddresses, and phoneNumbers) when using the other features.
  Contact properties that don't meet the above criteria will be selectable and
  implement their default action, but they will not be returned.
*/

import UIKit
import ContactsUI

class ForSelectionOfPropertyViewController: BaseTableViewController {
    // MARK: - Handle All Contacts

    /// Show all contacts.
    override func handleAllContacts() {
        let picker = CNContactPickerViewController()
        picker.delegate = self

        /*
            Only show the given and family names, email addresses, phone numbers,
            and postal addresses of a contact.
        */
        picker.displayedPropertyKeys = [CNContactGivenNameKey, CNContactFamilyNameKey, CNContactEmailAddressesKey,
                                        CNContactPhoneNumbersKey, CNContactPostalAddressesKey]
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Email Addresses

    /**
        When users select a contact's email address, it dismisses the view
        controller and returns the email address using
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​). When users select
        other properties, it implements their default action.
    */
    override func handleContactsWithEmailAddresses() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfProperty = NSPredicate(format: "(key == 'emailAddresses')")
        navigationController?.present(picker, animated: true, completion: nil)
    }

    // MARK: - Handle Contacts With Postal Addresses

    /**
        When users select a contact's postal address, it dismisses the view
        controller and returns the birthday using
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​). When users select
        other properties, it implements their default action.
    */
    override func handleContactsWithPostalAddresses() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfProperty = NSPredicate(format: "key == 'postalAddresses'")
        navigationController?.present(picker, animated: true, completion: nil)
    }

     // MARK: - Handle Contacts With Two or More Phone Numbers

    /**
        When users select a contact's phone number, it dismisses the view
        controller and returns the phone number using
        CNContactPickerDelegate's contact​Picker(_:​did​Select:​). When users select
        other properties, it implements their default action.
    */
    override func handleContactsWithPhoneNumbers() {
        let picker = CNContactPickerViewController()
        picker.delegate = self
        picker.predicateForSelectionOfProperty = NSPredicate(format: "key == 'phoneNumbers'")
        navigationController?.present(picker, animated: true, completion: nil)
    }
}

/**
    Extends `ForSelectionOfPropertyViewController` to conform to the
    `CNContactPickerDelegate` protocol.
*/
extension ForSelectionOfPropertyViewController: CNContactPickerDelegate {
    /**
        Called when tapping the contact property associated a feature such as
        emailAddresses, postalAddresses, or phoneNumbers.
    */
    func contactPicker(_ picker: CNContactPickerViewController, didSelect contactProperty: CNContactProperty) {
        selectedContactProperty = contactProperty
    }

    /// Called when tapping "Cancel" in the contacts picker view.
    func contactPickerDidCancel(_ picker: CNContactPickerViewController) {
        print("\(AppConfiguration.Messages.dismissPicker)")
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfConta.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-AppDelegate.swift.md)

