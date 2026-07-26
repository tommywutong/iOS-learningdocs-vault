---
title: Product.PurchaseError
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseerror
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseerror.json'
content_hash: 'sha256:c888725e2aae6490'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.PurchaseError

<sub>Enumeration</sub>

Error information for product purchase errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PurchaseError
```

## Overview

The [purchase(options:)](<purchase(options_).md>) function may throw a purchase error.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [LocalizedError](../../foundation/localizederror.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting Purchase Error Codes

- [Product.PurchaseError.invalidOfferIdentifier](purchaseerror/invalidofferidentifier.md) — The promotional offer identifier provided in the purchase options is invalid.
- [Product.PurchaseError.productUnavailable](purchaseerror/productunavailable.md) — The product isn’t available.
- [Product.PurchaseError.purchaseNotAllowed](purchaseerror/purchasenotallowed.md) — The user isn’t allowed to make purchases.
- [Product.PurchaseError.ineligibleForOffer](purchaseerror/ineligibleforoffer.md) — The user isn’t eligible for the offer.
- [Product.PurchaseError.invalidOfferPrice](purchaseerror/invalidofferprice.md) — The price of the offer isn’t valid.
- [Product.PurchaseError.invalidOfferSignature](purchaseerror/invalidoffersignature.md) — The offer signature isn’t valid.
- [Product.PurchaseError.invalidQuantity](purchaseerror/invalidquantity.md) — The quantity to purchase is invalid.
- [Product.PurchaseError.missingOfferParameters](purchaseerror/missingofferparameters.md) — The offer parameters are missing.

### Enumeration Cases

- [Product.PurchaseError.paymentMethodBindingConfigurationRequired](purchaseerror/paymentmethodbindingconfigurationrequired.md) — The customer needs to add a payment method to their Apple Account before making a purchase; use [PaymentMethodBinding](../paymentmethodbinding.md) to prompt the customer and bind the payment method.

## See Also

### Purchasing a product

- [purchase(options:)](<purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-3bivf.md>) — Processes a purchase for the product.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-8eai6.md>) — Processes a purchase for the product.
- [PurchaseOption](purchaseoption.md) — Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [PurchaseResult](purchaseresult.md) — The result of a purchase.
