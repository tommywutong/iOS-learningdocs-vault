---
title: redoMenuItemTitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/redomenuitemtitle
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redomenuitemtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redomenuitemtitle.json'
content_hash: 'sha256:84020ab03c990ecf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redoMenuItemTitle

<sub>Instance Property</sub>

The title of the Redo menu command, such as Redo Paste.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var redoMenuItemTitle: String { get }
```

## Discussion

Returns “Redo” if no action name has been assigned or `nil` if there is nothing to redo.

## See Also

### Getting and localizing the menu item title

- [undoMenuItemTitle](undomenuitemtitle.md) — The title of the Undo menu command, such as Undo Paste.
- [- undoMenuTitleForUndoActionName:](<undomenutitle(forundoactionname_).md>) — Returns the localized title of the Undo menu command for the identified action.
- [- redoMenuTitleForUndoActionName:](<redomenutitle(forundoactionname_).md>) — Returns the localized title of the Redo menu command for the identified action.
