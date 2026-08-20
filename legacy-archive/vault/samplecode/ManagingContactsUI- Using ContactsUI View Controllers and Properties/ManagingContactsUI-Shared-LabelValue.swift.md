---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_Shared_LabelValue_swift.html
archived_at: '2026-07-18T03:14:30.483008Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-Shared-AppExtensions.swift.md)[Previous](ManagingContactsUI-Shared-Section.swift.md)

# ManagingContactsUI/Shared/LabelValue.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Structure used to represent a label and its value.
*/

import Foundation

struct LabelValue {
    // MARK: - Properties

    var label: String?
    var value: String

    // MARK: - Initializers

    init(label: String? = nil, value: String) {
        self.label = label
        self.value = value
    }
}
```

[Next](ManagingContactsUI-Shared-AppExtensions.swift.md)[Previous](ManagingContactsUI-Shared-Section.swift.md)

