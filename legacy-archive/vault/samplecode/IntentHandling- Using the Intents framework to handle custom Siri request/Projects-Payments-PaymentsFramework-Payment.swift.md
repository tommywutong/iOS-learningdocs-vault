---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_Payment_swift.html
archived_at: '2026-07-18T03:13:01.367411Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-PaymentProvider.swift.md)[Previous](Projects-Payments-PaymentsFramework-Payment%2BDictionaryRepresentable.swift.md)

# Projects/Payments/PaymentsFramework/Payment.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A struct that defines a payment made with our app.
*/

import Foundation

public struct Payment: Equatable {

    // MARK: Properties

    public let contact: Contact

    public let amount: NSDecimalNumber

    public let currencyCode: String

    public let date: Date?

    // MARK: Public initializer

    public init(contact: Contact, amount: NSDecimalNumber, currencyCode: String, date: Date? = nil) {
        self.contact = contact
        self.amount = amount
        self.currencyCode = currencyCode
        self.date = date
    }
}

public func ==(lhs: Payment, rhs: Payment) -> Bool {
    return lhs.contact.emailAddress == rhs.contact.emailAddress &&
            lhs.amount == rhs.amount &&
            lhs.currencyCode == rhs.currencyCode &&
            lhs.date == rhs.date
}
```

[Next](Projects-Payments-PaymentsFramework-PaymentProvider.swift.md)[Previous](Projects-Payments-PaymentsFramework-Payment%2BDictionaryRepresentable.swift.md)

