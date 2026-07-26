---
title: 'iso8601ComponentsWithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/iso8601componentswithtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/iso8601componentswithtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/iso8601componentswithtimezone%28includingfractionalseconds%3Adateseparator%3Adatetimeseparator%3Atimeseparator%3Atimezoneseparator%3A%29.json'
content_hash: 'sha256:9ceaf873a37bf5ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# iso8601ComponentsWithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)

<sub>Type Method</sub>

Creates a regex component to match an ISO 8601 date and time string, including time zone, and capture the string as a `DateComponents` using the time zone as specified in the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func iso8601ComponentsWithTimeZone(includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator = .omitted) -> Self
```

## Parameters

- `includingFractionalSeconds` — Specifies if the string contains fractional seconds.

- `dateSeparator` — The separator between date components.

- `dateTimeSeparator` — The separator between date and time parts.

- `timeSeparator` — The separator between time components.

- `timeZoneSeparator` — The separator between time parts in the time zone.

## Return Value

A `RegexComponent` to match an ISO 8601 string, including time zone.
