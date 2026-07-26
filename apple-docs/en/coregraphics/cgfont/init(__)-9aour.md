---
title: 'init(_:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/init(_:)-9aour'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/init(_:)-9aour'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/init%28_%3A%29-9aour.json'
content_hash: 'sha256:193af21867be1a75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# init(_:)

<sub>Initializer</sub>

Creates a font object from data supplied from a data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ provider: CGDataProvider)
```

## Parameters

- `provider` — A data provider.

## Return Value

The font object or `NULL` if the font can’t be created. In Objective-C, you’re responsible for releasing this object using [CGFontRelease](../cgfontrelease.md).

## Discussion

Before drawing text in a Core Graphics context, you must set the font in the current graphics state by calling the function [CGContextSetFontSize](<../cgcontext/setfontsize(__).md>).

## See Also

### Creating Font Objects

- [CGFontCreateWithFontName](<init(__)-1p4b.md>) — Creates a font object corresponding to the font specified by a PostScript or full name.
