---
title: PencilDoubleTapGestureValue
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencildoubletapgesturevalue
source_url: 'https://developer.apple.com/documentation/swiftui/pencildoubletapgesturevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencildoubletapgesturevalue.json'
content_hash: 'sha256:afd9963eb94199ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PencilDoubleTapGestureValue

<sub>Structure</sub>

Describes the value of an Apple Pencil double-tap gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PencilDoubleTapGestureValue
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the gesture values

- [hoverPose](pencildoubletapgesturevalue/hoverpose.md) — The location and distance of an Apple Pencil hovering in the area above the view’s bounds when the double-tap gesture occurred.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilSqueezeGestureValue](pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
