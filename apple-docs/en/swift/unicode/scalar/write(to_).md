---
title: 'write(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/write(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/write(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/write%28to%3A%29.json'
content_hash: 'sha256:39b5112476a071f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# write(to:)

<sub>Instance Method</sub>

Writes the textual representation of the Unicode scalar into the given output stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write<Target>(to target: inout Target) where Target : TextOutputStream
```

## Parameters

- `target` — An output stream.

## See Also

### Printing and Displaying a Scalar

- [description](description.md) — A textual representation of the Unicode scalar.
- [escaped(asASCII:)](<escaped(asascii_).md>) — Returns a string representation of the Unicode scalar.
- [utf16](utf16.md)
- [UTF16View](utf16view.md)
- [debugDescription](debugdescription.md) — An escaped textual representation of the Unicode scalar, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `Unicode.Scalar` instance.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the `Unicode.Scalar` instance. _(deprecated)_
