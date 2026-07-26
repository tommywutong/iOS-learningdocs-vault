---
title: 'autosave(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/autosave(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/autosave(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/autosave%28completionhandler%3A%29.json'
content_hash: 'sha256:ac30006c2765e457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# autosave(completionHandler:)

<sub>Instance Method</sub>

Initiates automatic saving of documents with unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func autosave(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func autosave() async -> Bool
```

## Parameters

- `completionHandler` — A block with code to execute after automatic saving concludes. The block returns no value and has one parameter: - **`success`** — [true](../../swift/true.md) if the autosaving operation succeeds, otherwise [false](../../swift/false.md). The block is invoked on the calling queue.

## Discussion

[UIDocument](../uidocument.md) periodically invokes this method to initiate a save operation if there are unsaved changes. You shouldn’t call this method directly. Subclasses can override it if they want to do special things with autosaving. The default implementation of this method invokes the [hasUnsavedChanges](hasunsavedchanges.md) method and, if that returns [true](../../swift/true.md), it invokes the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method.

This method should only be invoked for period-based saves. You may invoke it with the `success` parameter of the completion-handler parameter set to [false](../../swift/false.md) and return; this makes it safe to not actually save when [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) is invoked. However, if you call [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), saving of document data must occur.

## See Also

### Tracking changes and autosaving

- [hasUnsavedChanges](hasunsavedchanges.md) — A Boolean value that indicates whether the document has any unsaved changes.
- [- updateChangeCount:](<updatechangecount(__).md>) — Updates the change counter by indicating the kind of change.
- [undoManager](undomanager.md) — The undo manager for the document.
- [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>) — Updates the change count with reference to a change-count token passed in by UIKit.
