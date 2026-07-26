---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/subscript(_:)-84ykx'
source_url: 'https://developer.apple.com/documentation/swift/range/subscript(_:)-84ykx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/subscript%28_%3A%29-84ykx.json'
content_hash: 'sha256:462866fb4422ea2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Range<Bound>.Index) -> Range<Bound>.Element { get }
```

## Parameters

- `position` — The position of the element to access. `position` must be a valid index of the range, and must not equal the range’s end index.

## Overview

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.
