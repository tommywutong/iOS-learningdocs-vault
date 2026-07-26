---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/subscript%28_%3A%29.json'
content_hash: 'sha256:8e42184c7bd2e00c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: InlineArray<count, Element>.Index) -> Element { get set }
```

## Parameters

- `i` — The position of the element to access. `i` must be a valid index of the array that is not equal to the `endIndex` property.

## Overview

> [!abstract] Complexity
> O(1)
