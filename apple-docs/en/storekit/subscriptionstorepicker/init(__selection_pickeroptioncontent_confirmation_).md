---
title: 'init(_:selection:pickerOptionContent:confirmation:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstorepicker/init(_:selection:pickeroptioncontent:confirmation:)'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorepicker/init(_:selection:pickeroptioncontent:confirmation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorepicker/init%28_%3Aselection%3Apickeroptioncontent%3Aconfirmation%3A%29.json'
content_hash: 'sha256:d7d477510737cef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStorePicker](../subscriptionstorepicker.md)

# init(_:selection:pickerOptionContent:confirmation:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ configuration: SubscriptionStoreControlStyleConfiguration, selection: Binding<SubscriptionStoreControlStyleConfiguration.Option?>, @ViewBuilder pickerOptionContent: @escaping (SubscriptionStoreControlStyleConfiguration.PickerOption) -> PickerContent, @ViewBuilder confirmation: @escaping (SubscriptionStoreControlStyleConfiguration.Option) -> ConfirmationContent)
```

## See Also

### Managing a subscription picker’s selection state

- [init(selection:pickerContent:confirmation:)](<init(selection_pickercontent_confirmation_).md>)
