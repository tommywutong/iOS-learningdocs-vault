---
title: ulpOfOne
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/ulpofone
source_url: 'https://developer.apple.com/documentation/swift/float16/ulpofone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/ulpofone.json'
content_hash: 'sha256:297c498006096aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# ulpOfOne

<sub>Type Property</sub>

The unit in the last place of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var ulpOfOne: Float16 { get }
```

## Discussion

The positive difference between 1.0 and the next greater representable number. The `ulpOfOne` constant corresponds to the C macros `FLT_EPSILON`, `DBL_EPSILON`, and others with a similar purpose.
