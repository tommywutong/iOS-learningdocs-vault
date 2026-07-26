---
title: 'formUnion(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/formunion(_:)-4ht9l'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/formunion(_:)-4ht9l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/formunion%28_%3A%29-4ht9l.json'
content_hash: 'sha256:de32f6d6f7c201e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# formUnion(_:)

<sub>Instance Method</sub>

Inserts the elements of another set into this option set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func formUnion(_ other: Self)
```

## Parameters

- `other` — An option set.

## Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.
