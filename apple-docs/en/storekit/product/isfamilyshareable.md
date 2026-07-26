---
title: isFamilyShareable
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/isfamilyshareable
source_url: 'https://developer.apple.com/documentation/storekit/product/isfamilyshareable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/isfamilyshareable.json'
content_hash: 'sha256:e15051d57f249a08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# isFamilyShareable

<sub>Instance Property</sub>

A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let isFamilyShareable: Bool
```

## Discussion

Check the value of [isFamilyShareable](isfamilyshareable.md) to learn whether an in-app purchase is sharable with the family group.

When displaying in-app purchases in your app, indicate whether the product includes Family Sharing to help customers make a selection that best fits their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect. For more information about setting up Family Sharing, see [Turn-on Family Sharing for in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases).
