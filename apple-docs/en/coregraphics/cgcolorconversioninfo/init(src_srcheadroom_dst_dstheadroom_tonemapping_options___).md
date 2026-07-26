---
title: 'init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:_:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfo/init%28src%3Asrcheadroom%3Adst%3Adstheadroom%3Atonemapping%3Aoptions%3A_%3A%29.json'
content_hash: 'sha256:822832ecd9221405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorConversionInfo](../cgcolorconversioninfo.md)

# init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:_:)

<sub>Initializer</sub>

> [!warning] Deprecated
> declared Swift name 'init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:)' was adjusted to 'init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:_:)' because it does not have the correct number of parameters (6 vs. 7); please report this to its maintainer

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(src source: CGColorSpace, srcHeadroom source_headroom: Float, dst target: CGColorSpace, dstHeadroom target_headroom: Float, toneMapping method: CGToneMapping, options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```
