---
title: layoutDirection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/layoutdirection
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/layoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/layoutdirection.json'
content_hash: 'sha256:0e7c77a2fec2b4b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# layoutDirection

<sub>Instance Property</sub>

The layout direction associated with the current environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var layoutDirection: LayoutDirection { get set }
```

## Discussion

Use this value to determine or set whether the environment uses a left-to-right or right-to-left direction.

## See Also

### Setting a layout direction

- [layoutDirectionBehavior(_:)](<../view/layoutdirectionbehavior(__).md>) — Sets the behavior of this view for different layout directions.
- [LayoutDirectionBehavior](../layoutdirectionbehavior.md) — A description of what should happen when the layout direction changes.
- [LayoutDirection](../layoutdirection.md) — A direction in which SwiftUI can lay out content.
- [LayoutRotationUnaryLayout](../layoutrotationunarylayout.md)
