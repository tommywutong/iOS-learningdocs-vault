---
title: masksFocusEffectToContents
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/masksfocuseffecttocontents
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/masksfocuseffecttocontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/masksfocuseffecttocontents.json'
content_hash: 'sha256:a61baaf0866930f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# masksFocusEffectToContents

<sub>Instance Property</sub>

A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.

<sub>tvOS</sub>

```swift
var masksFocusEffectToContents: Bool { get set }
```

## Discussion

Set this property to [false](../../swift/false.md) when using multi-layer images or when using images that are completely opaque. Set this property to [true](../../swift/true.md) only when the image view contains a single-layer image with transparency. When set to [true](../../swift/true.md), the system uses the image’s alpha channel to create an appropriate floating focused appearance. For example, the system masks the shadow based on the alpha channel of the image.

The aspect ratio of the image view and its displayed image must be the same. Rendering with transparency affects performance, so enable this option only when needed.

## See Also

### Managing focus-related behaviors

- [adjustsImageWhenAncestorFocused](adjustsimagewhenancestorfocused.md) — A Boolean value that determines whether the image view responds when an ancestor gains focus.
- [focusedFrameGuide](focusedframeguide.md) — The layout guide to use when the image view is focused.
