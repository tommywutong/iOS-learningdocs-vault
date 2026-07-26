---
title: selectedColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolorwell/selectedcolor
source_url: 'https://developer.apple.com/documentation/uikit/uicolorwell/selectedcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolorwell/selectedcolor.json'
content_hash: 'sha256:14d67999ce6b206e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColorWell](../uicolorwell.md)

# selectedColor

<sub>Instance Property</sub>

The selected color in the color picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedColor: UIColor? { get set }
```

## Discussion

When a person selects a new color in the color picker, the system generates the control event [UIControlEventValueChanged](../uicontrol/event/valuechanged.md).

This property is KVO-compliant.

## See Also

### Configuring color picker attributes

- [title](title.md) — The title for the color picker.
- [maximumLinearExposure](maximumlinearexposure.md) — The maximum exposure to apply to a color when returned by the color well.
- [supportsAlpha](supportsalpha.md) — A Boolean value that determines whether the color picker supports alpha values.
- [supportsEyedropper](supportseyedropper.md) — If set to `NO` the eyedropper functionality is not supported for this color well.
