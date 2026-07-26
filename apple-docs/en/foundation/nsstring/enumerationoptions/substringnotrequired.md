---
title: substringNotRequired
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/enumerationoptions/substringnotrequired
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/substringnotrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/enumerationoptions/substringnotrequired.json'
content_hash: 'sha256:e8585dad7e4abdd9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSString](../../nsstring.md) · [EnumerationOptions](../enumerationoptions.md)

# substringNotRequired

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var substringNotRequired: NSString.EnumerationOptions { get }
```

## Discussion

A way to indicate that the block does not need substring, in which case `nil` will be passed. This is simply a performance shortcut.

## See Also

### Constants

- [NSStringEnumerationByLines](bylines.md)
- [NSStringEnumerationByParagraphs](byparagraphs.md)
- [NSStringEnumerationByComposedCharacterSequences](bycomposedcharactersequences.md)
- [NSStringEnumerationByWords](bywords.md)
- [NSStringEnumerationBySentences](bysentences.md)
- [NSStringEnumerationReverse](reverse.md)
- [NSStringEnumerationLocalized](localized.md)
