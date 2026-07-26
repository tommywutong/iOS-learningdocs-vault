---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/match/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/match/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/match/init%28_%3A%29.json'
content_hash: 'sha256:b073f890aa46ce7f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Regex](../../regex.md) · [Match](../match.md)

# init(_:)

<sub>Initializer</sub>

Creates a regular expression match with a dynamic capture list from the given match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<OtherOutput>(_ match: Regex<OtherOutput>.Match)
```

## Parameters

- `match` — A regular expression match to convert to a match with type-erased captures.

## Discussion

You can use this initializer to convert a `Regex.Match` with strongly-typed captures into a match with the type-eraser `AnyRegexOutput` as its output type.
