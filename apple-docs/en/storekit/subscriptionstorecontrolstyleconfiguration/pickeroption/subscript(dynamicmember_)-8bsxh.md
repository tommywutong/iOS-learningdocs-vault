---
title: 'subscript(dynamicMember:)'
framework: StoreKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-8bsxh'
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-8bsxh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/subscript%28dynamicmember%3A%29-8bsxh.json'
content_hash: 'sha256:7ceedceb2b8137d9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [PickerOption](../pickeroption.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Facilitates accessing product properties on a picker option value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<Product, T>) -> T { get }
```

## Discussion

You don’t use this subscript directly. Instead, access the properties of a [Product](../../product.md) instance directly on a [PickerOption](../pickeroption.md) value.

## See Also

### Dynamic member lookup support

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-2ahxy.md>) — Facilitates accessing optional subscription properties on a picker option value.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-4f3i1.md>) — Facilitates accessing subscription properties on a picker option value.
