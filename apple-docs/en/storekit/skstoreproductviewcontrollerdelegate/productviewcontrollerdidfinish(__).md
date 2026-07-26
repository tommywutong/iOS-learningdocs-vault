---
title: 'productViewControllerDidFinish(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontrollerdelegate/productviewcontrollerdidfinish%28_%3A%29.json'
content_hash: 'sha256:dbe7f016ea97238c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreProductViewControllerDelegate](../skstoreproductviewcontrollerdelegate.md)

# productViewControllerDidFinish(_:)

<sub>Instance Method</sub>

Called when the user dismisses the store screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func productViewControllerDidFinish(_ viewController: SKStoreProductViewController)
```

## Parameters

- `viewController` — The store view controller whose interface was dismissed by the user.

## Discussion

Your delegate should call the [dismissModalViewControllerAnimated:](../../uikit/uiviewcontroller/dismissmodalviewcontrolleranimated_.md) method on the view controller that originally presented the store screen. If your app paused any other activities before presenting the store, it can restart those services in this method.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
