---
title: 'preciseLocation(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/preciselocation(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/preciselocation(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/preciselocation%28in%3A%29.json'
content_hash: 'sha256:8992f3e1379154c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# preciseLocation(in:)

<sub>Instance Method</sub>

Returns a precise location for the touch, when available.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func preciseLocation(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view that contains the touch.

## Return Value

A precise location for the touch.

## Discussion

Use this method to get additional precision for a touch (when available). Do not use the returned point for hit testing. In some cases, hit testing can indicate that the touch is within a view, but hit testing against the more precise location may indicate that the touch is outside of the view.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
