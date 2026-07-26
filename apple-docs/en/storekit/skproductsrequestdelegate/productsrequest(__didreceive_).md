---
title: 'productsRequest(_:didReceive:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductsrequestdelegate/productsrequest(_:didreceive:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/productsrequest(_:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsrequestdelegate/productsrequest%28_%3Adidreceive%3A%29.json'
content_hash: 'sha256:df0e12759c7d721d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductsRequestDelegate](../skproductsrequestdelegate.md)

# productsRequest(_:didReceive:)

<sub>Instance Method</sub>

Accepts the App Store response that contains the app-requested product information.

> [!warning] Deprecated
> Get products using Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse)
```

## Parameters

- `request` — The product request sent to the Apple App Store.

- `response` — Detailed information about the list of products.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
