---
title: UITrackingLayoutGuide
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitrackinglayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uitrackinglayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrackinglayoutguide.json'
content_hash: 'sha256:d1c44916c5f4da70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITrackingLayoutGuide

<sub>Class</sub>

A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITrackingLayoutGuide
```

## Relationships

- **Inherits From**: [UILayoutGuide](uilayoutguide.md)

- **Inherited By**: [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## Topics

### Configuring automatic constraint activation

- [- setConstraints:activeWhenNearEdge:](<uitrackinglayoutguide/setconstraints(__activewhennearedge_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [- setConstraints:activeWhenAwayFromEdge:](<uitrackinglayoutguide/setconstraints(__activewhenawayfrom_).md>) — Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [- constraintsActiveWhenNearEdge:](<uitrackinglayoutguide/constraints(activewhennearedge_).md>) — Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [- constraintsActiveWhenAwayFromEdge:](<uitrackinglayoutguide/constraints(activewhenawayfrom_).md>) — Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.

### Tracking constraints

- [- removeAllTrackedConstraints](<uitrackinglayoutguide/removealltrackedconstraints().md>) — Stops the layout guide from tracking any constraints.

## See Also

### Keyboard layout

- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md) — Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md) — A layout guide that represents the space the keyboard occupies in your app’s layout.
