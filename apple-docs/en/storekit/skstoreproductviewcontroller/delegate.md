---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontroller/delegate.json'
content_hash: 'sha256:fe44a28889d6302d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreProductViewController](../skstoreproductviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The store view controller’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
weak var delegate: (any SKStoreProductViewControllerDelegate)? { get set }
```

## Discussion

Your application must set the delegate before presenting the store view controller.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Setting a delegate

- [SKStoreProductViewControllerDelegate](../skstoreproductviewcontrollerdelegate.md) — A protocol to call when the customer dismisses the store screen.
