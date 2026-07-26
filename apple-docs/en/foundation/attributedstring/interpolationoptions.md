---
title: AttributedString.InterpolationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/interpolationoptions
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/interpolationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/interpolationoptions.json'
content_hash: 'sha256:eff876359c7b658f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.InterpolationOptions

<sub>Structure</sub>

Options that affect the behavior of string interpolation on the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct InterpolationOptions
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Type Properties

- [insertAttributesWithoutMerging](interpolationoptions/insertattributeswithoutmerging.md) — By default, interpolating an AttributedString will result in the final string having all attributes present at its interpolation point, plus all attributes from the beginning of the interpolated AttributedString. Specify this option to instead indicate that pre-existing attributes at the point of interpolation (e.g., those specified with Markdown syntax) must be ignored. The result will only have the attributes from the interpolated AttributedString. This option has no effect when formatting a plain-text String, since all attributes will be stripped anyway.
