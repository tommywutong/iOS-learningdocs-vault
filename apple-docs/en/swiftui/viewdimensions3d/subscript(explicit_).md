---
title: 'subscript(explicit:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewdimensions3d/subscript(explicit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewdimensions3d/subscript(explicit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewdimensions3d/subscript%28explicit%3A%29.json'
content_hash: 'sha256:59134e5918da5135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewDimensions3D](../viewdimensions3d.md)

# subscript(explicit:)

<sub>Instance Subscript</sub>

Gets the explicit value of the given depth alignment guide

<sub>visionOS</sub>

```swift
subscript(explicit guide: DepthAlignment) -> CGFloat? { get }
```

## Overview

Find the depth offset of a particular guide in the corresponding view by using that guide as an index to read from the context:

```swift
.alignmentGuide(.front) { context in
    context[.front] - 10
}
```

This subscript returns `nil` if no value exists for the guide.

For information about using subscripts in Swift to access member elements of a collection, list, or, sequence, see [Subscripts](https://docs.swift.org/swift-book/LanguageGuide/Subscripts.html) in _The Swift Programming Language_.
