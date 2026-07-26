---
title: UIIndirectScribbleInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiindirectscribbleinteractiondelegate-hdh
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh.json'
content_hash: 'sha256:e37e717a51d1d68e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIIndirectScribbleInteractionDelegate

<sub>Protocol</sub>

Methods that customize behavior on views that aren’t formally text input views.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIIndirectScribbleInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying Elements

- [ElementIdentifier](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md) — A unique identifier for a control that isn’t a text field in a Scribble interaction.

### Managing Focus

- [indirectScribbleInteraction(_:isElementFocused:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__iselementfocused_).md>) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__focuselementifneeded_referencepoint_completion_).md>) — Asks the delegate to focus an element to handle text edits.
- [indirectScribbleInteraction(_:shouldDelayFocusForElement:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__shoulddelayfocusforelement_).md>) — Allow the delegate to delay focusing an element.

### Tracking Scribble Input

- [indirectScribbleInteraction(_:willBeginWritingInElement:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__willbeginwritinginelement_).md>) — Informs the delegate when the user begins writing.
- [indirectScribbleInteraction(_:didFinishWritingInElement:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__didfinishwritinginelement_).md>) — Informs the delegate when the user finishes writing.

### Finding Elements and Frames

- [indirectScribbleInteraction(_:frameForElement:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__frameforelement_).md>) — Asks the delegate to provide the frame of an element.
- [indirectScribbleInteraction(_:requestElementsIn:completion:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__requestelementsin_completion_).md>) — Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

### Instance Methods

- [indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__focuselementifneeded_referencepoint_).md>)
- [indirectScribbleInteraction(_:requestElementsIn:)](<uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(__requestelementsin_).md>)

## See Also

### Custom views

- [UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md) — An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [ElementIdentifier](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md) — A unique identifier for a control that isn’t a text field in a Scribble interaction.
