---
title: 'firstRange(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/firstrange(of:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/firstrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/firstrange%28of%3A%29.json'
content_hash: 'sha256:f7cd39611524117a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# firstRange(of:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of a given collection within this collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstRange<C>(of other: C) -> Range<Self.Index>? where C : Collection, Self.Element == C.Element
```

## Parameters

- `other` — The collection to search for.

## Return Value

A range in the collection of the first occurrence of `sequence`. Returns nil if `sequence` is not found.
