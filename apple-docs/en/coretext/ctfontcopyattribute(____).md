---
title: 'CTFontCopyAttribute(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyattribute(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyattribute(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyattribute%28_%3A_%3A%29.json'
content_hash: 'sha256:8a4e1c97b0bf0541'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyAttribute(_:_:)

<sub>Function</sub>

Returns the value associated with an arbitrary attribute of the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyAttribute(_ font: CTFont, _ attribute: CFString) -> CFTypeRef?
```

## Parameters

- `font` — The font reference.

- `attribute` — The requested attribute.

## Return Value

A retained reference to an arbitrary attribute or `NULL` if the requested attribute is not present.

## Discussion

Refer to the attribute definitions documentation for information as to how each attribute is packaged as a `CFType`.

## See Also

### Getting Font Data

- [CTFontCopyFontDescriptor](<ctfontcopyfontdescriptor(__).md>) — Returns the normalized font descriptor for the given font reference.
- [CTFontGetSize](<ctfontgetsize(__).md>) — Returns the point size of the given font.
- [CTFontGetMatrix](<ctfontgetmatrix(__).md>) — Returns the transformation matrix of the given font.
- [CTFontGetSymbolicTraits](<ctfontgetsymbolictraits(__).md>) — Returns the symbolic traits of the given font.
- [CTFontCopyTraits](<ctfontcopytraits(__).md>) — Returns the traits dictionary of the given font.
- [CTFontCopyDefaultCascadeListForLanguages](<ctfontcopydefaultcascadelistforlanguages(____).md>) — Retrieves an ordered list of font substitution preferences.
