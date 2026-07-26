---
title: 'pointerStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/pointerstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/pointerstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/pointerstyle%28_%3A%29.json'
content_hash: 'sha256:e683e17b0a29e38d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# pointerStyle(_:)

<sub>Instance Method</sub>

Sets the pointer style to display when the pointer is over the view.

<sub>macOS, visionOS</sub>

```swift
nonisolated func pointerStyle(_ style: PointerStyle?) -> some View

```

## Parameters

- `style` — The pointer style to use.

## Return Value

A view that changes the style of the pointer when hovered.

## Discussion

Refer to [PointerStyle](../pointerstyle.md) for a list of available pointer styles.

For guidance on choosing an appropriate pointer style, refer to [Pointing devices](../../design/human-interface-guidelines/pointing-devices.md) in the Human Interface Guidelines.

In this example, the pointer style indicates rectangular selection is possible while the Option modifier key is pressed:

```swift
enum ToolMode {
    // ...
    case selection
}

struct ImageEditorView: View {
    @State private var toolMode?

    var body: some View {
        ImageCanvasView()
            .pointerStyle(
                toolMode == .selection ? .rectSelection : nil)
            .onModifierKeysChanged { _, modifierKeys in
                if modifierKeys.contains(.option) {
                    toolMode = .selection
                } else {
                    toolMode = nil
                }
            }
    }
}
```

## See Also

### Modifying pointer appearance

- [PointerStyle](../pointerstyle.md) — A style describing the appearance of the pointer (also called a cursor) when it’s hovered over a view.
- [pointerVisibility(_:)](<pointervisibility(__).md>) — Sets the visibility of the pointer when it’s over the view.
