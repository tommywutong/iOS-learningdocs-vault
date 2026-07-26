---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/description
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/description.json'
content_hash: 'sha256:ae6bc804fffdb5ea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# description

<sub>Instance Property</sub>

A textual representation of the Unicode scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## See Also

### Printing and Displaying a Scalar

- [write(to:)](<write(to_).md>) — Writes the textual representation of the Unicode scalar into the given output stream.
- [escaped(asASCII:)](<escaped(asascii_).md>) — Returns a string representation of the Unicode scalar.
- [utf16](utf16.md)
- [UTF16View](utf16view.md)
- [debugDescription](debugdescription.md) — An escaped textual representation of the Unicode scalar, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `Unicode.Scalar` instance.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the `Unicode.Scalar` instance. _(deprecated)_
