---
title: CGColorConversionInfoTransformType
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorconversioninfotransformtype
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfotransformtype.json'
content_hash: 'sha256:31f13cb34ee3ec9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorConversionInfoTransformType

<sub>Enumeration</sub>

Constants describing how a color conversion uses color spaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGColorConversionInfoTransformType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kCGColorConversionTransformApplySpace](cgcolorconversioninfotransformtype/transformapplyspace.md) — Specifies a color conversion between one color profile and another.
- [kCGColorConversionTransformFromSpace](cgcolorconversioninfotransformtype/transformfromspace.md) — Specifies a color conversion from a device color space to a color profile.
- [kCGColorConversionTransformToSpace](cgcolorconversioninfotransformtype/transformtospace.md) — Specifies a color conversion from a color profile to a device color space.

### Initializers

- [init(rawValue:)](<cgcolorconversioninfotransformtype/init(rawvalue_).md>)

## See Also

### Creating a Color Conversion

- [CGColorConversionInfoCreate](<cgcolorconversioninfo/init(src_dst_).md>) — Creates a conversion between two specified color spaces.
- [CGColorConversionInfoCreateWithOptions](<cgcolorconversioninfo/init(optionssrc_dst_options_).md>)
