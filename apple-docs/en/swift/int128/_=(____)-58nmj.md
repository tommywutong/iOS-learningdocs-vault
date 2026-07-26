---
title: '%=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/_=(_:_:)-58nmj'
source_url: 'https://developer.apple.com/documentation/swift/int128/_=(_:_:)-58nmj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/_%3D%28_%3A_%3A%29-58nmj.json'
content_hash: 'sha256:69c8e05a6e8a54f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# %=(_:_:)

<sub>Operator</sub>

Divides the first value by the second and stores the remainder in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func %= (a: inout Int128, b: Int128)
```

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
