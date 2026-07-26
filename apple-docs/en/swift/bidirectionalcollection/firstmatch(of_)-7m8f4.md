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
doc_path: '/documentation/swift/bidirectionalcollection/firstmatch(of:)-7m8f4'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/firstmatch(of:)-7m8f4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/firstmatch%28of%3A%29-7m8f4.json'
content_hash: 'sha256:3614464e94f2938a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# firstMatch(of:)

<sub>Instance Method</sub>

Returns the first match of the specified regex within the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstMatch<Output>(of r: some RegexComponent) -> Regex<Output>.Match?
```

## Return Value

The first match of `regex` in the collection, or `nil` if there isn’t a match.
