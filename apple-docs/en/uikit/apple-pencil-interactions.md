---
title: Apple Pencil interactions
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/apple-pencil-interactions
source_url: 'https://developer.apple.com/documentation/uikit/apple-pencil-interactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/apple-pencil-interactions.json'
content_hash: 'sha256:f4112b9c17b646e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Apple Pencil interactions

<sub>API Collection</sub>

Handle user interactions like double tap and squeeze on Apple Pencil.

## Overview

Apple Pencil interactions let a person perform certain actions in your app by double-tapping or squeezing an Apple Pencil. Support Apple Pencil interactions to give people a quick way to perform their preferred action, such as switching between drawing tools, or a custom action that you define in your app.

![](../../../attachments/8e17660a264e7968650999ab74dedbf6/media-4403818@2x.png)

<sub>Two illustrations showing a hand double-tapping Apple Pencil with the index finger and a hand squeezing Apple Pencil near the tip.</sub>

- To learn more about supporting double-tap and squeeze interactions, read [Handling double taps from Apple Pencil](../applepencil/handling-double-taps-from-apple-pencil.md) and [Handling squeezes from Apple Pencil](../applepencil/handling-squeezes-from-apple-pencil.md).
- To learn more about handling touches, read [Handling input from Apple Pencil](handling-input-from-apple-pencil.md).
- To learn more about incorporating hand-drawn content in your app, see [Drawing with PencilKit](../pencilkit/drawing-with-pencilkit.md).

> [!note] Note
> Only Apple Pencil Pro supports squeeze interactions. The first-generation Apple Pencil doesn’t support Apple Pencil interactions.

## Topics

### Essentials

- [Handling double taps from Apple Pencil](../applepencil/handling-double-taps-from-apple-pencil.md) — Detect and respond to double taps a person makes on Apple Pencil.
- [Handling squeezes from Apple Pencil](../applepencil/handling-squeezes-from-apple-pencil.md) — Detect and respond to squeezes a person makes on Apple Pencil Pro.
- [Handling input from Apple Pencil](handling-input-from-apple-pencil.md) — Learn how to detect and respond to touches from Apple Pencil.

### Apple Pencil interactions in SwiftUI

- [onPencilDoubleTap(perform:)](<../swiftui/view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [PencilDoubleTapGestureValue](../swiftui/pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [onPencilSqueeze(perform:)](<../swiftui/view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [PencilSqueezeGesturePhase](../swiftui/pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGestureValue](../swiftui/pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilPreferredAction](../swiftui/pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilHoverPose](../swiftui/pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteractionDelegate](uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Tap](uipencilinteraction/tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](uipencilinteraction/squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [Phase](uipencilinteraction/phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

## See Also

### User interactions

- [Touches, presses, and gestures](touches-presses-and-gestures.md) — Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Menus and shortcuts](menus-and-shortcuts.md) — Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Drag and drop](drag-and-drop.md) — Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](pointer-interactions.md) — Support pointer interactions in your custom controls and views.
- [Focus-based navigation](focus-based-navigation.md) — Navigate the interface of your UIKit app using a remote, game controller, or keyboard.
- [Accessibility for UIKit](accessibility-for-uikit.md) — Make your UIKit apps accessible to everyone who uses iOS and tvOS.
