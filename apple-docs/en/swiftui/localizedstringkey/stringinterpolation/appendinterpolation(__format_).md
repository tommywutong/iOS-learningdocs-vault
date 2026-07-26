---
title: 'appendInterpolation(_:format:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28_%3Aformat%3A%29.json'
content_hash: 'sha256:b7a90b8562bf027d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(_:format:)

<sub>Instance Method</sub>

Appends the formatted representation  of a nonstring type supported by a corresponding format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

## Parameters

- `input` — The instance to format and append.

- `format` — A format style to use when converting `input` into an attributed string representation.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format a [Date](../../../foundation/date.md) with a [Date.FormatStyle](../../../foundation/date/formatstyle.md) and append it to static text. The resulting interpolation implicitly creates a [LocalizedStringKey](../../localizedstringkey.md), which a [Text](../../text.md) uses to provide its content.

```swift
Text("The time is \(myDate, format: Date.FormatStyle(date: .omitted, time:.complete).attributedStyle)")
```

## See Also

### Appending to an interpolation

- [appendInterpolation(_:)](<appendinterpolation(__).md>) — Appends an attributed substring to a string interpolation.
- [appendInterpolation(_:specifier:)](<appendinterpolation(__specifier_).md>) — Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [appendInterpolation(_:formatter:)](<appendinterpolation(__formatter_).md>) — Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [appendInterpolation(_:style:)](<appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)](<appendinterpolation(timerinterval_pausetime_countsdown_showshours_).md>) — Appends a timer interval to a string interpolation.
- [appendLiteral(_:)](<appendliteral(__).md>) — Appends a literal string.
