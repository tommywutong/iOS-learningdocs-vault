---
title: 'prefixMatch(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/prefixmatch(of:)-2fwv6'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/prefixmatch(of:)-2fwv6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/prefixmatch%28of%3A%29-2fwv6.json'
content_hash: 'sha256:8a0c7507778fef77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# prefixMatch(of:)

<sub>Instance Method</sub>

Matches part of the regex, starting at the beginning, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefixMatch<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> Regex<Output>.Match?
```

## Parameters

- `content` — A closure that returns a regex to match against.

## Return Value

The match if there is one, or `nil` if none.
