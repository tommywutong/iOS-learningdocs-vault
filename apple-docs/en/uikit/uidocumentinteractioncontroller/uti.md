---
title: uti
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/uti
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/uti'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/uti.json'
content_hash: 'sha256:563cb43c4f31654c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# uti

<sub>Instance Property</sub>

The type of the target file.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var uti: String? { get set }
```

## Discussion

The value of this property is used to determine which apps are capable of opening the document. The default value is determined automatically whenever possible. However, if the document is a custom type that cannot be determined readily, the value of this property may be `nil`. If you know the type of the document, you can set the value of this property explicitly.

## See Also

### Accessing the target document’s attributes

- [URL](url.md) — The URL identifying the target file on the local filesystem.
- [name](name.md) — The name of the target file.
- [icons](icons.md) — The images associated with the target file.
- [annotation](annotation.md) — Custom property list information for the target file.
