---
title: options
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/section/options
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section/options.json'
content_hash: 'sha256:9e4b28a3d7d60601'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [Section](../section.md)

# options

<sub>Instance Property</sub>

The subscription options to merchandise within a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [SubscriptionStoreControlStyleConfiguration.Option]
```

## Discussion

This property represents the main content of a section. The view your style creates needs to provide a control to subscribe to each option in the array.

Use the properties of each [Option](../option.md) value to declare your control style, and use the [subscribe()](<../option/subscribe().md>) method in response to a subscribe interaction.

> [!tip] Tip
> Use [SubscriptionOptionSection](../../subscriptionoptionsection.md) to configure the contents of a section when creating a [SubscriptionStoreView](../../subscriptionstoreview.md).
