---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_Payments_AppDelegate_swift.html
archived_at: '2026-07-18T03:13:01.577752Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsIntentsExtension-INPerson%2BContact.swift.md)[Previous](Projects-Payments-Payments-PaymentHistoryViewController.swift.md)

# Projects/Payments/Payments/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
*/

import UIKit
import Intents
import PaymentsFramework

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func applicationDidFinishLaunching(_ application: UIApplication) {
        // Register names of contacts that may not be in the user's address book.
        let contactNames = Contact.sampleContacts.map { $0.formattedName }
        INVocabulary.shared().setVocabularyStrings(NSOrderedSet(array: contactNames), of: .contactName)
    }
}
```

[Next](Projects-Payments-PaymentsIntentsExtension-INPerson%2BContact.swift.md)[Previous](Projects-Payments-Payments-PaymentHistoryViewController.swift.md)

