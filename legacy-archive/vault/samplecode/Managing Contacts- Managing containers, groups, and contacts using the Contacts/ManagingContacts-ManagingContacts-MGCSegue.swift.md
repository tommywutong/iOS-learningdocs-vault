---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_MGCSegue_swift.html
archived_at: '2026-07-18T03:14:28.866837Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-AppDelegate.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCParsingUtilities.swift.md)

# ManagingContacts/ManagingContacts/MGCSegue.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Structure used to represent segues to be performed after selecting a
                feature. Defines main to take the user from the main screen of
                a tab to a final screen that displays the expected results associated 
                with the selected feature.
                Defines related to take the user from the main screen of a tab
                to an intermediate screen that allows you to select
                containers, groups, or contacts, then to the final screen that 
                displays the expected results associated with the selected feature.
                Main properties starting with "perform" indicate that
                implementing its associated feature will involve navigating between
                three screens: the main screen of a tab, intermediate screen, and 
                final screen that displays the feature's expected results.
*/

import UIKit

struct MGCSegue {
    // MARK: - Properties

    /// First segue executed after selecting a feature.
    var main: String

    /// Second segue executed from an intermediate screen to the final screen.
    var related: String?


    // MARK: - Initialization

    init(main: String, related: String? = nil) {
        self.main = main
        self.related = related
    }
}
```

[Next](ManagingContacts-ManagingContacts-AppDelegate.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCParsingUtilities.swift.md)

