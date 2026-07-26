---
title: focusedFrameGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/focusedframeguide
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/focusedframeguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/focusedframeguide.json'
content_hash: 'sha256:88ce830b1956b1e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# focusedFrameGuide

<sub>Instance Property</sub>

The layout guide to use when the image view is focused.

<sub>tvOS</sub>

```swift
var focusedFrameGuide: UILayoutGuide { get }
```

## Discussion

The layout guide in this property represents the display frame of the image view when it’s focused. You can use this property to align other elements of your interface to the image view or to adjust the constraints of your interface.

When the [adjustsImageWhenAncestorFocused](adjustsimagewhenancestorfocused.md) property is set to [true](../../swift/true.md), the image view automatically applies this layout guide when the image view becomes focused.

## See Also

### Managing focus-related behaviors

- [adjustsImageWhenAncestorFocused](adjustsimagewhenancestorfocused.md) — A Boolean value that determines whether the image view responds when an ancestor gains focus.
- [masksFocusEffectToContents](masksfocuseffecttocontents.md) — A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.
