---
title: UILayoutSupport
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutsupport
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutsupport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutsupport.json'
content_hash: 'sha256:bf1248e864c61f2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILayoutSupport

<sub>Protocol</sub>

A set of methods that provide layout support and access to layout anchors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UILayoutSupport : NSObjectProtocol
```

## Overview

This protocol is implemented by the [UIViewController](uiviewcontroller.md) properties [topLayoutGuide](uiviewcontroller/toplayoutguide.md) and [bottomLayoutGuide](uiviewcontroller/bottomlayoutguide.md) to support using Auto Layout with a view controller’s view. You can use layout guides as layout items in the [NSLayoutConstraint](nslayoutconstraint.md) factory methods.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating constraints using layout anchors

- [bottomAnchor](uilayoutsupport/bottomanchor.md) — A layout anchor representing the guide’s bottom edge.
- [heightAnchor](uilayoutsupport/heightanchor.md) — A layout anchor representing the guide’s height.
- [topAnchor](uilayoutsupport/topanchor.md) — A layout anchor representing the guide’s top edge.

### Performing layout calculations

- [length](uilayoutsupport/length.md) — Provides the length, in points, of the portion of a view controller’s view that is overlaid by translucent or transparent UIKit bars.

## See Also

### Constraints

- [Positioning content within layout margins](positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [NSLayoutConstraint](nslayoutconstraint.md) — The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
