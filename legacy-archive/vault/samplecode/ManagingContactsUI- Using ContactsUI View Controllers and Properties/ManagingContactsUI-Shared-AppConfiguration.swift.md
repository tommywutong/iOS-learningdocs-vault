---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_Shared_AppConfiguration_swift.html
archived_at: '2026-07-18T03:14:30.335546Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](LICENSE.txt.md)[Previous](ManagingContactsUI-Shared-Helper.swift.md)

# ManagingContactsUI/Shared/AppConfiguration.swift

```
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Handles the application's configuration information.
*/

import Foundation

class AppConfiguration {
    // MARK: - AppConfiguration.TableViewCellLabels

    struct TableViewCellLabels {
        static let contact = "Contact:"
        static let key = "Key:"
        static let label = "Label:"
        static let namelessContact = "No Name"
        static let value = "Value:"
    }

    // MARK: - AppConfiguration.TableViewCellLabels

    struct TableViewCellIdentifiers {
        static let cell = "cellID"
    }

    // MARK: - AppConfiguration.Messages

    struct Messages {
        static let accessDeniedOrRestricted = "Access denied or restricted."
        static let added = "was successfully added."
        static let couldNotFind = " Could not find"
        static let error = "Error: "
        static let dismissPicker = "Dismissing contact picker view controller."
        static let inContacts = "in Contacts."
        static let okButton = "OK"
        static let status = "Status"
        static let wasSelected = "was selected."
    }
}
```

[Next](LICENSE.txt.md)[Previous](ManagingContactsUI-Shared-Helper.swift.md)

