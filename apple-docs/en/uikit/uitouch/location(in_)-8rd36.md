---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/location(in:)-8rd36'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/location(in:)-8rd36'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/location%28in%3A%29-8rd36.json'
content_hash: 'sha256:37536feee6dd6b98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# location(in:)

<sub>Instance Method</sub>

Returns the current location of the touch in the coordinate system of the given view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view object in whose coordinate system you want the touch located. A custom view that is handling the touch may specify `self` to get the touch location in its own coordinate system. Pass `nil` to get the touch location in the window’s coordinates.

## Return Value

A point specifying the location of the receiver in `view`.

## Discussion

This method returns the current location of a [UITouch](../uitouch.md) object in the coordinate system of the specified view. Because the touch object might have been forwarded to a view from another view, this method performs any necessary conversion of the touch location to the coordinate system of the specified view.

## See Also

### Getting the location of a touch

- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
