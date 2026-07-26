---
title: descriptionVisibility
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/descriptionvisibility
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/descriptionvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/descriptionvisibility.json'
content_hash: 'sha256:dd0539f752ab4093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../subscriptionstorecontrolstyleconfiguration.md)

# descriptionVisibility

<sub>Instance Property</sub>

The visibility of product descriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var descriptionVisibility: Visibility { get }
```

## Discussion

Use this property if you choose to support configuring the description visibility in your custom style. It reflects the value that the ancestor view sets with the [productDescription(_:)](<../../swiftui/view/productdescription(__).md>) view modifier.
