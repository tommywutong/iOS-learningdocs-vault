---
title: 'CTFontCopyDefaultCascadeListForLanguages(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopydefaultcascadelistforlanguages(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopydefaultcascadelistforlanguages(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopydefaultcascadelistforlanguages%28_%3A_%3A%29.json'
content_hash: 'sha256:d682e8e2c4bec521'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyDefaultCascadeListForLanguages(_:_:)

<sub>Function</sub>

Retrieves an ordered list of font substitution preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyDefaultCascadeListForLanguages(_ font: CTFont, _ languagePrefList: CFArray?) -> CFArray?
```

## Parameters

- `font` — The font reference.

- `languagePrefList` — The language preference list, an ordered array of [CFString](../corefoundation/cfstring.md)s of ISO language codes.

## Return Value

An ordered list of [CTFontDescriptor](ctfontdescriptor.md)s for font fallback according to the given language preferences.

## Discussion

When the original `font` used for text layout and rendering does not support a certain Unicode character from the provided text, the system follows this list to pick a fallback font that includes the character.

The font alternatives in the cascade list match the original font’s style, weight, and width.

## See Also

### Getting Font Data

- [CTFontCopyFontDescriptor](<ctfontcopyfontdescriptor(__).md>) — Returns the normalized font descriptor for the given font reference.
- [CTFontCopyAttribute](<ctfontcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute of the given font.
- [CTFontGetSize](<ctfontgetsize(__).md>) — Returns the point size of the given font.
- [CTFontGetMatrix](<ctfontgetmatrix(__).md>) — Returns the transformation matrix of the given font.
- [CTFontGetSymbolicTraits](<ctfontgetsymbolictraits(__).md>) — Returns the symbolic traits of the given font.
- [CTFontCopyTraits](<ctfontcopytraits(__).md>) — Returns the traits dictionary of the given font.
