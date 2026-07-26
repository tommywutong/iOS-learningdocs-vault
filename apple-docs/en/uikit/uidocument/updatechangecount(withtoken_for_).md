---
title: 'updateChangeCount(withToken:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/updatechangecount(withtoken:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/updatechangecount(withtoken:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/updatechangecount%28withtoken%3Afor%3A%29.json'
content_hash: 'sha256:4e012d7ed7702f41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# updateChangeCount(withToken:for:)

<sub>Instance Method</sub>

Updates the change count with reference to a change-count token passed in by UIKit.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func updateChangeCount(withToken changeCountToken: Any, for saveOperation: UIDocument.SaveOperation)
```

## Parameters

- `changeCountToken` — An object to use as a change-count token. `UIDocument` obtained this token earlier by calling [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>).

- `saveOperation` — A constant that indicates whether the save operation is writing a new file or overwriting an existing one. See [SaveOperation](saveoperation.md) for descriptions of these constants.

## Discussion

To get autosaving capabilities for your documents, you must implement change tracking. Typically you do this by using an [UndoManager](../../foundation/undomanager.md) object (assigned to [undoManager](undomanager.md) property) to register changes or by calling the [- updateChangeCount:](<updatechangecount(__).md>) method every time the user makes a change; UIKit then automatically determines whether there are unsaved changes and returns the proper value from [hasUnsavedChanges](hasunsavedchanges.md). If you take neither of these approaches (and you want the autosaving feature), you must implement this method as well as [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) and [hasUnsavedChanges](hasunsavedchanges.md).

You implement the [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) method to return a change-count token that UIKit uses to encapsulate the history of document changes for a particular save operation. The token can be any object that represents the current change state of the document. This method is called at the start of the default implementation of the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method. At the end of this default implementation, [UIDocument](../uidocument.md) calls this method ([- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>)), passing in the change-count token. You implement this method to compare the token with the one returned earlier; by doing so, you can determine if the document has acquired new unsaved changes between the start and end of an asynchronous write operation. You can then return the proper value from your override of [hasUnsavedChanges](hasunsavedchanges.md).

## See Also

### Tracking changes and autosaving

- [hasUnsavedChanges](hasunsavedchanges.md) — A Boolean value that indicates whether the document has any unsaved changes.
- [- updateChangeCount:](<updatechangecount(__).md>) — Updates the change counter by indicating the kind of change.
- [undoManager](undomanager.md) — The undo manager for the document.
- [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) — Initiates automatic saving of documents with unsaved changes.
