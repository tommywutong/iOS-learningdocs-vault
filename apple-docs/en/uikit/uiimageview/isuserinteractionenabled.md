---
title: isUserInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/isuserinteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/isuserinteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/isuserinteractionenabled.json'
content_hash: 'sha256:a9ee291ba24c4623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# isUserInteractionEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether user events are ignored and removed from the event queue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isUserInteractionEnabled: Bool { get set }
```

## Discussion

This property is inherited from the [UIView](../uiview.md) parent class. This class changes the default value of this property to [false](../../swift/false.md).

## See Also

### Configuring the image view

- [highlighted](ishighlighted.md) — A Boolean value that determines whether the image is highlighted.
- [tintColor](tintcolor.md) — A color used to tint template images in the view hierarchy.
