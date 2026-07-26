---
title: progress
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/progress
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/progress.json'
content_hash: 'sha256:f8f0ffec3c315b2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# progress

<sub>Instance Property</sub>

The upload or download progress of a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var progress: Progress? { get }
```

## Discussion

The value of this property is valid while [UIDocumentStateProgressAvailable](state/progressavailable.md) is set.

## See Also

### Accessing document attributes

- [fileURL](fileurl.md) — The file URL you use to initialize the document.
- [localizedName](localizedname.md) — The localized name of the document.
- [fileType](filetype.md) — The file type of the document.
- [fileModificationDate](filemodificationdate.md) — The date and time your app last modified the document file.
- [documentState](documentstate.md) — The current state of the document.
