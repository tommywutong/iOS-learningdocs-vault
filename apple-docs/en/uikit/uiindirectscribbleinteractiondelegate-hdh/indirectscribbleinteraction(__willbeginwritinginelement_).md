---
title: 'indirectScribbleInteraction(_:willBeginWritingInElement:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction(_:willbeginwritinginelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-hdh/indirectscribbleinteraction%28_%3Awillbeginwritinginelement%3A%29.json'
content_hash: 'sha256:28039ccdecb9e7bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-hdh.md)

# indirectScribbleInteraction(_:willBeginWritingInElement:)

<sub>Instance Method</sub>

Informs the delegate when the user begins writing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func indirectScribbleInteraction(_ interaction: any UIInteraction, willBeginWritingInElement elementIdentifier: Self.ElementIdentifier)
```

## Parameters

- `interaction` — The interaction where the user started writing.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Discussion

Use this to hide custom placeholders or other UI elements that can interfere with writing.

## Default Implementations

### UIIndirectScribbleInteractionDelegate Implementations

- [indirectScribbleInteraction(_:willBeginWritingInElement:)](<indirectscribbleinteraction(__willbeginwritinginelement_)-8qsa.md>)

## See Also

### Tracking Scribble Input

- [indirectScribbleInteraction(_:didFinishWritingInElement:)](<indirectscribbleinteraction(__didfinishwritinginelement_).md>) — Informs the delegate when the user finishes writing.
