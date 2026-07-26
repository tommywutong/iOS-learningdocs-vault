---
title: 'firstMatch(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/firstmatch(of:)-6v8ci'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/firstmatch(of:)-6v8ci'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/firstmatch%28of%3A%29-6v8ci.json'
content_hash: 'sha256:4899ec7de5aeddb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# firstMatch(of:)

<sub>Instance Method</sub>

Returns the first match for the regex within this collection, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstMatch<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> Regex<Output>.Match?
```

## Parameters

- `content` — A closure that returns the regex to search for.

## Return Value

The first match for the regex created by `content` in this collection, or `nil` if no match is found.
