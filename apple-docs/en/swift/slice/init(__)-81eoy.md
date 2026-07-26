---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/init(_:)-81eoy'
source_url: 'https://developer.apple.com/documentation/swift/slice/init(_:)-81eoy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/init%28_%3A%29-81eoy.json'
content_hash: 'sha256:b6c5aefafa5a9b48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance of a collection containing the elements of a sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements` — The sequence of elements for the new collection.
