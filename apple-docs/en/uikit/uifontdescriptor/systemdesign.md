---
title: UIFontDescriptor.SystemDesign
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 5.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/systemdesign
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/systemdesign.json'
content_hash: 'sha256:2b3b04f83a8a8a68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# UIFontDescriptor.SystemDesign

<sub>Structure</sub>

Constants that describe the system-defined typeface designs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct SystemDesign
```

## Overview

Use these constants to specify a system-provided typeface design, such as:

- SF Pro in iOS or SF Compact in watchOS ([UIFontDescriptorSystemDesignDefault](systemdesign/default.md))
- SF Pro Rounded in iOS or SF Compact Rounded in watchOS ([UIFontDescriptorSystemDesignRounded](systemdesign/rounded.md))
- SF Mono ([UIFontDescriptorSystemDesignMonospaced](systemdesign/monospaced.md))
- New York ([UIFontDescriptorSystemDesignSerif](systemdesign/serif.md))

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Typeface designs

- [UIFontDescriptorSystemDesignDefault](systemdesign/default.md) — The default typeface for an app’s user interface.
- [UIFontDescriptorSystemDesignRounded](systemdesign/rounded.md) — The rounded variant of the default typeface.
- [UIFontDescriptorSystemDesignMonospaced](systemdesign/monospaced.md) — The monospace variant of the default typeface.
- [UIFontDescriptorSystemDesignSerif](systemdesign/serif.md) — The serif variant of the default typeface.

### Initializers

- [init(rawValue:)](<systemdesign/init(rawvalue_).md>) — Creates a typeface design constant with the specified raw value.

## See Also

### Constants

- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [SymbolicTraits](symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [Class](class.md) — Constants that classify certain stylistic qualities of the font.
- [AttributeName](attributename.md) — Constants that describe font attributes.
- [FeatureKey](featurekey.md) — Keys for retrieving feature settings.
- [TraitKey](traitkey.md) — Keys for retrieving the font descriptor’s trait information.
- [Weight](../uifont/weight.md) — Constants that represent standard typeface styles.
- [Width](../uifont/width.md)
