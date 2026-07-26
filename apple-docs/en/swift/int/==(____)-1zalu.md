---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/==(_:_:)-1zalu'
source_url: 'https://developer.apple.com/documentation/swift/int/==(_:_:)-1zalu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/%3D%3D%28_%3A_%3A%29-1zalu.json'
content_hash: 'sha256:4f7c546471126520'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the two given values are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

## Parameters

- `lhs` — An integer to compare.

- `rhs` — Another integer to compare.

## Discussion

You can check the equality of instances of any `BinaryInteger` types using the equal-to operator (`==`). For example, you can test whether the first `UInt8` value in a string’s UTF-8 encoding is equal to the first `UInt32` value in its Unicode scalar view:

```swift
let gameName = "Red Light, Green Light"
if let firstUTF8 = gameName.utf8.first,
    let firstScalar = gameName.unicodeScalars.first?.value {
    print("First code values are equal: \(firstUTF8 == firstScalar)")
}
// Prints "First code values are equal: true"
```
