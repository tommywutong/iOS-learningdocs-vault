---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(_:)-2t931'
source_url: 'https://developer.apple.com/documentation/swift/string/init(_:)-2t931'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28_%3A%29-2t931.json'
content_hash: 'sha256:fc6259414eb60cfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(_:)

<sub>Initializer</sub>

Creates a string corresponding to the given collection of Unicode scalars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ unicodeScalars: String.UnicodeScalarView)
```

## Parameters

- `unicodeScalars` — A collection of Unicode scalar values.

## Discussion

You can use this initializer to create a new string from a slice of another string’s `unicodeScalars` view.

```swift
let picnicGuest = "Deserving porcupine"
if let i = picnicGuest.unicodeScalars.firstIndex(of: " ") {
    let adjective = String(picnicGuest.unicodeScalars[..<i])
    print(adjective)
}
// Prints "Deserving"
```

The `adjective` constant is created by calling this initializer with a slice of the `picnicGuest.unicodeScalars` view.

## See Also

### Working with String Views

- [unicodeScalars](unicodescalars.md) — The string’s value represented as a collection of Unicode scalar values.
- [init(_:)](<init(__)-11jx3.md>) — Creates a String having the given content.
- [utf16](utf16.md) — A UTF-16 encoding of `self`.
- [init(_:)](<init(__)-wbcx.md>) — Creates a string corresponding to the given sequence of UTF-16 code units.
- [init(_:)](<init(__)-expd.md>) — Creates a String having the given content.
- [utf8](utf8.md) — A UTF-8 encoding of `self`.
- [init(_:)](<init(__)-6sprj.md>) — Creates a string corresponding to the given sequence of UTF-8 code units.
- [init(_:)](<init(__)-83bub.md>) — Creates a String having the given content.
