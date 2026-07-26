---
title: insertAttributesWithoutMerging
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/interpolationoptions/insertattributeswithoutmerging
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/interpolationoptions/insertattributeswithoutmerging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/interpolationoptions/insertattributeswithoutmerging.json'
content_hash: 'sha256:f9a1a91bf9851b0f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [InterpolationOptions](../interpolationoptions.md)

# insertAttributesWithoutMerging

<sub>Type Property</sub>

By default, interpolating an AttributedString will result in the final string having all attributes present at its interpolation point, plus all attributes from the beginning of the interpolated AttributedString. Specify this option to instead indicate that pre-existing attributes at the point of interpolation (e.g., those specified with Markdown syntax) must be ignored. The result will only have the attributes from the interpolated AttributedString. This option has no effect when formatting a plain-text String, since all attributes will be stripped anyway.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let insertAttributesWithoutMerging: AttributedString.InterpolationOptions
```
