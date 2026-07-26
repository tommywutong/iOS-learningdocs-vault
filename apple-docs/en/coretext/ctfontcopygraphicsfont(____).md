---
title: 'CTFontCopyGraphicsFont(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopygraphicsfont(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopygraphicsfont(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopygraphicsfont%28_%3A_%3A%29.json'
content_hash: 'sha256:5f7cb52dd5f3abf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyGraphicsFont(_:_:)

<sub>Function</sub>

Returns a Core Graphics font reference and attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyGraphicsFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont
```

## Parameters

- `font` — The font reference.

- `attributes` — On output, points to a font descriptor containing additional attributes from the font. Can be `NULL`. Must be released by the caller.

## Return Value

A [CGFont](../coregraphics/cgfont.md) object for the given font reference.

## See Also

### Converting Fonts

- [CTFontCreateWithGraphicsFont](<ctfontcreatewithgraphicsfont(________).md>) — Creates a new font reference from an existing Core Graphics font reference.
- [CTFontGetPlatformFont](<ctfontgetplatformfont(____).md>) — Returns an ATS font reference and attributes. _(deprecated)_
- [CTFontCreateWithPlatformFont](<ctfontcreatewithplatformfont(________).md>) — Creates a new font reference from an ATS font reference. _(deprecated)_
- [CTFontCreateWithQuickdrawInstance](<ctfontcreatewithquickdrawinstance(________).md>) — Returns a font reference for the given QuickDraw instance. _(deprecated)_
