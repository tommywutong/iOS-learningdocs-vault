---
title: textScaling
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/textscaling
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/textscaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/textscaling.json'
content_hash: 'sha256:d26b1c8e8b2de847'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# textScaling

<sub>Type Property</sub>

The text-scaling mode to use when displaying the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let textScaling: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](../../../uikit/nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. When saving a document, include this attribute to specify the type of scaling to apply to the text at display time.

## See Also

### Getting the font-scaling options

- [sourceTextScaling](sourcetextscaling.md) — The text-scaling mode you used when creating the text.
