---
title: CGFontCreateWithPlatformFont
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgfontcreatewithplatformfont
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfontcreatewithplatformfont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfontcreatewithplatformfont.json'
content_hash: 'sha256:7590d0096b04dc3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFontCreateWithPlatformFont

<sub>Function</sub>

Creates a font object from an Apple Type Services (ATS) font.

> [!warning] Deprecated
> Use Core Text, documented in [Core Text](../coretext.md), instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGFontRefCGFontCreateWithPlatformFont(void *platformFontReference);
```

## Parameters

- `platformFontReference` — A generic pointer to a font object. The font should be of a type appropriate to the platform on which your program is running. For macOS, you should pass a pointer to an ATS font.

## Return Value

The font object, or `NULL` if the platform font could not be located. In Objective-C, you’re responsible for releasing this object using [CGFontRelease](cgfontrelease.md).

## Discussion

Before drawing text in a Core Graphics context, you must set the font in the current graphics state. For ATS Fonts, call this function to create a font, and pass it to [CGContextSetFont](<cgcontext/setfont(__).md>).

### Special Considerations

This function is deprecated because it takes a pointer to an `ATSFontRef` object—itself deprecated—and is used almost solely by QuickDraw-based applications. There’s no direct one-to-one replacement for the function. Clients using ATSUI and QuickDraw should move to Core Text and Core Graphics instead.

## See Also

### Creating Font Objects

- [CGFontCreateWithDataProvider](<cgfont/init(__)-9aour.md>) — Creates a font object from data supplied from a data provider.
- [CGFontCreateWithFontName](<cgfont/init(__)-1p4b.md>) — Creates a font object corresponding to the font specified by a PostScript or full name.
