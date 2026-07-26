---
title: UIDropOperation.copy
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropoperation/copy
source_url: 'https://developer.apple.com/documentation/uikit/uidropoperation/copy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropoperation/copy.json'
content_hash: 'sha256:8329887f9d2fa784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropOperation](../uidropoperation.md)

# UIDropOperation.copy

<sub>Case</sub>

A drop operation type specifying that the data represented by the drag items should be copied to the destination view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case copy
```

## Discussion

This operation is used most often. When the user performs a drop activity, the [- dropInteraction:performDrop:](<../uidropinteractiondelegate/dropinteraction(__performdrop_).md>) delegate method is called. Your implementation of this delegate method should copy the data from the drag items to the destination view.

## See Also

### Drop operation types

- [UIDropOperationCancel](cancel.md) — A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperationForbidden](forbidden.md) — A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperationMove](move.md) — A drop operation type specifying that the data represented by the drag items should be moved, not copied.
