---
title: debugDescription
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/debugdescription
source_url: 'https://developer.apple.com/documentation/swift/float80/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/debugdescription.json'
content_hash: 'sha256:3b6eb04e1f9ad776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of the value, suitable for debugging.

<sub>macOS</sub>

```swift
var debugDescription: String { get }
```

## Discussion

This property has the same value as the `description` property, except that NaN values are printed in an extended format.
