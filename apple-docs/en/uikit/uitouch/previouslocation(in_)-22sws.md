---
title: 'previousLocation(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/previouslocation(in:)-22sws'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/previouslocation(in:)-22sws'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/previouslocation%28in%3A%29-22sws.json'
content_hash: 'sha256:52078bd7b9f5c10f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# previousLocation(in:)

<sub>Instance Method</sub>

Returns the previous location of the touch in the coordinate system of the given view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func previousLocation(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view object in whose coordinate system you want the touch located. A custom view that is handling the touch may specify `self` to get the touch location in its own coordinate system. Pass `nil` to get the touch location in the window’s coordinates.

## Return Value

This method returns the previous location of a [UITouch](../uitouch.md) object in the coordinate system of the specified view. Because the touch object might have been forwarded to a view from another view, this method performs any necessary conversion of the touch location to the coordinate system of the specified view.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
