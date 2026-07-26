---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazyfiltersequence/subscript(_:)-6uzbx'
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/subscript(_:)-6uzbx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/subscript%28_%3A%29-6uzbx.json'
content_hash: 'sha256:eee7c263ecb6c724'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses a view of this collection with the elements at the given indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(subranges: RangeSet<Self.Index>) -> DiscontiguousSlice<Self> { get }
```

## Parameters

- `subranges` — The indices of the elements to retrieve from this collection.

## Return Value

A collection of the elements at the positions in `subranges`.

## Overview

> [!abstract] Complexity
> O(1)
