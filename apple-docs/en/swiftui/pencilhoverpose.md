---
title: PencilHoverPose
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilhoverpose
source_url: 'https://developer.apple.com/documentation/swiftui/pencilhoverpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilhoverpose.json'
content_hash: 'sha256:49c50c4649f0dfbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PencilHoverPose

<sub>Structure</sub>

A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PencilHoverPose
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the hover characteristics

- [altitude](pencilhoverpose/altitude.md) — A value that represents the altitude angle of the hovering Apple Pencil.
- [anchor](pencilhoverpose/anchor.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [azimuth](pencilhoverpose/azimuth.md) — A value that represents the azimuth angle of a hovering Apple Pencil.
- [location](pencilhoverpose/location.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [roll](pencilhoverpose/roll.md) — A value that represents the barrel roll angle of the hovering Apple Pencil.
- [zDistance](pencilhoverpose/zdistance.md) — The normalized distance between the screen and a hovering Apple Pencil.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
