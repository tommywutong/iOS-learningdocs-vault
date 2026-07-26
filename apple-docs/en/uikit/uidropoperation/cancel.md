---
title: UIDropOperation.cancel
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropoperation/cancel
source_url: 'https://developer.apple.com/documentation/uikit/uidropoperation/cancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropoperation/cancel.json'
content_hash: 'sha256:7f044265cf029f13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropOperation](../uidropoperation.md)

# UIDropOperation.cancel

<sub>Case</sub>

A drop operation type specifying that no data should be transferred, thereby canceling the drag.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case cancel
```

## Discussion

If the user attempts a drop activity, the drag operation is canceled and the [- dropInteraction:performDrop:](<../uidropinteractiondelegate/dropinteraction(__performdrop_).md>) delegate method isn’t called.

## See Also

### Drop operation types

- [UIDropOperationForbidden](forbidden.md) — A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperationCopy](copy.md) — A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperationMove](move.md) — A drop operation type specifying that the data represented by the drag items should be moved, not copied.
