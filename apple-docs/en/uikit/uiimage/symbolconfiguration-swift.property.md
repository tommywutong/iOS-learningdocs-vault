---
title: symbolConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.property.json'
content_hash: 'sha256:12c843e4f259adcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# symbolConfiguration

<sub>Instance Property</sub>

The configuration details for a symbol image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var symbolConfiguration: UIImage.SymbolConfiguration? { get }
```

## Discussion

Use this property to access the traits and rendering attributes associated with the symbol image. The system uses the specified details to determine which variant of the image to load and draw and how to render it, falling back on the current environment as needed for any unspecified values. For symbol images, the default value of this property is a symbol image configuration object with unspecified values. For other image types, the default value of this property is `nil`.

You can’t modify this property directly, but you can use the [- imageWithConfiguration:](<withconfiguration(__).md>) when you want to create a new image object with a specific set of traits.

If the image is a symbol image, this property always contains a [SymbolConfiguration](symbolconfiguration-swift.class.md) object.

## See Also

### Getting the image configuration

- [configuration](configuration-swift.property.md) — The configuration details for the image.
- [traitCollection](traitcollection.md) — The trait collection that describes the current variant of the image.
