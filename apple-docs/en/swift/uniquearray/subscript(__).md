---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/subscript%28_%3A%29.json'
content_hash: 'sha256:7057b6654eda2787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Int) -> Element { borrow mutate }
```

## Parameters

- `position` — The position of the element to access. The position must be a valid index of the array that is not equal to the `endIndex` property.

## Overview

> [!abstract] Complexity
> O(1)
