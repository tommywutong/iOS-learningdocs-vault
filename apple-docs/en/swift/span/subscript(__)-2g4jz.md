---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/subscript(_:)-2g4jz'
source_url: 'https://developer.apple.com/documentation/swift/span/subscript(_:)-2g4jz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/subscript%28_%3A%29-2g4jz.json'
content_hash: 'sha256:3703a933c52eff91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index in the `Span`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Span<Element>.Index) -> Element { get }
```

## Parameters

- `position` — The offset of the element to access. `position` must be greater or equal to zero, and less than `count`.

## Overview

> [!abstract] Complexity
> O(1)
