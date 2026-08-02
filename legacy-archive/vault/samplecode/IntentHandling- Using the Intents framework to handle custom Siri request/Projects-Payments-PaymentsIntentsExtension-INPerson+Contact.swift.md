---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsIntentsExtension_INPerson_Contact_swift.html
archived_at: '2026-07-18T03:13:01.431425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsIntentsExtension-SendPaymentIntentHandler.swift.md)[Previous](Projects-Payments-Payments-AppDelegate.swift.md)

# Projects/Payments/PaymentsIntentsExtension/INPerson+Contact.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Extends `INPerson` to add an initializer that accepts a `Contact`.
*/

import PaymentsFramework
import Intents

extension INPerson {
    convenience init(contact: Contact) {
        let handle = INPersonHandle(value: contact.emailAddress, type: .emailAddress)
        self.init(personHandle: handle, nameComponents: contact.nameComponents, displayName: contact.formattedName, image: nil, contactIdentifier: nil, customIdentifier: nil)
    }
}
```

[Next](Projects-Payments-PaymentsIntentsExtension-SendPaymentIntentHandler.swift.md)[Previous](Projects-Payments-Payments-AppDelegate.swift.md)

