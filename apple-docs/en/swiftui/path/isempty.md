---
title: isEmpty
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/path/isempty
source_url: 'https://developer.apple.com/documentation/swiftui/path/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/isempty.json'
content_hash: 'sha256:4f3184cd75b46c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value indicating whether the path contains zero elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## See Also

### Getting the path’s characteristics

- [boundingRect](boundingrect.md) — A rectangle containing all path segments.
- [cgPath](cgpath.md) — An immutable path representing the elements in the path.
- [contains(_:eoFill:)](<contains(__eofill_).md>) — Returns true if the path contains a specified point.
- [currentPoint](currentpoint.md) — Returns the last point in the path, or nil if the path contains no points.
- [description](description.md) — A description of the path that may be used to recreate the path via `init?(_:)`.
