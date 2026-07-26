---
title: UIDropOperation.forbidden
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropoperation/forbidden
source_url: 'https://developer.apple.com/documentation/uikit/uidropoperation/forbidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropoperation/forbidden.json'
content_hash: 'sha256:a2fa79523607a378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropOperation](../uidropoperation.md)

# UIDropOperation.forbidden

<sub>Case</sub>

A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case forbidden
```

## Discussion

You use this operation to signal that the drop activity isn’t allowed at this specific time and place. The drag operation is canceled.

## See Also

### Drop operation types

- [UIDropOperationCancel](cancel.md) — A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperationCopy](copy.md) — A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperationMove](move.md) — A drop operation type specifying that the data represented by the drag items should be moved, not copied.
