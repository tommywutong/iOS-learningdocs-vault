---
title: majorRadiusTolerance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/majorradiustolerance
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/majorradiustolerance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/majorradiustolerance.json'
content_hash: 'sha256:1d813db092922bdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# majorRadiusTolerance

<sub>Instance Property</sub>

The tolerance (in points) of the touch’s radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var majorRadiusTolerance: CGFloat { get }
```

## Discussion

This value determines the accuracy of the value in the [majorRadius](majorradius.md) property. Add this value to the radius to get the maximum touch radius. Subtract the value to get the minimum touch radius.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
