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
doc_path: '/documentation/swift/bidirectionalcollection/firstrange(of:)-5sum7'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/firstrange(of:)-5sum7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/firstrange%28of%3A%29-5sum7.json'
content_hash: 'sha256:29c99ca0023bf471'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

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

A range in the collection of the first occurrence of `sequence`. Returns `nil` if `sequence` is not found.
