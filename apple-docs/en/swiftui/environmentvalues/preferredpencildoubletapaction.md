---
title: preferredPencilDoubleTapAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/preferredpencildoubletapaction
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/preferredpencildoubletapaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/preferredpencildoubletapaction.json'
content_hash: 'sha256:f4a8a644e5744c21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# preferredPencilDoubleTapAction

<sub>Instance Property</sub>

The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var preferredPencilDoubleTapAction: PencilPreferredAction { get }
```

## Discussion

You can read this value by creating a property with the [Environment](../environment.md) property wrapper and using it inside the action closure of the [onPencilDoubleTap(perform:)](<../view/onpencildoubletap(perform_).md>) view modifier as an indication of what to do after the user double-taps their Apple Pencil:

```swift
@Environment(\.preferredPencilDoubleTapAction) private var preferredAction

var body: some View {
    MyDrawingCanvas()
        .onPencilDoubleTap { value in
            switch preferredAction {
                ...
            }
        }
}
```

In macOS, this value cannot be changed by users and is always set to [switchEraser](../pencilpreferredaction/switcheraser.md).

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<../view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<../view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilSqueezeAction](preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](../pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](../pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](../pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](../pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](../pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
