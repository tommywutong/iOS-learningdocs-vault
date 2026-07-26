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
doc_path: /documentation/swift/float80/negate()
source_url: 'https://developer.apple.com/documentation/swift/float80/negate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/negate%28%29.json'
content_hash: 'sha256:c5d0250cf42bd12b'
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

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```
