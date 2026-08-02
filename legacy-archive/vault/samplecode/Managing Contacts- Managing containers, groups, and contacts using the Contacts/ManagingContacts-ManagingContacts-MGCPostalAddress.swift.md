---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCPostalAddress_swift.html
archived_at: '2026-07-18T03:14:28.846685Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-AddGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-TextFieldCell.swift.md)

# ManagingContacts/ManagingContacts/MGCPostalAddress.swift

```
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Structure used to represent a CNPostalAddress object.
*/

import UIKit

struct MGCPostalAddress {
    // MARK: - Properties

    /// Maps to the postal address' street.
    var street = String()

    /// Maps to the postal address' city.
    var city = String()

    /// Maps to the postal address' state.
    var state = String()

    /// Maps to the postal address' postal code.
    var postalCode = String()

    /// Maps to the postal address' country.
    var country = String()
}
```

[Next](ManagingContacts-ManagingContacts-AddGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-TextFieldCell.swift.md)

