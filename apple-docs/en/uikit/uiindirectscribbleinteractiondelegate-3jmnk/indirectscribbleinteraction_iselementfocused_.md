---
title: 'indirectScribbleInteraction:isElementFocused:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:iselementfocused:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:iselementfocused:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Aiselementfocused%3A.json'
content_hash: 'sha256:af191654a0b70a89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:isElementFocused:

<sub>Instance Method</sub>

Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction isElementFocused:(UIScribbleElementIdentifier) elementIdentifier;
```

## Parameters

- `interaction` — The interaction asking for the focused state.

- `elementIdentifier` — The identifier of the element the interaction is asking about.

## Return Value

Returns `true` if the element is the one currently focused.

## See Also

### Managing focus

- [indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md) — Asks the delegate to focus an element to handle text edits.
- [indirectScribbleInteraction:shouldDelayFocusForElement:](indirectscribbleinteraction_shoulddelayfocusforelement_.md) — Allows the delegate to delay focusing an element.
