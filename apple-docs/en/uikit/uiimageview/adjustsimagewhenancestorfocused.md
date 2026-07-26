---
title: adjustsImageWhenAncestorFocused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/adjustsimagewhenancestorfocused
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/adjustsimagewhenancestorfocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/adjustsimagewhenancestorfocused.json'
content_hash: 'sha256:244c3922226ed0c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# adjustsImageWhenAncestorFocused

<sub>Instance Property</sub>

A Boolean value that determines whether the image view responds when an ancestor gains focus.

<sub>tvOS</sub>

```swift
var adjustsImageWhenAncestorFocused: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md) and an ancestor of the image view becomes focused, the image view adjusts the frame of its image using the [focusedFrameGuide](focusedframeguide.md) property. On supported Apple TV devices, setting this property to true renders the image with a Liquid Glass effect when it gains focus.

The default value of this property is [false](../../swift/false.md).

## See Also

### Managing focus-related behaviors

- [focusedFrameGuide](focusedframeguide.md) — The layout guide to use when the image view is focused.
- [masksFocusEffectToContents](masksfocuseffecttocontents.md) — A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.
