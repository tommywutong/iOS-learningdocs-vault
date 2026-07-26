---
title: negate()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/negate()-6fr8s
source_url: 'https://developer.apple.com/documentation/swift/float80/negate()-6fr8s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/negate%28%29-6fr8s.json'
content_hash: 'sha256:9ea49100f2e8857d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# negate()

<sub>Instance Method</sub>

Replaces this value with its additive inverse.

<sub>macOS</sub>

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
