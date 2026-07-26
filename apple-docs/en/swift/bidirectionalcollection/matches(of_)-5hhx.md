---
title: 'matches(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/matches(of:)-5hhx'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/matches(of:)-5hhx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/matches%28of%3A%29-5hhx.json'
content_hash: 'sha256:9a5b94028c36909e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# matches(of:)

<sub>Instance Method</sub>

Returns a collection containing all matches of the specified regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func matches<Output>(of r: some RegexComponent) -> [Regex<Output>.Match]
```

## Return Value

A collection of matches of `regex`.
