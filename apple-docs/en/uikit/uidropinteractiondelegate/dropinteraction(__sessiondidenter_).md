---
title: 'dropInteraction(_:sessionDidEnter:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidenter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Asessiondidenter%3A%29.json'
content_hash: 'sha256:3bdff57140a29ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:sessionDidEnter:)

<sub>Instance Method</sub>

Tells the delegate the drop session has moved into the drop interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidEnter session: any UIDropSession)
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drop session that has moved into the interaction’s view.

## See Also

### Tracking the drop movements

- [- dropInteraction:sessionDidUpdate:](<dropinteraction(__sessiondidupdate_).md>) — Tells the delegate the drop session has changed.
- [- dropInteraction:sessionDidExit:](<dropinteraction(__sessiondidexit_).md>) — Tells the delegate the drop session has moved out of the drop interaction’s view.
- [- dropInteraction:sessionDidEnd:](<dropinteraction(__sessiondidend_).md>) — Tells the delegate the drop session has ended.
