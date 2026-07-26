---
title: localDragSession
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropsession/localdragsession
source_url: 'https://developer.apple.com/documentation/uikit/uidropsession/localdragsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsession/localdragsession.json'
content_hash: 'sha256:e87f67a015e1946e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropSession](../uidropsession.md)

# localDragSession

<sub>Instance Property</sub>

The drag session that corresponds to this drop session, for in-app drag activities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var localDragSession: (any UIDragSession)? { get }
```

## Discussion

The local drag session is `nil` if the drag activity started in a different app.
