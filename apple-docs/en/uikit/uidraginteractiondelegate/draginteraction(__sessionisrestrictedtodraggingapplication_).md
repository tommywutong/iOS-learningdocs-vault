---
title: 'dragInteraction(_:sessionIsRestrictedToDraggingApplication:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteractiondelegate/draginteraction%28_%3Asessionisrestrictedtodraggingapplication%3A%29.json'
content_hash: 'sha256:787ad71777170622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteractionDelegate](../uidraginteractiondelegate.md)

# dragInteraction(_:sessionIsRestrictedToDraggingApplication:)

<sub>Instance Method</sub>

Asks the delegate whether the system should restrict the drag session to the app that started the session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drag session to restrict or not restrict.

## Return Value

[true](../../swift/true.md) if you want to restrict the drag session to the app that started it; otherwise [false](../../swift/false.md), which is the default if you don’t provide this method.

## Discussion

If you return [true](../../swift/true.md) and the user attempts to drop the drag items onto another app, the system cancels the session.

> [!note] Note
> The system calls this method only on devices that support dragging across apps.

## See Also

### Restricting the drag behavior

- [- dragInteraction:sessionAllowsMoveOperation:](<draginteraction(__sessionallowsmoveoperation_).md>) — Asks the delegate whether the session allows the move operation.
