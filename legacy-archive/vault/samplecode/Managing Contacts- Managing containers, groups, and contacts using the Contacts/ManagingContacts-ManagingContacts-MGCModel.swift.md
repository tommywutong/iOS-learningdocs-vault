---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCModel_swift.html
archived_at: '2026-07-18T03:14:28.758140Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-MGCParsingUtilities.swift.md)[Previous](ManagingContacts-ManagingContacts-ContactsMenu.swift.md)

# ManagingContacts/ManagingContacts/MGCModel.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class used to populate the UI and perform navigation between
                scenes.
*/

import UIKit

class MGCModel {
    // MARK: - Properties

    /// Specifies the tab to be populated.
    var tab = String()

    /// Specifies the tab's content.
    var content = [AnyObject]()

    /// Determines which information to display in the tab.
    var category: String?

    /// Specifies the segue to be executed.
    var segue: MGCSegue?


    // MARK: - Initialization

    init(tab: String, content: [AnyObject] = [], category: String? = nil, segue: MGCSegue? = nil) {
        self.tab = tab
        self.content = content
        self.category = category
        self.segue = segue
    }
}
```

[Next](ManagingContacts-ManagingContacts-MGCParsingUtilities.swift.md)[Previous](ManagingContacts-ManagingContacts-ContactsMenu.swift.md)

