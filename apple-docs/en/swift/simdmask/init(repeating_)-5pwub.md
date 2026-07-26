---
title: 'init(repeating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simdmask/init(repeating:)-5pwub'
source_url: 'https://developer.apple.com/documentation/swift/simdmask/init(repeating:)-5pwub'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask/init%28repeating%3A%29-5pwub.json'
content_hash: 'sha256:8cb401e7a9be5166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDMask](../simdmask.md)

# init(repeating:)

<sub>Initializer</sub>

A vector with the specified scalar in all lanes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating value: Self.Scalar)
```

## Discussion

Equivalent to:

```swift
var result = Self()
for i in result.indices {
  result[i] = scalar
}
```
