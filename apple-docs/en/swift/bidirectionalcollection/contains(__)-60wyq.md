---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/contains(_:)-60wyq'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/contains(_:)-60wyq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/contains%28_%3A%29-60wyq.json'
content_hash: 'sha256:584d80d2c143a31a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this collection contains a match for the regex, where the regex is created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(@RegexComponentBuilder _ content: () -> some RegexComponent) -> Bool
```

## Parameters

- `content` — A closure that returns a regex to search for within this collection.

## Return Value

`true` if the regex returned by `content` matched anywhere in this collection, otherwise `false`.
