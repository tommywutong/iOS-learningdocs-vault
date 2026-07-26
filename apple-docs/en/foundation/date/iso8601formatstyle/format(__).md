---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/format%28_%3A%29.json'
content_hash: 'sha256:a5b8ef5520df468f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Creates a locale-aware ISO 8601 string representation from a date value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Date) -> String
```

## Parameters

- `value` — The date to format.

## Return Value

A string ISO 8601 representation of the date.

## Discussion

The [format(_:)](<format(__).md>) instance method generates a ISO 8601 formatted string from the provided date. Once you create a style, you can use it to format dates multiple times.

In the following example, a format style is created to guide parsing a set of string representations of dates. Another format style is created and applied repeatedly to produce customized ISO 8601 string representations of those dates for a different locale.

```swift
let input8601Format = Date.ISO8601FormatStyle()
    .dateSeparator(.dash)
    .year()
    .month()
    .day()

// Parse dates from strings using the input format defined above.
let introDate01 = try? Date("2007-01-09", strategy: input8601Format)
let introDate02 = try? Date("2010-01-27", strategy: input8601Format)
let meetingDate2021 = try? Date("2021-06-07", strategy: input8601Format)

let outputFormat = Date.ISO8601FormatStyle() // define format style for string output
    .locale(Locale(identifier: "en_US"))
    .year()
    .month()
    .day()
    .weekOfYear()

// Apply the output format to the three dates below.
if let meet2021 = meetingDate2021 {
    print(outputFormat.format(meet2021))
}
// 202106W2301
if let intro02 = introDate02 {
    print(outputFormat.format(intro02))
}
// 201001W0403
if let intro01 = introDate01 {
    print(outputFormat.format(intro01))
}
// 200701W0202
```
