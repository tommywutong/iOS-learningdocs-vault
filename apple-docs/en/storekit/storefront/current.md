---
title: current
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storefront/current
source_url: 'https://developer.apple.com/documentation/storekit/storefront/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storefront/current.json'
content_hash: 'sha256:a3bfcfbf8f3e7bce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Storefront](../storefront.md)

# current

<sub>Type Property</sub>

The current App Store storefront for product purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var current: Storefront? { get async }
```

## Discussion

Use [current](current.md) to determine a customer’s current storefront region and offer in-app products suitable for that region. You maintain your own list of product identifiers and the storefronts in which you make them available.

## See Also

### Storefront information

- [Storefront](../storefront.md) — The region and unique identifier of the App Store storefront for the device.
- [updates](updates.md) — The asynchronous sequence that emits storefront information when the system updates the storefront.
