---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_UpdateContactViewController_swift.html
archived_at: '2026-07-18T03:14:29.281094Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCContact.swift.md)[Previous](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)

# ManagingContacts/ManagingContacts/UpdateContactViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to update the following 
                properties of an existing contact: profile picture's thumbnail, 
                first name, last name, organization name, email, phone number, 
                and postal address (street, city, state, country, and zip code).
*/

import UIKit

class UpdateContactViewController: UITableViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate, UITextFieldDelegate {
    // MARK: - Properties

    @IBOutlet weak fileprivate var profileImage: UIImageView!
    @IBOutlet weak fileprivate var firstName: UITextField!
    @IBOutlet weak fileprivate var lastName: UITextField!
    @IBOutlet weak fileprivate var organization: UITextField!

    @IBOutlet weak fileprivate var lblEmail: UILabel!
    @IBOutlet weak fileprivate var email: UITextField!
    @IBOutlet weak fileprivate var lblPhoneNumber: UILabel!
    @IBOutlet weak fileprivate var phoneNumber: UITextField!

    @IBOutlet weak fileprivate var street: UITextField!
    @IBOutlet weak fileprivate var city: UITextField!
    @IBOutlet weak fileprivate var state: UITextField!
    @IBOutlet weak fileprivate var country: UITextField!
    @IBOutlet weak fileprivate var zipCode: UITextField!

    /**
        - returns: A model object representing a CNContact object. Contains
                   information to be updated.
    */
    var contact: MGCContact!

    /// Indicates whether the user has selected a profile picture for their contact.
    fileprivate var didSelectPicture: Bool?

    // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
        configureView(withContact: contact)
    }


    // MARK: - Update UI

    /// Update the UI with the provided contact information.
    fileprivate func configureView(withContact contact: MGCContact) {
        // Update the profile image if the provided contact's imageData exists.
        if let withProfilePicture = contact.profilePicture, let imageData = withProfilePicture.imageData {
            profileImage.image = UIImage(data: imageData as Data)
        }

        // Update the name textfields.
        firstName.text = contact.firstName
        lastName.text = contact.lastName
        organization.text = contact.organization


        // Update the email textfield and its matching label.
        if let withEmail = contact.email {

            lblEmail.text = withEmail.label
            email.text = withEmail.value
        }

        // Update the phone number field and its matching label.
        if let withPhoneNumber = contact.phoneNumber {

            lblPhoneNumber.text = withPhoneNumber.label
            phoneNumber.text = withPhoneNumber.value
        }

        // Update the postal address fields.
        if let withPostalAddress = contact.postalAddress {

            let postalAddress = withPostalAddress.address
            street.text = postalAddress!.street
            city.text = postalAddress!.city
            state.text = postalAddress!.state
            zipCode.text = postalAddress!.postalCode
            country.text = postalAddress!.country
        }
    }


    // MARK: - UITextFieldDelegate

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
         textField.resignFirstResponder()

        // Enable Save in the navigation bar when textField has a value.
        navigationItem.rightBarButtonItem!.isEnabled = !(textField.text!.isEmpty)
        return true
    }

    func textFieldDidBeginEditing(_ textField: UITextField) {
        // Disable Save anytime the user is editing a textfield.
        navigationItem.rightBarButtonItem!.isEnabled = false
    }


    // MARK: - UIImagePickerControllerDelegate

    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        // Dismiss the picker if the user canceled the operation.
        dismiss(animated: true, completion: nil)
    }

    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        /* The info dictionary contains multiple representations of the image. 
           Let's use the original one.
        */
        guard let selectedImage = info[UIImagePickerControllerOriginalImage] as? UIImage else { return }

        // Set profileImage to display the selected image.
        profileImage.image = selectedImage

        /* profilePicture is set to defaultPhoto, by default. When the user
           selects a picture from the Photo library, we replace defaultPhoto
           with it and set didSelectPicture to true.
        */
        didSelectPicture = true

        // Also enable Save the navigation bar when the user has selected an image.
        navigationItem.rightBarButtonItem!.isEnabled = true

        // Dismiss the picker.
        dismiss(animated: true, completion: nil)
    }


    // MARK: - Select a Profile Picture

    /// Allows the user to select a profile picture for their contact.
    @IBAction fileprivate func selectProfilePicture(_ sender: UITapGestureRecognizer) {
        /* UIImagePickerController is a view controller that lets a user pick
           media from their photo library.
        */
        let imagePickerController = UIImagePickerController()

        // Only allow photos to be picked, not taken.
        imagePickerController.sourceType = .photoLibrary

        // Make sure ViewController is notified when the user picks an image.
        imagePickerController.delegate = self

        present(imagePickerController, animated: true, completion: nil)
    }


    // MARK: - Navigation

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        /* Fetch and send back all entered values after the user has tapped
           Save in the navigation bar.
        */
        if navigationItem.rightBarButtonItem == sender as? UIBarButtonItem {

            if let image = profileImage.image, let imgData = UIImagePNGRepresentation(image), let _ = self.didSelectPicture {
                contact.profilePicture = MGCLabelValue(imageData: imgData)
            }

            contact.firstName = firstName.text!
            contact.lastName = lastName.text!
            contact.organization = organization.text!

            contact.email = MGCLabelValue(label: lblEmail.text!, value: email.text!)
            contact.phoneNumber = MGCLabelValue(label: lblPhoneNumber.text!, value: phoneNumber.text!)

            let postalAddress = MGCPostalAddress(street: street.text!, city: city.text!, state: state.text!, postalCode: zipCode.text!, country: country.text!)
            if let currentPostalAddress = contact.postalAddress {
                contact.postalAddress = MGCLabelValue(label: currentPostalAddress.label, address: postalAddress)
            }
            else {
                contact.postalAddress = MGCLabelValue(address: postalAddress)
            }
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCContact.swift.md)[Previous](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)

