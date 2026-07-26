---
title: UIPencilPreferredAction.ignore
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.1+, iPadOS 12.1+, Mac Catalyst 13.1+, visionOS 26.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilpreferredaction/ignore
source_url: 'https://developer.apple.com/documentation/uikit/uipencilpreferredaction/ignore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilpreferredaction/ignore.json'
content_hash: 'sha256:ff0533150d95ec67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilPreferredAction](../uipencilpreferredaction.md)

# UIPencilPreferredAction.ignore

<sub>Case</sub>

An action that does nothing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case ignore
```

## Discussion

The system returns this action if any of the following conditions are true:

- The Apple Pencil doesn’t have a configured preferred action.
- The iPad’s accessibility settings disable Apple Pencil interactions.

## See Also

### Preferred actions

- [UIPencilPreferredActionSwitchEraser](switcheraser.md) — An action that switches between the current tool and the eraser.
- [UIPencilPreferredActionSwitchPrevious](switchprevious.md) — An action that switches between the current tool and the last used tool.
- [UIPencilPreferredActionShowColorPalette](showcolorpalette.md) — An action that toggles the display of the color palette.
- [UIPencilPreferredActionShowInkAttributes](showinkattributes.md) — An action that toggles the display of the selected tool’s ink attributes.
- [UIPencilPreferredActionShowContextualPalette](showcontextualpalette.md) — An action that toggles shows a contextual palette of markup tools, or undo and redo options if tools aren’t available.
- [UIPencilPreferredActionRunSystemShortcut](runsystemshortcut.md) — An action that runs a system shortcut.
