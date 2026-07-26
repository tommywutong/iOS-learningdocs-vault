---
title: progressAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state/progressavailable
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state/progressavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state/progressavailable.json'
content_hash: 'sha256:5872790ee093f622'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocument](../../uidocument.md) · [State](../state.md)

# progressAvailable

<sub>Type Property</sub>

The document is being downloaded or uploaded and progress information is available.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var progressAvailable: UIDocument.State { get }
```

## Discussion

When this state is set, you can use the [progress](../../../foundation/progressreporting/progress.md) property of the document to monitor the current operation.

## See Also

### Constants

- [UIDocumentStateNormal](normal.md) — The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [UIDocumentStateClosed](closed.md) — There was an error in reading the document.
- [UIDocumentStateInConflict](inconflict.md) — Conflicts exist for the document file located at the file URL.
- [UIDocumentStateSavingError](savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateEditingDisabled](editingdisabled.md) — The document is busy and it isn’t currently safe for user edits.
