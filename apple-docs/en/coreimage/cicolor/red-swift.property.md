---
title: red
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolor/red-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/red-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/red-swift.property.json'
content_hash: 'sha256:f46246be818e8b24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# red

<sub>Instance Property</sub>

Returns the unpremultiplied red component of the color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var red: CGFloat { get }
```

## Discussion

If the [CIColor](../cicolor.md) was initialized with a `CGColor` in a non-RGB `CGColorSpace` then it will be converted to sRGB to get the red component.

## See Also

### Getting Color Components

- [colorSpace](colorspace.md) — Returns the `CGColorSpace` associated with the color
- [components](components.md) — Return a pointer to an array of `CGFloat` values including alpha.
- [numberOfComponents](numberofcomponents.md) — Returns the color components of the color including alpha.
- [green](green-swift.property.md) — Returns the unpremultiplied green component of the color.
- [blue](blue-swift.property.md) — Returns the unpremultiplied blue component of the color.
- [alpha](alpha.md) — Returns the alpha value of the color.
- [stringRepresentation](stringrepresentation.md) — Returns a formatted string with the unpremultiplied color and alpha components of the color.
