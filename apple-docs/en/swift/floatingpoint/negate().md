---
title: negate()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/negate()
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/negate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/negate%28%29.json'
content_hash: 'sha256:6e7f05d4c4731441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# negate()

<sub>Instance Method</sub>

Replaces this value with its additive inverse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override mutating func negate()
```

## Discussion

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```
