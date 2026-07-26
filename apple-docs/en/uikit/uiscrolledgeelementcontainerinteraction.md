---
title: UIScrollEdgeElementContainerInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrolledgeelementcontainerinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiscrolledgeelementcontainerinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrolledgeelementcontainerinteraction.json'
content_hash: 'sha256:4cebf03574b5d1e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScrollEdgeElementContainerInteraction

<sub>Class</sub>

Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIScrollEdgeElementContainerInteraction
```

## Overview

In the following example, an interaction is added to a container view of buttons that overlay the bottom edge of a scroll view.

```
let interaction = UIScrollEdgeElementContainerInteraction()
interaction.scrollView = scrollView
interaction.edge = .bottom
buttonContainer.addInteraction(interaction)
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Instance Properties

- [edge](uiscrolledgeelementcontainerinteraction/edge.md) — The edge of the scroll view to affect
- [scrollView](uiscrolledgeelementcontainerinteraction/scrollview.md) — The scroll view to affect

## See Also

### Interacting with adjacent views

- [UIBackgroundExtensionView](uibackgroundextensionview.md) — A view that extends content to fill its own bounds.
