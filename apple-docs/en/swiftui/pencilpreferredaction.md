---
title: PencilPreferredAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilpreferredaction
source_url: 'https://developer.apple.com/documentation/swiftui/pencilpreferredaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilpreferredaction.json'
content_hash: 'sha256:f584616b72180d34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PencilPreferredAction

<sub>Structure</sub>

An action that the user prefers to perform after double-tapping their Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PencilPreferredAction
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the preferred actions

- [ignore](pencilpreferredaction/ignore.md) — An action that does nothing.
- [runSystemShortcut](pencilpreferredaction/runsystemshortcut.md) — An action that runs a system shortcut.
- [showColorPalette](pencilpreferredaction/showcolorpalette.md) — An action that toggles the display of the color palette.
- [showContextualPalette](pencilpreferredaction/showcontextualpalette.md) — An action that toggles the display of the contextual palette, or the undo/redo panel if contextual palette is not available.
- [showInkAttributes](pencilpreferredaction/showinkattributes.md) — An action that toggles the display of the current tool’s ink attributes.
- [switchEraser](pencilpreferredaction/switcheraser.md) — An action that switches between the current tool and the eraser.
- [switchPrevious](pencilpreferredaction/switchprevious.md) — An action that switches between the current tool and the last used tool.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
