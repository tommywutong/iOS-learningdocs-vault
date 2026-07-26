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
doc_path: '/documentation/swift/bidirectionalcollection/matches(of:)-5eey9'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/matches(of:)-5eey9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/matches%28of%3A%29-5eey9.json'
content_hash: 'sha256:5e6dbb5998c95ad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# matches(of:)

<sub>Instance Method</sub>

Returns a collection containing all non-overlapping matches of the regex, created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func matches<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> [Regex<Output>.Match]
```

## Parameters

- `content` — A closure that returns the regex to search for.

## Return Value

A collection of matches for the regex returned by `content`. If no matches are found, the returned collection is empty.
