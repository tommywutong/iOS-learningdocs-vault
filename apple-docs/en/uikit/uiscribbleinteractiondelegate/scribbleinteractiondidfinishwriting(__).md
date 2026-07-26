---
title: 'scribbleInteractionDidFinishWriting(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting%28_%3A%29.json'
content_hash: 'sha256:bbc68e0c164c2432'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteractionDelegate](../uiscribbleinteractiondelegate.md)

# scribbleInteractionDidFinishWriting(_:)

<sub>Instance Method</sub>

Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func scribbleInteractionDidFinishWriting(_ interaction: UIScribbleInteraction)
```

## Parameters

- `interaction` — The interaction where the user finished writing.

## Discussion

Use this to reset placeholders or other UI elements, if appropriate, to their state from before the user started writing.

## See Also

### Tracking Scribble input

- [- scribbleInteractionWillBeginWriting:](<scribbleinteractionwillbeginwriting(__).md>) — Informs the delegate when the user begins writing in the view.
