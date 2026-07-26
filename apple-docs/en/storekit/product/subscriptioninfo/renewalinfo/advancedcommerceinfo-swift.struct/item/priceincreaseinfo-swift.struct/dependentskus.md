---
title: dependentSKUs
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.2+, iPadOS 26.2+, macOS 26.2+, tvOS 26.2+, visionOS 26.2+, watchOS 26.2+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/dependentskus
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/dependentskus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/dependentskus.json'
content_hash: 'sha256:80228cfae89da510'
translated: false
---

> Navigation: [Technologies](../../../../../../../technologies.md) · [StoreKit](../../../../../../../storekit.md) · [Product](../../../../../../product.md) · [SubscriptionInfo](../../../../../subscriptioninfo.md) · [RenewalInfo](../../../../renewalinfo.md) · [AdvancedCommerceInfo](../../../advancedcommerceinfo-swift.struct.md) · [Item](../../item.md) · [PriceIncreaseInfo](../priceincreaseinfo-swift.struct.md)

# dependentSKUs

<sub>Instance Property</sub>

An array of one or more SKUs on which the current subscription offer depends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let dependentSKUs: [String]
```

## Discussion

You can provide a list of SKUs and create a contingency scenario in which a person’s refusal to agree to a price increase results in the App Store canceling other, bundled services (the _dependent SKUs_). If the price increase requires a personʼs consent, and they don’t consent but instead cancel the subscription in the Manage Subscriptions view, the App Store cancels the dependent SKUs.

> [!important] Important
> You can’t create chains of dependent SKUs; for example, if SKU A has a dependent SKU B, B can’t have its own dependent SKU, C. However, B can have its own price increase.

## See Also

### Information about a price increase

- [price](price.md) — The cost of the price increase in the location-specific currency.
- [status](status-swift.property.md) — The status of the price increase.
