---
title: 'subscript(unchecked:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/subscript(unchecked:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/subscript(unchecked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/subscript%28unchecked%3A%29.json'
content_hash: 'sha256:dd2f1158081a82fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# subscript(unchecked:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(unchecked i: InlineArray<count, Element>.Index) -> Element { get set }
```

## Parameters

- `i` — The position of the element to access. `i` must be a valid index of the array that is not equal to the `endIndex` property.

## Overview

> [!warning] Warning
> This subscript trades safety for performance. Using an invalid index results in undefined behavior.

> [!abstract] Complexity
> O(1)
