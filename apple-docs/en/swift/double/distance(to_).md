---
title: 'distance(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/distance(to:)'
source_url: 'https://developer.apple.com/documentation/swift/double/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/distance%28to%3A%29.json'
content_hash: 'sha256:064f8c3ab0b0354e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance from this value to the given value, expressed as a stride.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: Double) -> Double
```

## Parameters

- `other` — The value to calculate the distance to.

## Return Value

The distance from this value to `other`.

## Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> [!abstract] Complexity
> O(1)

## See Also

### Infrequently Used Functionality

- [init()](<init().md>)
- [init(floatLiteral:)](<init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](<init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.
- [init(integerLiteral:)](<init(integerliteral_)-6hc7j.md>)
- [FloatLiteralType](floatliteraltype.md) — A type that represents a floating-point literal.
- [IntegerLiteralType](integerliteraltype.md) — A type that represents an integer literal.
- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [Stride](stride.md) — A type that represents the distance between two values.
- [write(to:)](<write(to_).md>) — Writes a textual representation of this instance into the given output stream.
- [hashValue](hashvalue.md) — The hash value.
