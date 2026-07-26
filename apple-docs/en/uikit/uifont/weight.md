---
title: UIFont.Weight
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 4.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/weight
source_url: 'https://developer.apple.com/documentation/uikit/uifont/weight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/weight.json'
content_hash: 'sha256:5e475899eeacf9b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# UIFont.Weight

<sub>Structure</sub>

Constants that represent standard typeface styles.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct Weight
```

## Overview

Use system-defined constants as interchangeable values for [UIFontWeightTrait](../uifontdescriptor/traitkey/weight.md). Each constant corresponds to a different value that indicates the weight of a font. Use these constants to specify the weight parameter in [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>). When providing a weight that doesn’t precisely match a font face in the family, the system locates a face that most closely matches the request.

> [!note] Note
> Font [familyNames](familynames.md) don’t include all system-defined font constants.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Comparable](../../swift/comparable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Using system-defined font weights

- [UIFontWeightUltraLight](weight/ultralight.md) — The ultra-light font weight.
- [UIFontWeightThin](weight/thin.md) — The thin font weight.
- [UIFontWeightLight](weight/light.md) — The light font weight.
- [UIFontWeightRegular](weight/regular.md) — The regular font weight.
- [UIFontWeightMedium](weight/medium.md) — The medium font weight.
- [UIFontWeightSemibold](weight/semibold.md) — The semibold font weight.
- [UIFontWeightBold](weight/bold.md) — The bold font weight.
- [UIFontWeightHeavy](weight/heavy.md) — The heavy font weight.
- [UIFontWeightBlack](weight/black.md) — The black font weight.

### Balancing the appearance of symbols and text

- [UIImageSymbolWeightForFontWeight](<weight/symbolweight().md>) — Provides the corresponding symbol weight for this font weight.

### Initializers

- [init(_:)](<weight/init(__).md>) — Creates a font weight.
- [init(rawValue:)](<weight/init(rawvalue_).md>) — Creates a font weight with the specified raw value.

## See Also

### Creating System Fonts

- [+ systemFontOfSize:](<systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [+ systemFontOfSize:weight:](<systemfont(ofsize_weight_).md>) — Returns the font object for standard interface items in the specified size and weight.
- [+ systemFontOfSize:weight:width:](<systemfont(ofsize_weight_width_).md>)
- [Width](width.md)
- [+ boldSystemFontOfSize:](<boldsystemfont(ofsize_).md>) — Returns the font object for standard interface items in boldface type in the specified size.
- [+ italicSystemFontOfSize:](<italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedSystemFontOfSize:weight:](<monospacedsystemfont(ofsize_weight_).md>) — Returns the fixed-width font for standard interface text in the specified size.
- [+ monospacedDigitSystemFontOfSize:weight:](<monospaceddigitsystemfont(ofsize_weight_).md>) — Returns the standard system font with all digits of consistent width.
