---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCContact_swift.html
archived_at: '2026-07-18T03:14:28.459271Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCLabelValue.swift.md)[Previous](ManagingContacts-ManagingContacts-UpdateContactViewController.swift.md)

# ManagingContacts/ManagingContacts/MGCContact.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class used to represent a CNContact object.
*/

import UIKit

class MGCContact {
    // MARK: - Properties

    /**
        Maps to the contact type. true indicates that the contact is of type
        Person. false indicates that its type is Organization.
    */
    var isPerson: Bool

    /// Maps to the contact's family name.
    var lastName: String

    /// Maps to the contact's given name.
    var firstName: String

    /// Maps to the contact's associated organization name.
    var organization: String

    /// Maps to the contact's phone number.
    var phoneNumber: MGCLabelValue?

    /// Maps to the contact's email address
    var email: MGCLabelValue?

    /// Maps to the contact's online URL address.
    var url: MGCLabelValue?

    /// Stores the contact's entered anniversary date.
    var anniversary: NSDateComponents?

    /// Maps to the contact's social profile.
    var socialProfile: MGCLabelValue?

    /// Maps to the contact's instant message address.
    var instantMessage: MGCLabelValue?

    /// Maps to the contact's postal address.
    var postalAddress: MGCLabelValue?

    /// Maps to the contact's thumbnail profile picture.
    var profilePicture: MGCLabelValue?


    // MARK: - Initialization

    init(isPerson: Bool = true, lastName: String = String(), firstName: String = String(), organization: String = String(), url: MGCLabelValue? = nil, socialProfile: MGCLabelValue? = nil, instantMessage: MGCLabelValue? = nil, anniversary: NSDateComponents? = nil) {
        self.isPerson = isPerson
        self.lastName = lastName
        self.firstName = firstName
        self.organization = organization
        self.url = url
        self.socialProfile = socialProfile
        self.instantMessage = instantMessage
        self.anniversary = anniversary
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCLabelValue.swift.md)[Previous](ManagingContacts-ManagingContacts-UpdateContactViewController.swift.md)

