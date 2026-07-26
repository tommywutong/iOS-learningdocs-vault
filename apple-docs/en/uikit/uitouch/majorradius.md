---
title: majorRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/majorradius
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/majorradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/majorradius.json'
content_hash: 'sha256:4f29264e68d8dd39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# majorRadius

<sub>Instance Property</sub>

The radius (in points) of the touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var majorRadius: CGFloat { get }
```

## Discussion

Use the value in this property to determine the size of the touch that was reported by the hardware. This value is an approximation of the size and can vary by the amount specified in the [majorRadiusTolerance](majorradiustolerance.md) property.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
