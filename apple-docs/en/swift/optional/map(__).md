---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/map(_:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/map%28_%3A%29.json'
content_hash: 'sha256:6e6a6cf32e672933'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# map(_:)

<sub>Instance Method</sub>

Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<E, U>(_ transform: (Wrapped) throws(E) -> U) throws(E) -> U? where E : Error, U : ~Copyable
```

## Parameters

- `transform` — A closure that takes the unwrapped value of the instance.

## Return Value

The result of the given closure. If this instance is `nil`, returns `nil`.

## Discussion

Use the `map` method with a closure that returns a non-optional value. This example performs an arithmetic operation on an optional integer.

```swift
let possibleNumber: Int? = Int("42")
let possibleSquare = possibleNumber.map { $0 * $0 }
print(possibleSquare)
// Prints "Optional(1764)"

let noNumber: Int? = nil
let noSquare = noNumber.map { $0 * $0 }
print(noSquare)
// Prints "nil"
```

## See Also

### Transforming an Optional Value

- [flatMap(_:)](<flatmap(__).md>) — Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.
