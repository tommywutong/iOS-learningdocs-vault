---
title: 'init(_:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstorebutton/init(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorebutton/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorebutton/init%28_%3A%29.json'
content_hash: 'sha256:6fb47b4a1dfc656b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreButton](../subscriptionstorebutton.md)

# init(_:)

<sub>Initializer</sub>

Creates a button with an automatic label that describes the subscription option and starts a subscribe interaction when someone selects the button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ option: SubscriptionStoreControlStyleConfiguration.Option)
```

## Discussion

You receive [Option](../subscriptionstorecontrolstyleconfiguration/option.md) values to initialize the subscribe button from the [makeBody(configuration:)](<../subscriptionstorecontrolstyle/makebody(configuration_).md>) method of your custom subscription store control style.
