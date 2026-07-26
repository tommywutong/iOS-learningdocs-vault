---
title: UIFontDescriptor.FeatureKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/featurekey
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/featurekey.json'
content_hash: 'sha256:939ca2c9a8d65622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# UIFontDescriptor.FeatureKey

<sub>Structure</sub>

Keys for retrieving feature settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct FeatureKey
```

## Overview

Use these keys when retrieving information from one of the dictionaries associated with the [UIFontDescriptorFeatureSettingsAttribute](attributename/featuresettings.md) key.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Keys

- [type](featurekey/type.md) — A key for identifying the font feature type.
- [selector](featurekey/selector.md) — A key for identifying the font feature selector.

### Initializers

- [init(_:)](<featurekey/init(__).md>) — Creates a font feature key.
- [init(rawValue:)](<featurekey/init(rawvalue_).md>) — Creates a font feature key with the specified raw value.

### Deprecated

- [UIFontFeatureTypeIdentifierKey](featurekey/featureidentifier.md) — A key for identifying a font feature type. _(deprecated)_
- [UIFontFeatureSelectorIdentifierKey](featurekey/typeidentifier.md) — A key for identifying the font feature selector. _(deprecated)_

## See Also

### Constants

- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [SystemDesign](systemdesign.md) — Constants that describe the system-defined typeface designs.
- [SymbolicTraits](symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [Class](class.md) — Constants that classify certain stylistic qualities of the font.
- [AttributeName](attributename.md) — Constants that describe font attributes.
- [TraitKey](traitkey.md) — Keys for retrieving the font descriptor’s trait information.
- [Weight](../uifont/weight.md) — Constants that represent standard typeface styles.
- [Width](../uifont/width.md)
