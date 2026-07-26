---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewdimensions/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewdimensions/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewdimensions/subscript%28_%3A%29.json'
content_hash: 'sha256:7c985735d1db8f1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewDimensions](../viewdimensions.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Gets the value of the given horizontal guide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(guide: HorizontalAlignment) -> CGFloat { get }
```

## Overview

Find the offset of a particular guide in the corresponding view by using that guide as an index to read from the context:

```swift
.alignmentGuide(.leading) { context in
    context[.leading] - 10
}
```

For information about using subscripts in Swift to access member elements of a collection, list, or, sequence, see [Subscripts](https://docs.swift.org/swift-book/LanguageGuide/Subscripts.html) in _The Swift Programming Language_.

## See Also

### Accessing guide values

- [subscript(explicit:)](<subscript(explicit_).md>) — Gets the explicit value of the given horizontal alignment guide.
