---
title: shouldShowFileExtensions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentpickerviewcontroller/shouldshowfileextensions
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/shouldshowfileextensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/shouldshowfileextensions.json'
content_hash: 'sha256:b21fe59acda93de9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# shouldShowFileExtensions

<sub>Instance Property</sub>

A Boolean value that determines whether the browser always shows file extensions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var shouldShowFileExtensions: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

> [!note] Note
> This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Configuring a document picker

- [documentPickerMode](documentpickermode.md) — The type of file transfer operation that the document picker uses. _(deprecated)_
- [UIDocumentPickerMode](../uidocumentpickermode.md) — Modes that define the type of file transfer operation that the document picker uses. _(deprecated)_
