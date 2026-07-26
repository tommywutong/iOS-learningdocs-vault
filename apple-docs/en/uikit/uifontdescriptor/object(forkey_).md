---
title: 'object(forKey:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/object(forkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/object(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/object%28forkey%3A%29.json'
content_hash: 'sha256:fc8af04ab19c22e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# object(forKey:)

<sub>Instance Method</sub>

Returns the font attribute that the corresponding key specifies.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func object(forKey anAttribute: UIFontDescriptor.AttributeName) -> Any?
```

## Parameters

- `anAttribute` — The font attribute key.

## Return Value

The font attribute corresponding to `anAttribute`. For valid values of `anAttribute`, see [AttributeName](attributename.md).

## See Also

### Querying a font descriptor

- [fontAttributes](fontattributes.md) — The font descriptor’s dictionary of attributes.
- [matrix](matrix.md) — The current transform matrix of the font descriptor.
- [pointSize](pointsize.md) — The point size of the font descriptor.
- [postscriptName](postscriptname.md) — The PostScript name of the font descriptor.
- [symbolicTraits](symbolictraits-swift.property.md) — The traits of the font descriptor.
- [SymbolicTraits](symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
