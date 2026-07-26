---
title: closed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state/closed
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state/closed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state/closed.json'
content_hash: 'sha256:02d5a364bc218ce3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocument](../../uidocument.md) · [State](../state.md)

# closed

<sub>Type Property</sub>

There was an error in reading the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var closed: UIDocument.State { get }
```

## Discussion

The document has either not been successfully opened, or has been since closed. The document properties might not be valid.

## See Also

### Constants

- [UIDocumentStateNormal](normal.md) — The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [UIDocumentStateInConflict](inconflict.md) — Conflicts exist for the document file located at the file URL.
- [UIDocumentStateSavingError](savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateEditingDisabled](editingdisabled.md) — The document is busy and it isn’t currently safe for user edits.
- [UIDocumentStateProgressAvailable](progressavailable.md) — The document is being downloaded or uploaded and progress information is available.
