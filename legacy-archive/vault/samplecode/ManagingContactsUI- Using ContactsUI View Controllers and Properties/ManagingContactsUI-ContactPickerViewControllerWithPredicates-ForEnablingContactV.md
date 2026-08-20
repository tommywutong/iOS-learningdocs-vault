---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewControllerWithPredicates_ForEnablingContactViewController_swift.html
archived_at: '2026-07-18T03:14:29.687952Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewController-SelectMultipleContacts.swift.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-BaseTableViewContro.md)

# ManagingContactsUI/ContactPickerViewControllerWithPredicates/ForEnablingContactViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements CNContactPickerViewController's predicateForEnablingContact
  instance property. Shows how to enable all contacts, only contacts that
  have an email address, only contacts with a postal address, only contacts that
  have 2 or more phone numbers, and only contacts that have a profile picture in
  the contact picker view. Users would be able to select enabled contacts and
  view their details. Contacts, which don't meet the above criteria, would be
  disabled in the picker view.
 */

import UIKit
import ContactsUI

class ForEnablingContactViewController: BaseTableViewController {
 // MARK: - Handle All Contacts

 /// Enable all contacts in the contacts picker view.
 override func handleAllContacts() {
    let picker = CNContactPickerViewController()
    navigationController?.present(picker, animated: true, completion: nil)
 }

 // MARK: - Handle Contacts With Email Addresses

 /// Only enable contacts with email addresses in the contacts picker view.
 override func handleContactsWithEmailAddresses() {
    let picker = CNContactPickerViewController()

    // Only show contacts with email addresses.
    picker.predicateForEnablingContact = NSPredicate(format: "emailAddresses.@count > 0")
    navigationController?.present(picker, animated: true, completion: nil)
 }

 // MARK: - Handle Contacts With Postal Addresses

 /// Only enable contacts with postal addresses in the contacts picker view.
 override func handleContactsWithPostalAddresses() {
    let picker = CNContactPickerViewController()

    // Only show contacts with postal addresses.
    picker.predicateForEnablingContact = NSPredicate(format: "postalAddresses.@count > 0")
    navigationController?.present(picker, animated: true, completion: nil)
 }

 // MARK: - Handle Contacts With Two or More Phone Numbers

 /// Only enable contacts with 2 or more phone numbers in the contacts picker view.
 override func handleContactsWithPhoneNumbers() {
    let picker = CNContactPickerViewController()

    // Only show contacts with two or more phone numbers.
    picker.predicateForEnablingContact = NSPredicate(format: "phoneNumbers.@count > 1")
    navigationController?.present(picker, animated: true, completion: nil)
 }

  // MARK: - Handle Contacts With Profile Picture

 /// Only enable contacts with a profile picture in the contacts picker view.
 override func handleContactsWithProfilePicture() {
    let picker = CNContactPickerViewController()

    // Only show contacts with a profile picture.
    picker.predicateForEnablingContact = NSPredicate(format: "imageDataAvailable == true")
    navigationController?.present(picker, animated: true, completion: nil)
 }
}
```

[Next](ManagingContactsUI-ContactPickerViewController-SelectMultipleContacts.swift.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-BaseTableViewContro.md)

