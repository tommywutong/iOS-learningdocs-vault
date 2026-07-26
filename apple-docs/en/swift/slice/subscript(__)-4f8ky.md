---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/subscript(_:)-4f8ky'
source_url: 'https://developer.apple.com/documentation/swift/slice/subscript(_:)-4f8ky'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/subscript%28_%3A%29-4f8ky.json'
content_hash: 'sha256:1e2b6283956fdf5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<R>(r: R) -> Self.SubSequence where R : RangeExpression, Self.Index == R.Bound { get set }
```
