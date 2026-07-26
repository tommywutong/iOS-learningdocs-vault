---
title: 'init(axialSpace:start:end:function:extendStart:extendEnd:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgshading/init(axialspace:start:end:function:extendstart:extendend:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgshading/init(axialspace:start:end:function:extendstart:extendend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgshading/init%28axialspace%3Astart%3Aend%3Afunction%3Aextendstart%3Aextendend%3A%29.json'
content_hash: 'sha256:4971b4a4f87aaa09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGShading](../cgshading.md)

# init(axialSpace:start:end:function:extendStart:extendEnd:)

<sub>Initializer</sub>

Creates a shading object to use for axial shading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(axialSpace space: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)
```

## Parameters

- `space` — The color space in which color values are expressed. Core Graphics retains this object; upon return, you may safely release it.

- `start` — The starting point of the axis, in the shading’s target coordinate space.

- `end` — The ending point of the axis, in the shading’s target coordinate space.

- `function` — A CGFunction object created by the function [CGFunctionCreate](<../cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>). This object refers to your function for creating an axial shading. Core Graphics retains this object; upon return, you may safely release it.

- `extendStart` — A Boolean value that specifies whether to extend the shading beyond the starting point of the axis.

- `extendEnd` — A Boolean value that specifies whether to extend the shading beyond the ending point of the axis.

## Return Value

A new Core Graphics axial shading. In Objective-C, you’re responsible for releasing this object using [CGShadingRelease](../cgshadingrelease.md).

## Discussion

An axial shading is a color blend that varies along a linear axis between two endpoints and extends indefinitely perpendicular to that axis. When you are ready to draw the shading, call the function [CGContextDrawShading](<../cgcontext/drawshading(__).md>).

## See Also

### Creating Shading Objects

- [CGShadingCreateRadial](<init(radialspace_start_startradius_end_endradius_function_extendstart_extendend_).md>) — Creates a shading object to use for radial shading.
