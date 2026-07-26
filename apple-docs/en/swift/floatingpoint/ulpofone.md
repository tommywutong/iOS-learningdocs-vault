---
title: ulpOfOne
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/ulpofone
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/ulpofone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/ulpofone.json'
content_hash: 'sha256:4e6bf3028cb9b987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# ulpOfOne

<sub>Type Property</sub>

The unit in the last place of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var ulpOfOne: Self { get }
```

## Discussion

The positive difference between 1.0 and the next greater representable number. `ulpOfOne` corresponds to the value represented by the C macros `FLT_EPSILON`, `DBL_EPSILON`, etc, and is sometimes called _epsilon_ or _machine epsilon_. Swift deliberately avoids using the term “epsilon” because:

- Historically “epsilon” has been used to refer to several different concepts in different languages, leading to confusion and bugs.
- The name “epsilon” suggests that this quantity is a good tolerance to choose for approximate comparisons, but it is almost always unsuitable for that purpose.

See also the `ulp` member property.

## Default Implementations

### FloatingPoint Implementations

- [ulpOfOne](ulpofone-3j2pj.md) — The unit in the last place of 1.0.
