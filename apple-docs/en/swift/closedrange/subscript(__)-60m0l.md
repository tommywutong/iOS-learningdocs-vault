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
doc_path: '/documentation/swift/closedrange/subscript(_:)-60m0l'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/subscript(_:)-60m0l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/subscript%28_%3A%29-60m0l.json'
content_hash: 'sha256:f882fa2beecf48e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: ClosedRange<Bound>.Index) -> Bound { get }
```

## Parameters

- `position` — The position of the element to access. `position` must be a valid index of the range, and must not equal the range’s end index.

## Overview

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.
