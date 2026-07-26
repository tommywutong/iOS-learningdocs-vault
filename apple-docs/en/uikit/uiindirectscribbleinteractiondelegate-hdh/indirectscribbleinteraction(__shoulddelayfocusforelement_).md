---
title: 'indirectScribbleInteraction(_:shouldDelayFocusForElement:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:shoulddelayfocusforelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Ashoulddelayfocusforelement%3A%29.json'
content_hash: 'sha256:48b5379b8e064d31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:shouldDelayFocusForElement:)

<sub>Instance Method</sub>

Allow the delegate to delay focusing an element.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, shouldDelayFocusForElement elementIdentifier: Self.ElementIdentifier) -> Bool
```

## Parameters

- `interaction` — The interaction asking about delaying focus.

- `elementIdentifier` — The identifier of the element the interaction is asking about.

## Return Value

Return [true](../../swift/true.md) to delay focusing the element; the default is [false](../../swift/false.md).

## Default Implementations

### UIIndirectScribbleInteractionDelegate Implementations

- [indirectScribbleInteraction(_:shouldDelayFocusForElement:)](<indirectscribbleinteraction(__shoulddelayfocusforelement_)-9dmtl.md>)

## See Also

### Managing Focus

- [indirectScribbleInteraction(_:isElementFocused:)](<indirectscribbleinteraction(__iselementfocused_).md>) — Asks the delegate if an element is currently focused, according to the internal state of the interaction’s view.
- [indirectScribbleInteraction(_:focusElementIfNeeded:referencePoint:completion:)](<indirectscribbleinteraction(__focuselementifneeded_referencepoint_completion_).md>) — Asks the delegate to focus an element to handle text edits.
