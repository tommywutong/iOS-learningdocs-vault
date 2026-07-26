---
title: undoRedo
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/undoredo
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/undoredo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/undoredo.json'
content_hash: 'sha256:329425f1adfbde11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# undoRedo

<sub>Type Property</sub>

Placement for commands that control the Undo Manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let undoRedo: CommandGroupPlacement
```

## Discussion

By default, this group includes the following commands in macOS:

- Undo
- Redo

## See Also

### Content updates

- [pasteboard](pasteboard.md) — Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.
- [textEditing](textediting.md) — Placement for commands that manipulate and transform text selections.
- [textFormatting](textformatting.md) — Placement for commands that manipulate and transform the styles applied to text selections.
