---
title: drawPattern
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatterncallbacks/drawpattern
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/drawpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatterncallbacks/drawpattern.json'
content_hash: 'sha256:6062c76bec842c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPatternCallbacks](../cgpatterncallbacks.md)

# drawPattern

<sub>Instance Property</sub>

A pointer to a custom function that draws thepattern. For information about this callback function, see [CGPatternDrawPatternCallback](../cgpatterndrawpatterncallback.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var drawPattern: CGPatternDrawPatternCallback?
```

## See Also

### Instance Properties

- [releaseInfo](releaseinfo.md) — An optional pointer to a custom function that’sinvoked when the pattern is released. [CGPatternReleaseInfoCallback](../cgpatternreleaseinfocallback.md).
- [version](version.md) — The version of the structure passed in as a parameterto the [CGPatternCreate](<../cgpattern/init(info_bounds_matrix_xstep_ystep_tiling_iscolored_callbacks_).md>). Forthis version of the structure, you should set this value to zero.
