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
doc_path: /documentation/swift/duration/unitsformatstyle/attributed-swift.property
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/attributed-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/attributed-swift.property.json'
content_hash: 'sha256:1dbb3f4160ce7a21'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# attributed

<sub>Instance Property</sub>

A property that formats the duration as an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributed: Duration.UnitsFormatStyle.Attributed { get }
```

## Discussion

Apply the `attributed` property to a configured [UnitsFormatStyle](../unitsformatstyle.md) to produce an [Attributed](attributed-swift.struct.md) style. You can then format a duration with this style to create a formatted   [AttributedString](../../../foundation/attributedstring.md). The formatted attributed string contains instances of [AttributeScopes.FoundationAttributes.DateFieldAttribute](../../../foundation/attributescopes/foundationattributes/datefieldattribute.md) and [AttributeScopes.FoundationAttributes.MeasurementAttribute](../../../foundation/attributescopes/foundationattributes/measurementattribute.md) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.UnitsFormatStyle(allowedUnits: [.hours, .minutes, .seconds],
                                      width: .abbreviated).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1 hr, 10 min, 32 sec` contains the following runs:

| Run | Attributes |
|---|---|
| `1` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = hours` |
| (space) | `Foundation.DurationFormatAttribute = hours` |
| `hr` | `Foundation.DurationFormatAttribute = hours`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `10` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = minutes` |
| (space) | `Foundation.DurationFormatAttribute = minutes` |
| `min` | `Foundation.DurationFormatAttribute = minutes`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `32` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = seconds` |
| (space) | `Foundation.DurationFormatAttribute = seconds` |
| `sec` | `Foundation.DurationFormatAttribute = seconds`, `Foundation.MeasurementAttribute = unit` |

## See Also

### Formatting a duration as an attributed string

- [Attributed](attributed-swift.struct.md) — A format style that formats durations as attributed strings.
