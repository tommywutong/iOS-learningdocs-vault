---
title: supportsAlpha
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolorwell/supportsalpha
source_url: 'https://developer.apple.com/documentation/uikit/uicolorwell/supportsalpha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorwell/supportsalpha.json'
content_hash: 'sha256:cb3b2eed0db1c28f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorWell](../uicolorwell.md)

# supportsAlpha

<sub>Instance Property</sub>

A Boolean value that determines whether the color picker supports alpha values.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportsAlpha: Bool { get set }
```

## Discussion

If this property is [false](../../swift/false.md), people can only pick fully opaque colors from the color picker.

## See Also

### Configuring color picker attributes

- [title](title.md) — The title for the color picker.
- [maximumLinearExposure](maximumlinearexposure.md) — The maximum exposure to apply to a color when returned by the color well.
- [supportsEyedropper](supportseyedropper.md) — If set to `NO` the eyedropper functionality is not supported for this color well.
- [selectedColor](selectedcolor.md) — The selected color in the color picker.
