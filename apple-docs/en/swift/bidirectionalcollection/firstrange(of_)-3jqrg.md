---
title: 'firstRange(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/firstrange(of:)-3jqrg'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/firstrange(of:)-3jqrg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/firstrange%28of%3A%29-3jqrg.json'
content_hash: 'sha256:c3435183d09abf59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# firstRange(of:)

<sub>Instance Method</sub>

Returns the range of the first match for the regex within this collection, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstRange(@RegexComponentBuilder of content: () -> some RegexComponent) -> Range<Self.Index>?
```

## Parameters

- `content` — A closure that returns a regex to search for.

## Return Value

A range in the collection of the first occurrence of the first match of if the regex returned by `content`. Returns `nil` if no match for the regex is found.
