---
title: numberOfComponents
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolor/numberofcomponents
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/numberofcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/numberofcomponents.json'
content_hash: 'sha256:8a76a34c580bcdf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# numberOfComponents

<sub>Instance Property</sub>

Returns the color components of the color including alpha.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var numberOfComponents: Int { get }
```

## Discussion

This number includes the alpha component if the color contains one.

Typically this number will be `4` for red, green, blue, and alpha. If the [CIColor](../cicolor.md) was initialized with a `CGColor` then the number will be the same as calling `CGColorGetNumberOfComponents()`

## See Also

### Getting Color Components

- [colorSpace](colorspace.md) — Returns the `CGColorSpace` associated with the color
- [components](components.md) — Return a pointer to an array of `CGFloat` values including alpha.
- [red](red-swift.property.md) — Returns the unpremultiplied red component of the color.
- [green](green-swift.property.md) — Returns the unpremultiplied green component of the color.
- [blue](blue-swift.property.md) — Returns the unpremultiplied blue component of the color.
- [alpha](alpha.md) — Returns the alpha value of the color.
- [stringRepresentation](stringrepresentation.md) — Returns a formatted string with the unpremultiplied color and alpha components of the color.
