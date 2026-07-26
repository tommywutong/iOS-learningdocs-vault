---
title: 'CTFontCopyVariationAxes(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyvariationaxes(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyvariationaxes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyvariationaxes%28_%3A%29.json'
content_hash: 'sha256:461f851b0c7b711a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyVariationAxes(_:)

<sub>Function</sub>

Returns an array of variation axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyVariationAxes(_ font: CTFont) -> CFArray?
```

## Parameters

- `font` — The font reference.

## Return Value

An array of variation axes dictionaries. Each variation axis dictionary contains the five variation axis keys listed in [Font Variation Axis Dictionary Keys](font-variation-axis-dictionary-keys.md).

## See Also

### Working With Font Variations

- [CTFontCopyVariation](<ctfontcopyvariation(__).md>) — Returns a variation dictionary from the font reference.
