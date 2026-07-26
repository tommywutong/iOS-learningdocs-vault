---
title: AVLegibleMediaOptionsMenuController.Delegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol.json'
content_hash: 'sha256:5bf907ce102a4f39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVLegibleMediaOptionsMenuController](../avlegiblemediaoptionsmenucontroller.md)

# AVLegibleMediaOptionsMenuController.Delegate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol Delegate : NSObjectProtocol
```

## Overview

Delegate protocol for AVLegibleMediaOptionsMenuController

Provides callbacks for caption preview display and enablement state changes.

## Relationships

- **Inherits From**: [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Responding to menu changes

- [- legibleMenuController:didChangeMenuState:](<delegate-swift.protocol/legiblemenucontroller(__didchange_).md>)
- [- legibleMenuController:didRequestCaptionPreviewForProfileID:](<delegate-swift.protocol/legiblemenucontroller(__didrequestcaptionpreviewforprofileid_).md>)
- [- legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview:](<delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(__).md>)

## See Also

### Configuring a delegate

- [delegate](delegate-swift.property.md)
