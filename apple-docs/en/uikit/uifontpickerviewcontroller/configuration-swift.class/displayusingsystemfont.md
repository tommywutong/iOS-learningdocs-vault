---
title: displayUsingSystemFont
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/displayusingsystemfont
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/displayusingsystemfont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/displayusingsystemfont.json'
content_hash: 'sha256:ac9b92dda8e4f453'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontPickerViewController](../../uifontpickerviewcontroller.md) · [Configuration](../configuration-swift.class.md)

# displayUsingSystemFont

<sub>Instance Property</sub>

A Boolean value that determines whether to use the system font for all font names in the font picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var displayUsingSystemFont: Bool { get set }
```

## Discussion

By default, the font picker uses each font face to display that font face name in the font picker. Set this property to [true](../../../swift/true.md) if you want the font picker to display all font names in the system font instead.
