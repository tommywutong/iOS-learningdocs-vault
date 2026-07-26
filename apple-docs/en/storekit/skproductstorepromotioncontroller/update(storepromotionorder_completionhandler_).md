---
title: 'update(storePromotionOrder:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionorder:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotioncontroller/update%28storepromotionorder%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:bdd84353133418bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductStorePromotionController](../skproductstorepromotioncontroller.md)

# update(storePromotionOrder:completionHandler:)

<sub>Instance Method</sub>

Overrides the promoted product order on this device.

> [!warning] Deprecated
> Use Product.PromotionInfo.updateProductOrder(byID:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func update(storePromotionOrder promotionOrder: [SKProduct], completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func update(promotionOrder: [SKProduct]) async throws
```

## Discussion

The default order of promoted in-app purchase products is set in App Store Connect. You can override this order per device. For example, you can promote an in-app purchase product that unlocks a specific level in your game when a user reaches the level immediately before the specified level.

To override the default product order, put the product information for the subset of products you want to reorder into an array, in the order you want them to appear in. Pass the array to the [- updateStorePromotionOrder:completionHandler:](<update(storepromotionorder_completionhandler_).md>) method. The products in the array are shown at the beginning of the list, followed by the remaining in-app purchase products, which are listed in the same relative order that you set in App Store Connect.

To cancel order overrides, send an empty product array to the [- updateStorePromotionOrder:completionHandler:](<update(storepromotionorder_completionhandler_).md>) method.  The in-app purchase products will be displayed in the default order.

## See Also

### Managing promoted product order

- [- fetchStorePromotionOrderWithCompletionHandler:](<fetchstorepromotionorder(completionhandler_).md>) — Reads the product order override that determines the promoted product order on this device. _(deprecated)_
