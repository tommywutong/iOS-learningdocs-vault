---
title: fileIconKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressuserinfokey/fileiconkey
source_url: 'https://developer.apple.com/documentation/foundation/progressuserinfokey/fileiconkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressuserinfokey/fileiconkey.json'
content_hash: 'sha256:854a48ace5d2a23f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressUserInfoKey](../progressuserinfokey.md)

# fileIconKey

<sub>Type Property</sub>

A key with a corresponding value that must be an image, typically an icon to represent the file.

<sub>macOS</sub>

```swift
static let fileIconKey: ProgressUserInfoKey
```

## Discussion

If present, the Finder uses this corresponding value to show the icon of a file that a progress object is tracking.

## See Also

### Using File Operation Keys

- [NSProgressFileAnimationImageKey](fileanimationimagekey.md) — A key with a corresponding value that is an image, typically an icon to represent the file.
- [NSProgressFileAnimationImageOriginalRectKey](fileanimationimageoriginalrectkey.md) — A key with a corresponding value that indicates the starting location of the image onscreen.
- [NSProgressFileCompletedCountKey](filecompletedcountkey.md) — A key with a corresponding value that represents the number of completed files.
- [NSProgressFileOperationKindKey](fileoperationkindkey.md) — A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [NSProgressFileTotalCountKey](filetotalcountkey.md) — A key with a corresponding value that represents the total number of files within a file operation.
- [NSProgressFileURLKey](fileurlkey.md) — A key with a corresponding value that represents the file URL of a file operation for the progress object.
