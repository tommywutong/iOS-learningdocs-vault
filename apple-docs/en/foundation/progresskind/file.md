---
title: file
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progresskind/file
source_url: 'https://developer.apple.com/documentation/foundation/progresskind/file'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progresskind/file.json'
content_hash: 'sha256:72acf836187908ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressKind](../progresskind.md)

# file

<sub>Type Property</sub>

The value that indicates that the progress is tracking a file operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let file: ProgressKind
```

## Discussion

If you set this value for the progress [kind](../progress/kind.md), set a value in the user info dictionary for the [NSProgressFileOperationKindKey](../progressuserinfokey/fileoperationkindkey.md).

The system assumes [Progress](../progress.md) of this kind uses bytes as the unit of work. The default implementation of [localizedDescription](../progress/localizeddescription.md) takes advantage of that to return more specific text than it does otherwise. If present, [localizedDescription](../progress/localizeddescription.md) uses the [NSProgressFileTotalCountKey](../progressuserinfokey/filetotalcountkey.md) and [NSProgressFileCompletedCountKey](../progressuserinfokey/filecompletedcountkey.md) keys in the [userInfo](../progress/userinfo.md) dictionary for the overall count of files.
