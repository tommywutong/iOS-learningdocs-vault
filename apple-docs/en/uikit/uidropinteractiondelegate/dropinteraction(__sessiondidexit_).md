---
title: 'dropInteraction(_:sessionDidExit:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidexit:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidexit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Asessiondidexit%3A%29.json'
content_hash: 'sha256:2cbe0ca620e7c7f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:sessionDidExit:)

<sub>Instance Method</sub>

Tells the delegate the drop session has moved out of the drop interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidExit session: any UIDropSession)
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drop session that has moved out of the interaction’s view.

## See Also

### Tracking the drop movements

- [- dropInteraction:sessionDidEnter:](<dropinteraction(__sessiondidenter_).md>) — Tells the delegate the drop session has moved into the drop interaction’s view.
- [- dropInteraction:sessionDidUpdate:](<dropinteraction(__sessiondidupdate_).md>) — Tells the delegate the drop session has changed.
- [- dropInteraction:sessionDidEnd:](<dropinteraction(__sessiondidend_).md>) — Tells the delegate the drop session has ended.
