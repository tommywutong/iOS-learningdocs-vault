---
title: UIPencilInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.1+, iPadOS 12.1+, Mac Catalyst 13.1+, visionOS 26.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteractiondelegate.json'
content_hash: 'sha256:43266d667bcbefa1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPencilInteractionDelegate

<sub>Protocol</sub>

The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPencilInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling double-tap interactions

- [- pencilInteraction:didReceiveTap:](<uipencilinteractiondelegate/pencilinteraction(__didreceivetap_).md>) — Tells the delegate when a person double-taps Apple Pencil.

### Handling squeeze interactions

- [- pencilInteraction:didReceiveSqueeze:](<uipencilinteractiondelegate/pencilinteraction(__didreceivesqueeze_).md>) — Tells the delegate when a person squeezes Apple Pencil.

### Deprecated

- [- pencilInteractionDidTap:](<uipencilinteractiondelegate/pencilinteractiondidtap(__).md>) — Tells the delegate that the user double-tapped Apple Pencil. _(deprecated)_

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [Tap](uipencilinteraction/tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](uipencilinteraction/squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [Phase](uipencilinteraction/phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.
