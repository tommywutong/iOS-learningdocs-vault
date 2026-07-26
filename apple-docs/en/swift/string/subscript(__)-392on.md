---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/subscript(_:)-392on'
source_url: 'https://developer.apple.com/documentation/swift/string/subscript(_:)-392on'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/subscript%28_%3A%29-392on.json'
content_hash: 'sha256:85263deee69ed7ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

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
