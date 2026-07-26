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
doc_path: '/documentation/swift/bidirectionalcollection/ranges(of:)-9qfdo'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/ranges(of:)-9qfdo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/ranges%28of%3A%29-9qfdo.json'
content_hash: 'sha256:292c332c85758761'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# ranges(of:)

<sub>Instance Method</sub>

Returns the ranges of the all non-overlapping matches for the regex within this collection, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ranges(@RegexComponentBuilder of content: () -> some RegexComponent) -> [Range<Self.Index>]
```

## Parameters

- `content` — A closure that returns a regex to search for.

## Return Value

A collection of ranges of all matches for the regex returned by `content`. Returns an empty collection if no match for the regex is found.
