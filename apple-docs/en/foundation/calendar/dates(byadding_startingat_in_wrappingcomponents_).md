---
title: 'dates(byAdding:startingAt:in:wrappingComponents:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/dates(byadding:startingat:in:wrappingcomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/dates(byadding:startingat:in:wrappingcomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/dates%28byadding%3Astartingat%3Ain%3Awrappingcomponents%3A%29.json'
content_hash: 'sha256:55eb2068e8d56bc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dates(byAdding:startingAt:in:wrappingComponents:)

<sub>Instance Method</sub>

Returns a sequence of `Date`s, calculated by repeatedly adding an amount of `DateComponents` to a starting `Date` and then to each subsequent result. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dates(byAdding components: DateComponents, startingAt start: Date, in range: Range<Date>? = nil, wrappingComponents: Bool = false) -> some Sendable & Sequence<Date>

```

## Parameters

- `components` — The components to add or subtract.

- `start` — The starting point of the search.

- `range` — The range of dates to allow in the result. The sequence terminates if the next result is not contained in this range. If `nil`, all results are allowed.

- `wrappingComponents` — If `true`, the component should be incremented and wrap around to zero/one on overflow, and should not cause higher components to be incremented. The default value is `false`.

## Return Value

A `Sequence` of `Date` values, or an empty sequence if no addition could be performed.
