---
title: 'indirectScribbleInteraction:requestElementsInRect:completion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:requestelementsinrect:completion:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:requestelementsinrect:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Arequestelementsinrect%3Acompletion%3A.json'
content_hash: 'sha256:c573bc3f06d6dd4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:requestElementsInRect:completion:

<sub>Instance Method</sub>

Asks the delegate to return the locations of text input elements inside the specified rectangle of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction requestElementsInRect:(CGRect) rect completion:(void (^)(NSArray<id<NSCopying,NSObject>> *elements)) completion;
```

## Parameters

- `interaction` — The interaction requesting to focus an element.

- `rect` — The rect around the area where the user is trying to write, in the interaction’s view coordinate system. Return only the elements intersecting this rect.

- `completion` — A completion handler that you must call, either synchronously or asynchronously. Pass an array of identifiers of the available elements, or an empty array if there are no elements.

## Discussion

Each rectangle returned by the completion handler represents an area where the user can start writing even if it’s not a text input field itself.

## See Also

### Finding elements and frames

- [indirectScribbleInteraction:frameForElement:](indirectscribbleinteraction_frameforelement_.md) — Asks the delegate to provide the frame of an element.
