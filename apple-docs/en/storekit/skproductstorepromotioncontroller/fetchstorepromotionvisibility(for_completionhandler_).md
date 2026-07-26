---
title: 'fetchStorePromotionVisibility(for:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionvisibility(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotioncontroller/fetchstorepromotionvisibility%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:996c64ef06e10522'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductStorePromotionController](../skproductstorepromotioncontroller.md)

# fetchStorePromotionVisibility(for:completionHandler:)

<sub>Instance Method</sub>

Reads the visibility setting of a promoted product in the App Store for this device.

> [!warning] Deprecated
> Get visibility from Product.PromotionInfo.currentOrder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func fetchStorePromotionVisibility(for product: SKProduct, completionHandler: (@Sendable (SKProductStorePromotionVisibility, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func promotionVisibility(for product: SKProduct) async throws -> SKProductStorePromotionVisibility
```

## Discussion

The default visibility for a promoted product is set in App Store Connect. Call [- fetchStorePromotionVisibilityForProduct:completionHandler:](<fetchstorepromotionvisibility(for_completionhandler_).md>) to determine if a product’s visibility is set to the default value or if it has been overridden to be hidden or shown.

## See Also

### Managing promoted product visibility

- [- updateStorePromotionVisibility:forProduct:completionHandler:](<update(storepromotionvisibility_for_completionhandler_).md>) — Updates the visibility of the product on the App Store, per device. _(deprecated)_
- [SKProductStorePromotionVisibility](../skproductstorepromotionvisibility.md) — The visibility settings that determine if an in-app purchase is visible on a device. _(deprecated)_
