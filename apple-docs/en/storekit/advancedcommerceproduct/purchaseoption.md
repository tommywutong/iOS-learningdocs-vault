---
title: AdvancedCommerceProduct.PurchaseOption
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/advancedcommerceproduct/purchaseoption
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchaseoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/purchaseoption.json'
content_hash: 'sha256:e01eef2960a86e2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# AdvancedCommerceProduct.PurchaseOption

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PurchaseOption
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Methods

- [onStorefrontChange(shouldContinuePurchase:)](<purchaseoption/onstorefrontchange(shouldcontinuepurchase_).md>) — A closure that determines whether the transaction continues if the device’s App Store storefront changes during a transaction.

## See Also

### Initiating purchases

- [purchase(compactJWS:confirmIn:options:)](<purchase(compactjws_confirmin_options_)-7x4bh.md>) — Processes a purchase for the product.
- [purchase(compactJWS:confirmIn:options:)](<purchase(compactjws_confirmin_options_)-54lkw.md>) — Processes a purchase for the product.
- [purchase(compactJWS:options:)](<purchase(compactjws_options_).md>) — Processes a purchase for the product.
- [PurchaseResult](purchaseresult.md)
