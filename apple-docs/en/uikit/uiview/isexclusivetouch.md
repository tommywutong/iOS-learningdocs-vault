---
title: isExclusiveTouch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/isexclusivetouch
source_url: 'https://developer.apple.com/documentation/uikit/uiview/isexclusivetouch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/isexclusivetouch.json'
content_hash: 'sha256:c8ec20b50e8cc96a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isExclusiveTouch

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver handles touch events exclusively.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isExclusiveTouch: Bool { get set }
```

## Discussion

Setting this property to [true](../../swift/true.md) causes the receiver to block the delivery of touch events to other views in the same window. The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the event-related behavior

- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [multipleTouchEnabled](ismultipletouchenabled.md) — A Boolean value that indicates whether the view receives more than one touch at a time.
