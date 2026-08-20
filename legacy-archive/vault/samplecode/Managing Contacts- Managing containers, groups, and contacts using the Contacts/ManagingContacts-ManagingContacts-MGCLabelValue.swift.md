---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCLabelValue_swift.html
archived_at: '2026-07-18T03:14:28.591686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCMenuSection.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCContact.swift.md)

# ManagingContacts/ManagingContacts/MGCLabelValue.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Structure used to represent a CNLabeledValue object.
*/

import UIKit

struct MGCLabelValue {
    // MARK: - Properties

    /// Maps to the label of a contact property value.
    var label: String

    /// Maps to a contact property value whose type is String such as the URL address.
    var value: String

    /// Maps to a contact property value whose type is Data such as the profile picture.
    var imageData: Data?

    /// Maps to a contact property value whose type is CNPostalAddress such as the postal address.
    var address: MGCPostalAddress?


    // MARK: - Initialization

    init(label: String = String(), value: String = String(), imageData: Data? = nil, address: MGCPostalAddress? = nil) {
        self.label = label
        self.value = value
        self.imageData = imageData
        self.address = address
    }


    // MARK: - hasLabelValue

    /// - returns: true if label and value both have values and false, otherwise.
    func hasLabelValue() -> Bool {
        return (!(label.isEmpty) && !(value.isEmpty))
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCMenuSection.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCContact.swift.md)

