---
title: 'format(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/timeformatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/format%28_%3A%29.json'
content_hash: 'sha256:7abaa44c2ed50f7a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [TimeFormatStyle](../timeformatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Creates a locale-aware string representation from a duration value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Duration) -> String
```

## Parameters

- `value` — The duration value to format.

## Return Value

A string representation of the duration, according to the style’s pattern and locale.

## Discussion

Use this method when you want to create a format style and repeatedly use it to format different durations. For one-off cases with default formatting, call the [formatted(_:)](<../formatted(__).md>) method of [Duration](../../duration.md) instead.
