---
title: recentSubscriptionStartDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate.json'
content_hash: 'sha256:3376dbf3d4edff25'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# recentSubscriptionStartDate

<sub>Instance Property</sub>

The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var recentSubscriptionStartDate: Date { get }
```

## Discussion

> [!important] Important
> Don’t use the [recentSubscriptionStartDate](recentsubscriptionstartdate.md) date to calculate days of paid service. For more information about paid days of service, see [Net revenue after a year](https://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

## See Also

### Getting subscription dates

- [renewalDate](renewaldate.md) — The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.
