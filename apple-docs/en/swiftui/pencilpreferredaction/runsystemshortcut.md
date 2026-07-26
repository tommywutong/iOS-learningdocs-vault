---
title: runSystemShortcut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilpreferredaction/runsystemshortcut
source_url: 'https://developer.apple.com/documentation/swiftui/pencilpreferredaction/runsystemshortcut'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilpreferredaction/runsystemshortcut.json'
content_hash: 'sha256:ee8555ade0270d61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilPreferredAction](../pencilpreferredaction.md)

# runSystemShortcut

<sub>Type Property</sub>

An action that runs a system shortcut.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let runSystemShortcut: PencilPreferredAction
```

## Discussion

If the user selects this as their preferred action to perform after double-tapping or squeezing their Apple Pencil, your app will never be notified when they do. Instead, you should only use this information to remind the user about their preference in your app’s UI.

## See Also

### Getting the preferred actions

- [ignore](ignore.md) — An action that does nothing.
- [showColorPalette](showcolorpalette.md) — An action that toggles the display of the color palette.
- [showContextualPalette](showcontextualpalette.md) — An action that toggles the display of the contextual palette, or the undo/redo panel if contextual palette is not available.
- [showInkAttributes](showinkattributes.md) — An action that toggles the display of the current tool’s ink attributes.
- [switchEraser](switcheraser.md) — An action that switches between the current tool and the eraser.
- [switchPrevious](switchprevious.md) — An action that switches between the current tool and the last used tool.
