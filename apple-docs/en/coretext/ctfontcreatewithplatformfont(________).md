---
title: 'CTFontCreateWithPlatformFont(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coretext/ctfontcreatewithplatformfont(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatewithplatformfont(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatewithplatformfont%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:988c25ebb7919b77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateWithPlatformFont(_:_:_:_:)

<sub>Function</sub>

Creates a new font reference from an ATS font reference.

> [!warning] Deprecated
> ATS is deprecated

<sub>macOS</sub>

```swift
func CTFontCreateWithPlatformFont(_ platformFont: ATSFontRef, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont?
```

## Parameters

- `platformFont` — A valid [ATSFontRef](atsfontref.md) object.

- `size` — The point size for the font reference. If `0.0` is specified the default font size of 12.0 is used.

- `matrix` — The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL`, the identity matrix is used. Optional.

- `attributes` — A [CTFontDescriptor](ctfontdescriptor.md) containing additional attributes that should be matched. Optional.

## Return Value

A new font reference for an [ATSFontRef](atsfontref.md) with the specified size, matrix, and additional attributes.

## See Also

### Converting Fonts

- [CTFontCopyGraphicsFont](<ctfontcopygraphicsfont(____).md>) — Returns a Core Graphics font reference and attributes.
- [CTFontCreateWithGraphicsFont](<ctfontcreatewithgraphicsfont(________).md>) — Creates a new font reference from an existing Core Graphics font reference.
- [CTFontGetPlatformFont](<ctfontgetplatformfont(____).md>) — Returns an ATS font reference and attributes. _(deprecated)_
- [CTFontCreateWithQuickdrawInstance](<ctfontcreatewithquickdrawinstance(________).md>) — Returns a font reference for the given QuickDraw instance. _(deprecated)_
