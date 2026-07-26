---
title: 'iso8601Components(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/iso8601components(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/iso8601components(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/iso8601components%28timezone%3Aincludingfractionalseconds%3Adateseparator%3Adatetimeseparator%3Atimeseparator%3A%29.json'
content_hash: 'sha256:298c2ce534cff931'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# iso8601Components(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)

<sub>Type Method</sub>

Creates a regex component to match an ISO 8601 date and time string without time zone, and capture the string as a `DateComponents` using the specified `timeZone`. If the string contains time zone designators, matches up until the start of time zone designators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func iso8601Components(timeZone: TimeZone, includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon) -> Self
```

## Parameters

- `timeZone` — The time zone to create the captured `DateComponents` with.

- `includingFractionalSeconds` — Specifies if the string contains fractional seconds.

- `dateSeparator` — The separator between date components.

- `dateTimeSeparator` — The separator between date and time parts.

- `timeSeparator` — The separator between time components.

## Return Value

A `RegexComponent` to match an ISO 8601 string.
