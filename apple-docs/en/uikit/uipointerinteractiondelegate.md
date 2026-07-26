---
title: UIPointerInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteractiondelegate.json'
content_hash: 'sha256:e2df6685362c99eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerInteractionDelegate

<sub>Protocol</sub>

An interface for handling pointer movements within the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPointerInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Defining pointer styles for regions

- [- pointerInteraction:regionForRequest:defaultRegion:](<uipointerinteractiondelegate/pointerinteraction(__regionfor_defaultregion_).md>) — Asks the delegate for a region as the pointer moves within the interaction’s view.
- [- pointerInteraction:styleForRegion:](<uipointerinteractiondelegate/pointerinteraction(__stylefor_).md>) — Asks the delegate for a pointer style after an interaction receives a new region.

### Handling animations for pointer regions

- [- pointerInteraction:willEnterRegion:animator:](<uipointerinteractiondelegate/pointerinteraction(__willenter_animator_).md>) — Informs the delegate when the pointer enters a given region.
- [- pointerInteraction:willExitRegion:animator:](<uipointerinteractiondelegate/pointerinteraction(__willexit_animator_).md>) — Informs the delegate when the pointer exits a given region.

## See Also

### Essentials

- [UIPointerInteraction](uipointerinteraction.md) — An interaction that enables support for effects on a view or customizes the pointer’s appearance within a region of an app.
- [Integrating pointer interactions into your iPad app](integrating-pointer-interactions-into-your-ipad-app.md) — Support touch interactions in your iPad app by adding pointer interactions to your views.
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md) — Provide a great user experience with pointing devices, by incorporating pointer content effects and shape customizations.
