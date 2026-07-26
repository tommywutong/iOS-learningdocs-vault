---
title: 'advanced(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/advanced%28by%3A%29.json'
content_hash: 'sha256:cf687d7108840ec1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a value that is offset the specified distance from this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by amount: Float16) -> Float16
```

## Return Value

A value that is offset from this value by `n`.

## Discussion

Use the `advanced(by:)` method in generic code to offset a value by a specified distance. If you’re working directly with numeric values, use the addition operator (`+`) instead of this method.

```swift
func addOne<T: Strideable>(to x: T) -> T
    where T.Stride: ExpressibleByIntegerLiteral
{
    return x.advanced(by: 1)
}

let x = addOne(to: 5)
// x == 6
let y = addOne(to: 3.5)
// y = 4.5
```

If this type’s `Stride` type conforms to `BinaryInteger`, then for a value `x`, a distance `n`, and a value `y = x.advanced(by: n)`, `x.distance(to: y) == n`. Using this method with types that have a noninteger `Stride` may result in an approximation. If the result of advancing by `n` is not representable as a value of this type, then a runtime error may occur.

> [!abstract] Complexity
> O(1)
