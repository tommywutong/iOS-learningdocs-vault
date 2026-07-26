---
title: pasteboard
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/pasteboard
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/pasteboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/pasteboard.json'
content_hash: 'sha256:109791b58e48eecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# pasteboard

<sub>Type Property</sub>

Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let pasteboard: CommandGroupPlacement
```

## Discussion

By default, this group includes the following commands in macOS:

- Cut
- Copy
- Paste
- Paste and Match Style
- Delete
- Select All

## See Also

### Content updates

- [textEditing](textediting.md) — Placement for commands that manipulate and transform text selections.
- [textFormatting](textformatting.md) — Placement for commands that manipulate and transform the styles applied to text selections.
- [undoRedo](undoredo.md) — Placement for commands that control the Undo Manager.
