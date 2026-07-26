---
title: 'indirectScribbleInteraction:frameForElement:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:frameforelement:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:frameforelement:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Aframeforelement%3A.json'
content_hash: 'sha256:1186e1413b9c0d96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:frameForElement:

<sub>Instance Method</sub>

Asks the delegate to provide the frame of an element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGRect) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction frameForElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Parameters

- `interaction` — The interaction requesting to focus an element.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Return Value

Returns the frame for the element, in the view coordinate system of the interaction.

## See Also

### Finding elements and frames

- [indirectScribbleInteraction:requestElementsInRect:completion:](indirectscribbleinteraction_requestelementsinrect_completion_.md) — Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.
