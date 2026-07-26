---
title: normal
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state/normal
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state/normal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state/normal.json'
content_hash: 'sha256:74d107d6296280c9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocument](../../uidocument.md) · [State](../state.md)

# normal

<sub>Type Property</sub>

The document is open, editing is enabled, and there are no conflicts or errors associated with it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var normal: UIDocument.State { get }
```

## See Also

### Constants

- [UIDocumentStateClosed](closed.md) — There was an error in reading the document.
- [UIDocumentStateInConflict](inconflict.md) — Conflicts exist for the document file located at the file URL.
- [UIDocumentStateSavingError](savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateEditingDisabled](editingdisabled.md) — The document is busy and it isn’t currently safe for user edits.
- [UIDocumentStateProgressAvailable](progressavailable.md) — The document is being downloaded or uploaded and progress information is available.
