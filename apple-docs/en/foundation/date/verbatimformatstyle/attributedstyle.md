---
title: attributedStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/verbatimformatstyle/attributedstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/verbatimformatstyle/attributedstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/verbatimformatstyle/attributedstyle.json'
content_hash: 'sha256:ab00644b089f2259'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [VerbatimFormatStyle](../verbatimformatstyle.md)

# attributedStyle

<sub>Instance Property</sub>

Return the type preserving attributed variant of this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributedStyle: Date.VerbatimFormatStyle.Attributed { get }
```

## Discussion

This style attributes the formatted date with the `AttributeScopes.FoundationAttributes.DateFormatFieldAttribute`.
