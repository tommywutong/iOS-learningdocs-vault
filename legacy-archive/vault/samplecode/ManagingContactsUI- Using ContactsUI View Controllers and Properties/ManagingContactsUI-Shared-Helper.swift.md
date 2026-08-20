---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_Shared_Helper_swift.html
archived_at: '2026-07-18T03:14:30.432160Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-Shared-AppConfiguration.swift.md)[Previous](ManagingContactsUI-Shared-AppExtensions.swift.md)

# ManagingContactsUI/Shared/Helper.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A helper class that is used to create an alert.
*/

import UIKit

class Helper {
    // MARK: - Create Alert

    /// - returns: An alert with a given title and message.
    class func alert(with message: String) -> UIAlertController {
        let alert = UIAlertController(title: AppConfiguration.Messages.status, message: message, preferredStyle: .actionSheet)

        let action = UIAlertAction(title: NSLocalizedString(AppConfiguration.Messages.okButton, comment: message),
                                   style: .default,
                                 handler: nil)

        alert.addAction(action)
        return alert
    }
}
```

[Next](ManagingContactsUI-Shared-AppConfiguration.swift.md)[Previous](ManagingContactsUI-Shared-AppExtensions.swift.md)

