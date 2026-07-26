---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/double/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/hashvalue.json'
content_hash: 'sha256:7d6344e3b922de0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# hashValue

<sub>Instance Property</sub>

The hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hashValue: Int { get }
```

## Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> [!important] Important
> `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

### Infrequently Used Functionality

- [init()](<init().md>)
- [init(floatLiteral:)](<init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](<init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.
- [init(integerLiteral:)](<init(integerliteral_)-6hc7j.md>)
- [FloatLiteralType](floatliteraltype.md) — A type that represents a floating-point literal.
- [IntegerLiteralType](integerliteraltype.md) — A type that represents an integer literal.
- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [Stride](stride.md) — A type that represents the distance between two values.
- [write(to:)](<write(to_).md>) — Writes a textual representation of this instance into the given output stream.
