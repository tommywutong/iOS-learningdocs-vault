---
title: 'formatted(_:referenceDate:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptionperiod/formatted(_:referencedate:)-8s3ar'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/formatted(_:referencedate:)-8s3ar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/formatted%28_%3Areferencedate%3A%29-8s3ar.json'
content_hash: 'sha256:f584f3868ed3b76c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionPeriod](../subscriptionperiod.md)

# formatted(_:referenceDate:)

<sub>Instance Method</sub>

Formats the subscription period using a format style that takes a duration as an input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S, referenceDate: Date = .now) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration
```

## Parameters

- `format` — A format style that has a duration as an input.

- `referenceDate` — The starting date of the subscription period. The default value is [now](../../../foundation/date/now.md).

## See Also

### Formatting the subscription period

- [formatted(_:referenceDate:)](<formatted(__referencedate_)-3t7wd.md>) — Formats the subscription period using a format style that takes a date range as an input.
