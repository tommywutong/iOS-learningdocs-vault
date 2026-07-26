---
title: 'dateRange(referenceDate:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptionperiod/daterange(referencedate:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/daterange(referencedate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/daterange%28referencedate%3A%29.json'
content_hash: 'sha256:648331e4033b5b53'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionPeriod](../subscriptionperiod.md)

# dateRange(referenceDate:)

<sub>Instance Method</sub>

The calculated date range of a subscription period, starting at the reference date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
func dateRange(referenceDate: Date = .now) -> Range<Date>
```

## Parameters

- `referenceDate` — A date you provide that indicates the lower bound of the returned date range. The default value is [now](../../../foundation/date/now.md).

## Return Value

The subscription period represented by two dates that are the lower bound and upper bound of the subscription period of the [SubscriptionPeriod](../subscriptionperiod.md) instance.

## Discussion

The date range calculates a single subscription period starting from the date you provide in `referenceDate`.

For example, if the subscription period of the [SubscriptionPeriod](../subscriptionperiod.md) instance is one month, and the `referenceDate` is February 1, the date range contains February 1 and March 1. If the `referenceDate` is Feb 15, the date range contains February 15 and March 15.

Use the [dateRange(referenceDate:)](<daterange(referencedate_).md>) with a [Date.ComponentsFormatStyle](../../../foundation/date/componentsformatstyle.md) to get a human-readable string representation of the subscription period.

Get the format style ([Date.ComponentsFormatStyle](../../../foundation/date/componentsformatstyle.md)) corresponding to product’s storefront using the [subscriptionPeriodFormatStyle](../subscriptionperiodformatstyle.md).
