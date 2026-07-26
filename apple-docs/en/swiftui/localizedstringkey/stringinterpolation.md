---
title: LocalizedStringKey.StringInterpolation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/localizedstringkey/stringinterpolation
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation.json'
content_hash: 'sha256:27b48524d4d016ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LocalizedStringKey](../localizedstringkey.md)

# LocalizedStringKey.StringInterpolation

<sub>Structure</sub>

Represents the contents of a string literal with interpolations while it’s being built, for use in creating a localized string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StringInterpolation
```

## Relationships

- **Conforms To**: [StringInterpolationProtocol](../../swift/stringinterpolationprotocol.md)

## Topics

### Appending to an interpolation

- [appendInterpolation(_:)](<stringinterpolation/appendinterpolation(__).md>) — Appends an attributed substring to a string interpolation.
- [appendInterpolation(_:specifier:)](<stringinterpolation/appendinterpolation(__specifier_).md>) — Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [appendInterpolation(_:format:)](<stringinterpolation/appendinterpolation(__format_).md>) — Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [appendInterpolation(_:formatter:)](<stringinterpolation/appendinterpolation(__formatter_).md>) — Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [appendInterpolation(_:style:)](<stringinterpolation/appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)](<stringinterpolation/appendinterpolation(timerinterval_pausetime_countsdown_showshours_).md>) — Appends a timer interval to a string interpolation.
- [appendLiteral(_:)](<stringinterpolation/appendliteral(__).md>) — Appends a literal string.

### Instance Methods

- [appendInterpolation(accessibilityName:)](<stringinterpolation/appendinterpolation(accessibilityname_).md>) — Appends a localized description of a color for accessibility to a string interpolation.

## See Also

### Creating a key from an interpolation

- [init(stringInterpolation:)](<init(stringinterpolation_).md>) — Creates a localized string key from the given string interpolation.
