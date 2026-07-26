---
title: 'updateChangeCount(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/updatechangecount(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/updatechangecount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/updatechangecount%28_%3A%29.json'
content_hash: 'sha256:ae109fe8741be7d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# updateChangeCount(_:)

<sub>Instance Method</sub>

Updates the change counter by indicating the kind of change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func updateChangeCount(_ change: UIDocument.ChangeKind)
```

## Parameters

- `change` — A constant that indicates whether a change has been made, cleared, undone, or redone. See [ChangeKind](changekind.md) for more information.

## Discussion

Calling this method can affect the value returned by [hasUnsavedChanges](hasunsavedchanges.md). You shouldn’t need to call method this if you access an [UndoManager](../../foundation/undomanager.md) object from the [undoManager](undomanager.md) property (or assign a custom one to it) and register changes with the undo manager.

## See Also

### Tracking changes and autosaving

- [hasUnsavedChanges](hasunsavedchanges.md) — A Boolean value that indicates whether the document has any unsaved changes.
- [undoManager](undomanager.md) — The undo manager for the document.
- [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>) — Updates the change count with reference to a change-count token passed in by UIKit.
- [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) — Initiates automatic saving of documents with unsaved changes.
