---
title: 'subscript(unchecked:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/subscript(unchecked:)-2no6f'
source_url: 'https://developer.apple.com/documentation/swift/span/subscript(unchecked:)-2no6f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/subscript%28unchecked%3A%29-2no6f.json'
content_hash: 'sha256:c880c542aa6dae78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# subscript(unchecked:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index in the `Span`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(unchecked position: Span<Element>.Index) -> Element { get }
```

## Parameters

- `position` — The offset of the element to access. `position` must be greater or equal to zero, and less than `count`.

## Overview

This subscript does not validate `position`. Using this subscript with an invalid `position` results in undefined behaviour.

> [!abstract] Complexity
> O(1)
