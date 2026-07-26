---
title: 'CTFontGetSymbolicTraits(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetsymbolictraits(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetsymbolictraits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetsymbolictraits%28_%3A%29.json'
content_hash: 'sha256:2e08dff77a8d3fe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetSymbolicTraits(_:)

<sub>Function</sub>

Returns the symbolic traits of the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetSymbolicTraits(_ font: CTFont) -> CTFontSymbolicTraits
```

## Parameters

- `font` — The font reference.

## Return Value

The symbolic traits of the font. This is equivalent to the `kCTFontSymbolicTrait` value of the traits dictionary.

## Discussion

See the Constants section of [CTFontDescriptor](ctfontdescriptor.md) for a definition of the font traits.

## See Also

### Getting Font Data

- [CTFontCopyFontDescriptor](<ctfontcopyfontdescriptor(__).md>) — Returns the normalized font descriptor for the given font reference.
- [CTFontCopyAttribute](<ctfontcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute of the given font.
- [CTFontGetSize](<ctfontgetsize(__).md>) — Returns the point size of the given font.
- [CTFontGetMatrix](<ctfontgetmatrix(__).md>) — Returns the transformation matrix of the given font.
- [CTFontCopyTraits](<ctfontcopytraits(__).md>) — Returns the traits dictionary of the given font.
- [CTFontCopyDefaultCascadeListForLanguages](<ctfontcopydefaultcascadelistforlanguages(____).md>) — Retrieves an ordered list of font substitution preferences.
