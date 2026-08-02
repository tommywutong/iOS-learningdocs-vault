---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_Contact_DictionaryRepresentable_swift.html
archived_at: '2026-07-18T03:13:01.083336Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-Payment%2BDictionaryRepresentable.swift.md)[Previous](Projects-Payments-PaymentsFramework-PaymentsFramework.h.md)

# Projects/Payments/PaymentsFramework/Contact+DictionaryRepresentable.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `Contact` to allow it to be represented as and initialized with an `NSDictionary`.
*/

import Foundation

extension Contact: DictionaryRepresentable {
    // MARK: Types

    private struct DictionaryKeys {
        static let familyName = "familyName"
        static let givenName = "givenName"
        static let emailAddress = "emailAddress"
    }

    // MARK: DictionaryRepresentable

    var dictionaryRepresentation: [String : Any] {
        var dictionary = [String: Any]()

        dictionary[DictionaryKeys.familyName] = nameComponents.familyName ?? ""
        dictionary[DictionaryKeys.givenName] = nameComponents.givenName ?? ""
        dictionary[DictionaryKeys.emailAddress] = emailAddress

        return dictionary
    }

    init?(dictionaryRepresentation dictionary: [String: Any]) {
        guard let emailAddress = dictionary[DictionaryKeys.emailAddress] as? String, !emailAddress.isEmpty else { return nil }

        var nameComponents = PersonNameComponents()
        nameComponents.familyName = dictionary[DictionaryKeys.familyName] as? String
        nameComponents.givenName = dictionary[DictionaryKeys.givenName] as? String

        self.nameComponents = nameComponents
        self.emailAddress = emailAddress
    }
}
```

[Next](Projects-Payments-PaymentsFramework-Payment%2BDictionaryRepresentable.swift.md)[Previous](Projects-Payments-PaymentsFramework-PaymentsFramework.h.md)

