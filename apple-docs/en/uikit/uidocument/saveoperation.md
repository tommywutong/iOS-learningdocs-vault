---
title: UIDocument.SaveOperation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/saveoperation
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/saveoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/saveoperation.json'
content_hash: 'sha256:7e9e6407a1b1b8c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# UIDocument.SaveOperation

<sub>Enumeration</sub>

Constants that specify the type of save operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum SaveOperation
```

## Overview

You specify one of these constants as a parameter in the following methods: [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>), [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>), [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>), [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>), [- changeCountTokenForSaveOperation:](<changecounttoken(for_).md>), and [- updateChangeCountWithToken:forSaveOperation:](<updatechangecount(withtoken_for_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDocumentSaveForCreating](saveoperation/forcreating.md) — The document is being saved for the first time.
- [UIDocumentSaveForOverwriting](saveoperation/foroverwriting.md) — The document is being saved by overwriting the current version.

### Initializers

- [init(rawValue:)](<saveoperation/init(rawvalue_).md>)

## See Also

### Constants

- [ChangeKind](changekind.md) — Constants that specify the kind of change to a document.
- [State](state.md) — Constants that specify the document state.
- [NSUserActivityDocumentURLKey](useractivityurlkey.md) — The key that identifies the document associated with a user activity.
