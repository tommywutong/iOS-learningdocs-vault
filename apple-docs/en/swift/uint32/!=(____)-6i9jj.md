---
title: '!=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint32/!=(_:_:)-6i9jj'
source_url: 'https://developer.apple.com/documentation/swift/uint32/!=(_:_:)-6i9jj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint32/%21%3D%28_%3A_%3A%29-6i9jj.json'
content_hash: 'sha256:d54eab5342e89107'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt32](../uint32.md)

# !=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the two given values are not equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func != <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

## Parameters

- `lhs` — An integer to compare.

- `rhs` — Another integer to compare.

## Discussion

You can check the inequality of instances of any `BinaryInteger` types using the not-equal-to operator (`!=`). For example, you can test whether the first `UInt8` value in a string’s UTF-8 encoding is not equal to the first `UInt32` value in its Unicode scalar view:

```swift
let gameName = "Red Light, Green Light"
if let firstUTF8 = gameName.utf8.first,
    let firstScalar = gameName.unicodeScalars.first?.value {
    print("First code values are different: \(firstUTF8 != firstScalar)")
}
// Prints "First code values are different: false"
```
