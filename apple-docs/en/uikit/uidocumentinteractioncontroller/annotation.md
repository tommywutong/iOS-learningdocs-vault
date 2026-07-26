---
title: annotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/annotation
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/annotation.json'
content_hash: 'sha256:2e8c37b101e52b9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# annotation

<sub>Instance Property</sub>

Custom property list information for the target file.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var annotation: Any? { get set }
```

## Discussion

Use this property to pass information about the document type to the app responsible for opening it. Although the type of this object should be one used to contain property list information—namely, [NSDictionary](../../foundation/nsdictionary.md), [NSArray](../../foundation/nsarray.md), [NSData](../../foundation/nsdata.md), [NSString](../../foundation/nsstring.md), [NSNumber](../../foundation/nsnumber.md), or [NSDate](../../foundation/nsdate.md)—the root object must be an [NSDictionary](../../foundation/nsdictionary.md).

## See Also

### Accessing the target document’s attributes

- [URL](url.md) — The URL identifying the target file on the local filesystem.
- [UTI](uti.md) — The type of the target file.
- [name](name.md) — The name of the target file.
- [icons](icons.md) — The images associated with the target file.
