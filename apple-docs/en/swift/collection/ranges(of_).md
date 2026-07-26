---
title: 'ranges(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/ranges(of:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/ranges(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/ranges%28of%3A%29.json'
content_hash: 'sha256:803cc07a39f3ea79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# ranges(of:)

<sub>Instance Method</sub>

Finds and returns the ranges of the all occurrences of a given sequence within the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ranges<C>(of other: C) -> [Range<Self.Index>] where C : Collection, Self.Element == C.Element
```

## Parameters

- `other` — The sequence to search for.

## Return Value

A collection of ranges of all occurrences of `other`. Returns an empty collection if `other` is not found.
