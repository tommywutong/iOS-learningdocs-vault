---
title: 'indirectScribbleInteraction(_:didFinishWritingInElement:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:didfinishwritinginelement:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:didfinishwritinginelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Adidfinishwritinginelement%3A%29.json'
content_hash: 'sha256:cee6bdd5480648c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:didFinishWritingInElement:)

<sub>Instance Method</sub>

Informs the delegate when the user finishes writing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, didFinishWritingInElement elementIdentifier: Self.ElementIdentifier)
```

## Parameters

- `interaction` — The interaction where the user finished writing.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## Default Implementations

### UIIndirectScribbleInteractionDelegate Implementations

- [indirectScribbleInteraction(_:didFinishWritingInElement:)](<indirectscribbleinteraction(__didfinishwritinginelement_)-9q7os.md>)

## See Also

### Tracking Scribble Input

- [indirectScribbleInteraction(_:willBeginWritingInElement:)](<indirectscribbleinteraction(__willbeginwritinginelement_).md>) — Informs the delegate when the user begins writing.
