---
title: 'insert(contentsOf:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/insert(contentsof:at:)-3z6ts'
source_url: 'https://developer.apple.com/documentation/swift/slice/insert(contentsof:at:)-3z6ts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/insert%28contentsof%3Aat%3A%29-3z6ts.json'
content_hash: 'sha256:b1db32401cbde0a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# insert(contentsOf:at:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert<S>(contentsOf newElements: S, at i: Slice<Base>.Index) where S : Collection, Base.Element == S.Element
```
