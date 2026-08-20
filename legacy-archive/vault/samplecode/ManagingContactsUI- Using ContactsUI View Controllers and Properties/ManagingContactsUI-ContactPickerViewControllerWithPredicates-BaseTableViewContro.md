---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactPickerViewControllerWithPredicates_BaseTableViewController_swift.html
archived_at: '2026-07-18T03:14:29.622948Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForEnablingContactV.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfConta.md)

# ManagingContactsUI/ContactPickerViewControllerWithPredicates/BaseTableViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A base view controller to share a table view between subclasses. Displays a
  navigation menu ("All Contacts", "Contacts with Email Addresses", "Contacts
  with Postal Addresses", "Contacts with Two or More Phone Numbers", "Contacts with
  Phone Numbers", and "Contacts with Profile Picture") and "Show Picker."
  Select any of the features then "Show Picker" to implement the associated
  feature.
 */

import UIKit
import Contacts

class BaseTableViewController: UITableViewController {
    // MARK: - Properties

    var selectedContact: CNContact?
    var selectedCellRowIndexPath: IndexPath?
    var selectedContactProperty: CNContactProperty?

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        /*
            Select "All Contacts" by default unless another feature is
            already selected.
        */
        let selection: IndexPath! = (selectedCellRowIndexPath == nil) ? IndexPath(row: 0, section: 0) : selectedCellRowIndexPath
        tableView.selectRow(at: selection, animated: true, scrollPosition: .top)
        tableView(tableView, didSelectRowAt: selection)

        if let fullName = selectedContact?.formattedName {
            alert(with: "\(fullName) \(AppConfiguration.Messages.wasSelected)")
            selectedContact = nil
        }

        if let property = selectedContactProperty, let value = property.nameMatchingValue, let key = property.nameMatchingKey?.lowercased() {
            alert(with: "\(property.contact.formattedName)'s \(key) (\(value)) \(AppConfiguration.Messages.wasSelected)")
            selectedContactProperty = nil
        }
    }

    // MARK: - Display Alert

    /// Create and display an alert.
    func alert(with message: String) {
        let alert = Helper.alert(with: message)
        present(alert, animated: true, completion: nil)
    }

    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: tableView.indexPathForSelectedRow!, animated: false)

        // "Show Picker" was tapped, implements the selected navigation feature.
        if indexPath == IndexPath(row: 0, section: 1) {
            showPicker()
        } else {
            // Add a checkmark to the selected feature.
            if let selectedIndexPath = selectedCellRowIndexPath {
                guard selectedIndexPath == indexPath else {
                    let newCell = tableView.cellForRow(at: indexPath)
                    let currentCell = tableView.cellForRow(at: selectedIndexPath)

                    if newCell?.accessoryType == UITableViewCellAccessoryType.none {
                        newCell?.accessoryType = UITableViewCellAccessoryType.checkmark
                        selectedCellRowIndexPath = indexPath
                    }

                    if currentCell?.accessoryType == UITableViewCellAccessoryType.checkmark {
                        currentCell?.accessoryType = UITableViewCellAccessoryType.none
                    }
                    return
                }
            } else {
                let newCell = tableView.cellForRow(at: indexPath)
                newCell?.accessoryType = .checkmark
                selectedCellRowIndexPath = indexPath
            }
        }
    }

    // MARK: - Show Contacts Picker

    /**
        Implements any of the following features:
        "All Contacts", "Contacts with Email Addresses", "Contacts
        with Postal Addresses", "Contacts with Two or More Phone Numbers",
        "Contacts with Phone Numbers", and "Contacts with Profile Picture."
    */
    func showPicker() {
        if let selectedCellRowIndexPath = selectedCellRowIndexPath {
            switch selectedCellRowIndexPath.row {
                // "All Contacts" was selected, implement handleAllContacts().
                case 0: handleAllContacts()
                /*
                    "Contacts with Email Addresses" was selected, implement
                    handleContactsWithEmailAddresses().
                */
                case 1: handleContactsWithEmailAddresses()
                /*
                    "Contacts with Postal Addresses" was selected, implement
                    handleContactsWithPostalAddresses().
                */
                case 2: handleContactsWithPostalAddresses()
                /*
                    "Contacts with Two or More Phone Numbers" or "Contacts with
                     Phone Numbers" was selected, implement
                     handleContactsWithPhoneNumbers(().
                */
                case 3: handleContactsWithPhoneNumbers()
                /*
                    "Contacts with Profile Picture" was selected, implement
                    handleContactsWithProfilePicture().
                */
                case 4: handleContactsWithProfilePicture()
               default: break
            }
        }
    }

    // MARK: - Predicate Handling Methods

    /// Implements the "All Contacts" feature.
    func handleAllContacts() {
    }

    /// Implements the "Contacts with Email Addresses" feature.
    func handleContactsWithEmailAddresses() {
    }

    /// Implements the "Contacts with Postal Addresses" feature.
    func handleContactsWithPostalAddresses() {
    }

    /**
        Implements the "Contacts with Two or More Phone Numbers" or "Contacts
        with Phone Numbers" feature.
    */
    func handleContactsWithPhoneNumbers() {
    }

    /// Implements the "Contacts with Profile Picture" feature.
    func handleContactsWithProfilePicture() {
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForEnablingContactV.md)[Previous](ManagingContactsUI-ContactPickerViewControllerWithPredicates-ForSelectionOfConta.md)

