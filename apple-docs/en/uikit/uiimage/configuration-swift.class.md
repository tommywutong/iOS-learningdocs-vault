---
title: UIImage.Configuration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/configuration-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/configuration-swift.class.json'
content_hash: 'sha256:e8104bbcea9cb77f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.Configuration

<sub>Class</sub>

A configuration object that contains the traits that the system uses when selecting the current image variant.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class Configuration
```

## Overview

Images may contain multiple variants to account for environmental factors, such as whether the interface is light or dark. The image configuration object lets you override the current environment and render an image with specific attributes. For example, you might want to render a specific version of your image to your interface.

[Configuration](configuration-swift.class.md) objects are immutable and you don’t create them directly. Instead, get an existing image configuration object from a [UITraitCollection](../uitraitcollection.md) or [UIImage](../uiimage.md) object. To add attributes to your configuration object, use the [- configurationByApplyingConfiguration:](<configuration-swift.class/applying(__).md>) method to create a new object that merges the existing object’s values with new values you supply. Assign the new object to the [preferredSymbolConfiguration](../uiimageview/preferredsymbolconfiguration.md) property of the [UIImageView](../uiimageview.md) object you use to display the image. If you draw the image directly, use the [- imageWithConfiguration:](<withconfiguration(__).md>) method to create a new image that contains the new attributes.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Inherited By**: [SymbolConfiguration](symbolconfiguration-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Modifying a configuration object

- [- configurationByApplyingConfiguration:](<configuration-swift.class/applying(__).md>) — Returns a configuration object that applies the specified configuration values on top of the current object’s values.
- [- configurationWithTraitCollection:](<configuration-swift.class/withtraitcollection(__).md>) — Returns a new configuration object that merges the current traits with the traits from the specified trait collection.

### Getting the configuration traits

- [traitCollection](configuration-swift.class/traitcollection.md) — The traits associated with the image configuration.

### Initializers

- [init(coder:)](<configuration-swift.class/init(coder_).md>)
- [+ configurationWithLocale:](<configuration-swift.class/init(locale_).md>)
- [+ configurationWithTraitCollection:](<configuration-swift.class/init(traitcollection_).md>)

### Instance Properties

- [locale](configuration-swift.class/locale.md)

### Instance Methods

- [- configurationWithLocale:](<configuration-swift.class/withlocale(__).md>)

## See Also

### Representations

- [UIImage](../uiimage.md) — An object that manages image data in your app.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
