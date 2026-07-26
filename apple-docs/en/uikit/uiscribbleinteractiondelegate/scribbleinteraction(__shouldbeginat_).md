---
title: 'scribbleInteraction(_:shouldBeginAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteraction(_:shouldbeginat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteraction(_:shouldbeginat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscribbleinteractiondelegate/scribbleinteraction%28_%3Ashouldbeginat%3A%29.json'
content_hash: 'sha256:8cea7bb80b33ac1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScribbleInteractionDelegate](../uiscribbleinteractiondelegate.md)

# scribbleInteraction(_:shouldBeginAt:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the delegate should allow writing at a specific location in the view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func scribbleInteraction(_ interaction: UIScribbleInteraction, shouldBeginAt location: CGPoint) -> Bool
```

## Parameters

- `interaction` — The text view asking if it can start receiving user input.

- `location` — The location of the text view as a [CGPoint](../../corefoundation/cgpoint.md) in the view’s coordinate system.

## Return Value

Return `false` to disallow writing at the specified location; otherwise return `true`.

## Discussion

Use this callback to temporarily suppress Scribble in text input views if your app supports drawing over text or special interaction when using Apple Pencil. In cases like this, consider providing a UI for the user to toggle between drawing and handwriting.

This callback can also return `false` for views that handle Apple Pencil events directly, like a drawing canvas, since nearby text fields could take over the events for writing.

## See Also

### Allowing and controlling Scribble interactions

- [- scribbleInteractionShouldDelayFocus:](<scribbleinteractionshoulddelayfocus(__).md>) — Tells the delegate to delay focusing the text input view.
