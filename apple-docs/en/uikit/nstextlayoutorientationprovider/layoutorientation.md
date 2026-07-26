---
title: layoutOrientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutorientationprovider/layoutorientation
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider/layoutorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutorientationprovider/layoutorientation.json'
content_hash: 'sha256:2f3645f763477bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutOrientationProvider](../nstextlayoutorientationprovider.md)

# layoutOrientation

<sub>Instance Property</sub>

The default layout orientation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutOrientation: NSLayoutManager.TextLayoutOrientation { get }
```

## Discussion

This property contains the default layout orientation for text in the object that adopts the protocol. If the text contains an explicit [verticalGlyphForm](../../foundation/nsattributedstring/key/verticalglyphform.md) attribute in Swift or an [NSVerticalGlyphFormAttributeName](../nsverticalglyphformattributename.md) attribute in Objective-C, that attribute overrides the value in this property. When rendering, TextKit assumes the coordinate system is appropriately rotated.

## See Also

### Getting layout orientation

- [TextLayoutOrientation](../nslayoutmanager/textlayoutorientation.md) — Constants that describe the text layout orientation.
