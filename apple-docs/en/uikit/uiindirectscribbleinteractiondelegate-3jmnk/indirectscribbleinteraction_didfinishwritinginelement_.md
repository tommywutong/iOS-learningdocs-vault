---
title: 'indirectScribbleInteraction:didFinishWritingInElement:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:didfinishwritinginelement:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:didfinishwritinginelement:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Adidfinishwritinginelement%3A.json'
content_hash: 'sha256:154297d393e1b146'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:didFinishWritingInElement:

<sub>Instance Method</sub>

Informs the delegate when the user finishes writing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction didFinishWritingInElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Parameters

- `interaction` — The interaction where the user finished writing.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## See Also

### Tracking Scribble input

- [indirectScribbleInteraction:willBeginWritingInElement:](indirectscribbleinteraction_willbeginwritinginelement_.md) — Informs the delegate when the user begins writing.
