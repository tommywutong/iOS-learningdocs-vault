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
doc_path: /documentation/swift/int/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/int/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/hashvalue.json'
content_hash: 'sha256:e2080e987a418097'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

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

- [init()](<init().md>) — Creates a new value equal to zero.
- [init(integerLiteral:)](<init(integerliteral_).md>)
- [IntegerLiteralType](integerliteraltype.md) — A type that represents an integer literal.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [Stride](stride.md) — A type that represents the distance between two values.
