---
title: 'dropInteraction(_:sessionDidUpdate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Asessiondidupdate%3A%29.json'
content_hash: 'sha256:7316e828cbbdd445'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:sessionDidUpdate:)

<sub>Instance Method</sub>

Tells the delegate the drop session has changed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: any UIDropSession) -> UIDropProposal
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drop session that has changed.

## Return Value

A drop proposal that contains the operation the delegate intends to perform. You may return a proposal containing the [UIDropOperationMove](../uidropoperation/move.md) operation only if the session’s [allowsMoveOperation](../uidragdropsession/allowsmoveoperation.md) is [true](../../swift/true.md).

## Discussion

You must implement this method if the drop interaction’s view can accept drop activities. If you don’t provide this method, the view cannot accept any drop activities.

The interaction calls this method when one of the following happens:

- The session enters the area of the drop interaction’s view.
- The session moves inside the area of the drop interaction’s view.
- The user adds a drag item to the session that within the area of the drop interaction’s view.

To get the location of the drop session after it has moved, call the session’s [- locationInView:](<../uidragdropsession/location(in_).md>) method.

## See Also

### Tracking the drop movements

- [- dropInteraction:sessionDidEnter:](<dropinteraction(__sessiondidenter_).md>) — Tells the delegate the drop session has moved into the drop interaction’s view.
- [- dropInteraction:sessionDidExit:](<dropinteraction(__sessiondidexit_).md>) — Tells the delegate the drop session has moved out of the drop interaction’s view.
- [- dropInteraction:sessionDidEnd:](<dropinteraction(__sessiondidend_).md>) — Tells the delegate the drop session has ended.
