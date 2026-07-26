---
title: fileURLKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressuserinfokey/fileurlkey
source_url: 'https://developer.apple.com/documentation/foundation/progressuserinfokey/fileurlkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressuserinfokey/fileurlkey.json'
content_hash: 'sha256:cec1bc6e4343ba37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressUserInfoKey](../progressuserinfokey.md)

# fileURLKey

<sub>Type Property</sub>

A key with a corresponding value that represents the file URL of a file operation for the progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fileURLKey: ProgressUserInfoKey
```

## Discussion

If present, [Progress](../progress.md) presents additional information in its localized description.

## See Also

### Using File Operation Keys

- [NSProgressFileAnimationImageKey](fileanimationimagekey.md) — A key with a corresponding value that is an image, typically an icon to represent the file.
- [NSProgressFileAnimationImageOriginalRectKey](fileanimationimageoriginalrectkey.md) — A key with a corresponding value that indicates the starting location of the image onscreen.
- [NSProgressFileCompletedCountKey](filecompletedcountkey.md) — A key with a corresponding value that represents the number of completed files.
- [NSProgressFileIconKey](fileiconkey.md) — A key with a corresponding value that must be an image, typically an icon to represent the file.
- [NSProgressFileOperationKindKey](fileoperationkindkey.md) — A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [NSProgressFileTotalCountKey](filetotalcountkey.md) — A key with a corresponding value that represents the total number of files within a file operation.
