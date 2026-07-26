---
title: descriptionVisibility
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/productviewstyleconfiguration/descriptionvisibility
source_url: 'https://developer.apple.com/documentation/storekit/productviewstyleconfiguration/descriptionvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productviewstyleconfiguration/descriptionvisibility.json'
content_hash: 'sha256:5a4788f6a9cf3b9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductViewStyleConfiguration](../productviewstyleconfiguration.md)

# descriptionVisibility

<sub>Instance Property</sub>

The visibility of product descriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let descriptionVisibility: Visibility
```

## Discussion

Subscription products have a localized [description](../product/description.md) property that you can conditionally display in your custom style. Use the [descriptionVisibility](../subscriptionstorecontrolstyleconfiguration/descriptionvisibility.md) property to check the value that the  [productDescription(_:)](<../../swiftui/view/productdescription(__).md>) view modifier configures on an ancestor of the [SubscriptionStoreView](../subscriptionstoreview.md).

Ignore this property if your style doesn’t need the capability to conditionally display the product description. For example, a compact control style may never show product descriptions.

If the view heirarachy doesn’t use the [productDescription(_:)](<../../swiftui/view/productdescription(__).md>) view modifier, the [descriptionVisibility](../subscriptionstorecontrolstyleconfiguration/descriptionvisibility.md) property is [automatic](../subscriptionstorecontrolstyle/automatic.md).
