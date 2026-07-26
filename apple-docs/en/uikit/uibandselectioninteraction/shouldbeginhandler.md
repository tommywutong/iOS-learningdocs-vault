---
title: shouldBeginHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/shouldbeginhandler
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/shouldbeginhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/shouldbeginhandler.json'
content_hash: 'sha256:d77f4b1404f32d69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# shouldBeginHandler

<sub>Instance Property</sub>

The handler that determines whether to start a band selection interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var shouldBeginHandler: ((UIBandSelectionInteraction, CGPoint) -> Bool)? { get set }
```

## Discussion

This property stores an optional handler block you use to selectively start the interaction. If you provide a handler, the [UIBandSelectionInteraction](../uibandselectioninteraction.md) object calls your handler upon successful recognition of the appropriate event sequence, but before it starts the interaction. Use your handler to specify whether you want the interaction to proceed.

Your handler block returns a Boolean that indicates whether to start the interaction. Return [true](../../swift/true.md) to start the interaction or [false](../../swift/false.md) to ignore the interaction and return the [UIBandSelectionInteraction](../uibandselectioninteraction.md) object to the [UIBandSelectionInteractionStatePossible](state-swift.enum/possible.md) state. The interaction object passes the following points to your handler:

- **interaction** — The [UIBandSelectionInteraction](../uibandselectioninteraction.md) object that’s ready to start the interaction.
- **point** — The starting point of the interaction, in your view’s coordinate space. You might use this value to prevent someone from starting interactions in disabled items or from specific regions of your view.
