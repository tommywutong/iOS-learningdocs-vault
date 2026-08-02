---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_Payment_DictionaryRepresentable_swift.html
archived_at: '2026-07-18T03:13:01.314700Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-Payment.swift.md)[Previous](Projects-Payments-PaymentsFramework-Contact%2BDictionaryRepresentable.swift.md)

# Projects/Payments/PaymentsFramework/Payment+DictionaryRepresentable.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `Payment` to allow it to be represented as and initialized with an `NSDictionary`.
*/

import Foundation

extension Payment: DictionaryRepresentable {
    // MARK: Types

    private struct DictionaryKeys {
        static let contact = "contact"
        static let amount = "amount"
        static let currencyCode = "currencyCode"
        static let date = "date"
    }

    // MARK: DictionaryRepresentable

    var dictionaryRepresentation: [String : Any] {
        var dictionary = [String: Any]()

        dictionary[DictionaryKeys.contact] = contact.dictionaryRepresentation
        dictionary[DictionaryKeys.amount] = amount.doubleValue
        dictionary[DictionaryKeys.currencyCode] = currencyCode

        if let date = date {
            dictionary[DictionaryKeys.date] = date
        }

        return dictionary
    }

    init?(dictionaryRepresentation dictionary: [String: Any]) {
        guard let contactDictionary = dictionary[DictionaryKeys.contact] as? [String: AnyObject], let contact = Contact(dictionaryRepresentation: contactDictionary) else { return nil }
        guard let doubleAmount = dictionary[DictionaryKeys.amount] as? Double else { return nil }
        guard let currencyCode = dictionary[DictionaryKeys.currencyCode] as? String else { return nil }

        let date = dictionary[DictionaryKeys.date] as? Date

        self.contact = contact
        self.amount = NSDecimalNumber(value: doubleAmount)
        self.currencyCode = currencyCode
        self.date = date
    }
}
```

[Next](Projects-Payments-PaymentsFramework-Payment.swift.md)[Previous](Projects-Payments-PaymentsFramework-Contact%2BDictionaryRepresentable.swift.md)

