---
title: isInBillingRetry
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/isinbillingretry
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/isinbillingretry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/isinbillingretry.json'
content_hash: 'sha256:6c77a7c9720f104a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# isInBillingRetry

<sub>Instance Property</sub>

A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let isInBillingRetry: Bool
```

## Discussion

This field indicates whether Apple is attempting to automatically renew an expired subscription. If a subscription expires due to a billing issue, a value of `true` indicates that Apple is still trying to renew the subscription. If the subscription is in a billing grace period, the optional [gracePeriodExpirationDate](graceperiodexpirationdate.md) contains a date.

Use the [isInBillingRetry](isinbillingretry.md) value along with [expirationReason](expirationreason-swift.property.md) for more insight, as the following table shows:

| Values | Description |
|---|---|
| [isInBillingRetry](isinbillingretry.md) is `false,` ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)  [expirationReason](expirationreason-swift.property.md) is `nil` | The auto-renewable subscription is active and not in a billing retry period.  ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is entitled to service. |
| [isInBillingRetry](isinbillingretry.md) is `true,` ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [expirationReason](expirationreason-swift.property.md) is [billingError](expirationreason-swift.struct/billingerror.md), ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [gracePeriodExpirationDate](graceperiodexpirationdate.md) has a date | The auto-renewable subscription is in a billing grace period.  ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is entitled to service until the date in [gracePeriodExpirationDate](graceperiodexpirationdate.md). |
| [isInBillingRetry](isinbillingretry.md) is `true,` ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [expirationReason](expirationreason-swift.property.md) is [billingError](expirationreason-swift.struct/billingerror.md), ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [gracePeriodExpirationDate](graceperiodexpirationdate.md) is `nil` | The auto-renewable subscription is in a billing retry period.  ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is not entitled to service. |
| [isInBillingRetry](isinbillingretry.md) is `false,`  ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [expirationReason](expirationreason-swift.property.md) is [billingError](expirationreason-swift.struct/billingerror.md) | The auto-renewable subscription expired and billing retry wasn’t able to recover the subscription. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is not entitled to service. |

## See Also

### Getting billing status

- [gracePeriodExpirationDate](graceperiodexpirationdate.md) — The date the billing grace period expires for the auto-renewable subscription.
