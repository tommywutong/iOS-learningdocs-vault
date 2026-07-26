---
title: PencilSqueezeGesturePhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilsqueezegesturephase
source_url: 'https://developer.apple.com/documentation/swiftui/pencilsqueezegesturephase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilsqueezegesturephase.json'
content_hash: 'sha256:b397729d60561646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PencilSqueezeGesturePhase

<sub>Enumeration</sub>

Describes the phase and value of an Apple Pencil squeeze gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@frozen enum PencilSqueezeGesturePhase
```

## Overview

When you use the [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) view modifier, you can handle the Apple Pencil squeeze gesture’s phase in the `action` closure.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Enumeration Cases

- [PencilSqueezeGesturePhase.active(_:)](<pencilsqueezegesturephase/active(__).md>) — The user started squeezing their Apple Pencil.
- [PencilSqueezeGesturePhase.ended(_:)](<pencilsqueezegesturephase/ended(__).md>) — The user successfully completed a squeeze gesture.
- [PencilSqueezeGesturePhase.failed](pencilsqueezegesturephase/failed.md) — The user started squeezing their Apple Pencil but failed to successfully complete the gesture.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
