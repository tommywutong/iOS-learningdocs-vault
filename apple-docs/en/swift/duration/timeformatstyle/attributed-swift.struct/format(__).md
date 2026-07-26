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
doc_path: '/documentation/swift/duration/timeformatstyle/attributed-swift.struct/format(_:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/attributed-swift.struct/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/attributed-swift.struct/format%28_%3A%29.json'
content_hash: 'sha256:e8cce45bc76efa85'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [TimeFormatStyle](../../timeformatstyle.md) · [Attributed](../attributed-swift.struct.md)

# format(_:)

<sub>Instance Method</sub>

Creates a locale-aware attributed string representation from a duration value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Duration) -> AttributedString
```

## Parameters

- `value` — The duration value to format.

## Return Value

A string representation of the duration, according to the style’s pattern and locale.

## Discussion

Use this method when you want to create a format style and repeatedly use it to format different durations. For one-off cases with default formatting, call the [formatted(_:)](<../../formatted(__).md>) method of [Duration](../../../duration.md) instead.
