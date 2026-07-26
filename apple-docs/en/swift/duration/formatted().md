---
title: formatted()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/formatted()
source_url: 'https://developer.apple.com/documentation/swift/duration/formatted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/formatted%28%29.json'
content_hash: 'sha256:20d0d8660ede219f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# formatted()

<sub>Instance Method</sub>

Formats the string using a localized hour-minute-second time pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted() -> String
```

## Return Value

A localized formatted string that describes the duration, such as `1:30:56` for a duration of 1 hour, 30 minutes, and 56 seconds in the U.S. English locale. In the Finnish locale, this returns `1.30.56`.

## Discussion

The following example shows the effect of applying the default formatting to a duration of two seconds:

```swift
let duration = Duration.seconds(2)
let formattedDuration = duration.formatted() // "0:00:02"
```

This method uses a default [TimeFormatStyle](timeformatstyle.md). To modify the formatting, customize a [TimeFormatStyle](timeformatstyle.md) or [UnitsFormatStyle](unitsformatstyle.md), then call [formatted(_:)](<formatted(__).md>) on the duration, passing in the style. You can also call `format(_:)` on the style, passing in a duration.

## See Also

### Formatting a duration

- [formatted(_:)](<formatted(__).md>) — Formats the duration, using the provided format style.
- [TimeFormatStyle](timeformatstyle.md) — A format style that shows durations in a compact, localized format with separators.
- [UnitsFormatStyle](unitsformatstyle.md) — A format style that shows durations with localized labeled components
