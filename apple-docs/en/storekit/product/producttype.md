---
title: Product.ProductType
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/producttype
source_url: 'https://developer.apple.com/documentation/storekit/product/producttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/producttype.json'
content_hash: 'sha256:23dec41360967d8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.ProductType

<sub>Structure</sub>

The types of in-app purchases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ProductType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the Product Type

- [consumable](producttype/consumable.md) — A consumable in-app purchase.
- [nonConsumable](producttype/nonconsumable.md) — A non-consumable in-app purchase.
- [nonRenewable](producttype/nonrenewable.md) — A non-renewing subscription.
- [autoRenewable](producttype/autorenewable.md) — An auto-renewable subscription.

### Getting a Localized Description

- [localizedDescription](producttype/localizeddescription.md)

### Type Properties

- [subscriptionBundle](producttype/subscriptionbundle.md) _(beta)_
- [subscriptionSuite](producttype/subscriptionsuite.md) _(beta)_

## See Also

### Getting product identifiers and type

- [id](id.md) — The unique product identifier.
- [type](type.md) — The in-app purchase product type.
