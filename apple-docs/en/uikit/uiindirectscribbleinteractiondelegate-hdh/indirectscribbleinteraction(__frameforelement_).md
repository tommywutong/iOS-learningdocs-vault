---
title: 'indirectScribbleInteraction(_:frameForElement:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:frameforelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Aframeforelement%3A%29.json'
content_hash: 'sha256:34b5e70dfb3c50cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:frameForElement:)

<sub>Instance Method</sub>

Asks the delegate to provide the frame of an element.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, frameForElement elementIdentifier: Self.ElementIdentifier) -> CGRect
```

## Parameters

- `interaction` — The interaction requesting to focus an element.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Return Value

Returns the frame for the element, in the view coordinate system of the interaction.

## See Also

### Finding Elements and Frames

- [indirectScribbleInteraction(_:requestElementsIn:completion:)](<indirectscribbleinteraction(__requestelementsin_completion_).md>) — Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.
