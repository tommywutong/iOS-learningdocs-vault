---
title: '-(_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/-(_:)-37tqf'
source_url: 'https://developer.apple.com/documentation/swift/float80/-(_:)-37tqf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/-%28_%3A%29-37tqf.json'
content_hash: 'sha256:1dd494cf2caaba17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# -(_:)

<sub>Operator</sub>

Returns the additive inverse of the specified value.

<sub>macOS</sub>

```swift
static func - (operand: Self) -> Self
```

## Return Value

The additive inverse of this value.

## Discussion

The negation operator (prefix `-`) returns the additive inverse of its argument.

```swift
let x = 21
let y = -x
// y == -21
```

The resulting value must be representable in the same type as the argument. In particular, negating a signed, fixed-width integer type’s minimum results in a value that cannot be represented.

```swift
let z = -Int8.min
// Overflow error
```
