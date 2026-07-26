---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/startindex
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/startindex.json'
content_hash: 'sha256:9f9c381f32b64b39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: Int { get }
```

## Discussion

`ArraySlice` instances are not always indexed from zero. Use `startIndex` and `endIndex` as the bounds for any element access, instead of `0` and `count`.

If the array is empty, `startIndex` is equal to `endIndex`.
