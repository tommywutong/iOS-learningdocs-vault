---
title: fileOperationKindKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressuserinfokey/fileoperationkindkey
source_url: 'https://developer.apple.com/documentation/foundation/progressuserinfokey/fileoperationkindkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressuserinfokey/fileoperationkindkey.json'
content_hash: 'sha256:1bde2f1d3ea9db19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressUserInfoKey](../progressuserinfokey.md)

# fileOperationKindKey

<sub>Type Property</sub>

A key with a corresponding value that indicates the kind of file operation a progress object represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fileOperationKindKey: ProgressUserInfoKey
```

## Discussion

When you set the property [kind](../progress/kind.md) on a progress to [NSProgressKindFile](../progresskind/file.md), set the corresponding value to one of the entries in Recognizing Kinds of File Operations.

## See Also

### Using File Operation Keys

- [NSProgressFileAnimationImageKey](fileanimationimagekey.md) — A key with a corresponding value that is an image, typically an icon to represent the file.
- [NSProgressFileAnimationImageOriginalRectKey](fileanimationimageoriginalrectkey.md) — A key with a corresponding value that indicates the starting location of the image onscreen.
- [NSProgressFileCompletedCountKey](filecompletedcountkey.md) — A key with a corresponding value that represents the number of completed files.
- [NSProgressFileIconKey](fileiconkey.md) — A key with a corresponding value that must be an image, typically an icon to represent the file.
- [NSProgressFileTotalCountKey](filetotalcountkey.md) — A key with a corresponding value that represents the total number of files within a file operation.
- [NSProgressFileURLKey](fileurlkey.md) — A key with a corresponding value that represents the file URL of a file operation for the progress object.
