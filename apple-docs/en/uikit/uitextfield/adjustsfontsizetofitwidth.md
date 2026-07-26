---
title: adjustsFontSizeToFitWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/adjustsfontsizetofitwidth
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/adjustsfontsizetofitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/adjustsfontsizetofitwidth.json'
content_hash: 'sha256:7111163789e2a490'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# adjustsFontSizeToFitWidth

<sub>Instance Property</sub>

A Boolean value that indicates whether to reduce the font size to fit the text string into the text field’s bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustsFontSizeToFitWidth: Bool { get set }
```

## Discussion

Normally, the text field’s content is drawn with the font you specify in the [font](font.md) property. If this property is set to [true](../../swift/true.md), however, and the contents in the [text](text.md) property exceed the text field’s bounding rectangle, the receiver starts reducing the font size until the string fits or the minimum font size is reached. The text is shrunk along the baseline.

The default value for this property is [false](../../swift/false.md). If you change it to [true](../../swift/true.md), you should also set an appropriate minimum font size by modifying the [minimumFontSize](minimumfontsize.md) property.

## See Also

### Sizing the text field’s text

- [minimumFontSize](minimumfontsize.md) — The size of the smallest permissible font when drawing the text field’s text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
