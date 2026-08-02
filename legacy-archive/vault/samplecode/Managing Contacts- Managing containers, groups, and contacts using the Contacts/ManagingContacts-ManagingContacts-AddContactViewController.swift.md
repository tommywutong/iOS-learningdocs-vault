---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_AddContactViewController_swift.html
archived_at: '2026-07-18T03:14:27.280223Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-AddContactToGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-EditViewController.swift.md)

# ManagingContacts/ManagingContacts/AddContactViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A table view controller that allows you to enter the first name, 
                last name, organization name, URL address' label and value,
                social profile's label and value, instant message address's label
                and value, and anniversary date or a new contact. Users can create 
                a contact, which is either a person or an organization.
*/

import UIKit
import Contacts

class AddContactViewController: UITableViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    // MARK: - Types

    fileprivate struct SegmentedControl {
        // Specifies the Person contact type.
        static let personSegment = 0
        // Specifies the Organization contact type.
        static let organizationSegment = 1
    }


    // MARK: - Properties

    @IBOutlet weak fileprivate var profileImage: UIImageView!
    @IBOutlet weak fileprivate var firstName: UITextField!
    @IBOutlet weak fileprivate var lastName: UITextField!
    @IBOutlet weak fileprivate var organization: UITextField!

    @IBOutlet weak fileprivate var lblURL: UITextField!
    @IBOutlet weak fileprivate var url: UITextField!

    @IBOutlet weak fileprivate var lblSocialProfile: UITextField!
    @IBOutlet weak fileprivate var socialProfile: UITextField!

    @IBOutlet weak fileprivate var lblInstantMessage: UITextField!
    @IBOutlet weak fileprivate var instantMessage: UITextField!

    /// Stores the entered anniversary.
    private var dateComponentsPicked: NSDateComponents?

    /// Indicates whether the user has selected a profile picture for their contact.
    fileprivate var didSelectPicture: Bool?

    /**
        - returns: A model object representing a CNContact object. 
                   Contains information entered by the user.
    */
    var contact: MGCContact!

    /**
        - returns: A Boolean value that indicates whether the user has tapped 
                   "Person" in the segmented control.
                   true implies that the user wishes to create a contact of type 
                   Person.
                   false implies that the user wishes to create a contact of type 
                   Organization.
    */
    fileprivate var didSelectPersonSegment: Bool = true {
        didSet {
            if didSelectPersonSegment {
                navigationItem.rightBarButtonItem!.isEnabled = !(firstName.text!.isEmpty) || !(lastName.text!.isEmpty)
            }
            else {
                navigationItem.rightBarButtonItem!.isEnabled = !(organization.text!.isEmpty)
            }
        }
    }


     // MARK: - View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()
    }


    // MARK: - UITextFieldDelegate

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()

        /* Enable Save in the navigation bar when textField has a value and the
           user has tapped Done on the keyboard of textField, which is either
           firstName, lastName, or organization.
        */
        if ((textField == firstName || textField == lastName) && didSelectPersonSegment) || (textField == organization && !didSelectPersonSegment) {
            navigationItem.rightBarButtonItem!.isEnabled = !(textField.text!.isEmpty)
        }
        return true
    }

    func textFieldDidBeginEditing(_ textField: UITextField) {
        /* Disable Save when textField has a value and the user has started
            typing into the firstName, lastName, or organization text fields.
        */
        if (textField == firstName || textField == organization || textField == lastName) && (!textField.text!.isEmpty) {
            navigationItem.rightBarButtonItem!.isEnabled = false
        }
    }


     // MARK: - Date Picker

    /// Handle date picker selection.
    @IBAction fileprivate func datePickerValueChanged(_ sender: UIDatePicker) {
        dateComponentsPicked = NSCalendar.current.dateComponents(Set([.day, .month]), from: sender.date) as NSDateComponents?
    }


    // MARK: - Segmented Control Tap

    /// Handle segmented control taps.
    @IBAction fileprivate func segmentedControlValueChanged(_ sender: UISegmentedControl) {
        // Set status to true if "Person" was tapped and false, otherwise.
        didSelectPersonSegment = (sender.selectedSegmentIndex == SegmentedControl.personSegment) ? true : false
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
        let selectedImage = info[UIImagePickerControllerOriginalImage] as! UIImage

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
        if navigationItem.rightBarButtonItem == sender as? UIBarButtonItem {
            // Create a model contact to be passed back for update.
            contact = MGCContact(isPerson: didSelectPersonSegment,
                                 lastName: lastName.text!,
                                firstName: firstName.text!,
                             organization: organization.text!,
                                      url: MGCLabelValue(label: lblURL.text!, value: url.text!),
                            socialProfile: MGCLabelValue(label: lblSocialProfile.text!, value: socialProfile.text!),
                           instantMessage: MGCLabelValue(label: lblInstantMessage.text!, value: instantMessage.text!),
                              anniversary: dateComponentsPicked)

            if let _ = self.didSelectPicture, let image = profileImage.image, let imgData = UIImagePNGRepresentation(image) {
                contact.profilePicture = MGCLabelValue(imageData: imgData)
            }
        }
    }


    // MARK: - Memory Management

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
```

[Next](ManagingContacts-ManagingContacts-AddContactToGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-EditViewController.swift.md)

