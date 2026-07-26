---
title: SKProductSubscriptionPeriod
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductsubscriptionperiod
source_url: 'https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductsubscriptionperiod.json'
content_hash: 'sha256:1e58c8135ddd1950'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductSubscriptionPeriod

<sub>Class</sub>

An object containing the subscription period duration information.

> [!warning] Deprecated
> Use Product.SubscriptionPeriod.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKProductSubscriptionPeriod
```

## Overview

A subscription period is a duration of time defined as some number of units, where a unit can be a [SKProductPeriodUnitDay](skproduct/periodunit/day.md), [SKProductPeriodUnitWeek](skproduct/periodunit/week.md), [SKProductPeriodUnitMonth](skproduct/periodunit/month.md), or [SKProductPeriodUnitYear](skproduct/periodunit/year.md).

For example, a subscription period of two weeks has a [unit](skproductsubscriptionperiod/unit.md) of a [SKProductPeriodUnitWeek](skproduct/periodunit/week.md), and a  [numberOfUnits](skproductsubscriptionperiod/numberofunits.md) equal to `2`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Subscription Period Details

- [numberOfUnits](skproductsubscriptionperiod/numberofunits.md) — The number of units per subscription period. _(deprecated)_
- [unit](skproductsubscriptionperiod/unit.md) — The increment of time that a subscription period is specified in. _(deprecated)_
- [PeriodUnit](skproduct/periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_

## See Also

### Getting Subscription Information

- [subscriptionGroupIdentifier](skproduct/subscriptiongroupidentifier.md) — The identifier of the subscription group to which the subscription belongs. _(deprecated)_
- [subscriptionPeriod](skproduct/subscriptionperiod.md) — The period details for products that are subscriptions. _(deprecated)_
- [PeriodUnit](skproduct/periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_
