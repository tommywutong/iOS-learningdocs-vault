---
title: asciiValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/asciivalue
source_url: 'https://developer.apple.com/documentation/swift/character/asciivalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/asciivalue.json'
content_hash: 'sha256:e6878dfdc5e1f3a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# asciiValue

<sub>Instance Property</sub>

The ASCII encoding value of this character, if it is an ASCII character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var asciiValue: UInt8? { get }
```

## Discussion

```swift
let chars: [Character] = ["a", " ", "™"]
for ch in chars {
    print(ch, "-->", ch.asciiValue)
}
// Prints:
// a --> Optional(97)
//   --> Optional(32)
// ™ --> nil
```

A character with the value “\\r\\n” (CR-LF) is normalized to “\\n” (LF) and has an `asciiValue` property equal to 10.

```swift
let cr = "\r" as Character
// cr.asciiValue == 13
let lf = "\n" as Character
// lf.asciiValue == 10
let crlf = "\r\n" as Character
// crlf.asciiValue == 10
```

## See Also

### Working with a Character’s Unicode Values

- [init(_:)](<init(__)-8hq6x.md>) — Creates a character containing the given Unicode scalar value.
- [unicodeScalars](unicodescalars.md)
- [UnicodeScalarView](unicodescalarview.md)
- [isASCII](isascii.md) — A Boolean value indicating whether this is an ASCII character.
