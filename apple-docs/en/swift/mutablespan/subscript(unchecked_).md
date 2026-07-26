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
doc_path: '/documentation/swift/mutablespan/subscript(unchecked:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/subscript(unchecked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/subscript%28unchecked%3A%29.json'
content_hash: 'sha256:b6e1f151430a386b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# subscript(unchecked:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index in the `MutableSpan`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(unchecked position: MutableSpan<Element>.Index) -> Element { borrow mutate }
```

## Parameters

- `position` — The offset of the element to access. `position` must be greater or equal to zero, and less than `count`.

## Overview

This subscript does not validate `position`; this is an unsafe operation.

> [!abstract] Complexity
> O(1)
