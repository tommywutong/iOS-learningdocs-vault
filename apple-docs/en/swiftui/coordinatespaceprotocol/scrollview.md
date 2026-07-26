---
title: scrollView
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/coordinatespaceprotocol/scrollview
source_url: 'https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/scrollview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/coordinatespaceprotocol/scrollview.json'
content_hash: 'sha256:0c6fd4e0944f4529'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CoordinateSpaceProtocol](../coordinatespaceprotocol.md)

# scrollView

<sub>Type Property</sub>

The named coordinate space that is added by the system for the innermost containing scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var scrollView: NamedCoordinateSpace { get }
```

## See Also

### Getting built-in coordinate spaces

- [immersiveSpace](immersivespace.md) — The named coordinate space that represents the currently opened [ImmersiveSpace](../immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.
- [global](global.md) — The global coordinate space at the root of the view hierarchy.
- [local](local.md) — The local coordinate space of the current view.
- [named(_:)](<named(__).md>) — Creates a named coordinate space using the given value.
- [scrollView(axis:)](<scrollview(axis_).md>) — The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.
