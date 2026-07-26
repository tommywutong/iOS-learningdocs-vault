---
title: UIPencilInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.1+, iPadOS 12.1+, Mac Catalyst 13.1+, visionOS 26.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction.json'
content_hash: 'sha256:b9b624a0c4782a6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPencilInteraction

<sub>Class</sub>

An interaction that tells your app when a person double-taps or squeezes Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPencilInteraction
```

## Overview

People can interact with certain models of Apple Pencil with a double tap or squeeze. To detect the double tap or squeeze in your app, create a [UIPencilInteraction](uipencilinteraction.md) object with a corresponding [delegate](uipencilinteraction/delegate.md) object. Then, add the interaction to your app’s view. When a person double-taps or squeezes Apple Pencil, the interaction calls the delegate’s corresponding [- pencilInteraction:didReceiveTap:](<uipencilinteractiondelegate/pencilinteraction(__didreceivetap_).md>) or [- pencilInteraction:didReceiveSqueeze:](<uipencilinteractiondelegate/pencilinteraction(__didreceivesqueeze_).md>) method.

For more information, read [Handling double taps from Apple Pencil](../applepencil/handling-double-taps-from-apple-pencil.md) and [Handling squeezes from Apple Pencil](../applepencil/handling-squeezes-from-apple-pencil.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating interactions

- [- initWithDelegate:](<uipencilinteraction/init(delegate_).md>) — Creates an interaction with the specified delegate.

### Handling interactions

- [delegate](uipencilinteraction/delegate.md) — The object that handles the double-tap or squeeze interactions a person makes on Apple Pencil.
- [UIPencilInteractionDelegate](uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.

### Enabling interactions

- [enabled](uipencilinteraction/isenabled.md) — A Boolean value that specifies whether the system reports double taps or squeezes on Apple Pencil to your app.

### Determining preferences for actions

- [preferredTapAction](uipencilinteraction/preferredtapaction.md) — A person’s preferred double-tap action for Apple Pencil, as specified in the Settings app.
- [preferredSqueezeAction](uipencilinteraction/preferredsqueezeaction.md) — A person’s preferred squeeze action for Apple Pencil, as specified in the Settings app.
- [UIPencilPreferredAction](uipencilpreferredaction.md) — The actions Apple Pencil can perform after a person performs a double tap or squeeze.

### Determining input type

- [prefersPencilOnlyDrawing](uipencilinteraction/preferspencilonlydrawing.md) — A person’s preference for drawing with Apple Pencil only, as specified in the Settings app or the system tool picker.

### Determining hover preview preferences

- [prefersHoverToolPreview](uipencilinteraction/prefershovertoolpreview.md) — A person’s preference for whether holding a supported model of Apple Pencil close to the screen shows a preview of the current drawing tool, as specified in the Settings app.

### Supporting types

- [Tap](uipencilinteraction/tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](uipencilinteraction/squeeze.md) — An interaction that represents a squeeze on Apple Pencil.

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteractionDelegate](uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Tap](uipencilinteraction/tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](uipencilinteraction/squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [Phase](uipencilinteraction/phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.
