---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/parse%28_%3A%29.json'
content_hash: 'sha256:a7fbc171d0b825ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# parse(_:)

<sub>Instance Method</sub>

Parses a string into a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: String) throws -> Date
```

## Parameters

- `value` — The string to parse.

## Return Value

An instance of `Date` parsed from the input string.

## Discussion

This method attempts to parse a provided string into an instance of date using the source date format style. The function throws an error if it can’t parse the input string into a date instance.

The date format style guides parsing the date instance from an input string, as the following example illustrates.

```swift
let birthdayFormatStyle = Date.ISO8601FormatStyle()    
    .dateSeparator(.dash)
    .timeSeparator(.colon)
    .year()
    .month()
    .day()
    .time(includingFractionalSeconds: false)

// Create a date instance from a string representation of a date.
let yourBirthdayString = "2021-02-17T14:33:25"
let yourBirthday = try? birthdayFormatStyle.parse(yourBirthdayString)
// Feb 17, 2021 at 8:33 AM
```

## See Also

### Parsing an ISO 8601 Format Style

- [parseStrategy](parsestrategy.md) — The strategy used to parse a string into a date.
