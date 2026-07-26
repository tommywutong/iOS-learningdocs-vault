---
title: 'subscript(dynamicMember:)'
framework: StoreKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-8sl2m'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-8sl2m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option/subscript%28dynamicmember%3A%29-8sl2m.json'
content_hash: 'sha256:615480b313d34f9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [Option](../option.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Facilitates accessing optional subscription properties on an option value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<Product.SubscriptionInfo, T?>) -> T? { get }
```

## Discussion

You don’t use this subscript directly. Instead, access the properties of a [SubscriptionInfo](../../product/subscriptioninfo.md) directly on a [Option](../option.md) value. For an example of using a dynamic member lookup, see [Option](../option.md).

## See Also

### Looking up dynamic members

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-wjww.md>) — Facilitates accessing subscription properties on an option value.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-9g2sm.md>) — Facilitates accessing product properties on an option value.
