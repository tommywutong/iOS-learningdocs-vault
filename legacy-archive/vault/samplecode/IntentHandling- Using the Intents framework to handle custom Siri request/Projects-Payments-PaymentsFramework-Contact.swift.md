---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_Contact_swift.html
archived_at: '2026-07-18T03:13:01.119944Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-PaymentsFramework.h.md)[Previous](Projects-Payments-PaymentsFramework-ContactLookup.swift.md)

# Projects/Payments/PaymentsFramework/Contact.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A struct that defines a contact that can receive payments from our app.
*/

import Intents

public struct Contact {

    private static let nameFormatter = PersonNameComponentsFormatter()

    public let nameComponents: PersonNameComponents

    public let emailAddress: String

    public var formattedName: String {
        return Contact.nameFormatter.string(from: nameComponents)
    }

    public init(givenName: String?, familyName: String?, emailAddress: String) {
        var nameComponents = PersonNameComponents()
        nameComponents.givenName = givenName
        nameComponents.familyName = familyName

        self.nameComponents = nameComponents
        self.emailAddress = emailAddress
    }

}

public extension Contact {
    static let sampleContacts = [
        Contact(givenName: "Anne", familyName: "Johnson", emailAddress: "anne.johnson@example.com"),
        Contact(givenName: "Maria", familyName: "Ruiz", emailAddress: "maria.ruiz@example.com"),
        Contact(givenName: "Mei", familyName: "Chen", emailAddress: "mei.chen@example.com"),
        Contact(givenName: "Gita", familyName: "Kumar", emailAddress: "gita.kumar@example.com"),
        Contact(givenName: "Bill", familyName: "James", emailAddress: "bill.james@example.com"),
        Contact(givenName: "Tom", familyName: "Clark", emailAddress: "tom.clark@example.com"),
        Contact(givenName: "Juan", familyName: "Chavez", emailAddress: "juan.chavez@example.com"),
        Contact(givenName: "Ravi", familyName: "Patel", emailAddress: "ravi.patel@example.com"),
    ]
}
```

[Next](Projects-Payments-PaymentsFramework-PaymentsFramework.h.md)[Previous](Projects-Payments-PaymentsFramework-ContactLookup.swift.md)

