---
title: 'offsetBy(dx:dy:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/offsetby(dx:dy:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/offsetby(dx:dy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/offsetby%28dx%3Ady%3A%29.json'
content_hash: 'sha256:d1c7627272f34a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# offsetBy(dx:dy:)

<sub>Instance Method</sub>

Returns a path constructed by translating all its points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func offsetBy(dx: CGFloat, dy: CGFloat) -> Path
```

## Parameters

- `dx` — The offset to apply in the horizontal axis.

- `dy` — The offset to apply in the vertical axis.

## Return Value

A new copy of the path with the offset applied to all points.

## See Also

### Transforming the path

- [applying(_:)](<applying(__).md>) — Returns a path constructed by applying the transform to all points of the path.
- [trimmedPath(from:to:)](<trimmedpath(from_to_).md>) — Returns a partial copy of the path.
