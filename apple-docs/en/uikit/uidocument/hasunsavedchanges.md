---
title: hasUnsavedChanges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/hasunsavedchanges
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/hasunsavedchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/hasunsavedchanges.json'
content_hash: 'sha256:f196034f0935e187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# hasUnsavedChanges

<sub>Instance Property</sub>

A Boolean value that indicates whether the document has any unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasUnsavedChanges: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the document has unsaved changes, otherwise [false](../../swift/false.md).

## Discussion

The default implementation of [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) initiates a save if this property returns [true](../../swift/true.md). Typical subclasses don’t need to override [hasUnsavedChanges](hasunsavedchanges.md). To implement change tracking, they should instead use an [UndoManager](../../foundation/undomanager.md) object (assigned to [undoManager](undomanager.md)) to register changes or call [- updateChangeCount:](<updatechangecount(__).md>) every time the user makes a change; UIKit then automatically determines whether there are unsaved changes.

## See Also

### Tracking changes and autosaving

- [- updateChangeCount:](<updatechangecount(__).md>) — Updates the change counter by indicating the kind of change.
- [undoManager](undomanager.md) — The undo manager for the document.
- [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>) — Updates the change count with reference to a change-count token passed in by UIKit.
- [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) — Initiates automatic saving of documents with unsaved changes.
