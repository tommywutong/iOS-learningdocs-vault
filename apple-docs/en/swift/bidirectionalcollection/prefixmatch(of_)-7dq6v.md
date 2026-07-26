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
doc_path: '/documentation/swift/bidirectionalcollection/prefixmatch(of:)-7dq6v'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/prefixmatch(of:)-7dq6v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/prefixmatch%28of%3A%29-7dq6v.json'
content_hash: 'sha256:0f26d92c040172ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# prefixMatch(of:)

<sub>Instance Method</sub>

Returns a match if this string is matched by the given regex at its start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefixMatch<R>(of regex: R) -> Regex<R.RegexOutput>.Match? where R : RegexComponent
```

## Parameters

- `regex` — The regular expression to match.

## Return Value

The match, if one is found. If there is no match, or a transformation in `regex` throws an error, this method returns `nil`.
