---
title: components
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/components
source_url: 'https://developer.apple.com/documentation/swift/duration/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/components.json'
content_hash: 'sha256:281d1bc7b4818411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# components

<sub>Instance Property</sub>

The composite components of the `Duration`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var components: (seconds: Int64, attoseconds: Int64) { get }
```

## Discussion

This is intended for facilitating conversions to existing time types. The attoseconds value will not exceed 1e18 or be lower than -1e18.
