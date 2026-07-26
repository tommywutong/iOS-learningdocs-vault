---
title: 'scribbleInteractionShouldDelayFocus(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteractionshoulddelayfocus%28_%3A%29.json'
content_hash: 'sha256:346a03d0cad928dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteractionDelegate](../uiscribbleinteractiondelegate.md)

# scribbleInteractionShouldDelayFocus(_:)

<sub>Instance Method</sub>

Tells the delegate to delay focusing the text input view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func scribbleInteractionShouldDelayFocus(_ interaction: UIScribbleInteraction) -> Bool
```

## Parameters

- `interaction` — The text input view asking about delaying focus.

## Return Value

Return `true` to delay focusing the text input, `false` otherwise.

## Discussion

Normally, Scribble focuses the target input as soon as the user starts writing. If you return `true` from this callback, Scribble waits until the user pauses briefly while writing. This is useful in cases where the view shifts or transforms when becoming first responder, which can be disruptive to a user trying to write in the field.

It’s preferable to adjust the UI behavior and minimize these kinds transformations to avoid the layout changes. Only use this method as a last resort, since transcription happens all at once instead of incrementally.

## See Also

### Allowing and controlling Scribble interactions

- [- scribbleInteraction:shouldBeginAtLocation:](<scribbleinteraction(__shouldbeginat_).md>) — Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.
