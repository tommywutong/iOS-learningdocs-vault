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
doc_path: '/documentation/swift/string/init(_:)-expd'
source_url: 'https://developer.apple.com/documentation/swift/string/init(_:)-expd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28_%3A%29-expd.json'
content_hash: 'sha256:be43c2c5f34c2cf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(_:)

<sub>Initializer</sub>

Creates a String having the given content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ codeUnits: Substring.UTF16View)
```

## Discussion

If `codeUnits` is an ill-formed code unit sequence, the result is `nil`.

> [!abstract] Complexity
> O(N), where N is the length of the resulting `String`’s UTF-16.

## See Also

### Working with String Views

- [unicodeScalars](unicodescalars.md) — The string’s value represented as a collection of Unicode scalar values.
- [init(_:)](<init(__)-2t931.md>) — Creates a string corresponding to the given collection of Unicode scalars.
- [init(_:)](<init(__)-11jx3.md>) — Creates a String having the given content.
- [utf16](utf16.md) — A UTF-16 encoding of `self`.
- [init(_:)](<init(__)-wbcx.md>) — Creates a string corresponding to the given sequence of UTF-16 code units.
- [utf8](utf8.md) — A UTF-8 encoding of `self`.
- [init(_:)](<init(__)-6sprj.md>) — Creates a string corresponding to the given sequence of UTF-8 code units.
- [init(_:)](<init(__)-83bub.md>) — Creates a String having the given content.
