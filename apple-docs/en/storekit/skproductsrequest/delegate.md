---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsrequest/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skproductsrequest/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsrequest/delegate.json'
content_hash: 'sha256:2af695d2411def3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductsRequest](../skproductsrequest.md)

# delegate

<sub>Instance Property</sub>

The delegate that receives the response of the app’s products request.

> [!warning] Deprecated
> Use Product.products(for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any SKProductsRequestDelegate)? { get set }
```

## See Also

### Setting the Delegate

- [SKProductsRequestDelegate](../skproductsrequestdelegate.md) — A set of methods the delegate implements so it receives the product information your app requests. _(deprecated)_
