---
title: 'applying(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/applying(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/applying(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/applying%28_%3A%29.json'
content_hash: 'sha256:3b26505d5b2086c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# applying(_:)

<sub>Instance Method</sub>

Returns a path constructed by applying the transform to all points of the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applying(_ transform: CGAffineTransform) -> Path
```

## Parameters

- `transform` — An affine transform to apply to the path.

## Return Value

A new copy of the path with the transform applied to all points.

## See Also

### Transforming the path

- [offsetBy(dx:dy:)](<offsetby(dx_dy_).md>) — Returns a path constructed by translating all its points.
- [trimmedPath(from:to:)](<trimmedpath(from_to_).md>) — Returns a partial copy of the path.
