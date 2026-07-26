---
title: undoMenuItemTitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/undomenuitemtitle
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undomenuitemtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undomenuitemtitle.json'
content_hash: 'sha256:5c6031cc08e3984a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoMenuItemTitle

<sub>Instance Property</sub>

The title of the Undo menu command, such as Undo Paste.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoMenuItemTitle: String { get }
```

## Discussion

Returns “Undo” if no action name has been assigned or `nil` if there is nothing to undo.

## See Also

### Getting and localizing the menu item title

- [redoMenuItemTitle](redomenuitemtitle.md) — The title of the Redo menu command, such as Redo Paste.
- [- undoMenuTitleForUndoActionName:](<undomenutitle(forundoactionname_).md>) — Returns the localized title of the Undo menu command for the identified action.
- [- redoMenuTitleForUndoActionName:](<redomenutitle(forundoactionname_).md>) — Returns the localized title of the Redo menu command for the identified action.
