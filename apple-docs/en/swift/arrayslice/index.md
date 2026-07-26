---
title: ArraySlice.Index
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/index
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/index.json'
content_hash: 'sha256:563c27f05b6efac5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# ArraySlice.Index

<sub>Type Alias</sub>

The index type for arrays, `Int`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Index = Int
```

## Discussion

`ArraySlice` instances are not always indexed from zero. Use `startIndex` and `endIndex` as the bounds for any element access, instead of `0` and `count`.
