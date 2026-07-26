---
title: allowedScrollTypesMask
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipangesturerecognizer/allowedscrolltypesmask
source_url: 'https://developer.apple.com/documentation/uikit/uipangesturerecognizer/allowedscrolltypesmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipangesturerecognizer/allowedscrolltypesmask.json'
content_hash: 'sha256:d3d95e00038178a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPanGestureRecognizer](../uipangesturerecognizer.md)

# allowedScrollTypesMask

<sub>Instance Property</sub>

A scroll type mask that enables recognition of scroll events.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowedScrollTypesMask: UIScrollTypeMask { get set }
```

## Discussion

Setting this mask enables the pan gesture to recognize scroll events, like a mouse scroll movement or a two-finger scroll on a track pad. See [UIScrollType](../uiscrolltype.md).

> [!note] Note
> Setting this property doesn’t disable scrolling through touches. To disable touch scrolling, return [false](../../swift/false.md) from [- gestureRecognizer:shouldReceiveTouch:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldreceive_)-16fuh.md>) or set the [allowedTouchTypes](../uigesturerecognizer/allowedtouchtypes.md) to an empty array.

## See Also

### Tracking scroll events

- [UIScrollTypeMask](../uiscrolltypemask.md) — A bit mask identifying the scroll type of a pan gesture.
- [UIScrollType](../uiscrolltype.md) — Constants that define the type of the scroll.
