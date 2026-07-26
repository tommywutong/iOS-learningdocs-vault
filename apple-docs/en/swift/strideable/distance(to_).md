---
title: 'distance(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/strideable/distance(to:)'
source_url: 'https://developer.apple.com/documentation/swift/strideable/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/strideable/distance%28to%3A%29.json'
content_hash: 'sha256:347517eac2fdc110'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Strideable](../strideable.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance from this value to the given value, expressed as a stride.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: Self) -> Self.Stride
```

## Parameters

- `other` — The value to calculate the distance to.

## Return Value

The distance from this value to `other`.

## Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> [!abstract] Complexity
> O(1)

## Default Implementations

### Strideable Implementations

- [distance(to:)](<distance(to_)-1mibk.md>) — Returns the distance from this value to the given value, expressed as a stride.
