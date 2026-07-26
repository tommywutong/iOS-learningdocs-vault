---
title: preferredPencilSqueezeAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/preferredpencilsqueezeaction
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction.json'
content_hash: 'sha256:b346524ef5b87754'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# preferredPencilSqueezeAction

<sub>Instance Property</sub>

The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var preferredPencilSqueezeAction: PencilPreferredAction { get }
```

## Discussion

You can read this value by creating a property with the [Environment](../environment.md) property wrapper and using it inside the action closure of the [onPencilSqueeze(perform:)](<../view/onpencilsqueeze(perform_).md>) view modifier as an indication of what to do when the user squeezes their Apple Pencil:

```swift
@Environment(\.preferredPencilSqueezeAction) private var preferredAction

var body: some View {
    MyDrawingCanvas()
        .onPencilSqueeze { phase in
            switch (phase, preferredAction) {
                ...
            }
        }
}
```

In macOS, this value cannot be changed by users and is always set to [showContextualPalette](../pencilpreferredaction/showcontextualpalette.md).

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<../view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<../view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](../pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](../pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](../pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](../pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](../pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
