---
title: 'onPencilSqueeze(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onpencilsqueeze(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onpencilsqueeze(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onpencilsqueeze%28perform%3A%29.json'
content_hash: 'sha256:cb8e8e3a2c230a99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onPencilSqueeze(perform:)

<sub>Instance Method</sub>

Adds an action to perform when the user squeezes their Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onPencilSqueeze(perform action: @escaping (PencilSqueezeGesturePhase) -> Void) -> some View

```

## Parameters

- `action` — The action to perform when the user squeezes their Apple Pencil.

## Return Value

A view that performs `action` when the user squeezes their Apple Pencil.

## Discussion

You should respect people’s setting for the squeeze gesture by reading the [preferredPencilSqueezeAction](../environmentvalues/preferredpencilsqueezeaction.md) environment value, if the setting makes sense in your app. If it doesn’t, consider giving people a way to specify custom behavior in your app instead.

In the example below, completing an Apple Pencil squeeze gesture will…

- do nothing if this is what the user selected in the Settings app,
- switch the tool to ”Lasso” if this is the action they have configured in the app,
- spill the ink if this is the action they have configured in the app,
- present a custom contextual palette if they haven’t configured a custom action in the app and this is what they selected in the Settings app.

```swift
enum MyPencilAction: String {
    case spillInk
    ...
}

@Environment(\.preferredPencilSqueezeAction) private var preferredAction
@AppStorage("customPencilSqueezeAction") private var customAction: MyPencilAction?

@State private var contextualPaletteAnchor: PopoverAttachmentAnchor?
@State private var contextualPalettePresented = false

var body: some View {
    MyDrawingCanvas()
        .onPencilSqueeze { phase in
            guard preferredAction != .ignore else {
                // Skip if this is what the user prefers.
                return
            }
            if let customAction {
                // If a custom action is configured, respect it.
                if customAction == .spillInk {
                    switch phase {
                        // Spill the ink while the user is squeezing their Apple Pencil.
                    }
                }
            } else if preferredAction == .showContextualPalette, case let .ended(value) = phase {
                // Present a custom contextual palette if the user prefers it.
                contextualPaletteAnchor = value.hoverPose?.anchor.map { .point($0) }
                contextualPalettePresented = true
            }
        }
        .popover(
            isPresented: $contextualPalettePresented,
            attachmentAnchor: contextualPaletteAnchor ?? .point(.center)
        ) {
            MyContextualPalette()
        }
```

> [!note] Note
> If multiple views with the `onPencilSqueeze` view modifier are visible, all their action closures will be performed when the user squeezes their Apple Pencil.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [preferredPencilDoubleTapAction](../environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](../environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](../pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](../pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](../pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](../pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](../pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
