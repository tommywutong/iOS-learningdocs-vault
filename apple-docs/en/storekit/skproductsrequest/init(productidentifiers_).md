---
title: 'init(productIdentifiers:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductsrequest/init(productidentifiers:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductsrequest/init(productidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsrequest/init%28productidentifiers%3A%29.json'
content_hash: 'sha256:b86c70881ab127fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductsRequest](../skproductsrequest.md)

# init(productIdentifiers:)

<sub>Initializer</sub>

Initializes the request with the set of product identifiers.

> [!warning] Deprecated
> Use Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(productIdentifiers: Set<String>)
```

## Parameters

- `productIdentifiers` — The list of product identifiers for the products you wish to retrieve descriptions of.

## Return Value

The initialized request object.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
