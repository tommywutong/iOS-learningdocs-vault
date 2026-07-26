---
title: 'init(radialSpace:start:startRadius:end:endRadius:function:extendStart:extendEnd:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgshading/init(radialspace:start:startradius:end:endradius:function:extendstart:extendend:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgshading/init(radialspace:start:startradius:end:endradius:function:extendstart:extendend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgshading/init%28radialspace%3Astart%3Astartradius%3Aend%3Aendradius%3Afunction%3Aextendstart%3Aextendend%3A%29.json'
content_hash: 'sha256:4dc7042413295a8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGShading](../cgshading.md)

# init(radialSpace:start:startRadius:end:endRadius:function:extendStart:extendEnd:)

<sub>Initializer</sub>

Creates a shading object to use for radial shading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(radialSpace space: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)
```

## Parameters

- `space` — The color space in which color values are expressed. Core Graphics retains this object; upon return, you may safely release it.

- `start` — The center of the starting circle, in the shading’s target coordinate space.

- `startRadius` — The radius of the starting circle, in the shading’s target coordinate space.

- `end` — The center of the ending circle, in the shading’s target coordinate space.

- `endRadius` — The radius of the ending circle, in the shading’s target coordinate space.

- `function` — A CGFunction object created by the function [CGFunctionCreate](<../cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>). This object refers to your function for creating a radial shading. Core Graphics retains this object; upon return, you may safely release it.

- `extendStart` — A Boolean value that specifies whether to extend the shading beyond the starting circle.

- `extendEnd` — A Boolean value that specifies whether to extend the shading beyond the ending circle.

## Return Value

A new Core Graphics radial shading. In Objective-C, you’re responsible for releasing this object using [CGShadingRelease](../cgshadingrelease.md).

## Discussion

A radial shading is a color blend that varies between two circles. To draw the shading, call the function [CGContextDrawShading](<../cgcontext/drawshading(__).md>).

## See Also

### Creating Shading Objects

- [CGShadingCreateAxial](<init(axialspace_start_end_function_extendstart_extendend_).md>) — Creates a shading object to use for axial shading.
