---
title: 'indirectScribbleInteraction(_:requestElementsIn:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:requestelementsin:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Arequestelementsin%3Acompletion%3A%29.json'
content_hash: 'sha256:2ea650dea88db047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:requestElementsIn:completion:)

<sub>Instance Method</sub>

Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, requestElementsIn rect: CGRect, completion: @escaping ([Self.ElementIdentifier]) -> Void)
```

## Parameters

- `interaction` — The interaction where the user finished writing.

- `rect` — The rect around the area where the user is trying to write, in the interaction’s view coordinate system. Return only the elements intersecting this rect.

- `completion` — A completion handler that you must call, either synchronously or asynchronously. Pass an array of identifiers of the available elements, or an empty array if there are no elements.

## Discussion

Each rectangle returned by the completion handler represents an area where the user can start writing even if it’s not a text input field itself.

## See Also

### Finding Elements and Frames

- [indirectScribbleInteraction(_:frameForElement:)](<indirectscribbleinteraction(__frameforelement_).md>) — Asks the delegate to provide the frame of an element.
