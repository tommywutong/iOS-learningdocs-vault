---
title: updates
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storefront/updates
source_url: 'https://developer.apple.com/documentation/storekit/storefront/updates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storefront/updates.json'
content_hash: 'sha256:837a8928a848c98e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Storefront](../storefront.md)

# updates

<sub>Type Property</sub>

The asynchronous sequence that emits storefront information when the system updates the storefront.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var updates: Storefront.Storefronts { get }
```

## Discussion

The storefront value can change at any time. Use [updates](updates.md) to listen for changes in this value. Respond to storefront changes by refreshing the list of your available products.

## See Also

### Storefront information

- [Storefront](../storefront.md) — The region and unique identifier of the App Store storefront for the device.
- [current](current.md) — The current App Store storefront for product purchases.
