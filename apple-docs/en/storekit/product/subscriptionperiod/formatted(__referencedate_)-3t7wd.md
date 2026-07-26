---
title: 'formatted(_:referenceDate:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptionperiod/formatted(_:referencedate:)-3t7wd'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/formatted(_:referencedate:)-3t7wd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/formatted%28_%3Areferencedate%3A%29-3t7wd.json'
content_hash: 'sha256:c7b918bb438f1707'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionPeriod](../subscriptionperiod.md)

# formatted(_:referenceDate:)

<sub>Instance Method</sub>

Formats the subscription period using a format style that takes a date range as an input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
func formatted<S>(_ format: S, referenceDate: Date = .now) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>
```

## Parameters

- `format` — A format style that has a date range input. The format style for a product is [subscriptionPeriodFormatStyle](../subscriptionperiodformatstyle.md).

- `referenceDate` — The lower bound date for a date range representing the subscription period. The default value is [now](../../../foundation/date/now.md).

## Discussion

Use the [formatted(_:referenceDate:)](<formatted(__referencedate_)-3t7wd.md>) method with [subscriptionPeriodFormatStyle](../subscriptionperiodformatstyle.md) to format the subscription period for the App Store locale, as the following example shows.

```swift
// Get a human-readable representation of a subscription period.
subscriptionPeriod.formatted(product.subscriptionPeriodFormatStyle, referenceDate: /* some date */)

```

## See Also

### Formatting the subscription period

- [formatted(_:referenceDate:)](<formatted(__referencedate_)-8s3ar.md>) — Formats the subscription period using a format style that takes a duration as an input.
