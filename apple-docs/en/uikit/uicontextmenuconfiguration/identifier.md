---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/identifier.json'
content_hash: 'sha256:81cc70c0fc3e4f7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# identifier

<sub>Instance Property</sub>

The unique identifier for this configuration object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: any NSCopying { get }
```

## Discussion

If you did not provide an identifier when creating this object, UIKit assigns a new [UUID](../../foundation/uuid.md) object to this property.
