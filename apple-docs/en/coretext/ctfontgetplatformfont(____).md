---
title: 'CTFontGetPlatformFont(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coretext/ctfontgetplatformfont(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetplatformfont(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetplatformfont%28_%3A_%3A%29.json'
content_hash: 'sha256:e2e4d053f5ca070a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetPlatformFont(_:_:)

<sub>Function</sub>

Returns an ATS font reference and attributes.

> [!warning] Deprecated
> ATS is deprecated

<sub>macOS</sub>

```swift
func CTFontGetPlatformFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> ATSFontRef
```

## Parameters

- `font` — The font reference.

- `attributes` — On output, points to a font descriptor containing additional attributes from the font. Can be `NULL`. Must be released by the caller.

## Return Value

An [ATSFontRef](atsfontref.md) object for the given font reference.

## See Also

### Converting Fonts

- [CTFontCopyGraphicsFont](<ctfontcopygraphicsfont(____).md>) — Returns a Core Graphics font reference and attributes.
- [CTFontCreateWithGraphicsFont](<ctfontcreatewithgraphicsfont(________).md>) — Creates a new font reference from an existing Core Graphics font reference.
- [CTFontCreateWithPlatformFont](<ctfontcreatewithplatformfont(________).md>) — Creates a new font reference from an ATS font reference. _(deprecated)_
- [CTFontCreateWithQuickdrawInstance](<ctfontcreatewithquickdrawinstance(________).md>) — Returns a font reference for the given QuickDraw instance. _(deprecated)_
