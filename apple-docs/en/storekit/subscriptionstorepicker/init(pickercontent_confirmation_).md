---
title: 'init(pickerContent:confirmation:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstorepicker/init(pickercontent:confirmation:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorepicker/init(pickercontent:confirmation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorepicker/init%28pickercontent%3Aconfirmation%3A%29.json'
content_hash: 'sha256:585641d56634cf31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStorePicker](../subscriptionstorepicker.md)

# init(pickerContent:confirmation:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(@ViewBuilder pickerContent: () -> PickerContent, @ViewBuilder confirmation: @escaping (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)
```

## See Also

### Creating a subscription store picker

- [init(_:pickerOptionContent:confirmation:)](<init(__pickeroptioncontent_confirmation_).md>)
