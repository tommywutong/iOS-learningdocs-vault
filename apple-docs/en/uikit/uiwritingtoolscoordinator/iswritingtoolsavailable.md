---
title: isWritingToolsAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/iswritingtoolsavailable
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/iswritingtoolsavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/iswritingtoolsavailable.json'
content_hash: 'sha256:8ecd8d1cc95648f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# isWritingToolsAvailable

<sub>Type Property</sub>

A Boolean value that indicates whether Writing Tools features are available to enable.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var isWritingToolsAvailable: Bool { get }
```

## Discussion

The value of this property is `true` when Writing Tools features are supported, even when the user has not enabled the feature. Writing Tools support might be unavailable because of device constraints.
