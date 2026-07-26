---
title: configuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/configuration-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/configuration-swift.property.json'
content_hash: 'sha256:c1b615a52739ea6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# configuration

<sub>Instance Property</sub>

The configuration details for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var configuration: UIImage.Configuration? { get }
```

## Discussion

Use this property to access the traits associated with the image. The system uses the specified traits to determine which variant of the image to load and draw, falling back on the current environment for any unspecified traits. The default value of this property is a configuration object with unspecified traits.

You can’t modify this property directly, but you can use the [- imageWithConfiguration:](<withconfiguration(__).md>) method to create a new image object with a specific set of traits. You might do so when you want to render the image yourself using a specific set of traits.

If the image is a symbol image, this property always contains a [SymbolConfiguration](symbolconfiguration-swift.class.md) object.

## See Also

### Getting the image configuration

- [symbolConfiguration](symbolconfiguration-swift.property.md) — The configuration details for a symbol image.
- [traitCollection](traitcollection.md) — The trait collection that describes the current variant of the image.
