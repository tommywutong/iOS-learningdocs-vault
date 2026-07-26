---
title: persistentStoreName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimanageddocument/persistentstorename
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/persistentstorename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/persistentstorename.json'
content_hash: 'sha256:52adaca7f7a2cbc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# persistentStoreName

<sub>Type Property</sub>

Returns the name for the persistent store file inside the document’s file package.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var persistentStoreName: String { get }
```

## Return Value

The name for the persistent store file inside the document’s file package.

## Discussion

This path component is appended to the document URL provided by [UIDocument](../uidocument.md). The default name is `persistentStore`.
