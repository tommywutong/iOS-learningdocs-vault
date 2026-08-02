---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCHelperClass_swift.html
archived_at: '2026-07-18T03:14:28.569788Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-BaseViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-SearchViewController.swift.md)

# ManagingContacts/ManagingContacts/MGCHelperClass.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A helper class that is used to create an alert.
*/

import UIKit

class MGCHelperClass {
    // MARK: - Create Alert Dialog

    /// - returns: An alert with a given title and message.
    class func alert(with title: String, message: String) -> UIAlertController {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .actionSheet)

        let action = UIAlertAction(title: NSLocalizedString(MGCAppConfiguration.Messages.ok, comment: MGCAppConfiguration.MainStoryboard.Cells.emptyString),
                                   style: .default,
                                 handler: nil)

        alert.addAction(action)
        return alert
    }
}
```

[Next](ManagingContacts-ManagingContacts-BaseViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-SearchViewController.swift.md)

