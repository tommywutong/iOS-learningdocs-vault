---
title: textEditing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/textediting
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/textediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/textediting.json'
content_hash: 'sha256:d987cb42e8c66058'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# textEditing

<sub>Type Property</sub>

Placement for commands that manipulate and transform text selections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let textEditing: CommandGroupPlacement
```

## Discussion

By default, this group includes the following commands in macOS:

- Find submenu
- Spelling and Grammar submenu
- Substitutions submenu
- Transformations submenu
- Speech submenu

## See Also

### Content updates

- [pasteboard](pasteboard.md) — Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.
- [textFormatting](textformatting.md) — Placement for commands that manipulate and transform the styles applied to text selections.
- [undoRedo](undoredo.md) — Placement for commands that control the Undo Manager.
