---
title: 'CTFontCreateWithQuickdrawInstance(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coretext/ctfontcreatewithquickdrawinstance(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatewithquickdrawinstance(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatewithquickdrawinstance%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d7d85b5ddfce643b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateWithQuickdrawInstance(_:_:_:_:)

<sub>Function</sub>

Returns a font reference for the given QuickDraw instance.

> [!warning] Deprecated
> Quickdraw font references are deprecated

<sub>macOS</sub>

```swift
func CTFontCreateWithQuickdrawInstance(_ name: ConstStr255Param?, _ identifier: Int16, _ style: UInt8, _ size: CGFloat) -> CTFont
```

## Parameters

- `name` — The QuickDraw font name. If zero length, `identifier` must be specified.

- `identifier` — The QuickDraw font identifier. Can be `0`, but if so, `name` must be specified.

- `style` — The QuickDraw font style.

- `size` — The point size for the font reference. If `0.0` is specified, the default size of 12.0 is used.

## Return Value

The best font instance matching the QuickDraw instance information.

## Discussion

This function is provided for compatibility support between Core Text and clients needing to support QuickDraw-style font references. QuickDraw is a deprecated technology in macOS 10.4 and later.

## See Also

### Converting Fonts

- [CTFontCopyGraphicsFont](<ctfontcopygraphicsfont(____).md>) — Returns a Core Graphics font reference and attributes.
- [CTFontCreateWithGraphicsFont](<ctfontcreatewithgraphicsfont(________).md>) — Creates a new font reference from an existing Core Graphics font reference.
- [CTFontGetPlatformFont](<ctfontgetplatformfont(____).md>) — Returns an ATS font reference and attributes. _(deprecated)_
- [CTFontCreateWithPlatformFont](<ctfontcreatewithplatformfont(________).md>) — Creates a new font reference from an ATS font reference. _(deprecated)_
