---
title: colors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/colors
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/colors.json'
content_hash: 'sha256:c0ded1989d50513a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# colors

<sub>Instance Property</sub>

An array of color objects in all pasteboard items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var colors: [UIColor]? { get set }
```

## Discussion

The value stored in this property is an array of [UIColor](../uicolor.md) objects. The associated array of representation types is [UIPasteboardTypeListColor](typelistcolor.md). Setting this property replaces all current items in the pasteboard with the new items. The returned array may have fewer objects than the number of pasteboard items; this happens if a pasteboard item does not have a value of the indicated type.

> [!note] Note
> Do not use this property to determine if a pasteboard contains color data. Instead, use the [hasColors](hascolors.md) property.

## See Also

### Getting and setting pasteboard items of standard data types

- [string](string.md) — The string value of the first pasteboard item.
- [strings](strings.md) — An array of strings in all pasteboard items.
- [image](image.md) — The image object of the first pasteboard item.
- [images](images.md) — An array of image objects in all pasteboard items.
- [URL](url.md) — The URL object of the first pasteboard item.
- [URLs](urls.md) — An array of URL objects in all pasteboard items.
- [color](color.md) — The color object of the first pasteboard item.
