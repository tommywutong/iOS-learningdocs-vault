---
title: fileAnimationImageOriginalRectKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressuserinfokey/fileanimationimageoriginalrectkey
source_url: 'https://developer.apple.com/documentation/foundation/progressuserinfokey/fileanimationimageoriginalrectkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressuserinfokey/fileanimationimageoriginalrectkey.json'
content_hash: 'sha256:e2c01225f2c1fc99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressUserInfoKey](../progressuserinfokey.md)

# fileAnimationImageOriginalRectKey

<sub>Type Property</sub>

A key with a corresponding value that indicates the starting location of the image onscreen.

<sub>macOS</sub>

```swift
static let fileAnimationImageOriginalRectKey: ProgressUserInfoKey
```

## Discussion

The associated value is an [NSValue](../nsvalue.md) that contains an [NSRect](../nsrect.md), in screen coordinates. This entry is optional, but if present, along with a value for [NSProgressFileAnimationImageKey](fileanimationimagekey.md), the Dock may show an animation. When the Dock has an item for the folder that contains the relevant file (such as the Downloads folder), the Dock uses this key to show an animation of the file flying into the Dock.

## See Also

### Using File Operation Keys

- [NSProgressFileAnimationImageKey](fileanimationimagekey.md) — A key with a corresponding value that is an image, typically an icon to represent the file.
- [NSProgressFileCompletedCountKey](filecompletedcountkey.md) — A key with a corresponding value that represents the number of completed files.
- [NSProgressFileIconKey](fileiconkey.md) — A key with a corresponding value that must be an image, typically an icon to represent the file.
- [NSProgressFileOperationKindKey](fileoperationkindkey.md) — A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [NSProgressFileTotalCountKey](filetotalcountkey.md) — A key with a corresponding value that represents the total number of files within a file operation.
- [NSProgressFileURLKey](fileurlkey.md) — A key with a corresponding value that represents the file URL of a file operation for the progress object.
