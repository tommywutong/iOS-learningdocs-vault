---
title: 'wholeMatch(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/wholematch(of:)-1wbp6'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/wholematch(of:)-1wbp6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/wholematch%28of%3A%29-1wbp6.json'
content_hash: 'sha256:3b849c44298d2acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# wholeMatch(of:)

<sub>Instance Method</sub>

Matches a regex in its entirety, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wholeMatch<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> Regex<Output>.Match?
```

## Parameters

- `content` — A closure that returns a regex to match against.

## Return Value

The match if there is one, or `nil` if none.
