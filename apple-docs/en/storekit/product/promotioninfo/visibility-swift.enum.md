---
title: Product.PromotionInfo.Visibility
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo/visibility-swift.enum
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/visibility-swift.enum.json'
content_hash: 'sha256:c73f381e1aa493da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# Product.PromotionInfo.Visibility

<sub>Enumeration</sub>

The visibility states for product promotion information.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum Visibility
```

## Overview

Use the visibility states to set the [visibility](visibility-swift.property.md) of a promoted in-app purchase. Call [update()](<update().md>) to save your changes.

The visibility states have the following effects on the user’s device:

- [Product.PromotionInfo.Visibility.visible](visibility-swift.enum/visible.md) makes the promoted in-app purchase visible in the App Store.
- [Product.PromotionInfo.Visibility.hidden](visibility-swift.enum/hidden.md) hides the promoted in-app purchase in the App Store.
- [Product.PromotionInfo.Visibility.appStoreConnectDefault](visibility-swift.enum/appstoreconnectdefault.md) let’s you control the visibility using settings in App Store Connect. For more information, see [Promote in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md)

## Topics

### Getting visibility states

- [Product.PromotionInfo.Visibility.appStoreConnectDefault](visibility-swift.enum/appstoreconnectdefault.md) — A visibility value for a promoted in-app purchase that uses the visibility setting from App Store Connect.
- [Product.PromotionInfo.Visibility.hidden](visibility-swift.enum/hidden.md) — A visibility value that hides a promoted in-app purchase on the App Store on a user’s device.
- [Product.PromotionInfo.Visibility.visible](visibility-swift.enum/visible.md) — A visibility value that makes a promoted in-app purchase visible on the App Store on a user’s device.

## See Also

### Managing promotion visibility

- [visibility](visibility-swift.property.md) — A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.
- [updateProductVisibility(_:for:)](<updateproductvisibility(__for_).md>) — Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.
