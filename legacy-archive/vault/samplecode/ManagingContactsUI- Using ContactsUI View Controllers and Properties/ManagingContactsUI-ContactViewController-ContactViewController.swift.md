---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_ContactViewController_ContactViewController_swift.html
archived_at: '2026-07-18T03:14:30.251682Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-AppDelegate.swift.md)[Previous](ManagingContactsUI-ContactViewController-AppDelegate.swift.md)

# ManagingContactsUI/ContactViewController/ContactViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shows how to create and display a new contact, an unknown contact, or existing
  contact using the CNContact​View​Controller class. Use the
  highlight​Property(with​Key:​identifier:​) property to highlight the contact's
  iPhone number. Creates and pushes the contact view controller. Demonstrate how
  to dismiss the contact view controller when using init(for​New​Contact:​) to
  create a new contact. Uses CNContact​View​Controller​Delegate's
  contactViewController(_:shouldPerformDefaultActionFor:) to prevent users from
  performing default actions such as dialing a phone number.
 */

import UIKit
import Contacts
import ContactsUI

class ContactViewController: UITableViewController {
    // MARK: - Types

    struct PhoneNumber {
        static let iPhone = "(408) 555-0126"
        static let mobile = "(415) 123-4567"
    }

    struct Name {
        static let family = "Appleseed"
        static let given = "Jane"
    }

    struct Address {
        static let street = "1 Infinite Loop"
        static let city = "Cupertino"
        static let state = "CA"
        static let postalCode = "95014"
    }

    struct CreateNewContact {
        static let textLabel = "Create New Contact"
        static let subtitle = "Enter data for a new contact."
    }

    struct CreateNewContactWithSomeData {
        static let textLabel = "Create New Contact With Existing Data"
        static let subtitle = "Save the new contact."
    }

    struct EditUnknownContact {
        static let textLabel = "Edit Unknown Contact"
        static let subtitle = "Add data to an existing person or use them to create a new contact."
    }

    struct DisplayOrEditContact {
        static let textLabel = "Display and Edit Contact"
        static let subtitle = "Show and edit a contact."
    }

    // MARK: - Properties

    var store = CNContactStore()
    /// Keep track of the selected table row.
    var tableRowSelected: IndexPath?

    /// Key to be highlighted in the view controller.
    var phoneNumberKey = "phoneNumbers"

    /// Message, which includes the contact's name that was successfully added.
    var message: String?

    /**
        Data model for the UI. The "Display and Edit Contact" feature uses
        fetchContact(with:completion:) that requires access to Contacts.
        The data property contains the CreateNewContact,
        CreateNewContactWithSomeData, EditUnknownContact, and
        DisplayOrEditContact structures when access was
        granted and CreateNewContact, CreateNewContactWithSomeData,
        EditUnknownContact, otherwise.
    */
    var data = [Section(section: [LabelValue(label: ContactViewController.CreateNewContact.textLabel,
                                                         value: ContactViewController.CreateNewContact.subtitle)]),
                            Section(section: [LabelValue(label: ContactViewController.CreateNewContactWithSomeData.textLabel,
                                                         value: ContactViewController.CreateNewContactWithSomeData.subtitle)]),
                            Section(section: [LabelValue(label: ContactViewController.EditUnknownContact.textLabel,
                                                         value: ContactViewController.EditUnknownContact.subtitle)])]

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
        checkContactsAccess()
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        /*
            If message exists, then a contact was successfully added.
            Let's show an alert to indicate it.
        */
        if let myMessage = message {
            alert(with: myMessage)
            message = nil
        }
    }
    // MARK: - Display Alert

    /// Create and display an alert.
    func alert(with message: String) {
        let alert = Helper.alert(with: message)
        navigationController?.present(alert, animated: true, completion: nil)
    }

    // MARK: - Contacts Access

    /**
        Checks the authorization status for Contacts. Requests access if the
        returned status is .notDetermined.
    */
    func checkContactsAccess() {
        switch CNContactStore.authorizationStatus(for: .contacts) {
            // Access was granted. Update the UI with the default navigation menu.
            case .authorized: configureMenuNavigation()
            case .notDetermined: self.store.requestAccess(for: .contacts, completionHandler: {(granted, _) in
                    if granted {
                        self.configureMenuNavigation()
                    }})
            // Access was denied or restricted.
            case .restricted, .denied: print(AppConfiguration.Messages.accessDeniedOrRestricted)
        }
    }

    /// Provides the full navigation menu when access was granted to Contacts.
    func configureMenuNavigation() {
        DispatchQueue.main.async {
            self.data = [Section(section: [LabelValue(label: ContactViewController.CreateNewContact.textLabel,
                                                      value: ContactViewController.CreateNewContact.subtitle)]),
                         Section(section: [LabelValue(label: ContactViewController.CreateNewContactWithSomeData.textLabel,
                                                      value: ContactViewController.CreateNewContactWithSomeData.subtitle)]),
                         Section(section: [LabelValue(label: ContactViewController.EditUnknownContact.textLabel,
                                                      value: ContactViewController.EditUnknownContact.subtitle)]),
                         Section(section: [LabelValue(label: ContactViewController.DisplayOrEditContact.textLabel,
                                                      value: ContactViewController.DisplayOrEditContact.subtitle)])]
            self.tableView.reloadData()
        }
    }

    // MARK: - UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        return data.count
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data[section].section.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return tableView.dequeueReusableCell(withIdentifier: AppConfiguration.TableViewCellIdentifiers.cell, for: indexPath)
    }

    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        let  section = data[indexPath.section].section
        let item = section[indexPath.row]

        cell.textLabel?.text = item.label
        cell.detailTextLabel?.text = item.value
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableRowSelected = indexPath

        switch indexPath.section {
            case 0: createContact()
            case 1: createContactWithSomeData()
            case 2: editUnknownContact()
            case 3: displayContact()
            default: break
        }
    }

    // MARK: - Create New Contact

    /**
        Called when users tap "Create New Contact" in the UI. Create and launch
        an empty contacts view controller.
    */
    func createContact() {
        // Create an empty contact view controller.
        let contactViewController = CNContactViewController(forNewContact: nil)
        // Set its delegate.
        contactViewController.delegate = self
        // Push it using the navigation controller.
        navigationController?.pushViewController(contactViewController, animated: true)
    }

    /**
        Called when users tap "Create New Contact With Existing Data" in the UI.
        Create and launch a contacts view controller with pre-filled fields.
    */
    func createContactWithSomeData() {
        let contact = CNMutableContact()

        // Given and family names.
        contact.familyName = ContactViewController.Name.family
        contact.givenName = ContactViewController.Name.given
        // Phone numbers.
        contact.phoneNumbers = [CNLabeledValue(label: CNLabelPhoneNumberiPhone,
                                               value: CNPhoneNumber(stringValue:ContactViewController.PhoneNumber.iPhone)),
                                CNLabeledValue(label: CNLabelPhoneNumberMobile,
                                               value: CNPhoneNumber(stringValue:ContactViewController.PhoneNumber.mobile))]

        // Postal address.
        let homeAddress = CNMutablePostalAddress()
        homeAddress.street = ContactViewController.Address.street
        homeAddress.city = ContactViewController.Address.city
        homeAddress.state = ContactViewController.Address.state
        homeAddress.postalCode = ContactViewController.Address.postalCode
        contact.postalAddresses = [CNLabeledValue(label: CNLabelHome, value: homeAddress)]

        // Create a contact view controller with the above contact.
        let contactViewController = CNContactViewController(forNewContact: contact)
        // Set its delegate.
        contactViewController.delegate = self
        // Push it using the navigation controller.
        navigationController?.pushViewController(contactViewController, animated: true)
    }

    // MARK: - Find Contact

    /// - returns: Exising contacts matching the specified name.
    func fetchContact(with name: String, completion: @escaping (_ contacts: [CNContact]) -> Void) {
        var result = [CNContact]()

        do {
            result = try store.unifiedContacts(matching: CNContact.predicateForContacts(matchingName: name),
                                            keysToFetch: [CNContactViewController.descriptorForRequiredKeys()])
        } catch let error as NSError {
            print("\(AppConfiguration.Messages.error) \(error.localizedDescription)")
        }

        DispatchQueue.main.async {
            completion(result)
        }
    }

     // MARK: - Display Existing Contact

    /**
        Called when users tap "Display and Edit Contact" in the UI. Searches
        for the contact specified whose last name and first name are respectively
        specified by contact.family and contact.given. If the search was
        successful, display the contact, allow users to edit the contact's
        information and to perform actions. Show an alert, otherwise.
    */
    func displayContact() {
        let name = "\(ContactViewController.Name.given) \(ContactViewController.Name.family)"

        fetchContact(with: name, completion: ({(contacts: [CNContact]) in
            DispatchQueue.main.async {
                if !contacts.isEmpty {
                    let contactViewController = CNContactViewController(for: contacts.first!)
                    contactViewController.allowsEditing = true
                    contactViewController.allowsActions = true
                    contactViewController.delegate = self

                    /*
                        Set the view controller's highlightProperty if
                        highlightedPropertyIdentifier exists. Thus, ensuring
                        that the contact's phone number specified by
                        highlightedPropertyIdentifier will be highlighted in the
                        UI.
                    */

                    if let highlightedPropertyIdentifiers = contacts.first?.phoneNumbers.first?.identifier {
                        contactViewController.highlightProperty(withKey: self.phoneNumberKey, identifier: highlightedPropertyIdentifiers)
                    }

                    // Show the view controller.
                    self.navigationController?.pushViewController(contactViewController, animated: true)
                } else {
                    self.alert(with: "\(AppConfiguration.Messages.couldNotFind) \(name) \(AppConfiguration.Messages.inContacts)")
                    if let selectedIndexPath = self.tableRowSelected {
                        self.tableView.deselectRow(at: selectedIndexPath, animated: false)
                    }
                }
            }
        }))
    }

     // MARK: - Display Unknown Contact

    /**
        Called when users tap "Edit Unknown Contact" in the UI. The view
        controller displays some contact information that you can either add to
        an existing contact or use them to create a new contact.
    */
    func editUnknownContact() {
        let contact = CNMutableContact()

        // Phone number.
        contact.phoneNumbers = [CNLabeledValue(label: CNLabelPhoneNumberiPhone,
                                               value: CNPhoneNumber(stringValue: ContactViewController.PhoneNumber.mobile))]
        // Postal address.
        let homeAddress = CNMutablePostalAddress()
        homeAddress.street = ContactViewController.Address.street
        homeAddress.city = ContactViewController.Address.city
        homeAddress.state = ContactViewController.Address.state
        homeAddress.postalCode = ContactViewController.Address.postalCode
        contact.postalAddresses = [CNLabeledValue(label: CNLabelHome, value: homeAddress)]

        // Create a view controller that allows editing.
        let contactViewController = CNContactViewController(forUnknownContact: contact)
        contactViewController.allowsEditing = true
        contactViewController.contactStore = CNContactStore()
        contactViewController.delegate = self

        // Push the unknown contact in the view controler.
        navigationController?.pushViewController(contactViewController, animated: true)
    }
}

/**
    Extends `ContactViewController` to conform to the
    `CNContactViewControllerDelegate` protocol.
*/
extension ContactViewController: CNContactViewControllerDelegate {
    /**
        Setting it to false prevents users to perform default actions such as
        dialing a phone number, when they select a contact property.
    */
    func contactViewController(_ viewController: CNContactViewController, shouldPerformDefaultActionFor property: CNContactProperty) -> Bool {
        return false
    }

    /**
        Used to dismiss the view controller when using init(for​New​Contact:​) to
        create a new contact.
    */
    func contactViewController(_ viewController: CNContactViewController, didCompleteWith contact: CNContact?) {
        if let tableRowSelected = tableRowSelected?.section, tableRowSelected == 0 || tableRowSelected == 1 {
            defer {
                _ = self.navigationController?.popViewController(animated: true)
            }

            guard let contact = contact else {
                return
            }

            message = "\(contact.formattedName) \(AppConfiguration.Messages.added)"
        }
    }
}
```

[Next](ManagingContactsUI-ContactPickerViewControllerWithPredicates-AppDelegate.swift.md)[Previous](ManagingContactsUI-ContactViewController-AppDelegate.swift.md)

