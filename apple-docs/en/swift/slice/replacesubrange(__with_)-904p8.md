---
title: 'replaceSubrange(_:with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/replacesubrange(_:with:)-904p8'
source_url: 'https://developer.apple.com/documentation/swift/slice/replacesubrange(_:with:)-904p8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/replacesubrange%28_%3Awith%3A%29-904p8.json'
content_hash: 'sha256:10ba83c3b21d2ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# replaceSubrange(_:with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange<C>(_ subRange: Range<Slice<Base>.Index>, with newElements: C) where C : Collection, Base.Element == C.Element
```
