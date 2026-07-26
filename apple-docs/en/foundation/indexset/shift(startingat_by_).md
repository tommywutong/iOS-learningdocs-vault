---
title: 'shift(startingAt:by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/shift(startingat:by:)'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/shift(startingat:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/shift%28startingat%3Aby%3A%29.json'
content_hash: 'sha256:d5815b61276a7800'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# shift(startingAt:by:)

<sub>Instance Method</sub>

For a positive delta, shifts the indexes in [index, INT_MAX] to the right, thereby inserting an “empty space” [index, delta], for a negative delta, shifts the indexes in [index, INT_MAX] to the left, thereby deleting the indexes in the range [index - delta, delta].

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func shift(startingAt integer: IndexSet.Element, by delta: Int)
```
