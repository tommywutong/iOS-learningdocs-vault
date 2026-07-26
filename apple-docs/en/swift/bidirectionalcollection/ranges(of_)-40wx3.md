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
doc_path: '/documentation/swift/bidirectionalcollection/ranges(of:)-40wx3'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/ranges(of:)-40wx3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/ranges%28of%3A%29-40wx3.json'
content_hash: 'sha256:1b451c950dfe0a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# ranges(of:)

<sub>Instance Method</sub>

Finds and returns the ranges of the all occurrences of a given sequence within the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ranges(of regex: some RegexComponent) -> [Range<Self.Index>]
```

## Parameters

- `regex` — The regex to search for.

## Return Value

A collection or ranges in the receiver of all occurrences of `regex`. Returns an empty collection if `regex` is not found.
