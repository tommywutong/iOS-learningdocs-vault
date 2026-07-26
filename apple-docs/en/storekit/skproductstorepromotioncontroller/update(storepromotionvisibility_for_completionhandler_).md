---
title: 'update(storePromotionVisibility:for:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/update(storepromotionvisibility:for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductstorepromotioncontroller/update%28storepromotionvisibility%3Afor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1500cfb2c0d2c221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductStorePromotionController](../skproductstorepromotioncontroller.md)

# update(storePromotionVisibility:for:completionHandler:)

<sub>Instance Method</sub>

Updates the visibility of the product on the App Store, per device.

> [!warning] Deprecated
> Use Product.PromotionInfo.updateProductVisibility(_:for:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func update(storePromotionVisibility promotionVisibility: SKProductStorePromotionVisibility, for product: SKProduct, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func update(promotionVisibility: SKProductStorePromotionVisibility, for product: SKProduct) async throws
```

## Discussion

An in-app purchase product’s default visibility setting is set up in App Store Connect.  You can override the default setting, or return it to the default set in App Store Connect using the values in [SKProductStorePromotionVisibility](../skproductstorepromotionvisibility.md).

Visibility settings apply per device.

## See Also

### Managing promoted product visibility

- [- fetchStorePromotionVisibilityForProduct:completionHandler:](<fetchstorepromotionvisibility(for_completionhandler_).md>) — Reads the visibility setting of a promoted product in the App Store for this device. _(deprecated)_
- [SKProductStorePromotionVisibility](../skproductstorepromotionvisibility.md) — The visibility settings that determine if an in-app purchase is visible on a device. _(deprecated)_
