---
title: 'distance(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/distance(to:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/distance%28to%3A%29.json'
content_hash: 'sha256:868fea709870af44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance from this value to the given value, expressed as a stride.

<sub>macOS</sub>

```swift
func distance(to other: Float80) -> Float80
```

## Parameters

- `other` — The value to calculate the distance to.

## Return Value

The distance from this value to `other`.

## Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> [!abstract] Complexity
> O(1)
