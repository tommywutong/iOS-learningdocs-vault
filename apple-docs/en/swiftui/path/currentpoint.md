---
title: currentPoint
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/path/currentpoint
source_url: 'https://developer.apple.com/documentation/swiftui/path/currentpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/currentpoint.json'
content_hash: 'sha256:7bdb2156a7ef00a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# currentPoint

<sub>Instance Property</sub>

Returns the last point in the path, or nil if the path contains no points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentPoint: CGPoint? { get }
```

## See Also

### Getting the path’s characteristics

- [boundingRect](boundingrect.md) — A rectangle containing all path segments.
- [cgPath](cgpath.md) — An immutable path representing the elements in the path.
- [contains(_:eoFill:)](<contains(__eofill_).md>) — Returns true if the path contains a specified point.
- [description](description.md) — A description of the path that may be used to recreate the path via `init?(_:)`.
- [isEmpty](isempty.md) — A Boolean value indicating whether the path contains zero elements.
