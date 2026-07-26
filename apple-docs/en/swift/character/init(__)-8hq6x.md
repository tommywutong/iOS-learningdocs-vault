---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/character/init(_:)-8hq6x'
source_url: 'https://developer.apple.com/documentation/swift/character/init(_:)-8hq6x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/init%28_%3A%29-8hq6x.json'
content_hash: 'sha256:c701f6f618df74d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# init(_:)

<sub>Initializer</sub>

Creates a character containing the given Unicode scalar value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ content: Unicode.Scalar)
```

## Parameters

- `content` — The Unicode scalar value to convert into a character.

## See Also

### Working with a Character’s Unicode Values

- [unicodeScalars](unicodescalars.md)
- [UnicodeScalarView](unicodescalarview.md)
- [isASCII](isascii.md) — A Boolean value indicating whether this is an ASCII character.
- [asciiValue](asciivalue.md) — The ASCII encoding value of this character, if it is an ASCII character.
