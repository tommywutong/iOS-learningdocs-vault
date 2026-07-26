---
title: UIDocument.State
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/state
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/state.json'
content_hash: 'sha256:0f1222856aa61b08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# UIDocument.State

<sub>Structure</sub>

Constants that specify the document state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct State
```

## Overview

A [UIDocument](../uidocument.md) object stores the current state of the document in the [documentState](documentstate.md) property. To receive notifications about changes in document state, observe the [UIDocumentStateChangedNotification](statechangednotification.md) notification.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIDocumentStateNormal](state/normal.md) — The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [UIDocumentStateClosed](state/closed.md) — There was an error in reading the document.
- [UIDocumentStateInConflict](state/inconflict.md) — Conflicts exist for the document file located at the file URL.
- [UIDocumentStateSavingError](state/savingerror.md) — There was an error in saving or reverting the document.
- [UIDocumentStateEditingDisabled](state/editingdisabled.md) — The document is busy and it isn’t currently safe for user edits.
- [UIDocumentStateProgressAvailable](state/progressavailable.md) — The document is being downloaded or uploaded and progress information is available.

### Initializers

- [init(rawValue:)](<state/init(rawvalue_).md>) — Creates a document state structure with the specified raw value.

## See Also

### Constants

- [ChangeKind](changekind.md) — Constants that specify the kind of change to a document.
- [SaveOperation](saveoperation.md) — Constants that specify the type of save operation.
- [NSUserActivityDocumentURLKey](useractivityurlkey.md) — The key that identifies the document associated with a user activity.
