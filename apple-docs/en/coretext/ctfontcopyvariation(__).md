---
title: 'CTFontCopyVariation(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyvariation(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyvariation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyvariation%28_%3A%29.json'
content_hash: 'sha256:b73360dbd4ebcd42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyVariation(_:)

<sub>Function</sub>

Returns a variation dictionary from the font reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyVariation(_ font: CTFont) -> CFDictionary?
```

## Parameters

- `font` — The font reference.

## Return Value

The current variation instance as a dictionary.

## Discussion

The keys for each variation correspond to the variation identifier obtained via [kCTFontVariationAxisIdentifierKey](kctfontvariationaxisidentifierkey.md), which represents the four-character axis code as a CFNumber object.

## See Also

### Working With Font Variations

- [CTFontCopyVariationAxes](<ctfontcopyvariationaxes(__).md>) — Returns an array of variation axes.
