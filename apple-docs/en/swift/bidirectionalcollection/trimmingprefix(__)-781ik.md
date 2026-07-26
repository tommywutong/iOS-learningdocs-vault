---
title: 'trimmingPrefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-781ik'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-781ik'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/trimmingprefix%28_%3A%29-781ik.json'
content_hash: 'sha256:a06339b5b702cd8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# trimmingPrefix(_:)

<sub>Instance Method</sub>

Returns a subsequence of this collection by removing the elements matching the regex from the start, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trimmingPrefix(@RegexComponentBuilder _ content: () -> some RegexComponent) -> Self.SubSequence
```

## Parameters

- `content` — A closure that returns the regex to search for at the start of this collection.

## Return Value

A collection containing the elements after those that match the regex returned by `content`. If the regex does not match at the start of the collection, the entire contents of this collection are returned.
