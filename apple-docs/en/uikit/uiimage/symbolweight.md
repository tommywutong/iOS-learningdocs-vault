---
title: UIImage.SymbolWeight
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolweight
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolweight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolweight.json'
content_hash: 'sha256:b5b3c6a0d0b791b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.SymbolWeight

<sub>Enumeration</sub>

Constants that indicate which weight variant of a symbol image to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum SymbolWeight
```

## Overview

The definition of a symbol image includes multiple scale and weight variants. The weight variants offer a way to progressively thicken some or all of the image’s lines. Weights do not correspond to a specific line thickness.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Symbol image weights

- [UIImageSymbolWeightUnspecified](symbolweight/unspecified.md) — An unspecified symbol image weight.
- [UIImageSymbolWeightUltraLight](symbolweight/ultralight.md) — An ultralight weight.
- [UIImageSymbolWeightThin](symbolweight/thin.md) — A thin weight
- [UIImageSymbolWeightLight](symbolweight/light.md) — A light weight.
- [UIImageSymbolWeightRegular](symbolweight/regular.md) — A regular weight.
- [UIImageSymbolWeightMedium](symbolweight/medium.md) — A medium weight.
- [UIImageSymbolWeightSemibold](symbolweight/semibold.md) — A semibold weight.
- [UIImageSymbolWeightBold](symbolweight/bold.md) — A bold weight.
- [UIImageSymbolWeightHeavy](symbolweight/heavy.md) — A heavy weight.
- [UIImageSymbolWeightBlack](symbolweight/black.md) — An ultra-heavy weight.

### Getting the font weight

- [UIFontWeightForImageSymbolWeight](<symbolweight/fontweight().md>) — The font weight for the specified symbol weight.

### Initializers

- [init(rawValue:)](<symbolweight/init(rawvalue_).md>)

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
- [SymbolScale](symbolscale.md) — Constants that indicate which scale variant of a symbol image to use.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md)
- [SymbolVariableValueMode](symbolvariablevaluemode.md)
