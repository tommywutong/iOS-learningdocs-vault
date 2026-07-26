---
title: UIDropOperation.move
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropoperation/move
source_url: 'https://developer.apple.com/documentation/uikit/uidropoperation/move'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropoperation/move.json'
content_hash: 'sha256:ab5855e3f02e2eeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropOperation](../uidropoperation.md)

# UIDropOperation.move

<sub>Case</sub>

A drop operation type specifying that the data represented by the drag items should be moved, not copied.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case move
```

## Discussion

You may use this operation only if the drop session’s [allowsMoveOperation](../uidragdropsession/allowsmoveoperation.md) property is [true](../../swift/true.md); otherwise, it’s treated as a [UIDropOperationCancel](cancel.md) operation. A move operation is allowed only within same app. Data shared with another app must be copied.

The system gives no special meaning to this operation. The [UIDragInteractionDelegate](../uidraginteractiondelegate.md) object and the [UIDropInteractionDelegate](../uidropinteractiondelegate.md) object must cooperate to produce the correct move results. For instance, the drop interaction delegate might insert the data in a new location while the drag interaction delegate removes the data from the old location.

## See Also

### Drop operation types

- [UIDropOperationCancel](cancel.md) — A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperationForbidden](forbidden.md) — A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperationCopy](copy.md) — A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
