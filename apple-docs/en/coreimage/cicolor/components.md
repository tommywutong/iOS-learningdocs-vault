---
title: components
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolor/components
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/components.json'
content_hash: 'sha256:b61871fb5c68e813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# components

<sub>Instance Property</sub>

Return a pointer to an array of `CGFloat` values including alpha.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var components: UnsafePointer<CGFloat> { get }
```

## Discussion

Typically this array will contain `4` `CGFloat` values for red, green, blue, and alpha. If the [CIColor](../cicolor.md) was initialized with a `CGColor` then returned pointer will be the same as calling `CGColorGetComponents()`

## See Also

### Getting Color Components

- [colorSpace](colorspace.md) — Returns the `CGColorSpace` associated with the color
- [numberOfComponents](numberofcomponents.md) — Returns the color components of the color including alpha.
- [red](red-swift.property.md) — Returns the unpremultiplied red component of the color.
- [green](green-swift.property.md) — Returns the unpremultiplied green component of the color.
- [blue](blue-swift.property.md) — Returns the unpremultiplied blue component of the color.
- [alpha](alpha.md) — Returns the alpha value of the color.
- [stringRepresentation](stringrepresentation.md) — Returns a formatted string with the unpremultiplied color and alpha components of the color.
