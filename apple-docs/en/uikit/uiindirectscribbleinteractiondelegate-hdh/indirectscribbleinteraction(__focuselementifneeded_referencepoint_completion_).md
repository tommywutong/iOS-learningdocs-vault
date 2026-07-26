---
title: 'indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:focuselementifneeded:referencepoint:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Afocuselementifneeded%3Areferencepoint%3Acompletion%3A%29.json'
content_hash: 'sha256:ddcbbe4822db9bd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)

<sub>Instance Method</sub>

Asks the delegate to focus an element to handle text edits.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, focusElementIfNeeded elementIdentifier: Self.ElementIdentifier, referencePoint focusReferencePoint: CGPoint, completion: @escaping ((any UIResponder & UITextInput)?) -> Void)
```

## Parameters

- `interaction` — The interaction requesting to focus an element.

- `elementIdentifier` — The identifier of the element that should receive focus.

- `focusReferencePoint` — A [CGPoint](../../corefoundation/cgpoint.md) inside the element’s view.

- `completion` — A completion handler that you must call, either synchronously or asynchronously. On success, the first parameter should be the text input that became first responder and that handles text operations for this element. On failure, call the completion with a `nil` parameter.

## Return Value

In response to this callback, the implementation should make this element the currently focused one, and make the corresponding [UITextInput](../uitextinput.md) become first responder.

If the element isn’t focused already, set the text selection to the character location closest to `focusReferencePoint` to avoid any scrolling or shifting of content.

If the element is already focused, make no changes to the selection. Before returning you must still call the completion handler with a reference to [UITextInput](../uitextinput.md).

## See Also

### Managing Focus

- [indirectScribbleInteraction(_:isElementFocused:)](<indirectscribbleinteraction(__iselementfocused_).md>) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction(_:shouldDelayFocusForElement:)](<indirectscribbleinteraction(__shoulddelayfocusforelement_).md>) — Allow the delegate to delay focusing an element.
