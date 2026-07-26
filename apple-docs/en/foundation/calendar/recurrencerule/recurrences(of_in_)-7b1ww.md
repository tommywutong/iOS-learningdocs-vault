---
title: 'recurrences(of:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/recurrences(of:in:)-7b1ww'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/recurrences(of:in:)-7b1ww'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/recurrences%28of%3Ain%3A%29-7b1ww.json'
content_hash: 'sha256:73efb9413fc14b60'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# recurrences(of:in:)

<sub>Instance Method</sub>

Find recurrences of the given date

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func recurrences(of start: Date, in range: PartialRangeUpTo<Date>) -> some Sendable & Sequence<Date>

```

## Parameters

- `start` — The date which defines the starting point for the recurrence rule.

- `range` — A range of dates which to search for recurrences.

## Return Value

A sequence of dates conforming to the recurrence rule, in the given `range`. An empty sequence if the rule doesn’t match any dates.

## Discussion

The calculations are implemented according to RFC-5545 and RFC-7529.
