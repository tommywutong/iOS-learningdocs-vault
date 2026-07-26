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
doc_path: '/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-1luge'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-1luge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/trimmingprefix%28_%3A%29-1luge.json'
content_hash: 'sha256:abaa88cfcc4c3fe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# trimmingPrefix(_:)

<sub>Instance Method</sub>

Returns a new collection of the same type by removing the initial elements that matches the given regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trimmingPrefix(_ regex: some RegexComponent) -> Self.SubSequence
```

## Parameters

- `regex` — The regex to remove from this collection.

## Return Value

A collection containing the elements that does not match `regex` from the start.
