---
title: CGFontRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfontrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfontrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfontrelease.json'
content_hash: 'sha256:a9eff8c4f0248081'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFontRelease

<sub>Function</sub>

Decrements the retain count of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGFontRelease(CGFontRef font);
```

## Parameters

- `font` — The font to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `font` parameter is `NULL`.

## See Also

### Retaining and Releasing a CGFont Object

- [CGFontRetain](cgfontretain.md) — Increments the retain count of a font.
