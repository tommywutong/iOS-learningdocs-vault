---
title: sourceTextScaling
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/sourcetextscaling
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/sourcetextscaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/sourcetextscaling.json'
content_hash: 'sha256:325ab184722c7aa7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# sourceTextScaling

<sub>Type Property</sub>

The text-scaling mode to associate with the document’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let sourceTextScaling: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

The value of this property is one of the options of the [NSTextScalingType](../../../uikit/nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this option to specify the text-scaling mode to associate with the document’s contents on disk.

## See Also

### Getting the font-scaling options

- [targetTextScaling](targettextscaling.md) — The text scaling mode to use after reading the text from disk.
