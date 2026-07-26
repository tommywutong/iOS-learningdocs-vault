---
title: 'CTFontGetGlyphCount(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetglyphcount(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetglyphcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetglyphcount%28_%3A%29.json'
content_hash: 'sha256:cfed0f903cd2e45a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetGlyphCount(_:)

<sub>Function</sub>

Returns the number of glyphs of the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetGlyphCount(_ font: CTFont) -> CFIndex
```

## Parameters

- `font` — The font reference.

## Return Value

The number of glyphs in the font.

## See Also

### Getting Font Metrics

- [CTFontGetAscent](<ctfontgetascent(__).md>) — Returns the scaled font-ascent metric of the given font.
- [CTFontGetDescent](<ctfontgetdescent(__).md>) — Returns the scaled font-descent metric of the given font.
- [CTFontGetLeading](<ctfontgetleading(__).md>) — Returns the scaled font-leading metric of the given font.
- [CTFontGetUnitsPerEm](<ctfontgetunitsperem(__).md>) — Returns the units-per-em metric of the given font.
- [CTFontGetBoundingBox](<ctfontgetboundingbox(__).md>) — Returns the scaled bounding box of the given font.
- [CTFontGetUnderlinePosition](<ctfontgetunderlineposition(__).md>) — Returns the scaled underline position of the given font.
- [CTFontGetUnderlineThickness](<ctfontgetunderlinethickness(__).md>) — Returns the scaled underline-thickness metric of the given font.
- [CTFontGetSlantAngle](<ctfontgetslantangle(__).md>) — Returns the slant angle of the given font.
- [CTFontGetCapHeight](<ctfontgetcapheight(__).md>) — Returns the cap-height metric of the given font.
- [CTFontGetXHeight](<ctfontgetxheight(__).md>) — Returns the x-height metric of the given font.
