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
doc_path: '/documentation/swift/bidirectionalcollection/contains(_:)-1l08t'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/contains(_:)-1l08t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/contains%28_%3A%29-1l08t.json'
content_hash: 'sha256:fe7b93fbc4b7de13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the collection contains the given regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ regex: some RegexComponent) -> Bool
```

## Parameters

- `regex` — A regex to search for within this collection.

## Return Value

`true` if the regex was found in the collection, otherwise `false`.
