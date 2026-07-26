---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewdimensions3d/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewdimensions3d/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewdimensions3d/subscript%28_%3A%29.json'
content_hash: 'sha256:27d8a77048a2e92c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewDimensions3D](../viewdimensions3d.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Gets the value of the given depth guide.

<sub>visionOS</sub>

```swift
subscript(guide: DepthAlignment) -> CGFloat { get }
```

## Overview

Find the offset of a particular guide in the corresponding view by using that guide as an index to read from the context:

```swift
.alignmentGuide(.front) { context in
    context[.front] - 10
}
```

For information about using subscripts in Swift to access member elements of a collection, list, or, sequence, see [Subscripts](https://docs.swift.org/swift-book/LanguageGuide/Subscripts.html) in _The Swift Programming Language_.
