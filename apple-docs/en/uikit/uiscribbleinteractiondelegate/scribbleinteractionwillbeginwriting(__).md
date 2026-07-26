---
title: 'scribbleInteractionWillBeginWriting(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting%28_%3A%29.json'
content_hash: 'sha256:05a8ceee5bf39519'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteractionDelegate](../uiscribbleinteractiondelegate.md)

# scribbleInteractionWillBeginWriting(_:)

<sub>Instance Method</sub>

Informs the delegate when the user begins writing in the view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func scribbleInteractionWillBeginWriting(_ interaction: UIScribbleInteraction)
```

## Parameters

- `interaction` — The interaction where the user started writing.

## Discussion

Use this method to hide custom placeholders or other UI elements that can interfere with writing.

## See Also

### Tracking Scribble input

- [- scribbleInteractionDidFinishWriting:](<scribbleinteractiondidfinishwriting(__).md>) — Informs the delegate that the user stops writing in the view, after Scribble transcribes and enters the last word.
