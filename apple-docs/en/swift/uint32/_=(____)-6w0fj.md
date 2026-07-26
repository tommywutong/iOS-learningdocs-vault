---
title: '%=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint32/_=(_:_:)-6w0fj'
source_url: 'https://developer.apple.com/documentation/swift/uint32/_=(_:_:)-6w0fj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint32/_%3D%28_%3A_%3A%29-6w0fj.json'
content_hash: 'sha256:d1295418599e6f10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt32](../uint32.md)

# %=(_:_:)

<sub>Operator</sub>

Divides the first value by the second and stores the remainder in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func %= (lhs: inout UInt32, rhs: UInt32)
```

## Parameters

- `lhs` — The value to divide.

- `rhs` — The value to divide `lhs` by. `rhs` must not be zero.

## Discussion

The result has the same sign as `lhs` and has a magnitude less than `rhs.magnitude`.

```swift
var x = 22
x %= 5
// x == 2

var y = 22
y %= -5
// y == 2

var z = -22
z %= -5
// z == -2
```
