---
title: 'dragInteraction(_:sessionAllowsMoveOperation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Asessionallowsmoveoperation%3A%29.json'
content_hash: 'sha256:7a54bc900e248b1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:sessionAllowsMoveOperation:)

<sub>Instance Method</sub>

Asks the delegate whether the session allows the move operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drag session that should, or should not, allow the move operation.

## Return Value

[true](../../swift/true.md) if the session allows moving drag items to the destination view; otherwise [false](../../swift/false.md). The default is [true](../../swift/true.md) if you don’t provide this method.

## Discussion

The [UIDropOperationMove](../uidropoperation/move.md) operation only applies to drop activities within the same app. Drag items dropped onto another app are always copied.

## See Also

### Restricting the drag behavior

- [- dragInteraction:sessionIsRestrictedToDraggingApplication:](<draginteraction(__sessionisrestrictedtodraggingapplication_).md>) — Asks the delegate whether the system should restrict the drag session to the app that started the session.
