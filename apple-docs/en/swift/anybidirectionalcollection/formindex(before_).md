---
title: 'formIndex(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anybidirectionalcollection/formindex(before:)'
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/formindex(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/formindex%28before%3A%29.json'
content_hash: 'sha256:3f7f8b3093bdf15b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# formIndex(before:)

<sub>Instance Method</sub>

Replaces the given index with its predecessor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(before i: inout AnyBidirectionalCollection<Element>.Index)
```

## Parameters

- `i` — A valid index of the collection. `i` must be greater than `startIndex`.
