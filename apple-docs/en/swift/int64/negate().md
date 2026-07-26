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
doc_path: /documentation/swift/int64/negate()
source_url: 'https://developer.apple.com/documentation/swift/int64/negate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/negate%28%29.json'
content_hash: 'sha256:0fc4833d705e2d6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int64](../int64.md)

# negate()

<sub>Instance Method</sub>

Replaces this value with its additive inverse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func negate()
```

## Discussion

The following example uses the `negate()` method to negate the value of an integer `x`:

```swift
var x = 21
x.negate()
// x == -21
```

The resulting value must be representable within the value’s type. In particular, negating a signed, fixed-width integer type’s minimum results in a value that cannot be represented.

```swift
var y = Int8.min
y.negate()
// Overflow error
```
