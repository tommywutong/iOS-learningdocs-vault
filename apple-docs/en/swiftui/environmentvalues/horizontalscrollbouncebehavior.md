---
title: horizontalScrollBounceBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/horizontalscrollbouncebehavior
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/horizontalscrollbouncebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/horizontalscrollbouncebehavior.json'
content_hash: 'sha256:e3e3e2569f6ce132'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# horizontalScrollBounceBehavior

<sub>Instance Property</sub>

The scroll bounce mode for the horizontal axis of scrollable views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var horizontalScrollBounceBehavior: ScrollBounceBehavior { get set }
```

## Discussion

Use the [scrollBounceBehavior(_:axes:)](<../view/scrollbouncebehavior(__axes_).md>) view modifier to set this value in the [Environment](../environment.md).

## See Also

### Configuring scroll bounce behavior

- [scrollBounceBehavior(_:axes:)](<../view/scrollbouncebehavior(__axes_).md>) — Configures the bounce behavior of scrollable views along the specified axis.
- [verticalScrollBounceBehavior](verticalscrollbouncebehavior.md) — The scroll bounce mode for the vertical axis of scrollable views.
- [ScrollBounceBehavior](../scrollbouncebehavior.md) — The ways that a scrollable view can bounce when it reaches the end of its content.
