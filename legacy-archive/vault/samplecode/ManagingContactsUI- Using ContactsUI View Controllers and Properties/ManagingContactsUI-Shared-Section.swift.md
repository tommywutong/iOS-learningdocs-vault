---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_Shared_Section_swift.html
archived_at: '2026-07-18T03:14:30.519806Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-Shared-LabelValue.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectSingleContact.swift.md)

# ManagingContactsUI/Shared/Section.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Structure used to represent a section of LabelValue items.
*/

import Foundation

struct Section {
    // MARK: - Properties

    /// Title of the section.
    var title: String?

    /// Contains a section  of LabelValue items.
    var section: [LabelValue]

    // MARK: - Initializers

    init(title: String? = nil, section: [LabelValue]) {
        self.title = title
        self.section = section
    }
}
```

[Next](ManagingContactsUI-Shared-LabelValue.swift.md)[Previous](ManagingContactsUI-ContactPickerViewController-SelectSingleContact.swift.md)

