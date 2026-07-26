---
title: 'indirectScribbleInteraction(_:isElementFocused:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:iselementfocused:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Aiselementfocused%3A%29.json'
content_hash: 'sha256:a73f9de1098bceee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:isElementFocused:)

<sub>Instance Method</sub>

Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, isElementFocused elementIdentifier: Self.ElementIdentifier) -> Bool
```

## Parameters

- `interaction` — The interaction asking for the focused state.

- `elementIdentifier` — The identifier of the element the interaction is asking about.

## Return Value

Returns [true](../../swift/true.md) if the element is the one currently focused.

## See Also

### Managing Focus

- [indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)](<indirectscribbleinteraction(__focuselementifneeded_referencepoint_completion_).md>) — Asks the delegate to focus an element to handle text edits.
- [indirectScribbleInteraction(_:shouldDelayFocusForElement:)](<indirectscribbleinteraction(__shoulddelayfocusforelement_).md>) — Allow the delegate to delay focusing an element.
