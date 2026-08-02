---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCMenuSectionFeature_swift.html
archived_at: '2026-07-18T03:14:28.626047Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-ContainersMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-UpdateGroupViewController.swift.md)

# ManagingContacts/ManagingContacts/MGCMenuSectionFeature.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Model class used to represent a feature to be performed in the app.
*/

import UIKit

class MGCMenuSectionFeature {
    // MARK: - Properties

    /// Indicates whether the feature is enabled in the tab.
    var enabled: Bool

    /// Provides the feature's title.
    var label: String

    /// Segue to be performed when the feature is tapped.
    var segue: MGCSegue

    /// Title of the next screen to be displayed after selecting this feature.
    var title: String


    // MARK: - Initialization

    init(enabled: Bool, label: String, segue: MGCSegue, title: String) {
        self.enabled = enabled
        self.label = label
        self.segue = segue
        self.title = title
    }
}
```

[Next](ManagingContacts-ManagingContacts-ContainersMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-UpdateGroupViewController.swift.md)

