---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/view
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/view.json'
content_hash: 'sha256:385a818bd3eedd90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# view

<sub>Instance Property</sub>

The view to which touches are being delivered, if any.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var view: UIView? { get }
```

## Discussion

The value of this property is the view object to which touches are being delivered, which is not necessarily the view the touch is currently in. For example, when a gesture recognizer recognizes the touch, this property is `nil` because no view is receiving the touch.

## See Also

### Getting the location of a touch

- [- locationInView:](<location(in_)-8rd36.md>) — Returns the current location of the touch in the coordinate system of the given view.
- [- previousLocationInView:](<previouslocation(in_)-22sws.md>) — Returns the previous location of the touch in the coordinate system of the given view.
- [window](window.md) — The window in which the touch initially occurred.
- [majorRadius](majorradius.md) — The radius (in points) of the touch.
- [majorRadiusTolerance](majorradiustolerance.md) — The tolerance (in points) of the touch’s radius.
- [- preciseLocationInView:](<preciselocation(in_).md>) — Returns a precise location for the touch, when available.
- [- precisePreviousLocationInView:](<precisepreviouslocation(in_).md>) — Returns a precise previous location for the touch, when available.
