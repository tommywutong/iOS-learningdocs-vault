---
title: UIIndirectScribbleInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk.json'
content_hash: 'sha256:9756a00f9a2b084a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIIndirectScribbleInteractionDelegate

<sub>Protocol</sub>

Methods that customize behavior on views that aren’t formally text input views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UIIndirectScribbleInteractionDelegate <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing focus

- [indirectScribbleInteraction:isElementFocused:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_iselementfocused_.md) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md) — Asks the delegate to focus an element to handle text edits.
- [indirectScribbleInteraction:shouldDelayFocusForElement:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_shoulddelayfocusforelement_.md) — Allows the delegate to delay focusing an element.

### Tracking Scribble input

- [indirectScribbleInteraction:willBeginWritingInElement:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_willbeginwritinginelement_.md) — Informs the delegate when the user begins writing.
- [indirectScribbleInteraction:didFinishWritingInElement:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_didfinishwritinginelement_.md) — Informs the delegate when the user finishes writing.

### Finding elements and frames

- [indirectScribbleInteraction:frameForElement:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_frameforelement_.md) — Asks the delegate to provide the frame of an element.
- [indirectScribbleInteraction:requestElementsInRect:completion:](uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_requestelementsinrect_completion_.md) — Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

## See Also

### Custom views

- [UIIndirectScribbleInteraction](uiindirectscribbleinteraction-2dap8.md) — An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [UIScribbleElementIdentifier](uiscribbleelementidentifier.md) — The element’s unique identifier.
