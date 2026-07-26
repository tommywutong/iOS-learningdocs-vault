---
title: 'undoMenuTitle(forUndoActionName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/undomenutitle(forundoactionname:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undomenutitle(forundoactionname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undomenutitle%28forundoactionname%3A%29.json'
content_hash: 'sha256:dbdc04734f6b39a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoMenuTitle(forUndoActionName:)

<sub>Instance Method</sub>

Returns the localized title of the Undo menu command for the identified action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func undoMenuTitle(forUndoActionName actionName: String) -> String
```

## Parameters

- `actionName` — The name of the undo action.

## Return Value

The localized title of the undo menu item.

## Discussion

Override this method if you want to customize the localization behavior. This method is invoked by [undoMenuItemTitle](undomenuitemtitle.md).

## See Also

### Getting and localizing the menu item title

- [undoMenuItemTitle](undomenuitemtitle.md) — The title of the Undo menu command, such as Undo Paste.
- [redoMenuItemTitle](redomenuitemtitle.md) — The title of the Redo menu command, such as Redo Paste.
- [- redoMenuTitleForUndoActionName:](<redomenutitle(forundoactionname_).md>) — Returns the localized title of the Redo menu command for the identified action.
