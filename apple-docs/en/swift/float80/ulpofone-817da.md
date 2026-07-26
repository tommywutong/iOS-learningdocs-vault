---
title: ulpOfOne
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/ulpofone-817da
source_url: 'https://developer.apple.com/documentation/swift/float80/ulpofone-817da'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/ulpofone-817da.json'
content_hash: 'sha256:fb3d265ec4e58355'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# ulpOfOne

<sub>Type Property</sub>

The unit in the last place of 1.0.

<sub>macOS</sub>

```swift
static var ulpOfOne: Self { get }
```

## Discussion

The positive difference between 1.0 and the next greater representable number. `ulpOfOne` corresponds to the value represented by the C macros `FLT_EPSILON`, `DBL_EPSILON`, etc, and is sometimes called _epsilon_ or _machine epsilon_. Swift deliberately avoids using the term “epsilon” because:

- Historically “epsilon” has been used to refer to several different concepts in different languages, leading to confusion and bugs.
- The name “epsilon” suggests that this quantity is a good tolerance to choose for approximate comparisons, but it is almost always unsuitable for that purpose.

See also the `ulp` member property.
