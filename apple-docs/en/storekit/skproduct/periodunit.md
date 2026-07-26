---
title: SKProduct.PeriodUnit
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/periodunit
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/periodunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/periodunit.json'
content_hash: 'sha256:bc1456b0a3dd5825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# SKProduct.PeriodUnit

<sub>Enumeration</sub>

Values representing the duration of an interval, from a day up to a year.

> [!warning] Deprecated
> Use Product.SubscriptionPeriod.Unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PeriodUnit
```

## Overview

The period unit represents the duration of an interval. Period units are used with the number of units to determine one period in [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Period Units

- [SKProductPeriodUnitDay](periodunit/day.md) — An interval lasting one day. _(deprecated)_
- [SKProductPeriodUnitMonth](periodunit/month.md) — An interval lasting one month. _(deprecated)_
- [SKProductPeriodUnitWeek](periodunit/week.md) — An interval lasting one week. _(deprecated)_
- [SKProductPeriodUnitYear](periodunit/year.md) — An interval lasting one year. _(deprecated)_

### Initializers

- [init(rawValue:)](<periodunit/init(rawvalue_).md>) _(deprecated)_

## See Also

### Getting Subscription Information

- [subscriptionGroupIdentifier](subscriptiongroupidentifier.md) — The identifier of the subscription group to which the subscription belongs. _(deprecated)_
- [subscriptionPeriod](subscriptionperiod.md) — The period details for products that are subscriptions. _(deprecated)_
- [SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md) — An object containing the subscription period duration information. _(deprecated)_
