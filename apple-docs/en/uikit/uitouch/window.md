---
title: window
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/window
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/window'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/window.json'
content_hash: 'sha256:b2c83ad26d538935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# window

<sub>Instance Property</sub>

The window in which the touch initially occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var window: UIWindow? { get }
```

## Discussion

The value of the property is the window in which the touch originally occurred. This window might not be the same window that currently contains the touch.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [view](view.md) — The view to which touches are being delivered, if any.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
