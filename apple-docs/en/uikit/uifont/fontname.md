---
title: fontName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/fontname
source_url: 'https://developer.apple.com/documentation/uikit/uifont/fontname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/fontname.json'
content_hash: 'sha256:07bd7ad17cf3186b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# fontName

<sub>Instance Property</sub>

The font face name.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var fontName: String { get }
```

## Discussion

The font name is a name such as `HelveticaBold` that incorporates the family name and any specific style information for the font. The value in this property is intended for an application’s internal usage only and should not be displayed.

## See Also

### Getting Font Name Attributes

- [familyName](familyname.md) — The font family name.
