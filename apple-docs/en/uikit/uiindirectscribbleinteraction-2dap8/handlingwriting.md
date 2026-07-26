---
title: handlingWriting
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiindirectscribbleinteraction-2dap8/handlingwriting
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-2dap8/handlingwriting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteraction-2dap8/handlingwriting.json'
content_hash: 'sha256:4a80766718e97090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIIndirectScribbleInteraction](../uiindirectscribbleinteraction-2dap8.md)

# handlingWriting

<sub>Instance Property</sub>

A Boolean value that indicates whether the user is actively writing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, getter=isHandlingWriting) BOOL handlingWriting;
```

## Discussion

Set to [true](../../swift/true.md) in between calls to [indirectScribbleInteraction:willBeginWritingInElement:](../uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_willbeginwritinginelement_.md) and [indirectScribbleInteraction:didFinishWritingInElement:](../uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_didfinishwritinginelement_.md) calls.
