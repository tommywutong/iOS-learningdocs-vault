---
title: allowsMoveOperation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragdropsession/allowsmoveoperation
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/allowsmoveoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/allowsmoveoperation.json'
content_hash: 'sha256:dd342c951198d6cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# allowsMoveOperation

<sub>Instance Property</sub>

A Boolean value that indicates whether the drag session permits moving drag items within the same app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsMoveOperation: Bool { get }
```

## Discussion

A move operation can be applied only within the same app. Drag items shared with another app are always copied.

The `allowsMoveOperation` value is determined by the return value of the source app’s drag interaction delegate’s  [- dragInteraction:sessionAllowsMoveOperation:](<../uidraginteractiondelegate/draginteraction(__sessionallowsmoveoperation_).md>) method. If `allowsMoveOperation` is [true](../../swift/true.md), the source app’s drop interaction delegate’s [- dropInteraction:sessionDidUpdate:](<../uidropinteractiondelegate/dropinteraction(__sessiondidupdate_).md>) method can return a drop proposal for a [UIDropOperationMove](../uidropoperation/move.md) operation.

## See Also

### Checking for drag and drop session restrictions

- [restrictedToDraggingApplication](isrestrictedtodraggingapplication.md) — A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.
