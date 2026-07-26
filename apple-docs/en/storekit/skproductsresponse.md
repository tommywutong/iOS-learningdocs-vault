---
title: SKProductsResponse
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsresponse
source_url: 'https://developer.apple.com/documentation/storekit/skproductsresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsresponse.json'
content_hash: 'sha256:63adb61e28e9c6eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductsResponse

<sub>Class</sub>

An App Store response to a request for information about a list of products.

> [!warning] Deprecated
> Get products using Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKProductsResponse
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Response Information

- [products](skproductsresponse/products.md) — A list of products, one product for each valid product identifier provided in the original request. _(deprecated)_
- [invalidProductIdentifiers](skproductsresponse/invalidproductidentifiers.md) — An array of product identifier strings that the App Store doesn’t recognize. _(deprecated)_

## See Also

### Product information

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md) — Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md) — Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [SKProductsRequest](skproductsrequest.md) — An object that can retrieve localized information from the App Store about a specified list of products. _(deprecated)_
- [SKProduct](skproduct.md) — Information about a registered product in App Store Connect. _(deprecated)_
