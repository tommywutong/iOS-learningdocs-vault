---
title: UIImage.SymbolScale
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolscale
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolscale.json'
content_hash: 'sha256:c8c4a17e2e68d562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.SymbolScale

<sub>Enumeration</sub>

Constants that indicate which scale variant of a symbol image to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum SymbolScale
```

## Overview

The definition of a symbol image includes multiple scale and weight variants. Scale variants offer a way to define the size of the image relative to layout guides in the symbol image’s definition file. The system chooses the appropriate size variant based on the available space and configuration options.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Symbol image scales

- [UIImageSymbolScaleDefault](symbolscale/default.md) — The default scale variant that matches the system usage.
- [UIImageSymbolScaleUnspecified](symbolscale/unspecified.md) — An unspecified scale.
- [UIImageSymbolScaleSmall](symbolscale/small.md) — The small variant of the symbol image.
- [UIImageSymbolScaleMedium](symbolscale/medium.md) — The medium variant of the symbol image
- [UIImageSymbolScaleLarge](symbolscale/large.md) — The large variant of the symbol image.

### Initializers

- [init(rawValue:)](<symbolscale/init(rawvalue_).md>)

## See Also

### Creating a symbol configuration

- [+ configurationWithPointSize:](<symbolconfiguration-swift.class/init(pointsize_).md>) — Creates a configuration object with the specified point-size information.
- [+ configurationWithPointSize:weight:](<symbolconfiguration-swift.class/init(pointsize_weight_).md>) — Creates a configuration object with the specified point-size and weight information.
- [+ configurationWithPointSize:weight:scale:](<symbolconfiguration-swift.class/init(pointsize_weight_scale_).md>) — Creates a configuration object with the specified point-size, weight, and scale information.
- [+ configurationWithScale:](<symbolconfiguration-swift.class/init(scale_).md>) — Creates a configuration object with the specified scale information.
- [+ configurationWithTextStyle:](<symbolconfiguration-swift.class/init(textstyle_).md>) — Creates a configuration object with the specified font text style information.
- [+ configurationWithTextStyle:scale:](<symbolconfiguration-swift.class/init(textstyle_scale_).md>) — Creates a configuration object with the specified font text style and scale information.
- [+ configurationWithWeight:](<symbolconfiguration-swift.class/init(weight_).md>) — Creates a configuration object with the specified weight information.
- [+ configurationWithFont:](<symbolconfiguration-swift.class/init(font_).md>) — Creates a configuration object with the specified font information.
- [+ configurationWithFont:scale:](<symbolconfiguration-swift.class/init(font_scale_).md>) — Creates a configuration object with the specified font and scale information.
- [SymbolWeight](symbolweight.md) — Constants that indicate which weight variant of a symbol image to use.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md)
- [SymbolVariableValueMode](symbolvariablevaluemode.md)
