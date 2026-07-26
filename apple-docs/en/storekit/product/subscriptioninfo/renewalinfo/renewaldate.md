---
title: renewalDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/renewaldate
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/renewaldate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/renewaldate.json'
content_hash: 'sha256:b9b7b5f75d01b570'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# renewalDate

<sub>Instance Property</sub>

The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
var renewalDate: Date? { get }
```

## Discussion

The [renewalDate](renewaldate.md) is a value that’s always present for auto-renewable subscriptions, even for expired subscriptions. This date indicates the expiration date of the most recent auto-renewable subscription purchase, including renewals, and may be in the past. For subscriptions that renew successfully, the [renewalDate](renewaldate.md) is the date when the subscription renews.

## See Also

### Getting subscription dates

- [recentSubscriptionStartDate](recentsubscriptionstartdate.md) — The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.
