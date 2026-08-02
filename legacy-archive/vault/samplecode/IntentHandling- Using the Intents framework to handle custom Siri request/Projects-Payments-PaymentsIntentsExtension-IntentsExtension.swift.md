---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsIntentsExtension_IntentsExtension_swift.html
archived_at: '2026-07-18T03:13:01.459854Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Ascent-Ascent-AppDelegate.swift.md)[Previous](Projects-Payments-PaymentsIntentsExtension-SendPaymentIntentHandler.swift.md)

# Projects/Payments/PaymentsIntentsExtension/IntentsExtension.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main extension entry point.
*/

import Intents
import PaymentsFramework

class IntentsExtension: INExtension {

    let paymentProvider = PaymentProvider()

    let contactLookup = ContactLookup()

    override func handler(for intent: INIntent) -> Any? {
        // Our sample is only configured to handle the `INSendPaymentIntent`.
        guard intent is INSendPaymentIntent else { fatalError("Unhandled intent type \(intent)") }

        return SendPaymentIntentHandler(paymentProvider: paymentProvider, contactLookup: contactLookup)
    }
}
```

[Next](Projects-Ascent-Ascent-AppDelegate.swift.md)[Previous](Projects-Payments-PaymentsIntentsExtension-SendPaymentIntentHandler.swift.md)

