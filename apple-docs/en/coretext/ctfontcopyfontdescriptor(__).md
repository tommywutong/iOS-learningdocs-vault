---
title: 'CTFontCopyFontDescriptor(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyfontdescriptor(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyfontdescriptor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyfontdescriptor%28_%3A%29.json'
content_hash: 'sha256:724ffd6543f79578'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyFontDescriptor(_:)

<sub>Function</sub>

Returns the normalized font descriptor for the given font reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyFontDescriptor(_ font: CTFont) -> CTFontDescriptor
```

## Parameters

- `font` — The font reference.

## Return Value

A normalized font descriptor for a font containing enough information to recreate this font at a later time.

## See Also

### Getting Font Data

- [CTFontCopyAttribute](<ctfontcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute of the given font.
- [CTFontGetSize](<ctfontgetsize(__).md>) — Returns the point size of the given font.
- [CTFontGetMatrix](<ctfontgetmatrix(__).md>) — Returns the transformation matrix of the given font.
- [CTFontGetSymbolicTraits](<ctfontgetsymbolictraits(__).md>) — Returns the symbolic traits of the given font.
- [CTFontCopyTraits](<ctfontcopytraits(__).md>) — Returns the traits dictionary of the given font.
- [CTFontCopyDefaultCascadeListForLanguages](<ctfontcopydefaultcascadelistforlanguages(____).md>) — Retrieves an ordered list of font substitution preferences.
