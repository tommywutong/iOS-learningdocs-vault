---
title: inConflict
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state/inconflict
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state/inconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state/inconflict.json'
content_hash: 'sha256:bc9c2d7f111e512f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocument](../../uidocument.md) · [State](../state.md)

# inConflict

<sub>Type Property</sub>

Conflicts exist for the document file located at the file URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var inConflict: UIDocument.State { get }
```

## Discussion

You can access these conflicting document versions by calling the [otherVersionsOfItem(at:)](<../../../foundation/nsfileversion/otherversionsofitem(at_).md>) class method of the [NSFileVersion](../../../foundation/nsfileversion.md) class. This method returns an array of [NSFileVersion](../../../foundation/nsfileversion.md) objects. You can then resolve the conflicting versions — for example, programmatically attempt to merge the versions or present the document versions to a person and request them to pick one.

## See Also

### Constants

- [UIDocumentStateNormal](normal.md) — The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [UIDocumentStateClosed](closed.md) — There was an error in reading the document.
- [UIDocumentStateSavingError](savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateEditingDisabled](editingdisabled.md) — The document is busy and it isn’t currently safe for user edits.
- [UIDocumentStateProgressAvailable](progressavailable.md) — The document is being downloaded or uploaded and progress information is available.
