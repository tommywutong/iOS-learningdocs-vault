---
title: fontDescriptor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/fontdescriptor
source_url: 'https://developer.apple.com/documentation/uikit/uifont/fontdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/fontdescriptor.json'
content_hash: 'sha256:c1d35b16369f2683'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# fontDescriptor

<sub>Instance Property</sub>

A font descriptor for the font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var fontDescriptor: UIFontDescriptor { get }
```

## Return Value

A font descriptor that describes the font.

## Discussion

The font descriptor contains a mutable dictionary of optional attributes for creating a `UIFont` object. See [UIFontDescriptor](../uifontdescriptor.md) for more information.

## See Also

### Getting Font Descriptors

- [UIFontDescriptor](../uifontdescriptor.md) — A collection of attributes that describes a font.
