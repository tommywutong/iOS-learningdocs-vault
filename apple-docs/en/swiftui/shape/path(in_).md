---
title: 'path(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/path(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/path(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/path%28in%3A%29.json'
content_hash: 'sha256:34ebb6940b438a64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# path(in:)

<sub>Instance Method</sub>

Describes this shape as a path within a rectangular frame of reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func path(in rect: CGRect) -> Path
```

## Parameters

- `rect` — The frame of reference for describing this shape.

## Return Value

A path that describes this shape.

## See Also

### Defining a shape’s size and path

- [sizeThatFits(_:)](<sizethatfits(__).md>) — Returns the size of the view that will render the shape, given a proposed size.
