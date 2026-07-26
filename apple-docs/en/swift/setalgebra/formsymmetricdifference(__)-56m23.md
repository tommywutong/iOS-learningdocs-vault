---
title: 'formSymmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/formsymmetricdifference(_:)-56m23'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/formsymmetricdifference(_:)-56m23'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/formsymmetricdifference%28_%3A%29-56m23.json'
content_hash: 'sha256:a7fad1bc60617749'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# formSymmetricDifference(_:)

<sub>Instance Method</sub>

Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formSymmetricDifference(_ other: Self)
```

## Parameters

- `other` — An option set.

## Discussion

This method is implemented as a `^` (bitwise XOR) operation on the two sets’ raw values.
