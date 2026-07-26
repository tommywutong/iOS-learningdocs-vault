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
doc_path: '/documentation/swift/rangereplaceablecollection/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/init%28_%3A%29.json'
content_hash: 'sha256:63fc6b3b75e80319'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance of a collection containing the elements of a sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements` — The sequence of elements for the new collection. `elements` must be finite.

## Default Implementations

### RangeReplaceableCollection Implementations

- [init(_:)](<init(__)-2c3y1.md>) — Creates a new instance of a collection containing the elements of a sequence.
