---
title: editingDisabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state/editingdisabled
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state/editingdisabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state/editingdisabled.json'
content_hash: 'sha256:bbb07256637b2660'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocument](../../uidocument.md) · [State](../state.md)

# editingDisabled

<sub>Type Property</sub>

The document is busy and it isn’t currently safe for user edits.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var editingDisabled: UIDocument.State { get }
```

## Discussion

This state is set just before [UIDocument](../../uidocument.md) calls the [- disableEditing](<../disableediting().md>) method. It calls [- enableEditing](<../enableediting().md>) when it becomes safe to edit again. [UIDocument](../../uidocument.md) also sets this state when an error prevents the reverting of a document.

## See Also

### Constants

- [UIDocumentStateNormal](normal.md) — The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [UIDocumentStateClosed](closed.md) — There was an error in reading the document.
- [UIDocumentStateInConflict](inconflict.md) — Conflicts exist for the document file located at the file URL.
- [UIDocumentStateSavingError](savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateProgressAvailable](progressavailable.md) — The document is being downloaded or uploaded and progress information is available.
