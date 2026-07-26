---
title: CGFontRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfontretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfontretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfontretain.json'
content_hash: 'sha256:1085bcea038d567d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFontRetain

<sub>Function</sub>

Increments the retain count of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGFontRefCGFontRetain(CGFontRef font);
```

## Parameters

- `font` — The font to retain.

## Return Value

The same font you specified in the `font` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `font` parameter is `NULL`.

## See Also

### Retaining and Releasing a CGFont Object

- [CGFontRelease](cgfontrelease.md) — Decrements the retain count of a font.
