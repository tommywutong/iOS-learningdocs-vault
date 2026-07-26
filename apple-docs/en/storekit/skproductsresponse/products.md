---
title: products
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsresponse/products
source_url: 'https://developer.apple.com/documentation/storekit/skproductsresponse/products'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsresponse/products.json'
content_hash: 'sha256:a6108707e0d8b60b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductsResponse](../skproductsresponse.md)

# products

<sub>Instance Property</sub>

A list of products, one product for each valid product identifier provided in the original request.

> [!warning] Deprecated
> Get products using Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var products: [SKProduct] { get }
```

## Discussion

The array consists of a list of [SKProduct](../skproduct.md) objects.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Response Information

- [invalidProductIdentifiers](invalidproductidentifiers.md) — An array of product identifier strings that the App Store doesn’t recognize. _(deprecated)_
