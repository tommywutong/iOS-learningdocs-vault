---
title: 'fetchStorePromotionOrder(completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionorder(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionorder%28completionhandler%3A%29.json'
content_hash: 'sha256:4f02611382284ed0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductStorePromotionController](../skproductstorepromotioncontroller.md)

# fetchStorePromotionOrder(completionHandler:)

<sub>Instance Method</sub>

Reads the product order override that determines the promoted product order on this device.

> [!warning] Deprecated
> Use Product.PromotionInfo.currentOrder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func fetchStorePromotionOrder(completionHandler: (@Sendable ([SKProduct], (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func promotionOrder() async throws -> [SKProduct]
```

## Discussion

This function returns an array of promoted products whose order is overridden on the given device.

If all the products appear in the default order, this method returns an empty array.

## See Also

### Managing promoted product order

- [- updateStorePromotionOrder:completionHandler:](<update(storepromotionorder_completionhandler_).md>) — Overrides the promoted product order on this device. _(deprecated)_
