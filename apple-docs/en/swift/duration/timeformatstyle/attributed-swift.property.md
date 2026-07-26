---
title: attributed
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/timeformatstyle/attributed-swift.property
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/attributed-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/attributed-swift.property.json'
content_hash: 'sha256:123b858c91576958'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [TimeFormatStyle](../timeformatstyle.md)

# attributed

<sub>Instance Property</sub>

A property that formats the duration as an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributed: Duration.TimeFormatStyle.Attributed { get }
```

## Discussion

Apply the `attributed` property to a configured [TimeFormatStyle](../timeformatstyle.md) to produce an [Attributed](attributed-swift.struct.md) style. You can then format a duration with this style to create a formatted [AttributedString](../../../foundation/attributedstring.md). The formatted attributed string contains instances of [AttributeScopes.FoundationAttributes.DateFieldAttribute](../../../foundation/attributescopes/foundationattributes/datefieldattribute.md) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.TimeFormatStyle(pattern: .hourMinuteSecond).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1:10:32` contains the following runs:

| Run | Attributes |
|---|---|
| `1` | `Foundation.DurationFormatAttribute = hours` |
| `:` | None |
| `10` | `Foundation.DurationFormatAttribute = minutes` |
| `:` | None |
| `32` | `Foundation.DurationFormatAttribute = seconds` |

## See Also

### Formatting a duration as an attributed string

- [Attributed](attributed-swift.struct.md) — A format style that formats durations as attributed strings.
