---
title: 'CTFontCreateWithGraphicsFont(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreatewithgraphicsfont(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatewithgraphicsfont(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatewithgraphicsfont%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9986d00f293c49f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateWithGraphicsFont(_:_:_:_:)

<sub>Function</sub>

Creates a new font reference from an existing Core Graphics font reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont
```

## Parameters

- `graphicsFont` — A valid Core Graphics font reference.

- `size` — The point size for the font reference. If `0.0` is specified the default font size of 12.0 is used.

- `matrix` — The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL`, the identity matrix is used. Optional.

- `attributes` — Additional attributes that should be matched. Optional.

## Return Value

A new font reference for an existing [CGFont](../coregraphics/cgfont.md) object with the specified size, matrix, and additional attributes.

## See Also

### Converting Fonts

- [CTFontCopyGraphicsFont](<ctfontcopygraphicsfont(____).md>) — Returns a Core Graphics font reference and attributes.
- [CTFontGetPlatformFont](<ctfontgetplatformfont(____).md>) — Returns an ATS font reference and attributes. _(deprecated)_
- [CTFontCreateWithPlatformFont](<ctfontcreatewithplatformfont(________).md>) — Creates a new font reference from an ATS font reference. _(deprecated)_
- [CTFontCreateWithQuickdrawInstance](<ctfontcreatewithquickdrawinstance(________).md>) — Returns a font reference for the given QuickDraw instance. _(deprecated)_
