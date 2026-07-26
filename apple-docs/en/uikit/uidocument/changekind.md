---
title: UIDocument.ChangeKind
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/changekind
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/changekind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/changekind.json'
content_hash: 'sha256:df335250a658be9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# UIDocument.ChangeKind

<sub>Enumeration</sub>

Constants that specify the kind of change to a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ChangeKind
```

## Overview

You specify one of these constants as a parameter of the [- updateChangeCount:](<updatechangecount(__).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDocumentChangeDone](changekind/done.md) — A change has been made to the document.
- [UIDocumentChangeUndone](changekind/undone.md) — A change to the document has been undone.
- [UIDocumentChangeRedone](changekind/redone.md) — An undone change to the document has been redone.
- [UIDocumentChangeCleared](changekind/cleared.md) — The document is cleared of outstanding changes.

### Initializers

- [init(rawValue:)](<changekind/init(rawvalue_).md>)

## See Also

### Constants

- [SaveOperation](saveoperation.md) — Constants that specify the type of save operation.
- [State](state.md) — Constants that specify the document state.
- [NSUserActivityDocumentURLKey](useractivityurlkey.md) — The key that identifies the document associated with a user activity.
