---
title: debugDescription
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/debugdescription
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/debugdescription.json'
content_hash: 'sha256:dfb8399bf04ebf21'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# debugDescription

<sub>Instance Property</sub>

An escaped textual representation of the Unicode scalar, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var debugDescription: String { get }
```

## See Also

### Printing and Displaying a Scalar

- [description](description.md) — A textual representation of the Unicode scalar.
- [write(to:)](<write(to_).md>) — Writes the textual representation of the Unicode scalar into the given output stream.
- [escaped(asASCII:)](<escaped(asascii_).md>) — Returns a string representation of the Unicode scalar.
- [utf16](utf16.md)
- [UTF16View](utf16view.md)
- [customMirror](custommirror.md) — A mirror that reflects the `Unicode.Scalar` instance.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the `Unicode.Scalar` instance. _(deprecated)_
