---
title: CTFontOrientation
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontorientation
source_url: 'https://developer.apple.com/documentation/coretext/ctfontorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontorientation.json'
content_hash: 'sha256:8a614272c00106ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontOrientation

<sub>Enumeration</sub>

The intended rendering orientation of the font for obtaining glyph metrics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontOrientation
```

## Overview

Use the values of this enumeration for [kCTFontOrientationAttribute](kctfontorientationattribute.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Font Orientations

- [kCTFontOrientationDefault](ctfontorientation/default.md) — The native orientation of the font.
- [kCTFontOrientationHorizontal](ctfontorientation/horizontal.md) — The horizontal orientation.
- [kCTFontOrientationVertical](ctfontorientation/vertical.md) — The vertical orientation.

### Deprecated Constants

- [kCTFontDefaultOrientation](ctfontorientation/kctfontdefaultorientation.md) — The native orientation of the font. _(deprecated)_
- [kCTFontHorizontalOrientation](ctfontorientation/kctfonthorizontalorientation.md) — The horizontal orientation. _(deprecated)_
- [kCTFontVerticalOrientation](ctfontorientation/kctfontverticalorientation.md) — The vertical orientation. _(deprecated)_

### Initializers

- [init(rawValue:)](<ctfontorientation/init(rawvalue_).md>)

## See Also

### Related Documentation

- [kCTFontOrientationAttribute](kctfontorientationattribute.md) — The orientation for the glyphs of the font.

### Accessing Font Attributes

- [Font Attributes](font-attributes.md) — The keys for accessing font attributes from a font descriptor.
- [CTFontFormat](ctfontformat.md) — The recognized format of the font.
- [CTFontPriority](ctfontpriority.md) — The priority of font descriptors when resolving duplicates and sorting match results.
