---
title: 'recurrences(of:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/recurrencerule/recurrences(of:in:)-4y30t'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/recurrencerule/recurrences(of:in:)-4y30t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/recurrencerule/recurrences%28of%3Ain%3A%29-4y30t.json'
content_hash: 'sha256:2a40f740dd0b2796'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RecurrenceRule](../recurrencerule.md)

# recurrences(of:in:)

<sub>Instance Method</sub>

Find recurrences of the given date

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func recurrences(of start: Date, in range: Range<Date>? = nil) -> some Sendable & Sequence<Date>

```

## Parameters

- `start` — The date which defines the starting point for the recurrence rule.

- `range` — A range of dates which to search for recurrences. If `nil`, return all recurrences of the event.

## Return Value

A sequence of dates conforming to the recurrence rule, in the given `range`. An empty sequence if the rule doesn’t match any dates.

## Discussion

The calculations are implemented according to RFC-5545 and RFC-7529.
