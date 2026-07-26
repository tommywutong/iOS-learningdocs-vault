---
title: timeDuration
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/timeduration
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/timeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/timeduration.json'
content_hash: 'sha256:db8c53726652d87c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# timeDuration

<sub>Type Property</sub>

A style for formatting a duration expressed as a range of dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var timeDuration: Date.ComponentsFormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [FormatStyle](../date/formatstyle.md). You typically do this when calling the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

The following example creates a one hour, thirty-five minute range between two dates, then uses SELF to format this duration as a string.

```swift
let now = Date.now
let future = now.addingTimeInterval(95)
let dateRange = now..<future
let formatted = dateRange.formatted(.timeDuration) // "1:35"
XCTAssertEqual(formatted, "1:35")
```

To use the Swift [Duration](../../swift/duration.md) type rather than `Date`, use [Duration.TimeFormatStyle](../../swift/duration/timeformatstyle.md) or [Duration.UnitsFormatStyle](../../swift/duration/unitsformatstyle.md) instead, and their corresponding static accessors, [time(pattern:)](<time(pattern_).md>) and [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<units(allowed_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>).

## See Also

### Applying duration styles

- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
- [time(pattern:)](<time(pattern_).md>) — Returns a style for formatting a duration using a provided pattern.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<units(allowed_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>) — Returns a style for formatting a duration that uses the specified units.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)](<units(allowed_width_maximumunitcount_zerovalueunits_valuelengthlimits_fractionalpart_).md>) — Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.
