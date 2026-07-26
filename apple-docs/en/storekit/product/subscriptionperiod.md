---
title: Product.SubscriptionPeriod
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionperiod
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod.json'
content_hash: 'sha256:b811c1a28788c331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.SubscriptionPeriod

<sub>Structure</sub>

Values that represent the duration of time between subscription renewals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionPeriod
```

## Overview

Use the [value](subscriptionperiod/value.md) and the [unit](subscriptionperiod/unit-swift.property.md) together to determine the subscription period. For example, if the unit is [Product.SubscriptionPeriod.Unit.month](subscriptionperiod/unit-swift.enum/month.md), and the [value](subscriptionperiod/value.md) is `3`, the subscription period is three months.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the subscription period

- [value](subscriptionperiod/value.md) — The number of period units.
- [unit](subscriptionperiod/unit-swift.property.md) — The increment of time for the subscription period.
- [Unit](subscriptionperiod/unit-swift.enum.md) — Units of time that describe subscription periods.

### Getting the period date range

- [dateRange(referenceDate:)](<subscriptionperiod/daterange(referencedate_).md>) — The calculated date range of a subscription period, starting at the reference date.

### Getting subscription periods

- [everySixMonths](subscriptionperiod/everysixmonths.md)
- [everyThreeDays](subscriptionperiod/everythreedays.md)
- [everyThreeMonths](subscriptionperiod/everythreemonths.md)
- [everyTwoMonths](subscriptionperiod/everytwomonths.md)
- [everyTwoWeeks](subscriptionperiod/everytwoweeks.md)
- [monthly](subscriptionperiod/monthly.md)
- [weekly](subscriptionperiod/weekly.md)
- [yearly](subscriptionperiod/yearly.md)

### Formatting the subscription period

- [formatted(_:referenceDate:)](<subscriptionperiod/formatted(__referencedate_)-3t7wd.md>) — Formats the subscription period using a format style that takes a date range as an input.
- [formatted(_:referenceDate:)](<subscriptionperiod/formatted(__referencedate_)-8s3ar.md>) — Formats the subscription period using a format style that takes a duration as an input.

## See Also

### Getting subscription information

- [subscription](subscription.md) — The subscription information for an auto-renewable subscripton.
- [SubscriptionInfo](subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionOffer](subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
- [Status](subscriptioninfo/status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
