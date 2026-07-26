---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/flatmap(_:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/flatmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/flatmap%28_%3A%29.json'
content_hash: 'sha256:af324e242f5c74c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# flatMap(_:)

<sub>Instance Method</sub>

Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<E, U>(_ transform: (Wrapped) throws(E) -> U?) throws(E) -> U? where E : Error, U : ~Copyable
```

## Parameters

- `transform` — A closure that takes the unwrapped value of the instance.

## Return Value

The result of the given closure. If this instance is `nil`, returns `nil`.

## Discussion

Use the `flatMap` method with a closure that returns an optional value. This example performs an arithmetic operation with an optional result on an optional integer.

```swift
let possibleNumber: Int? = Int("42")
let nonOverflowingSquare = possibleNumber.flatMap { x -> Int? in
    let (result, overflowed) = x.multipliedReportingOverflow(by: x)
    return overflowed ? nil : result
}
print(nonOverflowingSquare)
// Prints "Optional(1764)"
```

## See Also

### Transforming an Optional Value

- [map(_:)](<map(__).md>) — Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.
