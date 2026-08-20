---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_DictionaryRepresentable_swift.html
archived_at: '2026-07-18T03:13:01.213495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-ContactLookup.swift.md)[Previous](LICENSE.txt.md)

# Projects/Payments/PaymentsFramework/DictionaryRepresentable.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A type that implements the `DictionaryRepresentable` can be represented as and initialized with an `NSDictionary`.
*/

import Foundation

protocol DictionaryRepresentable {

    var dictionaryRepresentation: [String: Any] { get }

    init?(dictionaryRepresentation dictionary: [String: Any])
}
```

[Next](Projects-Payments-PaymentsFramework-ContactLookup.swift.md)[Previous](LICENSE.txt.md)

