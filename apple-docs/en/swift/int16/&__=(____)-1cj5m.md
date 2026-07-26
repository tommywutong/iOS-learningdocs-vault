---
title: '&<<=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int16/&__=(_:_:)-1cj5m'
source_url: 'https://developer.apple.com/documentation/swift/int16/&__=(_:_:)-1cj5m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int16/%26__%3D%28_%3A_%3A%29-1cj5m.json'
content_hash: 'sha256:4beaea125a993b1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int16](../int16.md)

# &\<\<=(_:_:)

<sub>Operator</sub>

Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func &<<= <Other>(lhs: inout Self, rhs: Other) where Other : BinaryInteger
```

## Parameters

- `lhs` — The value to shift.

- `rhs` — The number of bits to shift `lhs` to the left. If `rhs` is outside the range `0..<lhs.bitWidth`, it is masked to produce a value within that range.

## Discussion

The `&<<=` operator performs a _masking shift_, where the value used as `rhs` is masked to produce a value in the range `0..<lhs.bitWidth`. The shift is performed using this masked value.

The following example defines `x` as an instance of `UInt8`, an 8-bit, unsigned integer type. If you use `2` as the right-hand-side value in an operation on `x`, the shift amount requires no masking.

```swift
var x: UInt8 = 30                 // 0b00011110
x &<<= 2
// x == 120                       // 0b01111000
```

However, if you pass `19` as `rhs`, the method first bitmasks `rhs` to `3`, and then uses that masked value as the number of bits to shift `lhs`.

```swift
var y: UInt8 = 30                 // 0b00011110
y &<<= 19
// y == 240                       // 0b11110000
```
