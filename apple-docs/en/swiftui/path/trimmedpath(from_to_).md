---
title: 'trimmedPath(from:to:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/trimmedpath(from:to:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/trimmedpath(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/trimmedpath%28from%3Ato%3A%29.json'
content_hash: 'sha256:082e801b39a1a60a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# trimmedPath(from:to:)

<sub>Instance Method</sub>

Returns a partial copy of the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trimmedPath(from: CGFloat, to: CGFloat) -> Path
```

## Discussion

The returned path contains the region between `from` and `to`, both of which must be fractions between zero and one defining points linearly-interpolated along the path.

## See Also

### Transforming the path

- [applying(_:)](<applying(__).md>) — Returns a path constructed by applying the transform to all points of the path.
- [offsetBy(dx:dy:)](<offsetby(dx_dy_).md>) — Returns a path constructed by translating all its points.
