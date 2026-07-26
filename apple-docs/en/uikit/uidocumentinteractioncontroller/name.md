---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/name
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/name.json'
content_hash: 'sha256:649685a71d93ef5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# name

<sub>Instance Property</sub>

The name of the target file.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var name: String? { get set }
```

## Discussion

This property contains the filename without any preceding path information. The default value of this property is derived from the path information in the [URL](url.md) property. You can change the value of this property as needed if you want to associate a different name with the file.

## See Also

### Accessing the target document’s attributes

- [URL](url.md) — The URL identifying the target file on the local filesystem.
- [UTI](uti.md) — The type of the target file.
- [icons](icons.md) — The images associated with the target file.
- [annotation](annotation.md) — Custom property list information for the target file.
