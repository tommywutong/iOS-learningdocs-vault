---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteraction/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteraction/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteraction/location%28in%3A%29.json'
content_hash: 'sha256:d9a20da5b7566480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteraction](../uipreviewinteraction.md)

# location(in:)

<sub>Instance Method</sub>

Returns the location of the touch that started the interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func location(in coordinateSpace: (any UICoordinateSpace)?) -> CGPoint
```

## Parameters

- `coordinateSpace` — The coordinate space in which the touch location should be returned.

## Return Value

The [CGPoint](../../corefoundation/cgpoint.md) that represents the current location of the touch, translated into the requested coordinate space.

## Discussion

Use this method to establish the current location of the touch that triggered the preview interaction.

> [!note] Note
> [UIView](../uiview.md) adopts the [UICoordinateSpace](../uicoordinatespace.md) protocol, so you can find the touch location within a view in the view hierarchy.

When the preview interaction isn’t running, calling this method returns an invalid point. You must therefore only call this method in response to one of the delegate callbacks specified in [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md).

## See Also

### Handling preview interactions

- [view](view.md) — The view from which the preview interaction receives touch events.
- [- cancelInteraction](<cancel().md>) — Cancels the current preview interaction.
