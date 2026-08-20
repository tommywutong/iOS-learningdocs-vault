---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_Payments_PaymentsFramework_ContactLookup_swift.html
archived_at: '2026-07-18T03:13:01.046873Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-Payments-PaymentsFramework-Contact.swift.md)[Previous](Projects-Payments-PaymentsFramework-DictionaryRepresentable.swift.md)

# Projects/Payments/PaymentsFramework/ContactLookup.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A class that mimics asynchronous lookups of contacts.
*/


public class ContactLookup {

    public var contacts = Contact.sampleContacts

    public init() {}

    public func lookup(displayName: String, completion: (_ contacts: [Contact]) -> Void) {
        /*
            Here we are searching through a local array of contacts. This could
            instead be an asynchronous call to a remote server.
         */
        let nameFormatter = PersonNameComponentsFormatter()

        let matchingContacts = contacts.filter { contact in
            nameFormatter.style = .medium
            if nameFormatter.string(from: contact.nameComponents) == displayName {
                return true
            }

            nameFormatter.style = .short
            if nameFormatter.string(from: contact.nameComponents) == displayName {
                return true
            }

            return false
        }

        completion(matchingContacts)
    }

    public func lookup(emailAddress: String, completion: (_ contact: Contact?) -> Void) {
        /*
            Here we are searching through a local array of contacts. This could
            instead be an asynchronous call to a remote server.
         */
        for contact in contacts where contact.emailAddress == emailAddress {
            completion(contact)
        }

        completion(nil)
    }
}
```

[Next](Projects-Payments-PaymentsFramework-Contact.swift.md)[Previous](Projects-Payments-PaymentsFramework-DictionaryRepresentable.swift.md)

