---
title: 'indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:focuselementifneeded:referencepoint:completion:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:focuselementifneeded:referencepoint:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Afocuselementifneeded%3Areferencepoint%3Acompletion%3A.json'
content_hash: 'sha256:76a44f21c28cd853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:

<sub>Instance Method</sub>

Asks the delegate to focus an element to handle text edits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction focusElementIfNeeded:(UIScribbleElementIdentifier) elementIdentifier referencePoint:(CGPoint) focusReferencePoint completion:(void (^)(UIResponder<UITextInput> *focusedInput)) completion;
```

## Parameters

- `interaction` — The interaction requesting to focus an element.

- `elementIdentifier` — The identifier of the element that should receive focus.

- `focusReferencePoint` — A [CGPoint](../../corefoundation/cgpoint.md) inside the element’s view.

- `completion` — A completion handler that you must call, either synchronously or asynchronously. On success, the first parameter should be the text input that became first responder and that handles text operations for this element. On failure, call the completion with a `nil` parameter.

## Discussion

In response to this callback, the implementation should make this element the currently focused one, and make the corresponding [UITextInput](../uitextinput.md) become first responder.

If the element isn’t focused already, set the text selection to the character location closest to `focusReferencePoint` to avoid any scrolling or shifting of content.

If the element is already focused, make no changes to the selection. Before returning you must still call the completion handler with a reference to [UITextInput](../uitextinput.md).

## See Also

### Managing focus

- [indirectScribbleInteraction:isElementFocused:](indirectscribbleinteraction_iselementfocused_.md) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction:shouldDelayFocusForElement:](indirectscribbleinteraction_shoulddelayfocusforelement_.md) — Allows the delegate to delay focusing an element.
