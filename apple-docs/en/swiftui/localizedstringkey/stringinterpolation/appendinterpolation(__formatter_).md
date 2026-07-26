---
title: 'appendInterpolation(_:formatter:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28_%3Aformatter%3A%29.json'
content_hash: 'sha256:554a1d5bcf54397e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(_:formatter:)

<sub>Instance Method</sub>

Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<Subject>(_ subject: Subject, formatter: Formatter? = nil) where Subject : NSObject
```

## Parameters

- `subject` — An [NSObject](../../../objectivec/nsobject-swift.class.md) to append.

- `formatter` — A formatter to convert `subject` to a string representation.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a [Measurement](../../../foundation/measurement.md) value and a [MeasurementFormatter](../../../foundation/measurementformatter.md) to create a [LocalizedStringKey](../../localizedstringkey.md) that uses the formatter style [Formatter.UnitStyle.long](../../../foundation/formatter/unitstyle/long.md) when generating the measurement’s string representation. Rather than calling `appendInterpolation(_:formatter)` directly, the code gets the formatting behavior implicitly by using the `\()` string interpolation syntax.

```swift
let siResistance = Measurement(value: 640, unit: UnitElectricResistance.ohms)
let formatter = MeasurementFormatter()
formatter.unitStyle = .long
let key = LocalizedStringKey ("Resistance: \(siResistance, formatter: formatter)")
let text1 = Text(key) // Text contains "Resistance: 640 ohms"
```

## See Also

### Appending to an interpolation

- [appendInterpolation(_:)](<appendinterpolation(__).md>) — Appends an attributed substring to a string interpolation.
- [appendInterpolation(_:specifier:)](<appendinterpolation(__specifier_).md>) — Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [appendInterpolation(_:format:)](<appendinterpolation(__format_).md>) — Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [appendInterpolation(_:style:)](<appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)](<appendinterpolation(timerinterval_pausetime_countsdown_showshours_).md>) — Appends a timer interval to a string interpolation.
- [appendLiteral(_:)](<appendliteral(__).md>) — Appends a literal string.
