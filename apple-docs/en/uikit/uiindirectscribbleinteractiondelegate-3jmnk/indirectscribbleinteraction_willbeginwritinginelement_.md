---
title: 'indirectScribbleInteraction:willBeginWritingInElement:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:willbeginwritinginelement:'
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction:willbeginwritinginelement:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction%3Awillbeginwritinginelement%3A.json'
content_hash: 'sha256:2f87a405ffddef6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteractionDelegate](../uiindirectscribbleinteractiondelegate-3jmnk.md)

# indirectScribbleInteraction:willBeginWritingInElement:

<sub>Instance Method</sub>

Informs the delegate when the user begins writing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) indirectScribbleInteraction:(UIIndirectScribbleInteraction *) interaction willBeginWritingInElement:(UIScribbleElementIdentifier) elementIdentifier;
```

## Parameters

- `interaction` — The interaction where the user started writing.

- `elementIdentifier` — The identifier of the element that should receive focus.

## Discussion

Use this to hide custom placeholders or other UI elements that can interfere with writing.

## See Also

### Tracking Scribble input

- [indirectScribbleInteraction:didFinishWritingInElement:](indirectscribbleinteraction_didfinishwritinginelement_.md) — Informs the delegate when the user finishes writing.
