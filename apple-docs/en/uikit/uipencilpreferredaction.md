---
title: UIPencilPreferredAction
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.1+, iPadOS 12.1+, Mac Catalyst 13.1+, visionOS 26.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilpreferredaction
source_url: 'https://developer.apple.com/documentation/uikit/uipencilpreferredaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilpreferredaction.json'
content_hash: 'sha256:2087972d3be0c0fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPencilPreferredAction

<sub>Enumeration</sub>

The actions Apple Pencil can perform after a person performs a double tap or squeeze.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIPencilPreferredAction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Preferred actions

- [UIPencilPreferredActionIgnore](uipencilpreferredaction/ignore.md) — An action that does nothing.
- [UIPencilPreferredActionSwitchEraser](uipencilpreferredaction/switcheraser.md) — An action that switches between the current tool and the eraser.
- [UIPencilPreferredActionSwitchPrevious](uipencilpreferredaction/switchprevious.md) — An action that switches between the current tool and the last used tool.
- [UIPencilPreferredActionShowColorPalette](uipencilpreferredaction/showcolorpalette.md) — An action that toggles the display of the color palette.
- [UIPencilPreferredActionShowInkAttributes](uipencilpreferredaction/showinkattributes.md) — An action that toggles the display of the selected tool’s ink attributes.
- [UIPencilPreferredActionShowContextualPalette](uipencilpreferredaction/showcontextualpalette.md) — An action that toggles shows a contextual palette of markup tools, or undo and redo options if tools aren’t available.
- [UIPencilPreferredActionRunSystemShortcut](uipencilpreferredaction/runsystemshortcut.md) — An action that runs a system shortcut.

### Initializers

- [init(rawValue:)](<uipencilpreferredaction/init(rawvalue_).md>)

## See Also

### Determining preferences for actions

- [preferredTapAction](uipencilinteraction/preferredtapaction.md) — A person’s preferred double-tap action for Apple Pencil, as specified in the Settings app.
- [preferredSqueezeAction](uipencilinteraction/preferredsqueezeaction.md) — A person’s preferred squeeze action for Apple Pencil, as specified in the Settings app.
