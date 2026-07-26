---
title: 'appendInterpolation(_:specifier:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:specifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28_%3Aspecifier%3A%29.json'
content_hash: 'sha256:71dae75d2fc01dfb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(_:specifier:)

<sub>Instance Method</sub>

Appends a type, convertible to a string with a format specifier, to a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<T>(_ value: T, specifier: String) where T : _FormatSpecifiable
```

## Parameters

- `value` — The value to append.

- `specifier` — A format specifier to convert `subject` to a string representation, like `%f` for a [Double](../../../swift/double.md), or `%x` to create a hexidecimal representation of a [UInt32](../../../swift/uint32.md). For a list of available specifier strings, see [String Format Specifers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## See Also

### Appending to an interpolation

- [appendInterpolation(_:)](<appendinterpolation(__).md>) — Appends an attributed substring to a string interpolation.
- [appendInterpolation(_:format:)](<appendinterpolation(__format_).md>) — Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [appendInterpolation(_:formatter:)](<appendinterpolation(__formatter_).md>) — Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [appendInterpolation(_:style:)](<appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)](<appendinterpolation(timerinterval_pausetime_countsdown_showshours_).md>) — Appends a timer interval to a string interpolation.
- [appendLiteral(_:)](<appendliteral(__).md>) — Appends a literal string.
