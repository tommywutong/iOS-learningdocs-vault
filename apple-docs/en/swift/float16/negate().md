---
title: negate()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/negate()
source_url: 'https://developer.apple.com/documentation/swift/float16/negate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/negate%28%29.json'
content_hash: 'sha256:e98678a73791aacf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# negate()

<sub>Instance Method</sub>

Replaces this value with its additive inverse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func negate()
```

## Discussion

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```
