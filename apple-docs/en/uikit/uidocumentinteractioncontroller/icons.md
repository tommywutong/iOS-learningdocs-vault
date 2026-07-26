---
title: icons
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/icons
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/icons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/icons.json'
content_hash: 'sha256:9f14c2738dc4cd93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# icons

<sub>Instance Property</sub>

The images associated with the target file.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var icons: [UIImage] { get }
```

## Discussion

This property contains an array of [UIImage](../uiimage.md) objects containing the available icons for the given file. The images in the array are sorted from smallest to largest, with the smallest image located at index 0. The returned array always contains at least one image.

The images themselves are provided by the system and determined by the UTI of the file. Apps can register custom icons for their associated files by including the appropriate meta information in their `Info.plist` file. If no custom icon exists, the images in this property represent the generic document icon.

## See Also

### Accessing the target document’s attributes

- [URL](url.md) — The URL identifying the target file on the local filesystem.
- [UTI](uti.md) — The type of the target file.
- [name](name.md) — The name of the target file.
- [annotation](annotation.md) — Custom property list information for the target file.
