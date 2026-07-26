---
title: squareRoot()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/squareroot()
source_url: 'https://developer.apple.com/documentation/swift/float16/squareroot()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/squareroot%28%29.json'
content_hash: 'sha256:11a5ffb11dfe4e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# squareRoot()

<sub>Instance Method</sub>

Returns the square root of the value, rounded to a representable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func squareRoot() -> Self
```

## Return Value

The square root of the value.

## Discussion

The following example declares a function that calculates the length of the hypotenuse of a right triangle given its two perpendicular sides.

```swift
func hypotenuse(_ a: Double, _ b: Double) -> Double {
    return (a * a + b * b).squareRoot()
}

let (dx, dy) = (3.0, 4.0)
let distance = hypotenuse(dx, dy)
// distance == 5.0
```
