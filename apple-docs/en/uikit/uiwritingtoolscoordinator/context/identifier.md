---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/context/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/context/identifier.json'
content_hash: 'sha256:1bac422daefc17d0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Context](../context.md)

# identifier

<sub>Instance Property</sub>

The unique identifier of the context object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var identifier: UUID { get }
```

## Discussion

The [Context](../context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.
