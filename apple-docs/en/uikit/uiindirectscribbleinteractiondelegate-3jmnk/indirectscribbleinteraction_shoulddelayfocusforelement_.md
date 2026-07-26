---
title: 'indirectScribbleInteraction:shouldDelayFocusForElement:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:shoulddelayfocusforelement:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:shoulddelayfocusforelement:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Ashoulddelayfocusforelement%3A.json'
content_hash: 'sha256:727a24eb7c4024c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:shouldDelayFocusForElement:

<sub>Instance Method</sub>

Allows the delegate to delay focusing an element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction shouldDelayFocusForElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Parameters

- `interaction` — The interaction asking about delaying focus.

- `elementIdentifier` — The identifier of the element the interaction is asking about.

## Return Value

Return [true](../../swift/true.md) to delay focusing the element; the default is [false](../../swift/false.md).

## Discussion

Normally, Scribble focuses the target input as soon as the user begins writing. If you return `true` from this callback, it waits until the user pauses briefly. This is useful in cases where the view shifts or transforms when becoming first responder, which can be disruptive to a user trying to write into the field.

It’s preferable to adjust the UI behavior to avoid the layout changes. Only use delayed focus as a last resort, since transcription happens all at once instead of incrementally.

## See Also

### Managing focus

- [indirectScribbleInteraction:isElementFocused:](indirectscribbleinteraction_iselementfocused_.md) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:](indirectscribbleinteraction_focuselementifneeded_referencepoint_completion_.md) — Asks the delegate to focus an element to handle text edits.
