---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCMenuSection_swift.html
archived_at: '2026-07-18T03:14:28.658618Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-UpdateGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCLabelValue.swift.md)

# ManagingContacts/ManagingContacts/MGCMenuSection.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class used to represent a section of features in a tab.
*/

import UIKit

class MGCMenuSection {
    // MARK: - Properties

    /// Title of the section.
    var title: String

    /// Contains a section of features.
    var section: [MGCMenuSectionFeature]


    // MARK: - Initialization

    init(title: String, section: [MGCMenuSectionFeature]) {
        self.title = title
        self.section = section
    }
}
```

[Next](ManagingContacts-ManagingContacts-UpdateGroupViewController.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCLabelValue.swift.md)

