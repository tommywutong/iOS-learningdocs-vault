---
title: 'iso8601DateComponents(timeZone:dateSeparator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/iso8601datecomponents(timezone:dateseparator:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/iso8601datecomponents(timezone:dateseparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/iso8601datecomponents%28timezone%3Adateseparator%3A%29.json'
content_hash: 'sha256:9428c11899520e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# iso8601DateComponents(timeZone:dateSeparator:)

<sub>Type Method</sub>

Creates a regex component to match an ISO 8601 date string, such as “2015-11-14”, and capture the string as a `DateComponents`. The captured `DateComponents` would be at midnight in the specified `timeZone`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func iso8601DateComponents(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash) -> Self
```

## Parameters

- `timeZone` — The time zone to create the captured `Date` with.

- `dateSeparator` — The separator between date components.

## Return Value

A `RegexComponent` to match an ISO 8601 date string, not any time zone that may be in the string.
