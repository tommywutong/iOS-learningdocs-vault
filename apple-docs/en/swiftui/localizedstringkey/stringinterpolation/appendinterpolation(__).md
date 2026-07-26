---
title: 'appendInterpolation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28_%3A%29.json'
content_hash: 'sha256:5ff13b8c7fde13d2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(_:)

<sub>Instance Method</sub>

Appends an attributed substring to a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) mutating func appendInterpolation(_ attributedSubstring: AttributedSubstring)
```

## Parameters

- `attributedSubstring` — The attributed substring to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

The following example shows how to use a string interpolation to format an [AttributedSubstring](../../../foundation/attributedsubstring.md) and append it to static text. The resulting interpolation implicitly creates a [LocalizedStringKey](../../localizedstringkey.md), which a [Text](../../text.md) view uses to provide its content.

```swift
struct ContentView: View {

    var identificationNumberSuffix: AttributedSubstring {
        // …
    }

    var body: some View {
        Text("Identification: •••• •••• \(identificationNumberSuffix)!")
    }
}
```

For this example, assume that the app runs on a device set to a Russian locale, and has the following entry in a Russian-localized `Localizable.strings` file:

```swift
"Identification: •••• •••• %@" = "Идентификация: •••• •••• %@";
```

The attributed string `identificationNumberSuffix` replaces the format specifier `%@`,  maintaining its color attributes, when the [Text](../../text.md) view renders its contents:

## See Also

### Appending to an interpolation

- [appendInterpolation(_:specifier:)](<appendinterpolation(__specifier_).md>) — Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [appendInterpolation(_:format:)](<appendinterpolation(__format_).md>) — Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [appendInterpolation(_:formatter:)](<appendinterpolation(__formatter_).md>) — Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [appendInterpolation(_:style:)](<appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)](<appendinterpolation(timerinterval_pausetime_countsdown_showshours_).md>) — Appends a timer interval to a string interpolation.
- [appendLiteral(_:)](<appendliteral(__).md>) — Appends a literal string.
