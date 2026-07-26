---
title: undoManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/undomanager
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/undomanager.json'
content_hash: 'sha256:69523f4c3e0aa3f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# undoManager

<sub>Instance Property</sub>

The undo manager for the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var undoManager: UndoManager! { get set }
```

## Discussion

This property holds the document’s undo manager (an [UndoManager](../../foundation/undomanager.md) object). Accessing this property lazily creates a default undo manager if a custom undo manager hasn’t been set.

The undo manager for the document is registered as an observer of various [UndoManager](../../foundation/undomanager.md) notifications so that it can call [- updateChangeCount:](<updatechangecount(__).md>) as the user makes undoable changes to the document. When a subclass sets this property and implements registers changes with it, it doesn’t need to call [- updateChangeCount:](<updatechangecount(__).md>) directly or (more rarely) override [hasUnsavedChanges](hasunsavedchanges.md).

## See Also

### Tracking changes and autosaving

- [hasUnsavedChanges](hasunsavedchanges.md) — A Boolean value that indicates whether the document has any unsaved changes.
- [- updateChangeCount:](<updatechangecount(__).md>) — Updates the change counter by indicating the kind of change.
- [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>) — Updates the change count with reference to a change-count token passed in by UIKit.
- [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) — Initiates automatic saving of documents with unsaved changes.
