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
doc_path: '/documentation/swift/bidirectionalcollection/wholematch(of:)-7741n'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/wholematch(of:)-7741n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/wholematch%28of%3A%29-7741n.json'
content_hash: 'sha256:e1f3a9a19f024b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# wholeMatch(of:)

<sub>Instance Method</sub>

Returns a match if this string is matched by the given regex in its entirety.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wholeMatch<R>(of regex: R) -> Regex<R.RegexOutput>.Match? where R : RegexComponent
```

## Parameters

- `regex` — The regular expression to match.

## Return Value

The match, if one is found. If there is no match, or a transformation in `regex` throws an error, this method returns `nil`.
