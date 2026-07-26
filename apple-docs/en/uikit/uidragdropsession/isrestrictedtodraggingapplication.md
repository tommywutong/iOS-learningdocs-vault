---
title: isRestrictedToDraggingApplication
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragdropsession/isrestrictedtodraggingapplication
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/isrestrictedtodraggingapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/isrestrictedtodraggingapplication.json'
content_hash: 'sha256:71907a57efd8b63d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# isRestrictedToDraggingApplication

<sub>Instance Property</sub>

A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isRestrictedToDraggingApplication: Bool { get }
```

## Discussion

The value for this property is set by the source app’s drag interaction delegate method [- dragInteraction:sessionIsRestrictedToDraggingApplication:](<../uidraginteractiondelegate/draginteraction(__sessionisrestrictedtodraggingapplication_).md>).  If the value is [true](../../swift/true.md), the drag session is restricted to the app that started the drag operation.

## See Also

### Checking for drag and drop session restrictions

- [allowsMoveOperation](allowsmoveoperation.md) — A Boolean value that indicates whether the drag session permits moving drag items within the same app.
